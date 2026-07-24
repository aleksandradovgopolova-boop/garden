---
title: "AI OPS Change Control"
status: accepted
owner: "Engineering Enablement"
updated: 2026-07-18
review_cycle: monthly
source_of_truth: true
---

# AI OPS Change Control

## Pull request requirements

Every change states:

- what and why;
- risk class;
- source-of-truth links;
- acceptance criteria;
- tests and evidence;
- privacy, security, AI and accessibility impact;
- rollout and rollback.

## Review policy

- Small, self-contained changes are preferred.
- R1 requires independent review.
- R2 requires domain owner plus security/privacy review.
- R3 requires explicit human production approval.
- Accepted ADRs are append-only. A changed decision creates a new ADR that supersedes the old one.

## Branch protection target

The default branch should require:
- pull requests;
- passing checks;
- resolved conversations;
- current branch;
- code-owner review after real team handles are configured.
