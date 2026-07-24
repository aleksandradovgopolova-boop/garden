---
title: "S-006 — AI Preview and Diff"
status: accepted
owner: "Product Design"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# S-006 — AI Preview and Diff

## Product states

```text
Committed
→ Request
→ Proposal
→ Preview
→ Applied
```

Proposal and Preview are not committed Garden state.

## Preview contents

- user request;
- selected scope;
- assumptions;
- affected entities;
- visual before/after;
- textual change summary;
- per-change selection;
- warnings;
- Apply;
- Reject;
- return to request.

## Change units

AI proposal must be decomposed into atomic changes:

```yaml
change:
  id:
  entity_id:
  property:
  before:
  after:
  rationale:
  confidence:
  selected: true
```

Examples:
- atmosphere.light: 0.4 → 0.6
- object.lamp.position: x/y change
- ritual.description: text patch

## Partial apply

The user may deselect independent changes.

Dependencies must be shown:

> Moving the table also moves the lamp attached to it.

## Assumptions

Assumptions are:
- visible;
- editable;
- removable;
- not treated as facts about the user.

## Diff modes

### Visual diff
- overlay;
- side-by-side;
- toggle before/after.

### Text diff
- added;
- removed;
- unchanged context.

### Structural diff
- entities added;
- entities removed;
- relations changed.

## Unsafe or impossible proposal

The preview may state:
- change conflicts with privacy;
- object type unsupported;
- request exceeds selected scope;
- destructive action requires a separate flow.

## Apply receipt

After Apply:
- new version ID;
- summary;
- accepted changes;
- rejected changes;
- Undo action.

## Preview principle

> The user should never have to guess whether AI has already changed the Garden.
