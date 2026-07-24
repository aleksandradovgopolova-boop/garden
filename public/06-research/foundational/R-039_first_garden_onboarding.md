---
title: "R-039 — First Garden"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-039 — First Garden

## Core question
What is the smallest first experience that lets a person understand Garden?

## Decision
The first experience begins with one place.

Not a profile. Not a life survey. Not a personality test. Not a graph.

> Begin with somewhere you would like to return to.

## First-session path
```text
Welcome
→ choose blank or guided start
→ create one place
→ set atmosphere
→ add one object
→ optionally name the place
→ optionally create one ritual
→ leave
→ return directly
```

## Rules
- every step may be skipped;
- no forced emotional disclosure;
- no productivity goal;
- no invitation requirement;
- no completion meter;
- no reward for compliance.

## First AI assistance
AI asks whether help is wanted, proposes a bounded change and shows Preview before Apply.

## First value moment
The person leaves and later returns to a preserved place that remains recognizably theirs.

## Success criteria
The person understands Place, can edit atmosphere, recognizes authorship, can leave without penalty and does not mistake Garden for a game, tracker or notes app.

## Trigger Round
```yaml
trigger_round:
  problem: onboarding can over-explain and classify the person
  selected_cards:
    - Human-centric: begin with action
    - Storytelling: first return matters more than first build
    - Graphic Design: make emptiness intentional
  generated_hypotheses:
    - one preserved place can explain the product
    - leaving is part of onboarding
  conflicts_with_garden:
    - completion meter
    - personality quiz
  experiments:
    - blank versus guided start
    - first-return test
  rejected_directions:
    - long setup wizard
    - life-goal onboarding
```

## Principle
The first Garden is not built. It is begun.
