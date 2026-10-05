---
title: "AI Runtime Product Requirements"
status: accepted
owner: "Product + AI"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: true
related:
  - ../../engineering/ai-runtime/runtime-architecture.md
---

# AI Runtime Product Requirements

This document defines product-level obligations. The implementation source of truth is `internal/engineering/ai-runtime/runtime-architecture.md`.

## The runtime MUST

- treat AI output as a proposal until explicit Apply;
- expose scope, assumptions and affected entities;
- support partial Apply where dependencies allow it;
- preserve committed state after generation, validation or network failure;
- record provenance for applied changes;
- minimize private context;
- use structured, validated output;
- reject unauthorized or out-of-scope mutations;
- provide deterministic behavior for the first research prototype.

## The runtime MUST NOT

- infer identity, diagnosis or emotional truth;
- commit autonomously;
- expand context through an unrestricted semantic graph;
- log private prompts or user-authored content by default;
- hide uncertainty or dependencies.

## Acceptance evidence

The product requirement is satisfied only when the relevant tests, evals and research tasks demonstrate that users understand Preview, Apply and Undo.
