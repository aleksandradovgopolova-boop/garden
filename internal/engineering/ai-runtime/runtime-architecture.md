---
title: "P-007 — AI Runtime Architecture"
status: accepted
owner: "Engineering"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# P-007 — AI Runtime Architecture

```text
User Request → Intent Parser → Scope Resolver → Context Minimizer → Policy Check → Proposal Generator → Assumption Extractor → Change Plan → Preview → User Decision → Commit → Version → Undo
```

AI receives only selected entities, directly necessary context, the instruction and relevant constraints.

Allowed action types: describe, suggest, arrange, rewrite selected text, generate bounded variation, identify conflict, explain change, create draft.

Policy rejects diagnosis, hidden profiling, destructive bulk edits, access escalation, silent commit, cross-Garden leakage, semantic graph generation and manipulative copy.

Every proposal records model, prompt version, scope, assumptions, affected entities, acceptance decisions and committed patch.

> AI is a proposal engine, not an authority layer.
