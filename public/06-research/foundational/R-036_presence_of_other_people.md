---
title: "R-036 — Presence of Other People Without a Social Network"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-036 — Presence of Other People Without a Social Network

## Core question
How may another person be present without turning Garden into a social platform?

## Decision
Presence is contextual, not networked.

Allowed forms:
- mentioned in user-authored text;
- participant in a memory;
- invited viewer of one place;
- participant in one shared ritual;
- co-author of a specific entity;
- temporary guest.

## Rejected social layer
- followers;
- likes;
- public feed;
- profile discovery;
- friend recommendations;
- popularity metrics;
- social ranking.

## Shared place rule
A shared place never exposes unrelated private parts of a Garden. Ownership, edit history, departure and revocation must be explicit.

## Ending a relationship
Garden must support leaving, revoking access, exporting one’s contributions and freezing shared entities. It must not resurface shared memories after access ends unless explicitly requested.

## Trigger Round
```yaml
trigger_round:
  problem: collaboration drifts into social pressure
  selected_cards:
    - Human-centric: reduce comparison
    - Storytelling: allow traces without a feed
    - Business Design: define exit before entry
  generated_hypotheses:
    - people can be present through places rather than profiles
    - departure architecture is required before collaboration
  conflicts_with_garden:
    - public identity performance
    - infinite social discovery
  experiments:
    - read-only invited place
    - graceful departure
  rejected_directions:
    - social graph
    - engagement feed
```

## Principle
A person appears where they were invited, not everywhere the system can connect them.
