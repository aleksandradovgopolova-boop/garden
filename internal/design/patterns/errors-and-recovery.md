---
title: "S-007 — Error, Empty and Recovery States"
status: accepted
owner: "Product Design"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# S-007 — Error, Empty and Recovery States

## Empty states

### No Places
> You can begin with one place.

### Place with no Objects
> There is room here.

### No Rituals
> You have not created a ritual. Nothing is missing.

### No Memories
> No memories have been preserved here.

### No History
> Changes will appear here after the first saved version.

## Loading

Use neutral progress indicators.
Avoid botanical growth metaphors that imply obligation.

## Offline

States:
- offline, no draft;
- offline, local draft;
- reconnecting;
- sync conflict.

Copy:
> You are offline. Saved Garden content is still available. New changes will remain on this device until connection returns.

## Save failure

Requirements:
- preserve draft;
- show retry;
- allow copy/export of text;
- never dismiss automatically.

## Version conflict

```text
A newer version exists.
- Review differences
- Keep your draft
- Use latest version
```

No automatic overwrite.

## AI failure

Types:
- timeout;
- policy rejection;
- invalid output;
- provider unavailable;
- context too large;
- permission problem.

In all cases:
> Your Garden has not changed.

## Media failure

- preserve metadata;
- show retry;
- allow removal;
- avoid blocking unrelated save when safe.

## Destructive-action failure

If deletion fails:
- entity remains;
- show status;
- do not falsely confirm removal.

## Recovery

- autosaved local draft;
- explicit restore;
- version history;
- snapshot;
- export;
- support reference code for critical failures.

## State principle

> Failure must preserve user authorship and make system uncertainty visible.
