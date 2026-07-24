---
title: "P-006 — Entity Schemas"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# P-006 — Entity Schemas

Required entities: Garden, Place, ObjectInstance, Atmosphere, Ritual, RitualOccurrence, Memory, Version, Snapshot, ContextRelation, Preference, AuditEvent.

## Key invariants
- no automatic lifecycle transition;
- no semantic graph edges;
- no emotional inference fields;
- no streak or popularity fields;
- no autonomous AI commit;
- archive and delete remain distinct.

## Version
```yaml
version:
  id:
  entity_id:
  entity_type:
  parent_version_id:
  change_source: manual | ai
  patch:
  assumptions:
  created_by:
  created_at:
```

## Ritual occurrence
```yaml
ritual_occurrence:
  id:
  ritual_id:
  occurred_at:
  note:
  media:
```
No completion score or missed state.
