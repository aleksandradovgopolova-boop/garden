---
title: "Specification-Driven Development"
status: accepted
owner: "Product + Engineering"
updated: 2026-07-18
review_cycle: monthly
source_of_truth: true
---

# Specification-Driven Development

Every implementation task starts from a lightweight executable specification.

## Required fields

- problem and user value;
- scope and explicit non-goals;
- source-of-truth links;
- user-visible behavior;
- state transitions;
- acceptance criteria;
- error and recovery behavior;
- privacy, security, AI and accessibility impact;
- telemetry constraints;
- test plan;
- rollout and rollback.

## Requirement language

Use:

- **MUST** for mandatory behavior;
- **SHOULD** for preferred behavior with a documented exception path;
- **MAY** for optional behavior.

Avoid adjectives such as “simple”, “beautiful”, “smart” or “intuitive” without observable criteria.

## Traceability

Each PR links to one specification. Each acceptance criterion maps to one or more tests or review checks.
