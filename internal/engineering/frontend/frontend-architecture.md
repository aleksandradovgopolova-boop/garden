---
title: "P-009 — Frontend Architecture"
status: accepted
owner: "Engineering"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# P-009 — Frontend Architecture

Responsive web application with an HTML-first prototype path.

## Layers
App Shell; Routing; Domain Stores; Place Renderer; Interaction Layer; AI Proposal Layer; Version/Undo Layer; Persistence Adapter; Accessibility Layer; Guardrail Telemetry.

## Routes
```text
/garden
/places
/places/:placeId
/rituals
/rituals/:ritualId
/memories
/memories/:memoryId
/history
/settings/privacy
/settings/ai
/settings/data
```

Separate server state, draft, preview, committed state, undo stack, preferences and transient UI state. Preview never mutates committed state.

Place Renderer supports responsive composition, keyboard selection, reduced motion and a non-spatial fallback list.

> The frontend preserves the difference between draft, preview and committed reality.
