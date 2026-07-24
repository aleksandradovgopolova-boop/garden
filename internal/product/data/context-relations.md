---
title: "Garden Context Relation Architecture v1"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

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
