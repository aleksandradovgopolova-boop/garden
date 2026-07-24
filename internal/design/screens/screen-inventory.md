---
title: "S-001 — Screen Inventory"
status: accepted
owner: "Product Design"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# S-001 — Screen Inventory

## Purpose

Define the minimum complete set of screens required to test Garden Alpha as a coherent product rather than a collection of isolated concepts.

## Core screens

### 1. Welcome
Purpose:
- explain Garden in one sentence;
- offer Blank start and Guided start;
- state privacy default;
- avoid identity profiling.

Primary actions:
- Begin with an empty place
- Help me begin

Secondary:
- What is Garden?
- Privacy

### 2. First Place Setup
Fields and controls:
- optional place name;
- atmosphere preset;
- light;
- sound;
- time-of-day appearance;
- optional short description.

No progress meter.

### 3. Place View
Contains:
- world surface;
- object layer;
- atmosphere layer;
- quiet top bar;
- contextual inspector;
- direct navigation entry;
- edit action;
- AI action.

### 4. Object Library
Contains a small fixed Alpha set:
- seat;
- table;
- lamp;
- plant;
- shelf;
- textile;
- window or opening;
- water element;
- neutral marker object.

No rarity, price or locked states.

### 5. Object Placement
Capabilities:
- select;
- place;
- move;
- rotate where supported;
- resize where supported;
- remove;
- cancel;
- save.

Keyboard and non-drag alternatives required.

### 6. Ritual Editor
Fields:
- title;
- optional description;
- optional place;
- optional reminder;
- lifecycle state.

No frequency requirement.
No streak.
No target count.

### 7. Ritual Detail
Contains:
- ritual description;
- place;
- occurrences;
- add occurrence;
- pause, preserve, archive or end.

### 8. Memory Editor
Fields:
- optional title;
- body;
- media;
- date or period;
- one primary place;
- optional ritual;
- optional object.

### 9. Memory Detail
Contains:
- original memory;
- later reflections;
- literal context;
- archive, hide, export and delete.

No related memories rail.

### 10. Direct Navigation
Tabs or modes:
- Search
- Recent places
- Rituals
- Memories

No recommendation feed.

### 11. AI Request Composer
Contains:
- selected scope;
- user request;
- AI intensity;
- what AI may read;
- submit.

### 12. AI Assumptions
Contains:
- literal assumptions;
- editable scope;
- remove assumption;
- continue or cancel.

### 13. AI Preview
Contains:
- before;
- after;
- changed entities;
- change summary;
- partial apply controls;
- reject;
- apply;
- save as draft where applicable.

### 14. History
Contains:
- manual changes;
- AI changes;
- snapshots;
- provenance;
- restore preview.

### 15. Snapshot
Create and inspect a named preserved state.

### 16. Privacy Settings
Contains:
- ownership;
- AI data access;
- sessions;
- sharing status;
- data location summary.

### 17. Notifications
All categories off except required security notices.

### 18. Export
Choose:
- full Garden;
- places;
- rituals;
- memories;
- media;
- machine-readable data.

### 19. Delete
Distinguish:
- remove relation;
- archive;
- delete entity;
- delete Garden;
- close account.

### 20. Error and Recovery
Used for:
- failed save;
- offline;
- stale version;
- AI failure;
- export failure;
- permission failure.

## Alpha route map

```text
/
├── welcome
├── garden
├── places
│   ├── new
│   └── :placeId
├── rituals
│   ├── new
│   └── :ritualId
├── memories
│   ├── new
│   └── :memoryId
├── history
├── ai
│   └── preview/:proposalId
└── settings
    ├── privacy
    ├── notifications
    └── data
```

## Screen principle

> Every screen should answer where the person is, what can change, and whether that change is already real.
