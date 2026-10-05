---
title: "AI OPS"
status: accepted
owner: "AI OPS"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: true
---

# AI OPS

AI OPS is Garden’s governed development operating model. It combines human product judgment with specialized AI agents, specification-driven delivery, automated quality gates and traceable evidence.

## Core documents

- `operating-model.md` — responsibilities and workflow
- `agent-roles.md` — allowed roles and boundaries
- `spec-driven-development.md` — how work moves from intent to implementation
- `context-management.md` — how agents receive minimal relevant context
- `quality-gates.md` — required checks
- `security-and-trust.md` — agent security controls
- `evals-and-observability.md` — quality measurement
- `change-control.md` — review and approval policy
- `context-packs/` — reusable scoped context for recurring task types

## Principle

AI increases throughput only when the system also increases reviewability, safety and recovery.

## Kit qualification baseline

Installed release: AI Ops Kit 4.9.3, tag `v4.9.3`, commit `ad16611cec1ca65a659f597f7b3b0436df8e78b8`. This supersedes the earlier candidate main snapshot. See [installation evidence](installation-2026-10-05.md). Updates require PRs; auto-update is disabled. Full reference-product qualification remains pending.

The pilot must preserve the existing AGENTS.md and Canon, configure source paths and protected paths, produce an effective limited-context pack, pass installation/doctor/validation checks, and complete one bounded change with independent review, acceptance evidence and rollback. The Kit knowledge graph is operational metadata and must never become a semantic graph of Garden users. Define approval/risk mapping before execution.
