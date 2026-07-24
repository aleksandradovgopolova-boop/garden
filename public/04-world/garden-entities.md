---
title: "Garden Entities"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# Garden Entities

---

## Imported source: `P-006_entity_schemas_v0_1.md`

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

---

## Imported source: `garden_place_and_object_schema_v1.md`

# Garden Place and Object Schema v1

**Статус:** `implementation draft`

## Place

```yaml
place_id: uuid
garden_id: uuid
name: string | null
type: clearing | grove | pond_edge | quiet_corner | path_area | structure_area | custom
position:
  x: number
  y: number
boundary:
  width: number
  height: number
user_meaning: string | null
ritual_ids: [uuid]
object_ids: [uuid]
memory_ids: [uuid]
ambient:
  light: inherit | custom
  weather: inherit | custom
  soundscape: inherit | custom
visibility: visible | archived
created_at: datetime
updated_at: datetime
```

## Garden Object

```yaml
object_id: uuid
garden_id: uuid
place_id: uuid | null
type: plant | tree | stone | bench | lantern | water | bridge | path_detail | structure | decoration | relic | ambient_marker
appearance_id: string
position:
  x: number
  y: number
rotation: number
scale: number
z_index: integer
name: string | null
user_meaning: string | null
ritual_id: uuid | null
memory_id: uuid | null
state: active | resting | integrated | completed | released | archived
created_by: user | ai_suggestion
created_at: datetime
updated_at: datetime
```

## Rules

- AI suggestions require explicit confirmation.
- `user_meaning` is never inferred.
- Deleting an object does not delete a ritual by default.
- Deleting a ritual does not delete an object by default.
- Archive preserves user ownership.
- Destructive actions require undo or confirmation.

---

## Imported source: `garden_context_relation_architecture_v1.md`

# Garden Context Relation Architecture v1

**Статус:** `implementation proposal`

```yaml
garden_context_relation:
  relation_id: uuid
  garden_id: uuid
  source_entity_id: uuid
  source_entity_type: place | object | ritual | memory | version
  relation_type: located_in | contains | used_in | remembered_with | derived_from | version_of | belongs_to_lineage
  target_entity_id: uuid
  target_entity_type: place | object | ritual | memory | version
  created_by: user | system
  created_at:
  provenance:
```

## Invariants

- relation type must be enumerated;
- no custom semantic edges;
- no graph visualization;
- no auto-created relation from search;
- no emotional or symbolic relation inference;
- deleting relation does not delete either entity;
- Garden and «Нити» schemas remain separate.
