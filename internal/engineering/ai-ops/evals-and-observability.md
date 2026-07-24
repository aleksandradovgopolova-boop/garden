---
title: "AI OPS Evals and Observability"
status: accepted
owner: "AI OPS"
updated: 2026-07-18
review_cycle: monthly
source_of_truth: true
---

# AI OPS Evals and Observability

## Evaluate the system, not only the model

Track:

- specification adherence;
- functional correctness;
- regression rate;
- privacy and security violations;
- accessibility failures;
- unsupported assumptions;
- review rejection reasons;
- rollback frequency;
- time from specification to accepted change.

## Evaluation sets

Use synthetic or consented minimized examples. Maintain:

- happy paths;
- ambiguous instructions;
- conflicting documents;
- prompt-injection attempts;
- sensitive-data cases;
- partial failure and recovery;
- Garden boundary violations.

## Release gate

A model, prompt, tool or context-policy change cannot ship solely because average quality improved. Critical safety and privacy cases must pass their fixed thresholds.
