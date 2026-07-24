---
title: "Garden World Evolution Architecture v1"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# Garden World Evolution Architecture v1

```yaml
world_evolution:
  garden_id: uuid
  mode: stable | living | curated | manual | frozen
  ambient_layers:
    light:
    weather:
    sound:
    animals:
    water:
  persistent_change_policy:
    autonomous_growth: false
    autonomous_decay: false
    absence_effects: none
    user_confirmation_required: true
  history:
    snapshot_ids: [uuid]
    variant_ids: [uuid]
    change_log_ids: [uuid]
```

## Invariants

- ambient changes cannot alter persistent state;
- inactivity never changes world state;
- AI persistent changes require confirmation;
- migrations preserve user-authored meaning and layout.
