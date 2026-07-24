---
title: "Garden Navigation Architecture v1"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# Garden Navigation Architecture v1

**Статус:** `implementation proposal`

```yaml
garden_navigation:
  entry:
    default_target: overview | last_place | selected_place | selected_ritual
    remember_last_position: boolean
    quiet_overview: boolean
  spatial:
    enabled: boolean
    map_enabled: boolean
    paths_enabled: boolean
    landmarks_enabled: boolean
    camera_mode: overview | place | detail
  direct:
    search_enabled: true
    place_list_enabled: true
    ritual_list_enabled: true
    recent_enabled: true
    user_favorites_enabled: true
    command_palette_enabled: true
  orientation:
    current_place_visible: true
    breadcrumbs_visible: true
    privacy_indicator_visible: true
    mode_indicator_visible: true
  accessibility:
    list_tree_enabled: true
    keyboard_enabled: true
    reduced_motion_enabled: true
    direct_open_enabled: true
```

## Invariants

- every spatial destination has a direct route;
- no critical action requires traversal;
- no hidden areas block content;
- recent and favorite are separate;
- edit mode is always visible;
- privacy context is visible on deep-link landing.
