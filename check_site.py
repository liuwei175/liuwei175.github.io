#!/usr/bin/env python3
"""Validate the static site. Use --overlay before merging with the repository.

Python 3.9+; standard library only. This checks local links and HTML structure,
not the availability of external websites.
"""
from __future__ import annotations
import argparse
import json
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

class Page(HTMLParser):
    def __init__(self, text: str) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.refs: list[tuple[str, str]] = []
        self.tags: Counter[str] = Counter()
        self.errors: list[str] = []
        self.lang = ''
        self.viewport = False
        self.canonical = False
        self.feed(text)
        self.close()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = dict(attrs)
        self.tags[tag] += 1
        if tag == 'html':
            self.lang = d.get('lang') or ''
        if tag == 'meta' and d.get('name') == 'viewport':
            self.viewport = True
        if tag == 'link' and d.get('rel') == 'canonical':
            self.canonical = True
        if d.get('id'):
            self.ids.append(d['id'])
        if tag == 'img' and not d.get('alt'):
            self.errors.append('Image without an alternative description')
        attr = 'src' if tag in ('img','script') else 'href' if tag in ('a','link') else None
        if attr is not None and d.get(attr):
            self.refs.append((tag, d[attr]))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--overlay', action='store_true', help='Allow the existing repository portrait and favicon to be absent from the update package')
    args = ap.parse_args()
    root = Path(__file__).resolve().parent
    manifest = json.loads((root/'migration-manifest.json').read_text(encoding='utf-8'))
    expected = {row['path'] for row in manifest['pages']}
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*.html')}
    missing = sorted(expected-actual)
    errors = [f'Missing page: {p}' for p in missing]
    allowed = set(manifest['referenced_existing_assets']) if args.overlay else set()
    parsed: dict[Path, Page] = {}
    skipped: set[str] = set()
    n_internal = n_external = 0
    for relative in sorted(expected & actual):
        path = root/relative
        text = path.read_text(encoding='utf-8')
        page = Page(text)
        parsed[path] = page
        if not text.lower().startswith('<!doctype html>'):
            errors.append(f'{relative}: Missing HTML5 doctype')
        if not page.lang or not page.viewport or not page.canonical:
            errors.append(f'{relative}: Missing language, viewport, or canonical metadata')
        for required in ('h1','main','nav','title'):
            if page.tags[required] != 1:
                errors.append(f'{relative}: Expected one {required}, got {page.tags[required]}')
        duplicate_ids = [key for key,value in Counter(page.ids).items() if value>1]
        if duplicate_ids:
            errors.append(f'{relative}: Duplicate IDs: {duplicate_ids}')
        errors.extend(f'{relative}: {e}' for e in page.errors)
        for old in ('liuwei175&nbsp;art&nbsp;lsec.cc.ac.cn','PhDThesis.pdf','/raw/main/Slides.pdf','GPT 4.5'):
            if old in text:
                errors.append(f'{relative}: Outdated string: {old}')

    for path,page in parsed.items():
        for tag,ref in page.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                n_external += 1
                continue
            n_internal += 1
            local = (root/unquote(url.path.lstrip('/'))) if url.path.startswith('/') else (path.parent/unquote(url.path)) if url.path else path
            local = local.resolve()
            if not local.is_relative_to(root):
                errors.append(f'{path.name}: Link escapes site root: {ref}')
                continue
            if local.is_dir():
                local = local/'index.html'
            relative = local.relative_to(root).as_posix()
            if not local.is_file():
                if relative in allowed:
                    skipped.add(relative)
                    continue
                errors.append(f'{path.relative_to(root)}: Missing target: {ref}')
                continue
            if url.fragment and local.suffix == '.html':
                target = parsed.get(local)
                if target is None:
                    target = Page(local.read_text(encoding='utf-8'))
                if unquote(url.fragment) not in target.ids:
                    errors.append(f'{path.relative_to(root)}: Missing anchor: {ref}')

    print(f'Checked {len(parsed)} HTML pages, {n_internal} local references, {n_external} external references.')
    if skipped:
        print('Existing repository assets intentionally excluded from this overlay: '+', '.join(sorted(skipped)))
    print('External reference availability is not tested by this script.')
    if errors:
        print('\n'.join('ERROR: '+e for e in errors),file=sys.stderr)
        return 1
    print('PASS: local page links, anchors, required metadata, and image descriptions.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
