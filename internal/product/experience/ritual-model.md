---
title: "Garden Ritual Architecture v1"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# Garden Ritual Architecture v1

**Статус:** `implementation proposal`

```yaml
garden_ritual:
  ritual_id: uuid
  garden_id: uuid
  user_name: string
  literal_name: string | null
  description: string | null
  components: [component_link]
  time_relation:
    type: none | clock | daypart | event | season | epoch | subjective
    value:
  place_ids: [uuid]
  lineage_id: uuid | null
  lifecycle_state: forming | lived | resting | transformed | preserved | archived | ended
  record_mode: none | manual | retrospective | lightweight | detailed | imported
  reflection_mode: none | optional
  planned_frequency: null
  reminder_ids: [uuid]
  user_meaning: string | null
  provenance:
```

```yaml
ritual_occurrence:
  occurrence_id: uuid
  ritual_id: uuid
  started_at:
  ended_at:
  recorded_at:
  record_mode:
  place_id: uuid | null
  components_used: [uuid]
  user_note: string | null
  provenance:
```

## Invariants

- no streak fields;
- no failed occurrence;
- no quality score;
- no automatic lifecycle transition;
- no required frequency;
- no required logging;
- AI suggestions require confirmation.
