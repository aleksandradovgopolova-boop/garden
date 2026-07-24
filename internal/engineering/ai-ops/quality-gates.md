---
title: "AI OPS Quality Gates"
status: accepted
owner: "Engineering Enablement"
updated: 2026-07-18
review_cycle: monthly
source_of_truth: true
---

# AI OPS Quality Gates

## Documentation gate
- required metadata present;
- internal links valid;
- one source of truth per topic;
- no active `_final`, `_v1` or duplicate files;
- glossary updated for new domain terms.

## Product gate
- acceptance criteria observable;
- non-goals explicit;
- failure and recovery states defined;
- no conflict with Canon or product boundaries.

## Engineering gate
- type, lint and tests pass;
- state transitions are explicit;
- migrations are reversible or backed up;
- observability exists for critical paths.

## AI gate
- model access is least-privilege;
- inputs and outputs have schemas;
- untrusted content is treated as data, not instruction;
- deterministic fallbacks exist where required;
- evals cover safety and task quality;
- no private prompt logging by default.

## Security and privacy gate
- threat model updated for R2/R3 changes;
- authorization tested server-side;
- secrets scanning passes;
- deletion and export behavior tested;
- third-party processors documented.

## Accessibility gate
- keyboard completion;
- focus visibility;
- screen-reader labels;
- reduced motion;
- structured alternative to spatial interaction.

No agent may waive a failed gate.
