---
title: "AI OPS Operating Model"
status: accepted
owner: "AI OPS"
updated: 2026-07-18
review_cycle: monthly
source_of_truth: true
---

# AI OPS Operating Model

## Work loop

1. **Intent** — a human defines the outcome, user value and constraints.
2. **Specification** — acceptance criteria, non-goals, dependencies and risk class are written.
3. **Context assembly** — the agent receives only relevant canonical documents and code.
4. **Plan** — the agent proposes a small sequence of reversible changes.
5. **Execution** — implementation and tests are produced together.
6. **Automated verification** — lint, type, test, security, accessibility and documentation checks run.
7. **Independent review** — a different agent or human reviews the change against the specification.
8. **Human approval** — mandatory for high-risk changes.
9. **Release and observation** — deployment, telemetry and rollback readiness.
10. **Learning** — decisions, incidents and eval outcomes update the system.

## Separation of duties

The same agent should not be the sole author, reviewer and approver of a high-risk change.

## Risk classes

- **R0 — documentation-only:** no behavior or policy change.
- **R1 — reversible product/code change:** no private data or authorization impact.
- **R2 — sensitive:** AI context, privacy, security, data model, destructive behavior.
- **R3 — production critical:** deployment, migration, incident response, secret or permission changes.

R2 and R3 require human approval and explicit rollback.
