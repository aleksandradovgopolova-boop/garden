---
title: "Garden Memory Architecture v1"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# Garden Memory Architecture v1

```yaml
garden_memory:
  memory_id: uuid
  garden_id: uuid
  user_title: string | null
  date_or_period:
  primary_place_id: uuid | null
  ritual_id: uuid | null
  object_id: uuid | null
  media_ids: [uuid]
  original_note: string | null
  reflection_ids: [uuid]
  visibility: active | hidden | archived
  sensitivity:
    exclude_from_suggestions: true
    exclude_from_global_search: false
  provenance:
```

## Invariants

- maximum one primary place link in Alpha;
- no arbitrary semantic edges;
- no importance score;
- no automatic resurfacing;
- no inferred emotional meaning;
- original note is never overwritten by later reflection;
- inactivity does not affect state.
