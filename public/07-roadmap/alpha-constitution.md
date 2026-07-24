---
title: "Garden Alpha Constitution"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# Garden Alpha Constitution

## Mission
Garden is a personal digital place where a person may shape atmosphere, arrange meaningful objects, recognize rituals and preserve selected memories without productivity pressure, social ranking or AI control.

## Alpha hypothesis
A digital place can become personally meaningful through authorship, continuity and return—without becoming a game, habit tracker, social network or second brain.

## Primary scenario
```text
create Garden
→ create one Place
→ shape Atmosphere
→ place Objects
→ optionally create Ritual
→ leave
→ return directly
→ request AI change
→ Preview
→ Apply or reject
→ Undo
```

## Required entities
- Garden
- Place
- Object
- Atmosphere
- Ritual
- Ritual occurrence
- Snapshot
- Version
- Context relation
- User preference
- Audit event

## Product laws
1. The user is the author.
2. AI proposes; the user commits.
3. The world may vary; it may not rewrite itself.
4. Time adds history, never debt.
5. Rituals are recognized, not enforced.
6. Memory is selected, not manufactured.
7. Context is not a knowledge graph.
8. Private by default.
9. Silence is valid.
10. Direct and spatial navigation are equal.
11. No feature may require guilt.
12. Meaning belongs to the user.

## Hard exclusions
```yaml
- streaks
- points
- levels
- currency
- leaderboards
- public_feed
- followers
- likes
- graph_view
- backlinks
- autonomous_ai_commit
- emotional_diagnosis
- productivity_score
- decay_from_inactivity
- reengagement_pushes
- public_by_default
- marketplace
```

## Alpha screens
Welcome; Garden home; Create Place; Place view; Atmosphere; Object library; Object placement; Ritual editor; Direct navigation; AI proposal; Preview; History and Undo; Snapshot; Privacy; Export and deletion.

## AI contract
Every AI action requires explicit request, bounded context, visible assumptions, Preview, affected entities, Apply or Reject, Undo and version record.

## Metrics
Activation:
- first place created;
- separate-session return;
- successful Preview → Apply.

Quality:
- authorship;
- calmness;
- ownership;
- ease of leaving.

Guardrails:
- guilt;
- category confusion;
- accidental AI change;
- privacy confusion;
- unwanted notification;
- inability to undo.

## Development gate
Begin technical Alpha when the first-place flow is testable, five to eight people complete it, privacy and deletion paths exist, AI cannot commit without approval and version/Undo is stable.

## Next phase
P-001 Information Architecture  
P-002 Core User Flows  
P-003 Interaction Model  
P-004 Visual Language  
P-005 Design System  
P-006 Entity Schemas  
P-007 AI Runtime  
P-008 Security Architecture  
P-009 Frontend Architecture  
P-010 Prototype and Testing Plan

> Garden Alpha tests whether a person can create somewhere worth returning to, with no obligation to return.
