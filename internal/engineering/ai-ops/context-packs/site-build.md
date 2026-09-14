---
title: "Context Pack: Site Build"
status: accepted
owner: "AI OPS"
updated: 2026-09-14
review_cycle: quarterly
source_of_truth: false
---

# Context Pack: Site Build

## Mission

Change or debug the WowRepo static-site generator and its configuration
without altering published content meaning.

## Allowed repository paths

- `../../../../scripts/build_site.py`
- `../../../../scripts/requirements.txt`
- `../../../../public/wowrepo.yml`
- `../../../../.github/workflows/deploy-pages.yml`

## Required sources of truth

- `../../../../public/README.md`
- `../../../decisions/adr/ADR-004-public-internal-repository-surfaces.md`
- `../../../../AGENTS.md`

## Product boundaries

The generator renders only the `public/` content root. It never reads
`internal/`, `archive/`, `scripts/`, `templates/` or `.github/`.

## Known constraints

- `content_root` stays `public`; the internal/archive excludes stay in place.
- The build output is a local preview; nothing here is deployed by an agent.
- Dependencies are pinned in `scripts/requirements.txt`.

## Prohibited assumptions

- Do not assume network access at build time beyond declared dependencies.
- Do not widen the content root to include internal paths.

## Expected output

Updated generator or config with a successful local build and the
documentation gate passing.

## Verification commands

```bash
python scripts/quality_gates.py --gate docs
python scripts/build_site.py --out build
```

## Reviewed against sources on
2026-09-14
