#!/usr/bin/env python3
"""Derive the decision index and repository counts; --check rejects stale output."""
import argparse
import collections
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def generated(root=ROOT):
    registry = json.loads((root / 'internal/decisions/registry.json').read_text())
    intro = '''---
title: "Decision Log"
status: accepted
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: false
---

# Decision Log

Generated from [registry.json](registry.json) by `scripts/sync_repository.py`. Edit the registry and source record, then regenerate; this index does not grant approvals.

Accepted owner decisions were recovered from the preserved July archive with provenance. GDR-006A supersedes the user-language portion of GDR-006; GDR-013A supersedes the old optional-decoration framing of GDR-013. Other proposals remain proposals. ADR-005 preserves the initial private choice; ADR-007 supersedes it with the owner's later public choice. ADR-006 approves the first research slice.

The accepted status of a compilation or template never approves all embedded proposals. Proposed AI interpretation and measurement documents are not Canon. Accepted decisions change through new records, with scoped supersession and approval evidence.

| ID | Status | Record | Supersedes |
|---|---|---|---|
'''
    rows = []
    for record in sorted(registry['records'], key=lambda r: r['id']):
        relative = str(Path(record['path']).relative_to('internal/decisions'))
        scope = ' (user-language portion)' if record['id'] == 'GDR-006A' else ''
        supersedes = ', '.join(record['supersedes']) + scope or '—'
        rows.append(f'| {record["id"]} | {record["status"]} | [{record["id"]}]({relative}) | {supersedes} |')
    # Tracked files only: installed engine, caches and runtime output cannot alter counts.
    files = subprocess.check_output(['git', '-C', str(root), 'ls-files', '-z']).decode().split('\0')
    files = [f for f in files if f and (root / f).is_file()]
    markdown = [f for f in files if f.endswith('.md')]
    manifest = {
        'schema_version': 2,
        'repository': 'garden',
        'content_snapshot': 'p0-foundation-2026-10-05',
        'historical_package_version': '3.0-wowrepo-ai-ops',
        'visibility': 'public',
        'publication_enabled': False,
        'candidate_publication_surface': 'public/',
        'team_documentation_surface': 'internal/',
        'total_tracked_file_count': len(files),
        'public_markdown_count': sum(f.startswith('public/') for f in markdown),
        'internal_markdown_count': sum(f.startswith('internal/') for f in markdown),
        'active_markdown_count': sum(not f.startswith(('archive/', '.ai/', '.ai-ops/', '.claude/')) for f in markdown),
        'decision_count': len(registry['records']),
        'decision_status_counts': dict(sorted(collections.Counter(r['status'] for r in registry['records']).items())),
        'ai_ops_kit': {'installed': True, 'qualified': False, 'version': '4.9.3',
                       'release_commit': 'ad16611cec1ca65a659f597f7b3b0436df8e78b8', 'managed_file_count': 679},
        'metrics_command': 'python scripts/sync_repository.py --check',
        'validation_command': 'python scripts/check_docs.py',
    }
    return {
        'internal/decisions/decision-log.md': intro + '\n'.join(rows) + '\n',
        'MANIFEST.json': json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for rel, text in generated().items():
        path = ROOT / rel
        if args.check:
            if not path.exists() or path.read_text() != text:
                stale.append(rel)
        else:
            path.write_text(text, encoding='utf-8')
    if stale:
        print('ERROR: stale generated repository metadata: ' + ', '.join(stale))
        return 1
    print('Generated repository metadata is current.' if args.check else 'Repository metadata updated.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
