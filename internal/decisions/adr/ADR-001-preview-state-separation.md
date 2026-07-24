---
title: "ADR-001 — Preview State Separation"
status: accepted
owner: "Architecture"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# ADR-001 — Preview State Separation

Status: accepted

Garden maintains distinct Draft, Preview and Committed states. Apply is the only transition from Preview to Committed. Undo creates a new version rather than erasing history.
