#!/usr/bin/env python3
"""Check the actual WowRepo artifact, including pages absent from navigation."""
from __future__ import annotations
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.ids = set()
    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for attr in ('href', 'src'):
            if attr in attrs:
                self.urls.append(attrs[attr])


def check(out, public=ROOT / 'public', base='/garden'):
    out, public = out.resolve(), public.resolve()
    errors, parsed = [], {}
    if not out.is_dir():
        return [f'Missing build output: {out}']
    expected = set()
    for source in public.rglob('*.md'):
        rel = source.relative_to(public)
        route = Path('index.html') if rel.as_posix() == 'README.md' else rel.with_suffix('') / 'index.html'
        expected.add(route.as_posix())
        if not (out / route).is_file():
            errors.append(f'Public page missing from production artifact: {rel} -> {route}')
    for file in out.rglob('*'):
        if not file.is_file():
            continue
        rel = file.relative_to(out)
        if not file.resolve().is_relative_to(out):
            errors.append(f'Artifact symlink leaves output: {rel}')
            continue
        if set(rel.parts) & {'internal', 'archive', '.git', '.github', 'templates', 'scripts'} or file.suffix in {'.md', '.zip', '.py', '.yml', '.yaml'}:
            errors.append(f'Non-public source artifact: {rel}')
        if file.suffix == '.html':
            if rel.as_posix() not in expected and rel.as_posix() != '404.html':
                errors.append(f'Unexpected HTML page outside public content: {rel}')
            page = Page()
            page.feed(file.read_text(encoding='utf-8'))
            parsed[file] = page
    for file, page in parsed.items():
        rel = file.relative_to(out).as_posix()
        current_url = f'https://artifact.invalid{base}/' + (rel[:-10] if rel.endswith('index.html') else rel)
        for url in page.urls:
            if not url or url.startswith(('data:', 'mailto:', 'tel:', 'javascript:')):
                continue
            target = urlsplit(urljoin(current_url, url))
            if target.netloc != 'artifact.invalid':
                continue
            path = unquote(target.path)
            if base and path != base and not path.startswith(base + '/'):
                errors.append(f'Local link leaves deployment base: {rel} -> {url}')
                continue
            dest = (out / path[len(base):].lstrip('/')).resolve()
            if not dest.is_relative_to(out):
                errors.append(f'Local link leaves artifact: {rel} -> {url}')
                continue
            if dest.is_dir():
                dest /= 'index.html'
            if not dest.is_file():
                errors.append(f'Broken artifact link: {rel} -> {url}')
            elif target.fragment and dest in parsed and unquote(target.fragment) not in parsed[dest].ids:
                errors.append(f'Broken artifact anchor: {rel} -> {url}')
    return sorted(set(errors))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--public', type=Path, default=ROOT / 'public')
    parser.add_argument('--base', default='/garden')
    args = parser.parse_args()
    errors = check(args.out, args.public, args.base.rstrip('/'))
    for error in errors:
        print('ERROR:', error)
    print(f'Production artifact errors: {len(errors)}')
    return bool(errors)

if __name__ == '__main__':
    raise SystemExit(main())
