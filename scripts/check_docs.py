#!/usr/bin/env python3
"""Validate active documentation, publication paths and decision provenance."""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {'draft', 'proposed', 'accepted', 'deprecated', 'superseded', 'archived'}
REQUIRED = ('README.md', 'AGENTS.md', 'public/README.md', 'public/wowrepo.yml',
            'public/01-introduction/what-is-garden.md',
            'public/02-philosophy/garden-constitution.md', 'internal/README.md',
            'internal/governance/SOURCE_OF_TRUTH.md',
            'internal/governance/PUBLICATION_POLICY.md',
            'internal/engineering/ai-ops/README.md',
            'internal/decisions/registry.json')

class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently replacing authoritative metadata."""

def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f'duplicate YAML key: {key}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result

UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def load_yaml(text):
    return yaml.load(text, Loader=UniqueLoader)


def frontmatter(text):
    if not text.startswith('---\n'):
        raise ValueError('missing frontmatter')
    end = text.find('\n---\n', 4)
    if end < 0:
        raise ValueError('unclosed frontmatter')
    meta = load_yaml(text[4:end])
    if not isinstance(meta, dict):
        raise ValueError('frontmatter must be a mapping')
    return meta, text[end + 5:]


def active_files(root):
    # Deliberate roots: engine checkouts, builds and installed Kit are not Garden docs.
    return sorted([*root.glob('*.md'), *root.glob('.github/*.md'),
                   *root.glob('templates/**/*.md'), *root.glob('public/**/*.md'),
                   *root.glob('internal/**/*.md')])


def check(root=ROOT):
    root = root.resolve()
    errors, warnings, documents = [], [], {}
    titles = collections.defaultdict(list)
    for rel in REQUIRED:
        if not (root / rel).is_file():
            errors.append(f'Missing required file: {rel}')

    def link(source, target):
        if not isinstance(target, str):
            errors.append(f'Non-string link: {source.relative_to(root)}')
            return
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith('//'):
            # Public source links must not expose team/archive paths either.
            if source.is_relative_to(root / 'public') and re.search(r'/(?:internal|archive)/', parsed.path):
                errors.append(f'Public link to team/archive area: {source.relative_to(root)} -> {target}')
            return
        path = unquote(parsed.path)
        resolved = (source.parent / path).resolve() if path else source.resolve()
        if not resolved.is_relative_to(root):
            errors.append(f'Link leaves repository: {source.relative_to(root)} -> {target}')
        elif source.is_relative_to(root / 'public') and not resolved.is_relative_to(root / 'public'):
            errors.append(f'Public link leaves public/: {source.relative_to(root)} -> {target}')
        elif not resolved.exists():
            errors.append(f'Broken link: {source.relative_to(root)} -> {target}')

    for p in active_files(root):
        rel = p.relative_to(root).as_posix()
        text = p.read_text(encoding='utf-8')
        try:
            meta, body = frontmatter(text)
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f'Invalid frontmatter: {rel}: {exc}')
            continue
        documents[rel] = (meta, body)
        for key in ('title', 'status', 'owner', 'updated', 'review_cycle', 'source_of_truth'):
            if key not in meta:
                errors.append(f'Missing {key}: {rel}')
        for key in ('title', 'owner'):
            if not isinstance(meta.get(key), str) or not meta[key].strip():
                errors.append(f'{key} must be a nonempty string: {rel}')
        if meta.get('status') not in STATUSES:
            errors.append(f'Unknown status: {rel}: {meta.get("status")}')
        if type(meta.get('source_of_truth')) is not bool:
            errors.append(f'source_of_truth must be boolean: {rel}')
        try:
            updated = dt.date.fromisoformat(str(meta.get('updated')))
            if updated > dt.date.today():
                errors.append(f'Future updated date: {rel}')
        except ValueError:
            errors.append(f'Invalid updated date: {rel}')
        if meta.get('review_cycle') not in {'monthly', 'quarterly', 'yearly', 'annually'}:
            errors.append(f'Unknown review_cycle: {rel}')
        related = meta.get('related', [])
        if not isinstance(related, list):
            errors.append(f'related must be a list: {rel}')
        else:
            for target in related:
                link(p, target)
        for target in re.findall(r'\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)', body):
            link(p, target)
        if re.search(r'(_v\d|_final|final_|\bcopy\b)', p.stem, re.I):
            errors.append(f'Prohibited active filename: {rel}')
        match = re.search(r'^# (.+)$', body, re.M)
        if match:
            titles[match[1].strip()].append(rel)
        # Imported multi-document compilations have separate record statuses.
        preamble = body.split('## Imported source:', 1)[0].split('## Импортированный источник:', 1)[0]
        for status in re.findall(r'^\*\*Статус:\*\*\s*`?(' + '|'.join(sorted(STATUSES)) + r')\b', preamble, re.M):
            if status != meta.get('status'):
                errors.append(f'Body/frontmatter status conflict: {rel}: {status} != {meta.get("status")}')
        if rel.startswith('public/') and p.resolve() != p:
            errors.append(f'Public symlink not allowed: {rel}')

    for title, paths in titles.items():
        if len(paths) > 1 and title not in {'Garden', 'README', 'Releases'}:
            warnings.append(f'Duplicate H1 {title!r}: {paths}')

    try:
        cfg = load_yaml((root / 'public/wowrepo.yml').read_text())
        if cfg['site']['content_root'] != 'public':
            errors.append('WowRepo content_root must be public')
        excludes = cfg.get('exclude', [])
        for excluded in ('../internal', '../archive', '../scripts', '../templates', '../.github'):
            if excluded not in excludes:
                errors.append(f'WowRepo exclude missing: {excluded}')
        covered = {'public/README.md'}
        for item in cfg['navigation']:
            directory = (root / 'public' / item['path']).resolve()
            if not directory.is_relative_to(root / 'public') or not directory.is_dir():
                errors.append(f'Invalid public navigation path: {item["path"]}')
                continue
            covered.update(p.relative_to(root).as_posix() for p in directory.glob('*.md'))
        for rel in documents:
            if rel.startswith('public/') and rel not in covered:
                errors.append(f'Public page not ingested by WowRepo navigation: {rel}')
    except (KeyError, TypeError, ValueError, OSError, yaml.YAMLError) as exc:
        errors.append(f'Invalid WowRepo config: {exc}')

    registry_path = root / 'internal/decisions/registry.json'
    if registry_path.is_file():
        try:
            registry = json.loads(registry_path.read_text())
            records = registry['records']
            by_id = {r['id']: r for r in records}
            if len(by_id) != len(records):
                errors.append('Duplicate decision IDs')
            for r in records:
                if r['status'] not in STATUSES:
                    errors.append(f'Unknown decision status: {r["id"]}')
                source = root / r['path']
                if not source.is_file() or not source.resolve().is_relative_to(root):
                    errors.append(f'Missing decision source: {r["id"]}')
                    continue
                source_text = source.read_text()
                if r.get('heading') and r['heading'] not in source_text.splitlines():
                    errors.append(f'Missing decision heading: {r["id"]}')
                if r['path'] != 'internal/decisions/design-rules.md' and source.relative_to(root).as_posix() in documents:
                    if documents[source.relative_to(root).as_posix()][0]['status'] != r['status']:
                        errors.append(f'Decision registry status conflict: {r["id"]}')
                if r['path'] == 'internal/decisions/design-rules.md' and r.get('heading'):
                    section = source_text.split(r['heading'], 1)[1].split('## Imported source:', 1)[0]
                    state = re.search(r'^\*\*Статус:\*\*\s*`?(\w+)', section, re.M)
                    if not state or state[1] != r['status']:
                        errors.append(f'GDR registry status conflict: {r["id"]}')
                for target in r.get('supersedes', []):
                    if target not in by_id:
                        errors.append(f'Unknown supersedes target: {r["id"]} -> {target}')
            found = set(re.findall(r'^# (GDR-\d+)\b', (root / 'internal/decisions/design-rules.md').read_text(), re.M))
            found.update(p.stem.split('-', 2)[0] + '-' + p.stem.split('-', 2)[1] for p in (root / 'internal/decisions/adr').glob('ADR-*.md'))
            found.update(re.search(r'^# (\S+)', p.read_text(), re.M)[1] for p in (root / 'internal/decisions/gdr').glob('*.md'))
            if found != set(by_id):
                errors.append(f'Decision registry coverage mismatch: {sorted(found ^ set(by_id))}')
        except (ValueError, KeyError, TypeError, OSError) as exc:
            errors.append(f'Invalid decision registry: {exc}')
    return errors, warnings, len(active_files(root))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors, warnings, count = check(args.root)
    for error in errors:
        print('ERROR:', error)
    for warning in warnings:
        print('WARN:', warning)
    print(f'Checked {count} active Markdown files.\nErrors: {len(errors)}; warnings: {len(warnings)}')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
