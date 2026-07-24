---
title: "ADR-004 — Public and Internal Repository Surfaces"
status: accepted
owner: "Product + Architecture"
updated: 2026-07-18
review_cycle: yearly
source_of_truth: true
---
# ADR-004 — Public and Internal Repository Surfaces
## Decision
The repository has two explicit surfaces: `public/`, rendered by WowRepo, and `internal/`, used by the team and AI OPS. WowRepo uses `public/` as its only content root.

## Consequences
Public pages must be self-contained and safe; internal details cannot leak through navigation or search; publication is a reviewed transformation; public Canon and internal implementation must remain consistent; large products such as Garden and Niti may reuse this architecture.
