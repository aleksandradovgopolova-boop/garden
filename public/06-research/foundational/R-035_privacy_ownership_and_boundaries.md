---
title: "R-035 — Privacy, Ownership and Boundaries"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-035 — Privacy, Ownership and Boundaries

## Core question
Who owns a Garden, who may enter it, and what rights remain with the person?

## Decision
Garden is private by default. Access is explicit, bounded and revocable.

> Private by default. Shared by explicit choice. Revocable at any time.

## Separate rights
- account ownership;
- Garden ownership;
- entity authorship;
- data custody;
- access;
- export;
- deletion.

## Alpha defaults
```yaml
garden: private
place: inherits_garden
ritual: private
memory: private
ai_processing: only_after_explicit_request
sharing: off
```

## AI boundary
AI receives only the context necessary for the current request. No full-Garden scan, background emotional profiling or silent reuse of unrelated memories.

## Deletion
The interface distinguishes removing a relation, archiving an entity, deleting an entity, erasing personal data and closing an account.

## Enterprise disclosure
Enterprise deployments must disclose infrastructure operator, log access, retention, AI provider, training policy, administrator powers and legal-hold behavior.

## Trigger Round
```yaml
trigger_round:
  problem: privacy can become an empty settings promise
  selected_cards:
    - Human-centric: give control back
    - Business Design: define the actual owner
    - Innovation: make revocation first-class
    - Naming: use literal permission names
  generated_hypotheses:
    - privacy must be visible in ordinary flows
    - AI context selection should be inspectable
  conflicts_with_garden:
    - public by default
    - implied consent
    - silent administrator access
  experiments:
    - permission comprehension
    - revoke access
    - AI context preview
  rejected_directions:
    - social discovery
    - irreversible sharing
```

## Principle
Privacy is not a mode. It is the starting condition of Garden.
