---
title: "R-028 — Как рождаются места"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-028 — Как рождаются места

**Версия:** 0.1  
**Дата:** 17 июля 2026  
**Статус:** design research / place architecture  
**Контур:** Garden Atlas → Places / World / Product architecture

---

## 1. Главный вопрос

> Как набор объектов, путей, границ, света, памяти и повторных действий становится местом, к которому человек хочет возвращаться — не потому, что продукт его удерживает, а потому, что пространство стало своим?

---

## 2. Главный вывод

Место в Garden нельзя создать одним красивым шаблоном.

Оно возникает из сочетания:

- пространственной формы;
- доступных действий;
- атмосферы;
- повторного опыта;
- личного значения;
- времени;
- названия;
- памяти;
- ощущения контроля.

Place attachment — многомерная связь. Модель Scannell & Gifford рассматривает её через три измерения:

- **person** — кто связан с местом;
- **process** — чувства, мысли и действия;
- **place** — физические и социальные характеристики места.

### Garden position

> **Garden может предложить пространство и возможности. Своим место делает история человека с ним.**

---

## 3. Space and place

### Space

Геометрически организованная среда:

- координаты;
- дистанции;
- объекты;
- маршруты;
- размеры.

### Place

Пространство, которое стало:

- узнаваемым;
- используемым;
- названным;
- связанным с событиями;
- эмоционально или практически значимым.

### Product consequence

Garden must store both:

```yaml
space:
  geometry:
  objects:
  routes:
  boundaries:

place:
  name:
  meaning:
  repeated_uses:
  rituals:
  memories:
  atmosphere:
  history:
```

---

## 4. Place does not equal attachment

Не каждое место должно становиться эмоционально значимым.

В Garden допустимы:

- временные места;
- функциональные места;
- красивые, но нейтральные места;
- забытые места;
- места без названия;
- места, которые пользователь удаляет.

### Rule

Garden does not optimize for maximum attachment.

Attachment is a possible outcome, not a KPI.

---

## 5. The components of a place

Для проектирования Garden использует девять компонентов:

1. **Boundary** — где место начинается и заканчивается.
2. **Center** — что организует внимание.
3. **Path** — как в место входят и как его проходят.
4. **View** — что из него видно.
5. **Refuge** — где уменьшается экспозиция.
6. **Landmark** — как место узнают.
7. **Atmosphere** — свет, материал, звук, погода.
8. **Use** — что здесь можно делать.
9. **History** — что здесь происходило.

Не все компоненты обязательны.

---

## 6. Boundary

Граница помогает отличить одно место от другого.

Она может быть:

- физической;
- визуальной;
- световой;
- звуковой;
- материальной;
- смысловой;
- пользовательски названной.

### Examples

- край воды;
- ряд трав;
- изменение покрытия;
- тень дерева;
- мост;
- более тихий soundscape;
- название «Место для чтения».

### Risks

Слишком сильные границы создают:

- изоляцию;
- закрытость;
- ощущение уровней игры;
- трудную навигацию;
- иерархию мест.

### Principle

> A boundary should clarify a place before it restricts it.

---

## 7. Center

Центр — не обязательно геометрическая середина.

Им может стать:

- пруд;
- дерево;
- лавка;
- стол;
- свет;
- открытый участок;
- пустое пространство;
- вид.

### Garden rule

Место может иметь:

- один центр;
- несколько слабых центров;
- меняющийся центр;
- отсутствие явного центра.

AI не объявляет центральный объект «главной жизненной ценностью».

---

## 8. Paths and arrival

Путь влияет на то, как место раскрывается.

Варианты:

- прямой;
- извилистый;
- короткий;
- с порогом;
- с постепенным открытием вида;
- с несколькими входами;
- без выделенного маршрута.

### Product use

Place stores:

```yaml
arrival:
  entry_points:
  primary_path:
  optional_paths:
  reveal_style:
```

### No forced journey

Пользователь всегда может:

- открыть место из списка;
- перейти напрямую;
- использовать accessible navigation;
- отключить animated traversal.

---

## 9. Prospect and refuge

Prospect–refuge theory предполагает привлекательность сочетания:

- возможности видеть;
- возможности быть менее открытым для наблюдения.

Но эмпирическая база неоднородна, и этот паттерн нельзя превращать в универсальное правило безопасности или эстетики.

### Garden use

Offer adjustable spatial qualities:

- open;
- sheltered;
- mixed;
- enclosed;
- elevated;
- low;
- hidden;
- exposed.

### Never

- «Закрытые места подходят интровертам»;
- «Открытое пространство означает уверенность»;
- «Этот layout снизит тревогу».

---

## 10. Privacy

В Garden приватность имеет два слоя.

### Perceptual privacy

Как место ощущается визуально:

- скрыто;
- открыто;
- изолировано;
- доступно через порог.

### Data privacy

Кто реально может видеть:

- место;
- объект;
- память;
- ритуал;
- комментарий.

### Critical distinction

Закрытая визуальная форма не означает цифровую приватность.

Каждое место должно явно показывать:

- private;
- shared;
- public-facing preview;
- inherited permissions.

---

## 11. Density and emptiness

Плотность влияет на:

- legibility;
- calm;
- curiosity;
- visual noise;
- sense of ownership.

### Garden principle

Пустота является материалом места.

User may create:

- почти пустую поляну;
- плотный дикий угол;
- один объект на большой территории;
- насыщенную мастерскую.

Garden does not reward filling space.

No:

- empty-slot prompts;
- completion percentage;
- «место ещё не закончено»;
- automatic decoration.

---

## 12. Scale of places

Suggested hierarchy:

### Detail place

- стол;
- лавка;
- маленький угол.

### Room-like place

- мастерская;
- теплица;
- укрытая площадка.

### Landscape place

- поляна;
- берег;
- роща.

### Connector place

- мост;
- путь;
- порог;
- перекрёсток.

### Rule

Large places do not have higher status.

---

## 13. Naming

Название может:

- сделать место различимым;
- упростить возвращение;
- сохранить пользовательский язык;
- связать пространство с историей.

### Naming modes

- unnamed;
- literal;
- poetic;
- personal;
- temporary.

Examples:

- «Берег»;
- «Лавка у воды»;
- «Где я начала писать»;
- «Пока без названия».

### AI boundary

AI may suggest names only after invitation.

It must not infer a life chapter from the place.

---

## 14. Repeated use

Time spent and repeated experience can contribute to place attachment, but repetition does not guarantee attachment.

Garden may remember:

- visits;
- rituals used here;
- edits;
- snapshots;
- user-authored moments.

It does not show:

- visit streak;
- loyalty score;
- neglected place;
- attachment level.

### Possible history language

- «Здесь был создан ритуал…»
- «Это место выглядело так до появления пруда».

Not:

- «Ваше любимое место» unless user marks it.

---

## 15. Place memory

Place memory can involve:

- personal events;
- collective history;
- physical continuity;
- change;
- stories;
- objects.

Research connects place memory with place identity and attachment, but Garden must not treat the remembered story as objective truth.

### Requirements

- exact dates recoverable;
- user-authored descriptions;
- editable groupings;
- uncertainty preserved;
- snapshots separated from interpretations.

---

## 16. Place identity

A place can contribute to how someone describes themselves, but Garden must not produce identity claims.

Allowed:

> «Ты назвала это место “Мастерская книги”.»

Forbidden:

> «Это доказывает, что творчество — твоя настоящая идентичность.»

---

## 17. Social places

Garden may later contain shared places.

Possible:

- shared table;
- collaborative workshop;
- garden path between worlds;
- temporary visiting place.

Risks:

- surveillance;
- social comparison;
- unwanted entry;
- permission confusion;
- permanent traces;
- emotional expectations.

### Alpha

All places are private.

Shared place architecture requires a separate research cycle.

---

## 18. Templates

Place templates can reduce blank-canvas anxiety.

But a template may prescribe:

- lifestyle;
- emotional state;
- cultural norm;
- correct ritual;
- expected object set.

### Safe template

A template offers spatial structure, not a life script.

Example:

```yaml
template:
  name: sheltered_edge
  qualities:
    - one boundary
    - one open view
    - low object density
  objects_optional:
  suggested_uses: []
  symbolic_meaning: null
```

### User-facing examples

- Open clearing;
- Sheltered edge;
- Water place;
- Workshop;
- Crossing;
- Empty ground.

Not:

- Healing garden;
- Productivity zone;
- Anxiety corner;
- Successful-self space.

---

## 19. Place lifecycle

```yaml
place_state:
  forming:
  lived:
  resting:
  preserved:
  archived:
  removed:
```

These are user choices.

### Definitions

**Forming** — пользователь ещё собирает место.  
**Lived** — место используется, без quantitative threshold.  
**Resting** — сохранено без текущего использования.  
**Preserved** — пользователь хочет зафиксировать состояние.  
**Archived** — скрыто из основного мира.  
**Removed** — удалено с возможностью восстановления там, где возможно.

No automatic transitions from inactivity.

---

## 20. Change and continuity

Place attachment can make change meaningful and sometimes difficult.

Garden should support:

- preview;
- snapshot before change;
- undo;
- variant creation;
- partial transformation;
- preserving old version;
- moving objects without rewriting history.

### AI

AI may offer:

- «Сделать вариант»;
- «Сохранить текущее состояние»;
- «Изменить только освещение».

It should not pressure modernization or cleanup.

---

## 21. Orientation and legibility

Borrowing cautiously from spatial-image traditions, Garden can use:

- paths;
- edges;
- districts/areas;
- nodes;
- landmarks.

These are design heuristics, not mandatory ontology.

### Alpha

Every place should have:

- recognizable name or label;
- one accessible route;
- location in list/map;
- stable landmark or visual signature where useful;
- back navigation.

---

## 22. Place creation flow

### Step 1 — Choose or define spatial quality

- open;
- sheltered;
- mixed;
- empty;
- dense;
- water-adjacent.

### Step 2 — Establish boundary and arrival

Optional presets.

### Step 3 — Add a center or leave empty

No completion requirement.

### Step 4 — Add objects

From small, relevant families.

### Step 5 — Name or skip

### Step 6 — Link ritual or memory, or leave unlinked

### Step 7 — Preview accessibility and atmosphere

---

## 23. AI place assistance

AI may:

- translate intention into spatial alternatives;
- propose 2–3 layouts;
- explain practical consequences;
- check clutter and accessibility;
- preserve user constraints;
- generate reversible variants.

AI may not:

- diagnose through spatial preferences;
- call one place psychologically healthy;
- assign symbolic meaning;
- optimize attachment;
- redesign without confirmation;
- fill empty areas automatically.

---

## 24. Place architecture

```yaml
garden_place:
  place_id:
  garden_id:
  name:
  name_mode:
  geometry:
  boundary:
  center:
  arrival:
  paths:
  views:
  spatial_qualities:
  privacy:
  atmosphere:
  object_ids:
  ritual_ids:
  memory_ids:
  epoch_ids:
  user_meaning:
  lifecycle_state:
  snapshots:
  permissions:
  accessibility:
```

---

## 25. Alpha place set

Recommended starter possibilities:

1. **Open clearing** — low boundary, broad view.
2. **Sheltered edge** — partial boundary and outward view.
3. **Water place** — organized around pond or stream.
4. **Workshop** — denser object-oriented place.
5. **Crossing** — bridge/path threshold.
6. **Empty ground** — intentionally almost blank.

### Important

These are starting structures, not six personality types.

---

## 26. Alpha experiments

### A — Blank canvas vs spatial templates

Measure:

- start confidence;
- authorship;
- conformity;
- overload.

### B — Place-first vs ritual-first

Compare:

- create place, then link ritual;
- create ritual, then choose/create place.

### C — Named vs unnamed place

Measure recognition and perceived pressure to create meaning.

### D — Open vs sheltered

Measure preference variation, not psychological diagnosis.

### E — Empty-space permission

Compare neutral emptiness with prompts to add objects.

### F — Repeated use without metrics

Test whether history and snapshots create continuity without visit counts.

---

## 27. Candidate principles

1. Space becomes place through use, meaning and history.
2. Attachment is not a product KPI.
3. Boundaries clarify before they restrict.
4. A center is optional.
5. Direct navigation always exists.
6. Prospect/refuge are options, not universal prescriptions.
7. Visual privacy and data privacy are distinct.
8. Emptiness is a legitimate material.
9. Naming is optional and user-owned.
10. Repetition creates history, not a streak.
11. Templates describe space, not personality.
12. All lifecycle changes are user-controlled.
13. Changes are reversible and snapshot-friendly.
14. Places are private in Alpha.
15. AI proposes layouts, not meanings.

---

## 28. What Garden must not claim

- repeated visits prove attachment;
- one spatial configuration is universally safe;
- enclosed places are for introverts;
- open places indicate confidence;
- place attachment is always beneficial;
- every place needs a center;
- naming creates authentic meaning;
- a visually hidden place is digitally private;
- more objects make a place more complete;
- spatial preferences reveal identity or mental state.

---

## 29. Claim Registry

| Claim | Confidence | Status |
|---|---:|---|
| Place attachment is multidimensional across person, process and place | high | foundation |
| Time and repeated experience can contribute to attachment | medium-high | foundation, not deterministic |
| Place memory relates to identity and attachment | medium-high | foundation |
| Prospect/refuge is a universal preference law | low | rejected |
| Paths, boundaries and landmarks can support legibility | high as design heuristic | foundation |
| Naming may support recognition and personal meaning | medium-low | hypothesis |
| Place-first creation will improve authorship | low | Alpha hypothesis |
| Empty space can be a deliberate composition choice | normative/design principle | required |
| Visual enclosure guarantees privacy | rejected | safety boundary |
| Maximizing attachment is desirable | rejected | product boundary |

---

## 30. Verdict

A place is not a container waiting to be filled.

It is a relationship that can gradually become recognizable, useful, remembered and personal.

Garden should therefore help a person create:

- enough structure to orient;
- enough freedom to author;
- enough continuity to remember;
- enough reversibility to change.

> **Garden creates conditions for place. The person creates belonging.**
