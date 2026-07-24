---
title: "R-034 — Связи без графа: контекст, соседство и граница с «Нитями»"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-034 — Связи без графа: контекст, соседство и граница с «Нитями»

**Версия:** 0.1  
**Дата:** 17 июля 2026  
**Статус:** design research / contextual relations and product boundaries  
**Контур:** Garden Atlas → Context / Places / Objects / Rituals / Memory

---

## 1. Главный вопрос

> Как Garden может удерживать контекст между местами, объектами, ритуалами и воспоминаниями, не превращаясь в граф знаний, сеть мыслей, второй мозг или проект «Нити»?

---

## 2. Главный вывод

Garden не строит универсальную сеть смыслов.

Он использует только ограниченные связи, которые помогают понять:

- где находится сущность;
- к какому месту она относится;
- в каком ритуале участвует;
- какое пользовательское воспоминание с ней связано;
- откуда она появилась.

### Core principle

> **Garden supports situated context, not semantic expansion.**

---

## 3. Два разных типа продуктов

### «Нити»

Могут быть ориентированы на:

- мысли;
- заметки;
- идеи;
- знания;
- документы;
- аргументы;
- исследование;
- semantic retrieval;
- backlinks;
- граф связей;
- развитие интеллектуального контекста.

### Garden

Ориентирован на:

- места;
- атмосферу;
- объекты;
- ритуалы;
- выбранные воспоминания;
- присутствие;
- возвращение;
- личное пространство.

### Boundary

Garden does not compete with «Нити» on knowledge organization.

---

## 4. Context is not graph

Контекст отвечает:

- где это;
- рядом с чем это находится;
- в каком переживании участвует;
- к какой пользовательской практике относится.

Граф отвечает:

- с чем это связано семантически;
- какие идеи образуют кластер;
- какой узел центральный;
- какие связи неочевидны;
- что ещё система считает релевантным.

Garden нужен первый слой.

Второй слой относится к «Нитям».

---

## 5. Allowed relations

В Alpha допустимы только типизированные связи.

```yaml
allowed_relation_types:
  - located_in
  - contains
  - used_in
  - remembered_with
  - derived_from
  - version_of
  - belongs_to_lineage
```

Examples:

- объект расположен в месте;
- ритуал происходит в месте;
- объект используется в ритуале;
- память относится к месту;
- версия происходит от предыдущей;
- ритуал принадлежит lineage.

---

## 6. Disallowed relations

В Garden Alpha не создаются:

- related_to;
- similar_to;
- reminds_me_of;
- conceptually_connected_to;
- supports;
- contradicts;
- caused;
- symbolizes;
- emotionally_related_to.

Причина:

эти связи быстро превращают продукт в semantic graph и требуют интерпретации.

---

## 7. No arbitrary edges

Пользователь не рисует произвольные линии между всем подряд.

Нет:

- canvas графа;
- node map;
- backlinks panel;
- related entities sidebar;
- cluster visualization;
- graph density;
- centrality;
- automatic edges.

### Product rule

> Every relation must have a concrete product function.

---

## 8. Place as container, not node

Место может удерживать рядом:

- объекты;
- ритуалы;
- память;
- атмосферу.

Но место не является узлом knowledge graph.

Оно не получает:

- semantic weight;
- influence score;
- graph centrality;
- relevance rank.

Место — среда и контекст.

---

## 9. Adjacency

Garden may use spatial adjacency.

Examples:

- лавка рядом с водой;
- ритуал доступен из конкретного места;
- память открывается через объект;
- два места соединены тропой.

Adjacency is:

- visible;
- literal;
- local;
- user-authored.

It is not automatically interpreted as meaning.

---

## 10. Co-presence

Several entities may coexist in one place.

Garden can show:

- object;
- ritual;
- memory;
- atmosphere.

But co-presence does not imply:

- causality;
- emotional relation;
- conceptual similarity;
- narrative sequence.

### Principle

> Being together in Garden does not mean meaning the same thing.

---

## 11. Composition instead of graph

Garden’s organizing metaphor is composition.

A composition may include:

- spatial arrangement;
- sequence;
- rhythm;
- density;
- distance;
- visibility;
- layering.

This is different from graph structure.

### Graph asks

> What is connected?

### Composition asks

> What is present together, and how is it experienced?

---

## 12. Limited navigation

Navigation may move:

- Garden → Place;
- Place → Object;
- Place → Ritual;
- Place → Memory;
- Ritual → selected Place;
- Memory → primary Place.

It does not expand indefinitely through related content.

No endless rabbit holes.

---

## 13. No recommendation chain

Garden does not say:

- «Это напоминает другое воспоминание».
- «Возможно, эти ритуалы связаны».
- «Эти места отражают одну тему».
- «Лавка и дождь часто встречаются вместе».
- «Вот что ещё может быть важно».

Unless the user explicitly asks for a bounded search.

---

## 14. Search boundary

Search may retrieve entities matching:

- user words;
- literal labels;
- date;
- place;
- ritual;
- observable media content.

Search does not automatically create permanent relations.

A search result is not a graph edge.

---

## 15. AI boundary

AI may:

- help locate;
- explain existing relation types;
- identify broken references;
- suggest one direct link after user request;
- preserve provenance;
- detect duplicate objects.

AI may not:

- construct a life graph;
- infer hidden themes;
- generate a personal ontology;
- identify core beliefs;
- connect memories into a psychological narrative;
- migrate Garden content into a second-brain structure by default.

---

## 16. User meaning remains text, not ontology

Пользователь может написать:

> «Это место напоминает мне о начале новой жизни».

Garden stores this as user-authored text.

It does not automatically create entities:

- начало;
- новая жизнь;
- переход;
- идентичность;
- трансформация.

Meaning remains expression, not schema.

---

## 17. Tags

Tags in Garden are optional and limited.

Allowed uses:

- literal filtering;
- accessibility;
- import provenance;
- media description;
- user-defined grouping.

No default tag cloud.

No tag graph.

No automatic hierarchy.

### Alpha limits

- flat tags only;
- no nested ontology;
- no inferred emotional tags;
- no tag recommendations unless requested.

---

## 18. Collections

Garden may later support simple user-created collections.

Examples:

- места для тишины;
- вечерние ритуалы;
- сохранённые фотографии.

But collections are:

- explicit;
- flat;
- user-authored;
- optional.

They do not become dynamic semantic clusters.

---

## 19. Context cards

A contextual card may show:

```text
Место: Берег
Ритуал: Читать у воды
Объект: Лавка
Память: Дождь после работы
```

This gives orientation.

It does not show:

- “related memories”;
- “similar rituals”;
- “hidden connections”;
- “themes detected by AI”.

---

## 20. Export and interoperability

Garden and «Нити» may later interoperate.

Possible future boundary-safe actions:

- export a user-selected memory as a note;
- send a user-authored text to «Нити»;
- link back to Garden place by URL;
- import a selected note as literal text.

But:

- no automatic two-way graph sync;
- no merging data models;
- no shared ontology;
- no silent copying;
- no assumption that every Garden entity belongs in «Нити».

Separate research is required before integration.

---

## 21. Data model separation

```yaml
garden_context_relation:
  relation_id:
  source_entity_id:
  source_entity_type:
  relation_type:
  target_entity_id:
  target_entity_type:
  created_by:
  created_at:
  provenance:
```

Allowed relation types remain enumerated.

No custom semantic relation type in Alpha.

---

## 22. Relation lifecycle

A relation may be:

- created;
- edited where applicable;
- removed;
- restored;
- migrated.

Removing a relation does not delete the linked entities.

Example:

detaching a memory from a place does not delete the memory.

---

## 23. Explainable consequences

Before removing a relation, Garden explains literally:

> «Воспоминание останется в архиве, но больше не будет открываться из места “Берег”.»

Not:

> «Ты потеряешь важную связь».

---

## 24. Trigger Round

### Problem

How can Garden hold meaningful context without becoming «Нити»?

### Trigger 1 — Human-centric

**Prompt:** «А что если убрать всё лишнее?»

**Hypothesis:** Keep only relation types necessary for orientation, use and provenance.

**Outcome:** accepted architecture.

### Trigger 2 — Graphic Design

**Prompt:** «А что если работать с композицией, а не с элементами?»

**Hypothesis:** Spatial composition becomes Garden’s organizing model instead of graph topology.

**Outcome:** accepted product metaphor.

### Trigger 3 — Innovation

**Prompt:** «А что если ограничение — это преимущество?»

**Hypothesis:** Enumerated relation types protect Garden from feature drift and cognitive overload.

**Outcome:** accepted boundary.

### Trigger 4 — Business Design

**Prompt:** «А что если два продукта не должны сливаться?»

**Hypothesis:** Garden and «Нити» remain separate products and may later interoperate only through explicit user actions.

**Outcome:** accepted strategic decision.

### Trigger 5 — Naming

**Prompt:** «А что если назвать буквально?»

**Hypothesis:** UI uses concrete relation labels: «находится в», «используется в», «относится к».

**Outcome:** accepted language direction.

### Rejected interpretation

Building a “living network of meanings” inside Garden is rejected because it reproduces the core domain of «Нити».

---

## 25. Alpha context set

1. Place contains object.
2. Place may host ritual.
3. Memory may have one primary place.
4. Object may be used in ritual.
5. Versions preserve derivation.
6. Rituals preserve lineage.
7. Context card.
8. Literal breadcrumbs.
9. Flat user tags.
10. No graph view.
11. No backlinks.
12. No automatic related entities.
13. No semantic clustering.
14. No custom relation types.

---

## 26. Alpha experiments

### A — Context card vs related-content panel

Measure orientation, distraction and perceived complexity.

### B — Composition vs graph map

Verify that composition supports Garden use without creating knowledge-management expectations.

### C — Enumerated vs custom links

Measure clarity and misuse.

### D — Flat tags vs no tags

Measure retrieval without ontology growth.

### E — Garden-to-«Нити» manual export concept

Test whether users understand the products as separate.

---

## 27. Candidate principles

1. Context is not graph.
2. Garden uses typed, limited relations.
3. Every relation has a concrete function.
4. Place is a container, not a semantic node.
5. Co-presence does not imply meaning.
6. Composition replaces graph topology.
7. Search results do not create relations.
8. User meaning remains expression, not ontology.
9. No arbitrary edges.
10. No backlinks.
11. No automatic related content.
12. No semantic clustering.
13. Garden and «Нити» remain separate.
14. Integration, if any, is explicit and user-controlled.
15. Removing a relation does not delete entities.
16. Literal language precedes interpretation.

---

## 28. What Garden must not claim

- more connections create more meaning;
- all personal data belongs in one graph;
- spatial adjacency reveals emotional relation;
- AI can discover hidden themes safely;
- every memory should connect to multiple entities;
- graph navigation is inherently insightful;
- Garden should organize thoughts;
- Garden should become an external mind;
- Garden and «Нити» benefit from merging;
- user meaning should be converted into structured concepts.

---

## 29. Claim Registry

| Claim | Confidence | Status |
|---|---:|---|
| Typed relations can support orientation | high | foundation |
| Arbitrary semantic linking is necessary for Garden | low | rejected |
| Spatial composition may provide enough structure | medium | Alpha hypothesis |
| Co-presence implies conceptual relation | low | rejected |
| Enumerated relation types can reduce feature drift | high | product architecture principle |
| Search results should become permanent links | low | rejected |
| Garden and «Нити» should share one data model | low | rejected |
| Explicit export may support interoperability | medium | future hypothesis |
| User-authored meaning should remain readable text | high | foundation |
| Local context is sufficient for Alpha | medium-high | accepted scope |

---

## 30. Verdict

Garden does not need to reveal a hidden network beneath a person’s life.

It needs to let places, objects, rituals and selected memories remain together without explaining them away.

> **Garden holds things in context. «Нити» may connect ideas. They are not the same work.**
