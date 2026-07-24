---
title: "Сущности Garden"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# Сущности Garden

---

## Импортированный источник: `P-006_entity_schemas_v0_1.md`

# P-006 — Схемы сущностей

Обязательные сущности: Garden, Place, ObjectInstance, Atmosphere, Ritual, RitualOccurrence, Memory, Version, Snapshot, ContextRelation, Preference, AuditEvent.

## Ключевые инварианты
- никаких автоматических переходов жизненного цикла;
- никаких семантических рёбер графа;
- никаких полей вывода эмоций;
- никаких полей серий (streak) или популярности;
- никакой автономной фиксации со стороны ИИ;
- архивирование и удаление остаются разными действиями.

## Version
```yaml
version:
  id:
  entity_id:
  entity_type:
  parent_version_id:
  change_source: manual | ai
  patch:
  assumptions:
  created_by:
  created_at:
```

## Ritual occurrence
```yaml
ritual_occurrence:
  id:
  ritual_id:
  occurred_at:
  note:
  media:
```
Нет оценки завершения или состояния «пропущено».

---

## Импортированный источник: `garden_place_and_object_schema_v1.md`

# Схема Места и Объекта Garden v1

**Статус:** `implementation draft`

## Place

```yaml
place_id: uuid
garden_id: uuid
name: string | null
type: clearing | grove | pond_edge | quiet_corner | path_area | structure_area | custom
position:
  x: number
  y: number
boundary:
  width: number
  height: number
user_meaning: string | null
ritual_ids: [uuid]
object_ids: [uuid]
memory_ids: [uuid]
ambient:
  light: inherit | custom
  weather: inherit | custom
  soundscape: inherit | custom
visibility: visible | archived
created_at: datetime
updated_at: datetime
```

## Garden Object

```yaml
object_id: uuid
garden_id: uuid
place_id: uuid | null
type: plant | tree | stone | bench | lantern | water | bridge | path_detail | structure | decoration | relic | ambient_marker
appearance_id: string
position:
  x: number
  y: number
rotation: number
scale: number
z_index: integer
name: string | null
user_meaning: string | null
ritual_id: uuid | null
memory_id: uuid | null
state: active | resting | integrated | completed | released | archived
created_by: user | ai_suggestion
created_at: datetime
updated_at: datetime
```

## Правила

- Предложения ИИ требуют явного подтверждения.
- `user_meaning` никогда не выводится автоматически.
- Удаление объекта по умолчанию не удаляет ритуал.
- Удаление ритуала по умолчанию не удаляет объект.
- Архивирование сохраняет право собственности пользователя.
- Разрушительные действия требуют отмены или подтверждения.

---

## Импортированный источник: `garden_context_relation_architecture_v1.md`

# Архитектура контекстных связей Garden v1

**Статус:** `implementation proposal`

```yaml
garden_context_relation:
  relation_id: uuid
  garden_id: uuid
  source_entity_id: uuid
  source_entity_type: place | object | ritual | memory | version
  relation_type: located_in | contains | used_in | remembered_with | derived_from | version_of | belongs_to_lineage
  target_entity_id: uuid
  target_entity_type: place | object | ritual | memory | version
  created_by: user | system
  created_at:
  provenance:
```

## Инварианты

- тип связи должен быть перечислимым;
- никаких пользовательских семантических рёбер;
- никакой визуализации графа;
- никаких связей, создаваемых автоматически из поиска;
- никакого вывода эмоциональных или символических связей;
- удаление связи не удаляет ни одну из сущностей;
- схемы Garden и «Нити» остаются раздельными.
