---
title: "ADR-007 — Public Repository with Publication Disabled"
status: accepted
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: true
---

# ADR-007 — Public Repository with Publication Disabled

Status: accepted

## Decision and approval

On 2026-10-05, after GitHub rejected protection for the private repository on the current plan, the owner said “тогда оставь пока публичным)”. Restore Garden's public GitHub visibility and enable branch protection. This supersedes ADR-005's private-repository boundary. GitHub Pages remains disabled; no publication workflow is restored by this decision.

## Consequences

Every tracked file, including `internal/` and `archive/`, and public CI logs is publicly readable. `internal/` describes the intended working audience, not an access boundary. `public/` remains the renderer's candidate content root. Keep only publication-safe source material in the entire repository; credentials, production private content, raw participant data and confidential working materials must live outside this public repository in separately access-controlled storage.

A private repository would require a plan change to obtain branch protection. The owner selected public visibility for now; no purchase, collaborator invitation or separate repository creation is authorized by this decision.

## Publication and review

Future site publication still requires explicit owner approval, the publication policy and passing artifact checks. Required PR/check/conversation controls protect main against accidental writes, but do not make repository content confidential. Independent mandatory review requires a second owner-authorized reviewer.
