---
title: "Changelog"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: monthly
source_of_truth: false
---
# Changelog
## 2026-09-14 — AI OPS kit
- Installed the AI OPS operating model as a working kit.
- Added root `CLAUDE.md` agent operating guide.
- Added `.claude/` settings and a SessionStart hook that prepares the gates.
- Added `scripts/quality_gates.py` as the single verification entry point.
- Added concrete context packs for publication, ADR authoring, research and site build.
- Added the `evals/` suite with the fixed critical eval cases.
- Extended the documentation gate to require the new kit files.

## 2026-07-18 — Repository v3 / WowRepo public surface
- Split repository into `public/` and `internal/`.
- Made `public/` the only WowRepo content root.
- Added public introduction, world overview, roadmap, FAQ and credits.
- Added publication policy and two-audience source-of-truth map.
- Updated AI-agent rules to prevent internal-content leakage.
- Added ADR-004 and the reusable large-product repository standard.

## 2026-07-18 — Repository v2 / AI OPS
Added governed AI OPS operating model, risk classes, quality gates, evals and agent instructions.

## 2026-07-18 — Repository v1
Reorganized the original archive into a maintainable team repository.
