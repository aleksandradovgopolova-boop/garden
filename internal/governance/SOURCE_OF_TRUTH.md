---
title: "Source of Truth Map"
status: accepted
owner: "Product"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: true
---
# Source of Truth Map
## Candidate site publication truth
| Domain | Document |
|---|---|
| Product definition | `public/01-introduction/what-is-garden.md` |
| Purpose | `public/01-introduction/why-garden-exists.md` |
| Constitution | `public/02-philosophy/garden-constitution.md` |
| Principles | `public/03-principles/product-principles.md` |
| Boundaries | `public/03-principles/product-boundaries.md` |
| World model | `public/04-world/garden-entities.md` |
| Roadmap | `public/07-roadmap/roadmap.md` |

## Team implementation truth (publicly readable)
| Domain | Document |
|---|---|
| Alpha scope | `internal/product/alpha/alpha-scope.md` |
| Entity model | `internal/product/data/entity-model.md` |
| AI contract | `internal/product/ai/ai-runtime-requirements.md` |
| Preview | `internal/design/patterns/preview-and-apply.md` |
| Place Renderer | `internal/engineering/frontend/place-renderer.md` |
| AI OPS | `internal/engineering/ai-ops/README.md` |
| Security | `internal/engineering/security/security-architecture.md` |
| Decision status and provenance | `internal/decisions/registry.json` |
| Current slice acceptance | `internal/delivery/current/first-place-return-spec.md` |
| Current cycle | `internal/delivery/current/current-cycle.md` |

Public and internal documents may address the same domain for different audiences but must not contradict each other.

## Decision and scope precedence

Registered accepted owner amendments GDR-006A and GDR-013A resolve the legacy GDR-006 user-language and GDR-013 metaphor proposals. Proposed documents are not binding contracts. The accepted AI runtime architecture and AI runtime product requirements govern the later AI slice; the interpretation protocol is still proposed.

ADR-006 and the current slice specification determine immediate delivery scope; broader Alpha documents determine the later target. Research hypotheses and archive material are evidence, not automatic product requirements. Restored archive decisions require recorded provenance before they become active.
