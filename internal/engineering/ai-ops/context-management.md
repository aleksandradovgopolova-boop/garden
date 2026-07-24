---
title: "AI Context Management"
status: accepted
owner: "AI OPS"
updated: 2026-07-18
review_cycle: monthly
source_of_truth: true
---

# AI Context Management

## Minimal-context rule

Agents receive the smallest sufficient context, not the entire repository.

## Context precedence

1. task specification;
2. active source of truth;
3. accepted ADR and GDR;
4. current implementation;
5. relevant research;
6. archive only when explicitly requested.

## Context pack structure

- mission;
- allowed files;
- prohibited assumptions;
- product boundaries;
- acceptance criteria;
- expected artifact;
- verification commands.

## Freshness

Every context pack records its source document paths and update date. A pack is invalid when a linked source of truth has changed after the pack’s review date.
