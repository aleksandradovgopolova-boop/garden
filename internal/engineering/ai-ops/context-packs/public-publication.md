---
title: "Context Pack: Public Publication"
status: accepted
owner: "AI OPS"
updated: 2026-09-14
review_cycle: quarterly
source_of_truth: false
---

# Context Pack: Public Publication

## Mission

Move approved content into the public WowRepo surface, or edit existing
public pages, without leaking internal material.

## Allowed repository paths

- `public/`
- `scripts/build_site.py` (preview only)

## Required sources of truth

- `../../../governance/PUBLICATION_POLICY.md`
- `../../../governance/SOURCE_OF_TRUTH.md`
- `../../../../public/README.md`
- `../../../../AGENTS.md`

## Product boundaries

Public pages never depend on internal access. Internal documents may link to
public Canon, never the reverse.

## Known constraints

- Publication requires an explicit task and human approval.
- Public documents must not link to `internal/` or `archive/`.
- Public content language and voice follow the existing public pages.

## Prohibited assumptions

- Do not assume any internal document is cleared for publication.
- Do not restate unannounced commitments, roadmap dates or research data.

## Expected output

Updated `public/` Markdown with valid frontmatter and links, plus a note in
the pull request describing what was published and under which approval.

## Verification commands

```bash
python scripts/quality_gates.py --gate docs
python scripts/build_site.py --out build   # local preview only
```

## Reviewed against sources on
2026-09-14
