#!/usr/bin/env python3
"""Static-site generator implementing the WowRepo contract.

WowRepo renders the repository's ``public/`` surface as the public product
site. This script reads ``public/wowrepo.yml`` and turns every Markdown file
under the declared ``content_root`` into a self-contained static HTML site:
navigation from the config, a homepage from ``homepage``, per-page metadata,
internal ``.md`` -> ``.html`` link rewriting and a small client-side search.

Usage:
    python scripts/build_site.py [--out build] [--config public/wowrepo.yml]

Dependencies: PyYAML, Markdown (see scripts/requirements.txt).
Nothing here is deployed; the output directory is a local preview.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path

import markdown as md
import yaml

ROOT = Path(__file__).resolve().parents[1]
GITHUB_BLOB = "https://github.com/aleksandradovgopolova-boop/garden/blob/main"

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "attr_list", "nl2br"]


def split_frontmatter(text: str):
    """Return (meta_dict, body). Tolerates files without frontmatter."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            raw = text[4:end]
            body = text[end + 5 :]
            try:
                meta = yaml.safe_load(raw) or {}
            except yaml.YAMLError:
                meta = {}
            return meta, body
    return {}, text


def first_h1(body: str) -> str | None:
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else None


def out_relpath(rel: Path) -> Path:
    """Map a content-relative .md path to its output .html path.

    README.md -> index.html in the same directory.
    """
    if rel.name.lower() == "readme.md":
        return rel.with_name("index.html")
    return rel.with_suffix(".html")


def rewrite_links(html_text: str) -> str:
    """Rewrite relative *.md links to their generated *.html targets."""

    def repl(m: re.Match) -> str:
        href = m.group(2)
        if re.match(r"^(?:[a-z]+:|#|//|/)", href):
            return m.group(0)
        target, _, anchor = href.partition("#")
        if not target.endswith(".md"):
            return m.group(0)
        base = target[:-3]
        if base.rsplit("/", 1)[-1].lower() == "readme":
            base = base[: -len("readme")] + "index"
        new = base + ".html" + (("#" + anchor) if anchor else "")
        return f'{m.group(1)}="{new}"'

    return re.sub(r'(href)="([^"]+)"', repl, html_text)


def rel_to_root(out_rel: Path) -> str:
    """Prefix ('' or '../' * depth) to reach the site root from a page."""
    depth = len(out_rel.parts) - 1
    return "../" * depth


PAGE_TEMPLATE = """<!doctype html>
<html lang="{lang}" data-theme="auto">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title} · {site_title}</title>
<style>{css}</style>
</head>
<body>
<header class="topbar">
  <a class="brand" href="{root}index.html">{site_title}</a>
  <span class="tagline">{site_desc}</span>
  {search_box}
</header>
<div class="layout">
  <nav class="sidebar" aria-label="Навигация">{nav}</nav>
  <main class="content">
    <article class="doc">
      {meta_bar}
      {body}
    </article>
    <footer class="pagefoot">{footer}</footer>
  </main>
</div>
<script src="{root}assets/app.js"></script>
</body>
</html>
"""

CSS = """
:root{--bg:#fdfdfb;--fg:#22251f;--muted:#6b7167;--line:#e6e6df;--accent:#3f6b4a;--card:#f5f5ef;--code:#eef0ea;}
:root[data-theme=dark],@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#14160f;--fg:#e7e9df;--muted:#9aa08f;--line:#2b2e25;--accent:#8fc69a;--card:#1c1f16;--code:#1c1f16;}}
*{box-sizing:border-box}
html,body{margin:0}
body{background:var(--bg);color:var(--fg);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
.topbar{display:flex;align-items:baseline;gap:16px;padding:14px 22px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:5;flex-wrap:wrap}
.brand{font-weight:700;font-size:20px;color:var(--fg)}
.tagline{color:var(--muted);font-size:14px;flex:1;min-width:120px}
.search{flex:0 0 240px}
.search input{width:100%;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg);font-size:14px}
.layout{display:flex;align-items:flex-start;max-width:1180px;margin:0 auto}
.sidebar{flex:0 0 260px;padding:22px 14px 60px;position:sticky;top:57px;max-height:calc(100vh - 57px);overflow:auto;border-right:1px solid var(--line)}
.sidebar h4{margin:16px 8px 6px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.sidebar a{display:block;padding:5px 8px;border-radius:6px;color:var(--fg);font-size:14px}
.sidebar a:hover{background:var(--card);text-decoration:none}
.sidebar a.active{background:var(--card);color:var(--accent);font-weight:600}
.content{flex:1;min-width:0;padding:26px 40px 80px}
.doc{max-width:760px}
.doc h1{font-size:30px;line-height:1.2;margin:.2em 0 .5em}
.doc h2{font-size:22px;margin-top:1.6em;border-bottom:1px solid var(--line);padding-bottom:.2em}
.doc h3{font-size:18px;margin-top:1.4em}
.doc h4{font-size:15px;color:var(--muted);text-transform:none;letter-spacing:0}
.doc code{background:var(--code);padding:.12em .35em;border-radius:5px;font-size:.9em}
.doc pre{background:var(--code);padding:14px 16px;border-radius:10px;overflow:auto}
.doc pre code{background:none;padding:0}
.doc blockquote{margin:1em 0;padding:.4em 1em;border-left:3px solid var(--accent);background:var(--card);border-radius:0 8px 8px 0;color:var(--fg)}
.doc table{border-collapse:collapse;width:100%;display:block;overflow-x:auto;font-size:14px;margin:1em 0}
.doc th,.doc td{border:1px solid var(--line);padding:6px 10px;text-align:left;vertical-align:top}
.doc th{background:var(--card)}
.doc img{max-width:100%}
.metabar{display:flex;gap:14px;flex-wrap:wrap;color:var(--muted);font-size:13px;margin-bottom:18px}
.metabar .status{border:1px solid var(--line);border-radius:20px;padding:1px 10px}
.pagefoot{margin-top:60px;padding-top:16px;border-top:1px solid var(--line);color:var(--muted);font-size:13px}
.searchresults{position:absolute;right:22px;top:54px;width:min(420px,90vw);background:var(--bg);border:1px solid var(--line);border-radius:10px;box-shadow:0 8px 30px rgba(0,0,0,.15);max-height:60vh;overflow:auto;display:none;z-index:9}
.searchresults a{display:block;padding:9px 12px;border-bottom:1px solid var(--line);color:var(--fg)}
.searchresults a small{display:block;color:var(--muted)}
@media(max-width:820px){.sidebar{display:none}.content{padding:20px}}
"""

APP_JS = """(function(){
var INDEX = %s;
var box = document.getElementById('wr-search');
if(!box) return;
var results = document.createElement('div');
results.className='searchresults'; document.body.appendChild(results);
function esc(s){return s.replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
function run(q){
  q=q.trim().toLowerCase(); results.innerHTML='';
  if(q.length<2){results.style.display='none';return;}
  var root=box.getAttribute('data-root')||'';
  var hits=INDEX.map(function(p){
    var t=p.t.toLowerCase(), b=p.b.toLowerCase(), s=0;
    if(t.indexOf(q)>=0)s+=5; var i=b.indexOf(q); if(i>=0)s+=1;
    return {p:p,s:s,i:i};
  }).filter(function(h){return h.s>0;}).sort(function(a,b){return b.s-a.s;}).slice(0,12);
  if(!hits.length){results.style.display='none';return;}
  results.innerHTML=hits.map(function(h){
    var sn=''; if(h.i>=0){var st=Math.max(0,h.i-40);sn=(st>0?'…':'')+h.p.b.slice(st,h.i+60)+'…';}
    return '<a href="'+root+h.p.u+'">'+esc(h.p.t)+'<small>'+esc(sn)+'</small></a>';
  }).join('');
  results.style.display='block';
}
box.addEventListener('input',function(){run(box.value);});
document.addEventListener('click',function(e){if(e.target!==box&&!results.contains(e.target))results.style.display='none';});
})();
"""


def build(config_path: Path, out_dir: Path) -> dict:
    cfg = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    site = cfg.get("site", {})
    render = cfg.get("render", {})
    nav_cfg = cfg.get("navigation", [])
    content_root = ROOT / site.get("content_root", "public")
    lang = site.get("language", "en")
    site_title = site.get("title", "Site")
    site_desc = site.get("description", "")
    homepage = site.get("homepage", "README.md")

    # Excludes: resolve relative to content_root; skip anything inside.
    excludes = []
    for ex in cfg.get("exclude", []):
        excludes.append((content_root / ex).resolve())

    def excluded(p: Path) -> bool:
        rp = p.resolve()
        return any(str(rp).startswith(str(e)) for e in excludes)

    # Collect pages.
    pages = []  # dict: rel, out_rel, title, meta, body_md
    for mdfile in sorted(content_root.rglob("*.md")):
        if excluded(mdfile):
            continue
        rel = mdfile.relative_to(content_root)
        meta, body = split_frontmatter(mdfile.read_text(encoding="utf-8"))
        title = (meta.get("title") or first_h1(body) or rel.stem).strip().strip('"')
        pages.append(
            {
                "rel": rel,
                "out": out_relpath(rel),
                "title": title,
                "meta": meta,
                "body_md": body,
            }
        )

    by_out = {str(p["out"]): p for p in pages}

    # Build navigation model: config sections -> pages in that directory.
    def page_order(p):
        wr = p["meta"].get("wowrepo") or {}
        return (wr.get("order", 9999), str(p["rel"]))

    nav_sections = []
    claimed = set()
    for entry in nav_cfg:
        label = entry.get("label", entry.get("path", ""))
        path = entry.get("path", "")
        section_pages = [
            p for p in pages if str(p["rel"]).split("/", 1)[0] == path
        ]
        section_pages.sort(key=page_order)
        for p in section_pages:
            claimed.add(str(p["rel"]))
        nav_sections.append((label, section_pages))

    # Markdown -> HTML converter (reset per file for clean state).
    def render_md(body: str) -> str:
        conv = md.Markdown(extensions=MD_EXTENSIONS)
        return rewrite_links(conv.convert(body))

    # Search index (plain text, truncated).
    def plain(body: str) -> str:
        t = re.sub(r"```.*?```", " ", body, flags=re.S)
        t = re.sub(r"[#>*`_|\-]+", " ", t)
        t = re.sub(r"\s+", " ", t)
        return t.strip()[:600]

    search_index = [
        {"t": p["title"], "u": str(p["out"]).replace("\\", "/"), "b": plain(p["body_md"])}
        for p in pages
    ]

    # Write output.
    if out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / "assets").mkdir(parents=True, exist_ok=True)
    (out_dir / "assets" / "app.js").write_text(
        APP_JS % json.dumps(search_index, ensure_ascii=False), encoding="utf-8"
    )

    def nav_html(current_out: str, root: str) -> str:
        parts = []
        parts.append(f'<h4><a href="{root}index.html">Начало</a></h4>')
        for label, sec_pages in nav_sections:
            if not sec_pages:
                continue
            parts.append(f"<h4>{html.escape(label)}</h4>")
            for p in sec_pages:
                href = root + str(p["out"]).replace("\\", "/")
                cls = " class=\"active\"" if str(p["out"]) == current_out else ""
                parts.append(f'<a{cls} href="{href}">{html.escape(p["title"])}</a>')
        return "\n".join(parts)

    search_box = (
        '<span class="search"><input id="wr-search" type="search" '
        'placeholder="Поиск по сайту…" data-root="{root}" autocomplete="off"></span>'
        if render.get("allow_full_text_search")
        else ""
    )

    credits_page = by_out.get("09-credits/index.html") or by_out.get(
        "09-credits/credits.html"
    )

    for p in pages:
        out_rel = p["out"]
        root = rel_to_root(out_rel)
        body_html = render_md(p["body_md"])

        meta_items = []
        if render.get("show_document_status") and p["meta"].get("status"):
            meta_items.append(
                f'<span class="status">{html.escape(str(p["meta"]["status"]))}</span>'
            )
        if render.get("show_last_updated") and p["meta"].get("updated"):
            meta_items.append(f'Обновлено: {html.escape(str(p["meta"]["updated"]))}')
        if render.get("show_source_link"):
            src = f'{GITHUB_BLOB}/{site.get("content_root","public")}/{p["rel"].as_posix()}'
            meta_items.append(f'<a href="{src}">Источник</a>')
        meta_bar = (
            f'<div class="metabar">{" · ".join(meta_items)}</div>' if meta_items else ""
        )

        footer_bits = [f"Отрисовано WowRepo · {html.escape(site_title)}"]
        if credits_page:
            footer_bits.append(
                f'<a href="{root}{str(credits_page["out"]).replace(chr(92),"/")}">Благодарности</a>'
            )
        footer = " · ".join(footer_bits)

        page_html = PAGE_TEMPLATE.format(
            lang=lang,
            page_title=html.escape(p["title"]),
            site_title=html.escape(site_title),
            site_desc=html.escape(site_desc),
            css=CSS,
            root=root,
            nav=nav_html(str(out_rel), root),
            body=body_html,
            meta_bar=meta_bar,
            footer=footer,
            search_box=search_box.format(root=root),
        )
        dest = out_dir / out_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page_html, encoding="utf-8")

    return {
        "pages": len(pages),
        "sections": sum(1 for _, sp in nav_sections if sp),
        "unclaimed": [str(p["rel"]) for p in pages if str(p["rel"]) not in claimed],
        "out": str(out_dir),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Build the WowRepo public site.")
    ap.add_argument("--config", default=str(ROOT / "public" / "wowrepo.yml"))
    ap.add_argument("--out", default=str(ROOT / "build"))
    args = ap.parse_args()
    stats = build(Path(args.config), Path(args.out))
    print(f"Built {stats['pages']} pages, {stats['sections']} nav sections -> {stats['out']}")
    if stats["unclaimed"]:
        print("Pages outside navigation (reachable by direct link):")
        for u in stats["unclaimed"]:
            print("  -", u)


if __name__ == "__main__":
    main()
