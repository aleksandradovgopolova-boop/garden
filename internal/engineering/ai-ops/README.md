---
title: "AI OPS"
status: accepted
owner: "AI OPS"
updated: 2026-07-18
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
- `evals/` — the critical eval cases that gate AI-facing changes

## Kit

The operating model is installed as a working kit:

- `../../../CLAUDE.md` — the agent operating guide loaded on every run.
- `.claude/` — Claude Code settings and the SessionStart hook that prepares
  the environment for the quality gates.
- `../../../scripts/quality_gates.py` — the single verification entry point;
  run it before proposing a change.
- `context-packs/` — ready packs for publication, ADR authoring, research and
  site-build tasks.
- `evals/` — fixed critical cases for the release gate.

## Principle

AI increases throughput only when the system also increases reviewability, safety and recovery.
