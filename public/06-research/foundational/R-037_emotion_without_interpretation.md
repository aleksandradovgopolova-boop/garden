---
title: "R-037 — Emotion Without Interpretation"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-037 — Emotion Without Interpretation

## Core question
How can Garden receive emotional experience without diagnosing or explaining the person?

## Decision
Garden may hold user-authored emotional language and literal self-report. It does not infer inner truth.

> Garden can witness expression. It cannot claim interpretation.

## Allowed
- free text;
- user-selected words;
- optional private mood marker;
- “I do not know”;
- silence;
- deletion;
- no response.

## Forbidden
- diagnosis;
- personality scoring;
- trauma inference;
- attachment-style inference;
- emotional prediction;
- hidden risk ranking;
- “you are actually feeling…”;
- therapeutic positioning.

## AI response
AI may reflect literal wording, ask a gentle question, help rewrite a reflection or reduce stimulation when asked. It may not claim clinical authority or use vulnerability for retention.

## Right to silence
No entry means only that no entry was made. Garden cannot infer deterioration, avoidance or disengagement.

## Trigger Round
```yaml
trigger_round:
  problem: emotional features become surveillance or pseudo-therapy
  selected_cards:
    - Human-centric: let the person name the experience
    - Storytelling: preserve first-person voice
    - Innovation: design for silence
  generated_hypotheses:
    - literal reflection is safer than inferred mood
    - no-response mode should exist
  conflicts_with_garden:
    - diagnosis
    - emotional scoring
  experiments:
    - literal reflection assistant
    - user-defined vocabulary
  rejected_directions:
    - AI therapist
    - passive emotion detection
```

## Principle
Emotional meaning belongs to the person who lived it.
