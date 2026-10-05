---
title: "Current Product Roadmap"
status: accepted
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: true
---

# Current Product Roadmap

## P0 — Repository foundation

Public source repository with explicit confidentiality boundary and disabled Pages; restored owner-decision provenance; explicit proposal statuses; correct references; pinned WowRepo verification; required checks and accountable ownership; approved minimum slice. AI Ops Kit 4.9.3 at commit `38429f984acb7bde79884327b2916954f796f10c` is the candidate qualification baseline, not an installed or qualified dependency.

## P1 — First Place and Return

Qualify the Kit in an isolated change, then implement the [first research slice](../../delivery/current/first-place-return-spec.md). The slice must meet persistence, authorship, accessibility, privacy explanation and recovery criteria before participant sessions. Run five to eight moderated sessions and a later return; review failures and decide whether to proceed.

## P1 — Deterministic AI slice

After the first-place research gate: bounded deterministic proposals, separate Preview, partial Apply, version history and Undo. Follow ADR-001 and ADR-003. Test the AI interaction independently of model quality. No live model integration in this slice.

## P2 — Evidence-led Alpha expansion

Add Ritual, Memory, Snapshots and wider rights/recovery as the evidence requires. Production backend, accounts and live AI require their own technical and security/privacy acceptance gates. A local research gate is not a production-release gate.

No delivery dates are committed. The owner-approved ordering in ADR-006 replaces the July three-week planning sequence; the complete Alpha remains the longer-term scope.
