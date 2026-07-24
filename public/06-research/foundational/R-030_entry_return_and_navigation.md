---
title: "R-030 — Вход, возвращение и навигация по Garden"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-030 — Вход, возвращение и навигация по Garden

**Версия:** 0.1  
**Дата:** 17 июля 2026  
**Статус:** design research / navigation, orientation and return  
**Контур:** Garden Atlas → Navigation / Places / Rituals / Accessibility

---

## 1. Главный вопрос

> Как человек входит в Garden, понимает, где находится, находит важное и возвращается к нему — без бесконечного скролла, геймифицированного путешествия, пространственной дезориентации и принуждения «исследовать весь мир»?

---

## 2. Главный вывод

Навигация Garden должна поддерживать два равноправных способа существования:

1. **Spatial mode** — человек перемещается по миру и местам.
2. **Direct mode** — человек мгновенно открывает нужное через список, поиск, историю или ссылку.

### Core principle

> **Movement may create experience. Access must never depend on movement.**

---

## 3. Почему навигация здесь не просто UI

В обычном приложении навигация отвечает:

- где раздел;
- как открыть объект;
- как вернуться назад.

В Garden она дополнительно влияет на:

- чувство масштаба;
- ощущение места;
- темп;
- память;
- приватность;
- доступность;
- эмоциональное давление.

Если всё доступно только через мир, Garden становится игрой.

Если всё доступно только через меню, мир становится декорацией.

Нужна двойная архитектура.

---

## 4. Entry

Вход в Garden не должен каждый раз начинаться с одной и той же главной страницы.

Возможные точки входа:

- последнее открытое место;
- выбранное домашнее место;
- конкретный ритуал;
- snapshot;
- search result;
- notification target;
- shared link later;
- safety mode.

### User control

Пользователь выбирает:

- куда возвращаться по умолчанию;
- сохранять ли последнюю позицию;
- открывать ли Garden в quiet overview;
- входить ли сразу в конкретное место.

---

## 5. Return

Возвращение после паузы не является отдельным ритуалом реабилитации.

Нет:

- recap, который невозможно пропустить;
- «ты давно не была»;
- обязательного тура изменений;
- backlog;
- celebration of return;
- hidden updates.

Допустимо:

- кратко показать, что изменилось по инициативе пользователя или обновления;
- предложить открыть последнее место;
- открыть нейтральный обзор.

### Copy

> «Продолжить с того места, где ты остановилась.»

Не:

> «Сад рад, что ты вернулась.»

---

## 6. Spatial navigation

Spatial mode может включать:

- pan;
- zoom;
- переход между местами;
- paths;
- landmarks;
- map;
- place overview;
- camera presets.

### Requirements

- no forced walking;
- no artificial travel time;
- no stamina;
- no locked routes;
- no mandatory animation;
- no hidden critical controls in space.

---

## 7. Direct navigation

Direct mode includes:

- global search;
- place list;
- ritual list;
- recent;
- favorites chosen by user;
- history;
- command palette;
- deep links.

### Rule

Every spatial destination has a direct equivalent.

Every direct destination can reveal its place context where relevant.

---

## 8. Orientation

Пользователь должен понимать:

- где он находится;
- к какому месту относится объект;
- как вернуться;
- что находится рядом;
- какой режим открыт;
- изменяет ли он мир или только смотрит.

### Minimum orientation set

- place name;
- breadcrumb or spatial context;
- back/home;
- map/list switch;
- edit/view mode indicator;
- privacy indicator.

---

## 9. Map

Карта может помогать видеть:

- места;
- связи;
- пути;
- масштаб;
- приватные зоны;
- текущую позицию.

Но карта не должна:

- превращаться в карту уровней;
- показывать completion;
- подсвечивать undiscovered areas;
- создавать fog of war;
- ранжировать места;
- намекать, что сад недостаточно заполнен.

### Alpha

Simple schematic map.

Not a miniature simulation.

---

## 10. Search

Search is a primary capability, not an emergency exit from spatial design.

Search can find:

- place;
- ritual;
- object;
- memory;
- epoch;
- snapshot;
- user-authored text.

### Search result

Each result shows:

- literal title;
- entity type;
- place context;
- date where relevant;
- privacy;
- direct open;
- reveal in world.

---

## 11. Recent and favorites

### Recent

Generated from actual use.

Must not imply preference.

### Favorites

Explicitly selected by the user.

Garden does not calculate:

- favorite place;
- most important ritual;
- strongest memory;
- best route.

---

## 12. Paths

Paths may support:

- orientation;
- visual composition;
- transitions;
- place connection.

They do not:

- gate access;
- indicate progress;
- represent life stages automatically;
- force sequence.

A place may have no path and remain directly accessible.

---

## 13. Camera

Camera behavior strongly affects comfort.

Requirements:

- stable defaults;
- no automatic dramatic movement;
- no unsolicited zoom;
- no forced first-person view;
- reduced-motion option;
- reset view;
- remembered per-place preference.

### Modes

- overview;
- place;
- detail;
- list.

No cinematic mode by default.

---

## 14. Mode clarity

Garden distinguishes:

- View;
- Edit;
- Review;
- Archive;
- Safety.

The user always knows whether an action:

- only changes view;
- changes layout;
- changes data;
- changes history;
- affects permissions.

No invisible mode switching.

---

## 15. Breadcrumbs

Breadcrumbs can be spatial and semantic.

Example:

```text
Garden → Water Place → Bench → Memory
```

This helps connect:

- world;
- place;
- object;
- content.

Breadcrumbs are optional visually but always available in accessible navigation.

---

## 16. One place vs whole garden

Garden should not force constant zooming between global and local.

Possible entry scopes:

- whole garden;
- selected place;
- current ritual;
- object detail.

The user may spend weeks in one place without seeing the whole garden.

That is not incomplete usage.

---

## 17. Attention and distraction

Navigation should avoid:

- moving highlights;
- flashing landmarks;
- animated undiscovered areas;
- constant route suggestions;
- attention-seeking creatures;
- contextual popups during movement.

### Quiet navigation

Controls appear:

- on intent;
- on focus;
- in edit mode;
- through keyboard;
- through command palette.

---

## 18. Accessibility

Spatial interfaces can exclude users with:

- motor limitations;
- low vision;
- vestibular sensitivity;
- cognitive load sensitivity;
- screen-reader use;
- limited device performance.

### Requirements

- full list/tree representation;
- keyboard operation;
- screen-reader labels;
- no precision dragging requirement;
- reduced motion;
- zoom-independent text;
- direct open;
- logical focus order;
- no audio-only orientation.

---

## 19. Mobile navigation

Mobile requires a different interaction model.

Avoid:

- tiny freeform canvas;
- gesture-only controls;
- hidden edge gestures;
- accidental layout changes.

### Alpha mobile

- place cards;
- direct open;
- simple pan/zoom;
- edit handles;
- map/list switch;
- bottom navigation where needed.

---

## 20. Notifications and deep links

A notification may open directly to:

- ritual;
- place;
- memory review;
- setting.

It must not drop the user into an unexplained world position.

Deep link landing shows:

- what opened;
- where it belongs;
- how to exit;
- privacy context.

---

## 21. History navigation

History may be navigated through:

- timeline;
- epochs;
- snapshots;
- changes;
- place history.

No single mandatory chronology.

The user can return from history to current state clearly.

---

## 22. Trigger Round

### Problem

How can navigation preserve the experience of a world without making access slow or theatrical?

### Trigger 1 — Innovation

**Prompt:** «А что если до решения всего один клик или тап?»

**Hypothesis:** Every important entity can be opened directly from global navigation.

**Outcome:** accepted principle.

### Trigger 2 — Human-centric

**Prompt:** «А что если идея ограничивает выбор?»

**Hypothesis:** Spatial and direct navigation must remain equal, not primary and fallback.

**Outcome:** accepted boundary.

### Trigger 3 — Graphic Design

**Prompt:** «А что если создать структуру?»

**Hypothesis:** A stable hierarchy of Garden → Place → Object → Content can improve orientation.

**Outcome:** candidate architecture.

### Trigger 4 — Storytelling

**Prompt:** «А что если поделить на части?»

**Hypothesis:** Garden may be experienced place by place rather than as one continuous world.

**Outcome:** accepted direction.

### Trigger 5 — Business Design

**Prompt:** «А что если людям нравится работать за вас?»

**Hypothesis:** Users may create their own shortcuts, home places and navigation structures.

**Outcome:** candidate personalization.

### Rejected interpretation

Adding travel friction to make the world feel larger is rejected when it slows access or turns rituals into game traversal.

---

## 23. Navigation architecture

```yaml
garden_navigation:
  entry:
    default_target:
    remember_last_position:
    quiet_overview:
  spatial:
    enabled:
    map:
    paths:
    landmarks:
    camera_mode:
  direct:
    search:
    place_list:
    ritual_list:
    recent:
    user_favorites:
    command_palette:
  orientation:
    current_place:
    breadcrumbs:
    privacy_indicator:
    mode_indicator:
  accessibility:
    list_tree:
    keyboard:
    reduced_motion:
    direct_open:
```

---

## 24. Alpha navigation set

1. Quiet overview.
2. Place list.
3. Simple schematic map.
4. Global search.
5. Recent.
6. User favorites.
7. Direct deep links.
8. Breadcrumbs.
9. View/Edit mode distinction.
10. Reduced-motion and list-only mode.

---

## 25. Alpha experiments

### A — Spatial-first vs equal dual navigation

Measure:

- orientation;
- delight;
- speed;
- frustration;
- perceived gamefulness.

### B — Last place vs quiet overview entry

Measure preference and continuity.

### C — Map vs place list

Measure comprehension and accessibility.

### D — Breadcrumb visibility

Measure context understanding.

### E — Travel animation

Compare optional transition and instant open.

### F — One-place usage

Test whether Garden still feels complete when a user ignores the global world.

---

## 26. Candidate principles

1. Movement creates experience; access never depends on movement.
2. Spatial and direct navigation are equal.
3. Search is primary.
4. Every destination has a direct route.
5. Every direct result can reveal spatial context.
6. No forced walking or travel time.
7. No fog of war or completion map.
8. Entry point is user-controlled.
9. Return has no guilt ritual.
10. Mode is always visible.
11. Recent is not favorite.
12. Accessibility is not a fallback.
13. One-place usage is complete.
14. Camera never performs meaning.
15. Navigation does not simulate progress.

---

## 27. What Garden must not claim

- spatial navigation is more meaningful than direct access;
- slower movement increases attachment;
- a map must reveal the whole world;
- frequent return means a place is important;
- recent means favorite;
- one-place usage is incomplete;
- physical paths represent psychological progress;
- hidden areas create curiosity without cost;
- camera movement can safely direct emotion;
- spatial interfaces are inherently intuitive.

---

## 28. Claim Registry

| Claim | Confidence | Status |
|---|---:|---|
| Landmarks and stable structure can support orientation | high | foundation |
| Spatial navigation alone is sufficient for accessibility | rejected | boundary |
| Direct search weakens the world metaphor | low | rejected |
| Dual navigation may balance experience and efficiency | medium | Alpha hypothesis |
| Travel friction increases meaning | low | rejected |
| User-controlled entry may support continuity | medium | Alpha hypothesis |
| Breadcrumbs may improve context | medium-high | candidate |
| Recent use indicates preference | low | rejected |
| One-place usage can be complete | normative/product principle | required |
| Navigation should expose mode and privacy context | high | safety foundation |

---

## 29. Verdict

Garden should be a world a person can move through, but never a world they must traverse to reach themselves.

> **You may wander. You may also arrive directly. Both are Garden.**
