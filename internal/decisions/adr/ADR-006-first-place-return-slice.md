---
title: "ADR-006 — First Place and Return Before AI"
status: accepted
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: true
---

# ADR-006 — First Place and Return Before AI

Status: accepted

## Decision and approval

On 2026-10-05 the project owner confirmed “Да, начать с места и возвращения” in the P0 implementation chat. The first research slice is one authored Place with local persistence and direct return. Deterministic AI Preview, partial Apply and versioned Undo follow in a separate slice.

## Alternatives

Including AI Preview and Undo immediately would make the first learning cycle larger. They remain Alpha requirements, but are not required to learn whether an authored Place is worth returning to.

## Scope

See [first-place return specification](../../delivery/current/first-place-return-spec.md) for acceptance criteria, error handling, privacy, research and verification.

This changes delivery order and current cycle, not Garden's product Canon or ultimate Alpha scope. ADR-001 and ADR-003 remain accepted and apply when the AI slice is implemented.
