---
title: "Changelog"
status: accepted
owner: "Product"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: false
---
# Changelog
## 2026-10-05 — P0 repository foundation
- Owner initially chose private visibility, then restored public visibility after GitHub plan limitations; Pages remains deleted and legacy deployment disabled.
- Recovered original OWNER-DECISION-001, GDR-006A and GDR-013A from the historical archive with provenance.
- Added machine-readable decision registry, scoped supersession and generated decision index; corrected overstated proposal/draft statuses.
- Approved First Place/Save/Leave/Return as the first research slice; later AI and broader Alpha scope remain deferred.
- Replaced old engineering links and example ownership paths; pinned verification dependencies and WowRepo.
- Added regression checks for metadata, decisions, complete artifact coverage and publication boundary; all 54 candidate pages are ingested.
- Private branch protection API returned a plan-related HTTP 403; owner chose public visibility to allow protection. See GitHub controls for effective settings.
- WowRepo security audit remains an open dependency qualification item; no public publication is enabled.

## 2026-07-27 — WowRepo engine publication
- Switched the Pages build from the local Python preview to the external WowRepo engine. Historical publication is now disabled.

## 2026-07-24 — Initial repository import and Russian surface
- Imported the product-repository package and translated the candidate publication surface.

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
