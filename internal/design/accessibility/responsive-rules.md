---
title: "S-004 — Responsive Rules"
status: accepted
owner: "Product Design"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# S-004 — Responsive Rules

## Target classes

### Compact
320–599 px

### Medium
600–1023 px

### Large
1024–1439 px

### Wide
1440 px and above

These are behavior ranges, not device assumptions.

## Place View

### Compact
- world surface remains primary;
- contextual inspector becomes bottom sheet;
- object library becomes full-screen sheet;
- direct navigation opens full-screen;
- no hover-only controls;
- drag alternatives required.

### Medium
- world surface with collapsible side inspector;
- object library as overlay drawer;
- Preview may use stacked before/after.

### Large
- world surface plus persistent contextual inspector;
- direct navigation as lightweight overlay;
- Preview may use side-by-side comparison.

### Wide
- cap functional reading width;
- do not stretch controls;
- increase world breathing room rather than information density.

## Fixed viewport behavior

The Place Renderer should fit the available safe viewport:
- account for browser chrome;
- account for virtual keyboard;
- preserve controls;
- avoid content hidden behind bottom sheets;
- support orientation changes.

## Typography

- minimum body size 16 px equivalent;
- user zoom must not break layout;
- headings scale modestly;
- no essential text inside images.

## Touch targets

Minimum 44 × 44 CSS px where possible.

## Motion

Respect `prefers-reduced-motion`.
All spatial transitions need a non-animated equivalent.

## Keyboard

- logical tab order;
- visible focus;
- arrow-key movement where useful;
- object placement available through numeric or directional controls;
- Escape cancels draft state;
- Enter never commits destructive actions without confirmation.

## Responsive principle

> Compact layouts may reduce simultaneous visibility, but never reduce control, reversibility or access to direct navigation.
