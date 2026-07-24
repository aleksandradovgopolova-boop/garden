---
title: "S-002 — Detailed Wireflows"
status: accepted
owner: "Product Design"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# S-002 — Detailed Wireflows

## WF-01 — First Place

```text
Welcome
→ choose Blank
→ First Place Setup
→ choose atmosphere
→ optional name
→ Continue
→ Place View
→ optional Add Object
→ Exit
→ Garden Home
→ Open recent Place
```

Validation questions:
- Does the user understand that one place is enough?
- Does leaving feel permitted?
- Does returning prove continuity?

## WF-02 — Guided Start

```text
Welcome
→ Help me begin
→ choose starting intention
   - quiet
   - reading
   - thinking
   - resting
   - empty
→ Preview starting place
→ Use this start / Change / Start blank
→ Place View
```

Starting intention must not become a persistent user label.

## WF-03 — Manual Edit

```text
Place View
→ Edit
→ select atmosphere or object
→ make draft changes
→ Preview
→ Save
→ Version receipt
→ Undo available
```

Cancel returns to committed state.

## WF-04 — AI Edit

```text
Place View
→ Ask AI
→ AI Request Composer
→ inspect scope
→ submit
→ Assumptions
→ edit or remove assumptions
→ Generate Preview
→ compare before/after
→ deselect one change
→ Apply selected
→ Version receipt
→ Undo
```

## WF-05 — Create Ritual

```text
Place View
→ Add
→ Ritual
→ Ritual Editor
→ enter title
→ optional description
→ optional reminder
→ Save
→ Ritual appears in Place context
```

If reminder is enabled:
- choose time;
- choose expiry;
- choose channel;
- preview literal notification copy.

## WF-06 — Record Occurrence

```text
Ritual Detail
→ Record occurrence
→ optional note/media
→ Save
→ occurrence appears chronologically
```

No success animation.
No consistency score.

## WF-07 — Create Memory

```text
Place View
→ Add
→ Memory
→ Memory Editor
→ add text/media
→ primary place preselected
→ optional ritual/object
→ Save
→ Memory Detail
```

## WF-08 — Search and Direct Return

```text
Garden Home
→ Search
→ type literal phrase
→ results grouped by entity type
→ open result
```

Search results do not create relations or recommendations.

## WF-09 — Restore Version

```text
History
→ select version
→ inspect change and provenance
→ Preview restore
→ Restore
→ new version created
→ Undo
```

Restoration never erases intervening history.

## WF-10 — Delete

```text
Entity Detail
→ More
→ Delete
→ consequence explanation
→ choose export first or continue
→ confirm
→ deletion receipt
```

No emotional language.

## Wireflow rule

Every branch must include:
- back;
- cancel;
- failed state;
- retry;
- preserve user input;
- no silent commit.
