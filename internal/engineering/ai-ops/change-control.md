---
title: "AI OPS Change Control"
status: accepted
owner: "Engineering Enablement"
updated: 2026-10-05
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

## Actual GitHub enforcement

See [GitHub controls](../../governance/github-controls.md): after the owner restored public visibility on 2026-10-05, required PRs, checks, up-to-date branches and resolved conversations were enabled for main, including admins. CODEOWNERS assigns the existing accountable owner. Independent mandatory review requires an owner-authorized second reviewer and is not yet enforced. P0 changes are delivered as an unmerged PR for owner review.
