---
title: "R-038 — Notification Constitution"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-038 — Notification Constitution

## Core question
When may Garden interrupt a person?

## Decision
Garden is quiet by default. Interruption is exceptional.

> A Garden may wait.

## Allowed categories
1. User-requested reminders.
2. Security-critical notices.
3. Collaboration-critical notices.
4. System failures requiring action.

## Rejected
- “come back”;
- inactivity warnings;
- streak rescue;
- “your Garden misses you”;
- anniversary resurfacing;
- feature promotion disguised as care.

## Defaults
```yaml
marketing: off
return_prompts: off
ritual_reminders: off_until_user_sets
sound: off
badges: minimal
security: required
```

## Reminder language
Use: “You asked to be reminded about Evening Reading.”
Reject: “Do not break your rhythm.”

## Trigger Round
```yaml
trigger_round:
  problem: notifications turn care into pressure
  selected_cards:
    - Human-centric: protect attention
    - Naming: state why the message exists
    - Innovation: make silence default
  generated_hypotheses:
    - reminders should show provenance
    - reminders should expire rather than accumulate
  conflicts_with_garden:
    - guilt
    - anthropomorphic pressure
  experiments:
    - reminder provenance label
    - quiet onboarding
  rejected_directions:
    - re-engagement campaigns
    - emotional push copy
```

## Principle
Garden interrupts only when the person asked, safety requires it, or another explicit action needs acknowledgment.
