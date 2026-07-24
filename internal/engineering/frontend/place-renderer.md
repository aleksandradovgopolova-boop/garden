---
title: "S-005 — Place Renderer Specification"
status: accepted
owner: "Engineering"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# S-005 — Place Renderer Specification

## Purpose

Render a calm, editable spatial composition without requiring a game engine.

## Scene model

```yaml
place_scene:
  viewport:
  background:
  atmosphere_layers:
  object_instances:
  interaction_overlays:
  accessibility_representation:
```

## Coordinate system

Use normalized coordinates:

```yaml
x: 0.0–1.0
y: 0.0–1.0
scale:
rotation:
z_index:
anchor:
```

This allows responsive transformation across viewports.

## Renderer layers

1. Base canvas
2. Atmosphere
3. Structural elements
4. Objects
5. Contextual highlights
6. Interaction handles
7. System overlays

## Alpha rendering strategy

Prefer DOM/SVG/CSS composition or lightweight Canvas only where justified.

Do not introduce Unity or a full game engine for Alpha.

Selection criteria:
- accessibility;
- responsive behavior;
- editability;
- export;
- performance;
- testability.

## Object states

- idle;
- focused;
- selected;
- moving;
- invalid placement;
- draft;
- preview changed;
- committed.

## Placement rules

Alpha may use:
- soft snapping;
- safe bounds;
- overlap warnings;
- z-order constraints;
- optional grid.

No “wrong” aesthetic placement unless technically impossible.

## Atmosphere controls

Variables may include:
- light intensity;
- warmth;
- haze;
- ambient sound layer;
- motion amount;
- time-of-day visual state.

No variable may encode emotional diagnosis.

## Non-spatial representation

Every Place must also expose a structured list:

```text
Place
- Atmosphere
- Objects
- Rituals
- Memories
```

This is not a degraded mode. It is an equal accessibility route.

## Performance target

Prototype:
- first meaningful render under 2.5 s on ordinary hardware;
- interaction response under 100 ms where local;
- reduced effects on constrained devices.

## Renderer principle

> The renderer composes presence; it does not simulate a world that demands maintenance.
