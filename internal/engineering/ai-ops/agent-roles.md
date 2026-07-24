---
title: "AI Agent Roles"
status: accepted
owner: "AI OPS"
updated: 2026-07-18
review_cycle: monthly
source_of_truth: true
---

# AI Agent Roles

| Role | Purpose | May change | Must not approve alone |
|---|---|---|---|
| Product analyst | Clarify requirements and contradictions | Draft product docs | Canon and scope expansion |
| UX agent | Flows, states, copy and accessibility review | Design drafts | Dark-pattern or accessibility exceptions |
| Software engineer | Implement scoped changes and tests | Code and technical docs | Production deployment |
| Test engineer | Generate and run test suites | Test assets | Waiving failed gates |
| Security reviewer | Threat modeling and control review | Security findings | Accepting residual critical risk |
| Research agent | Synthesis and study support | Research drafts | Claims without evidence |
| Documentation steward | IA, links, metadata and consistency | Documentation | Product meaning changes |
| Release agent | Prepare release artifacts | Release drafts | Final production approval |

Agent roles are capabilities, not personas. Every run must have a declared task, scope, context pack and expected output.
