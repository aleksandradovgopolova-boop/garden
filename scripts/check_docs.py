from pathlib import Path
import re,sys,collections
ROOT=Path(__file__).resolve().parents[1]
errors=[]; warnings=[]
required=['README.md','AGENTS.md','public/README.md','public/wowrepo.yml','public/01-introduction/what-is-garden.md','public/02-philosophy/garden-constitution.md','internal/README.md','internal/governance/SOURCE_OF_TRUTH.md','internal/governance/PUBLICATION_POLICY.md','internal/engineering/ai-ops/README.md']
for rel in required:
    if not (ROOT/rel).exists(): errors.append(f'Missing required file: {rel}')
active=[p for p in ROOT.rglob('*.md') if 'archive' not in p.parts and '.git' not in p.parts]
titles=collections.defaultdict(list)
for p in active:
    text=p.read_text(encoding='utf-8'); rel=p.relative_to(ROOT).as_posix()
    if not text.startswith('---\n'): errors.append(f'Missing frontmatter: {rel}'); continue
    end=text.find('\n---\n',4)
    if end<0: errors.append(f'Invalid frontmatter: {rel}'); continue
    fm=text[4:end]
    for key in ('title:','status:','owner:','updated:','source_of_truth:'):
        if key not in fm: errors.append(f'Missing {key} in {rel}')
    m=re.search(r'^# (.+)$',text,re.M)
    if m: titles[m.group(1).strip()].append(rel)
    if re.search(r'(_v\d|_final|final_|\bcopy\b)',p.stem,re.I): errors.append(f'Prohibited active filename pattern: {rel}')
    if rel.startswith('public/') and re.search(r'\]\([^)]*(?:internal|archive)/',text): errors.append(f'Public document links to private area: {rel}')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
        if target.startswith(('http://','https://','mailto:','#')): continue
        target=target.split('#',1)[0]
        if not target: continue
        resolved=(p.parent/target).resolve()
        try: resolved.relative_to(ROOT.resolve())
        except ValueError: warnings.append(f'Link leaves repository: {rel} -> {target}'); continue
        if not resolved.exists(): errors.append(f'Broken internal link: {rel} -> {target}')
for title,paths in titles.items():
    if len(paths)>1 and title not in {'Garden','README','Releases'}: warnings.append(f"Duplicate H1 title '{title}': {', '.join(paths)}")
cfg=(ROOT/'public/wowrepo.yml').read_text(encoding='utf-8')
if 'content_root: public' not in cfg: errors.append('WowRepo content_root must be public')
for x in ('../internal','../archive','../scripts','../templates','../.github'):
    if x not in cfg: errors.append(f'WowRepo exclude missing: {x}')
for x in errors: print('ERROR:',x)
for x in warnings: print('WARN:',x)
print(f'Checked {len(active)} active Markdown files.')
print(f'Errors: {len(errors)}; warnings: {len(warnings)}')
sys.exit(1 if errors else 0)
