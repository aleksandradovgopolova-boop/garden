---
title: "First Place and Return — Research Slice Specification"
status: accepted
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: true
related:
  - ../../decisions/adr/ADR-006-first-place-return-slice.md
  - ../../../public/02-philosophy/garden-constitution.md
  - ../../engineering/frontend/place-renderer.md
---

# First Place and Return — Research Slice Specification

## Problem and hypothesis

Test whether a person can author a small digital Place and recognize it as their own on return, without a completion obligation. First research participants are adults recruited across notes-app, cozy-game and productivity-tool familiarity. This is a research sampling frame, not a validated market segment.

## Scope and non-goals

A responsive local prototype supports one Garden, one Place, an optional name, a small atmosphere preset set, a fixed object library, direct navigation and local persistence. An empty Place is a complete valid choice. No account, backend, cloud sync, live or mock AI, Ritual editor, Memory, notifications, snapshots or versioned Undo in this slice. Those features remain later Alpha work.

Garden-owned authored state does not change due to absence, time or return. Rendering may adapt to viewport without changing saved coordinates. The prototype has no third-party model or analytics integration.

## State and transitions

`New → Draft → explicit Save → Committed → Leave → Return to Committed`.

Draft and Committed are separate. Editing never persists changes as committed until Save succeeds. Cancel restores the committed view. Leaving with an unsaved draft offers Save, Discard or Stay. A cancelled navigation leaves the draft intact.

Save is atomic at the persistence boundary. A failed write preserves the previous committed Place and keeps the editable draft available for retry. Unsupported or corrupt local data produces a recoverable error; it is not silently overwritten.

## Observable acceptance criteria

| ID | Requirement | Evidence |
|---|---|---|
| FP-01 | A person creates one Place with a name optional and empty composition allowed. | Browser flow for empty and populated Place |
| FP-02 | Person selects atmosphere, adds/moves/removes an object and saves. | Browser flow and stored schema validation |
| FP-03 | Refresh and reopening the same browser profile restore the committed composition. | Persistence integration and browser restart test |
| FP-04 | Direct entry opens the saved Place without onboarding or forced walking. | Keyboard browser flow |
| FP-05 | Return after a simulated long absence preserves authored state without debt, decay or streak copy. | State comparison with advanced clock |
| FP-06 | Draft changes and cancelled editing do not mutate the committed Place. | State-transition tests |
| FP-07 | Failed storage writes preserve the last successful commit and offer retry. | Injected storage failure and recovery test |
| FP-08 | Every creation/edit/save/return action works by keyboard and structured controls; reduced motion is supported. | Keyboard and assistive-technology review |
| FP-09 | Export produces a versioned local JSON file; importing that export restores the same authored state after confirmation. Invalid input does not overwrite the current Place. | Round-trip and invalid import tests |
| FP-10 | Explicit confirmed local deletion removes drafts and committed state; the interface explains that exported files and browser/device copies are outside its control. | Delete/reload test and copy review |
| FP-11 | No private text or object composition is sent over the network or included in telemetry. | Network inspection; no model/analytics endpoints |
| FP-12 | Clearing browser storage or switching device/profile is accurately described as outside this prototype's persistence guarantee. | Privacy/storage explanation review |

## Data and security boundary

Use synthetic or participant-chosen non-sensitive content. Local-only is not encryption or cloud backup. Do not claim production privacy, account isolation or recovery from browser storage deletion. Local save errors, schema migration/version mismatch and deletion must be demonstrable before participant sessions. No external Alpha with real hosted user data is approved by this specification.

## Research and decision gate

Run five to eight moderated sessions after FP-01–FP-12 pass. Do not teach the philosophy before tasks. At least 80% should create/save/return without facilitator help; there must be zero critical privacy misunderstandings and no reported punishment for absence. Record denominator and individual failures; do not round away failures in a small sample. Observe whether a majority describe the experience as their own place. Willingness to return is exploratory; this round does not prove long-term voluntary return.

A follow-up return in a later session tests continuity. Record concerns, accessibility barriers and visual authorship feedback. The owner then decides revise, proceed to AI slice or stop. Meeting the gate does not approve production release.

## Implementation and rollout

Choose renderer after the accessibility/performance spike in ADR-002. Add runnable commands and map each FP criterion to tests or manual evidence in the implementation PR. Until code exists, this specification is approved scope, not evidence of completion.

Run locally first; enable participant access only in an owner-approved controlled environment with this storage boundary explained. Rollback to the previous build must preserve compatible saved data; before an incompatible schema change require a versioned export. Do not silently migrate or reset participant data.
