---
title: "S-008 — Analytics Event Taxonomy"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# S-008 — Analytics Event Taxonomy

## Principle

Collect the minimum telemetry needed to validate usability, safety and product comprehension.

Do not collect emotional content, memory text, ritual text or raw AI prompts in analytics.

## Event envelope

```yaml
event:
  event_name:
  event_version:
  timestamp:
  anonymous_or_user_id:
  session_id:
  entity_type:
  entity_id_hash:
  source_surface:
  properties:
```

## Activation events

- garden_created
- place_creation_started
- place_created
- atmosphere_changed
- object_placed
- ritual_created
- session_ended
- place_returned_in_new_session

## Navigation events

- spatial_navigation_used
- direct_navigation_opened
- search_performed
- search_result_opened
- recent_place_opened

## AI events

- ai_request_started
- ai_scope_reviewed
- ai_assumption_removed
- ai_preview_created
- ai_change_deselected
- ai_proposal_rejected
- ai_proposal_applied
- ai_apply_undone
- ai_error_shown

Do not log prompt text by default.

## History events

- version_opened
- restore_previewed
- version_restored
- manual_change_undone
- snapshot_created

## Privacy and rights

- privacy_settings_opened
- export_started
- export_completed
- deletion_explanation_opened
- entity_deleted
- account_deletion_started

## Guardrail signals

- save_error_shown
- version_conflict_shown
- privacy_help_opened
- undo_not_found
- preview_abandoned
- notification_disabled
- onboarding_exited

## Prohibited derived metrics

- emotional engagement score;
- ritual consistency score;
- personal growth score;
- Garden health;
- relationship intensity;
- memory importance;
- productivity score.

## Retention interpretation

Return may be measured for research, but never presented to the user as obligation or used alone as the product’s definition of success.

## Analytics principle

> Measure whether Garden works, not whether the person can be made to use it more.
