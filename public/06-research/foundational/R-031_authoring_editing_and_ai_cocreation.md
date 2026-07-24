---
title: "R-031 — Авторство, редактирование и совместное создание с AI"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-031 — Авторство, редактирование и совместное создание с AI

**Версия:** 0.1  
**Дата:** 17 июля 2026  
**Статус:** design research / authoring, editing and AI co-creation  
**Контур:** Garden Atlas → Authoring / AI / Versions / Safety

---

## 1. Главный вопрос

> Как человек создаёт и изменяет Garden вместе с AI так, чтобы система помогала формулировать, собирать и пробовать варианты, но не подменяла авторство, не применяла изменения молча и не превращала пользователя в редактора чужой версии его собственного мира?

---

## 2. Главный вывод

Garden должен различать:

1. **View** — наблюдение без изменения.
2. **Draft** — подготовка изменений вне текущего мира.
3. **Preview** — просмотр последствий.
4. **Apply** — явное принятие.
5. **Undo** — быстрый возврат.
6. **Version** — сохранённое состояние.
7. **Proposal** — предложение AI или другого автора.
8. **Commit** — зафиксированное пользовательское изменение.

### Core principle

> **AI may expand the field of possibilities. Only the user decides what becomes real.**

---

## 3. Почему авторство критично

Garden хранит не только данные, но и:

- личные места;
- ритуалы;
- связи;
- память;
- визуальные решения;
- пользовательские значения.

Поэтому редактирование затрагивает:

- контроль;
- идентичность;
- доверие;
- приватность;
- историю;
- ощущение собственного мира.

Даже визуально «лучшее» изменение может ощущаться как вторжение, если его сделал продукт без разрешения.

---

## 4. View and Edit

View и Edit должны быть различимы всегда.

### View

- можно перемещаться;
- открывать;
- читать;
- слушать;
- просматривать историю;
- не менять структуру.

### Edit

- можно размещать;
- перемещать;
- связывать;
- переименовывать;
- менять атмосферу;
- удалять;
- создавать варианты.

### Requirements

- явный индикатор режима;
- no accidental drag;
- no hidden autosave of structural change;
- выход из Edit не теряет draft без предупреждения;
- все изменения перечислены перед apply при массовом действии.

---

## 5. Draft-first authoring

Сложные изменения должны сначала существовать как draft.

Примеры:

- новая композиция места;
- перестройка маршрутов;
- AI-generated layout;
- сезонный вариант;
- изменение нескольких объектов;
- импорт структуры.

Draft:

- не влияет на текущий Garden;
- может быть сохранён;
- сравнивается с текущей версией;
- может быть удалён без последствий;
- не считается «незавершённой обязанностью».

---

## 6. Preview

Preview показывает:

- что изменится;
- какие объекты затронуты;
- что останется;
- что будет перемещено;
- какие связи изменятся;
- какие данные удалятся;
- можно ли вернуть.

### Preview is not persuasion

Preview не должен:

- делать новый вариант визуально «правильнее»;
- скрывать потери;
- использовать эмоциональный copy;
- подталкивать принять AI-предложение.

---

## 7. Apply

Изменение становится частью мира только после явного действия.

### Apply levels

#### Immediate

Для малых обратимых изменений:

- перемещение одного объекта;
- смена света;
- переименование.

#### Confirmed

Для заметных структурных изменений:

- удалить место;
- заменить layout;
- изменить privacy;
- архивировать связанную систему;
- применить AI-generated variant.

#### Typed confirmation

Только для редких действительно разрушительных действий.

Garden не использует excessive confirmation fatigue.

---

## 8. Undo and recovery

Undo должен быть:

- доступным;
- понятным;
- не скрытым во временном toast;
- применимым к пространственным изменениям;
- доступным через историю.

### Recovery layers

1. Immediate undo.
2. Session history.
3. Version restore.
4. Trash/recovery period.
5. Export backup.

No destructive action without a recovery story where technically feasible.

---

## 9. Versions

Garden version is a preserved state of:

- place;
- object arrangement;
- ritual system;
- atmosphere;
- whole garden.

### Version metadata

```yaml
version:
  version_id:
  scope:
  created_by:
  created_at:
  source:
  label:
  notes:
  parent_version:
  change_summary:
```

### Rules

- user may name versions;
- AI labels are suggestions;
- exact history remains;
- old versions are not called outdated;
- restoring creates a new current version instead of erasing history.

---

## 10. Proposals

AI changes are proposals.

A proposal includes:

- intent understood by AI;
- assumptions;
- affected scope;
- generated result;
- alternatives;
- risks;
- reversibility;
- confidence where relevant.

### Proposal statuses

- generated;
- viewed;
- edited;
- accepted;
- partially accepted;
- rejected;
- expired by user choice;
- archived.

Rejected proposals do not return as nudges.

---

## 11. Partial acceptance

Пользователь может принять:

- только один объект;
- только атмосферу;
- только название;
- только маршрут;
- только часть текста;
- только один из нескольких ритуалов.

### Principle

> AI output is decomposable.

Garden avoids all-or-nothing acceptance.

---

## 12. AI assumptions

When AI proposes a change, it should surface assumptions such as:

- intended use;
- object priority;
- accessibility constraints;
- desired density;
- preservation requirements;
- privacy scope.

The user can correct assumptions before generation.

AI must not infer:

- psychological need;
- hidden life goal;
- personality;
- emotional symbolism;
- preferred level of growth.

---

## 13. Explainability

Explainability in Garden is practical, not performative.

Useful explanation:

- why an object was placed there;
- which constraint was respected;
- why a route changed;
- what trade-off exists;
- what was preserved.

Not useful:

- theatrical chain-of-thought;
- pseudo-psychological reasoning;
- confidence theatre;
- vague “AI magic”.

---

## 14. User intent as an editable object

For substantial work, Garden may store a user-editable brief:

```yaml
authoring_intent:
  goal:
  must_keep:
  may_change:
  must_not_change:
  desired_feeling:
  practical_constraints:
  accessibility:
  privacy:
```

This brief belongs to the user and can be edited or deleted.

AI should not silently expand the goal.

---

## 15. Manual creation remains complete

Garden must remain usable without AI.

Manual authoring includes:

- create place;
- place object;
- link ritual;
- rename;
- set atmosphere;
- create snapshot;
- manage history.

AI is acceleration and divergence, not the only route to creation.

---

## 16. AI intensity

Possible settings:

- **Off** — no AI suggestions.
- **On request** — AI appears only after explicit invocation.
- **Assistive** — contextual suggestions without auto-apply.
- **Collaborative** — active proposal generation within a declared session.

No autonomous mode in Alpha.

---

## 17. Editing language

Garden avoids judgmental language.

Use:

- current;
- proposed;
- previous;
- alternative;
- preserved;
- removed;
- changed.

Avoid:

- improved;
- fixed;
- optimized;
- cleaner;
- better;
- mature;
- outdated,

unless the user explicitly defines the criterion.

---

## 18. Bulk changes

Bulk changes are high-risk.

Requirements:

- scope preview;
- affected entity count;
- before/after comparison;
- exclusions;
- partial apply;
- undo;
- version created automatically where appropriate.

Examples:

- change all materials;
- move all rituals from one place;
- archive an epoch;
- apply a new visual system.

---

## 19. Import and generation

Imported or generated content must preserve provenance.

For each entity:

- source;
- imported at;
- generated by;
- original file/reference;
- transformations;
- user edits.

No generated object should appear indistinguishable from user-authored history.

---

## 20. Deletion

Deletion must distinguish:

- unlink;
- hide;
- archive;
- move to trash;
- permanently delete.

The UI must explain what happens to linked:

- rituals;
- memories;
- versions;
- places;
- exports.

No object disappears because its parent was edited without showing consequences.

---

## 21. Collaboration readiness

Even though Alpha is private, architecture should prepare for:

- author identity;
- proposal;
- comment;
- approval;
- version;
- conflict;
- restore.

Shared editing requires separate research, but provenance begins now.

---

## 22. Trigger Round

### Problem

How can AI participate deeply in creation without becoming the invisible author?

### Trigger 1 — Human-centric

**Prompt:** «А что если создавать для одного человека?»

**Hypothesis:** AI begins from a user-editable brief rather than a generic template.

**Outcome:** accepted direction.

### Trigger 2 — Innovation

**Prompt:** «А что если до решения всего один клик или тап?»

**Hypothesis:** Small safe changes may be applied in one action with immediate undo.

**Outcome:** candidate with reversibility boundary.

### Trigger 3 — Graphic Design

**Prompt:** «А что если создать структуру?»

**Hypothesis:** Authoring flow follows Draft → Preview → Apply → Version.

**Outcome:** accepted architecture.

### Trigger 4 — Storytelling

**Prompt:** «А что если ваша история развивается прямо сейчас?»

**Hypothesis:** Creation history itself may be preserved as versions and proposals.

**Outcome:** accepted with user control.

### Trigger 5 — Business Design

**Prompt:** «А что если людям нравится работать за вас?»

**Hypothesis:** User effort in shaping AI output is part of ownership, not friction to eliminate entirely.

**Outcome:** strategic hypothesis.

### Rejected interpretation

Fully autonomous “make my garden better” editing is rejected because criteria are ambiguous and authorship becomes invisible.

---

## 23. Authoring architecture

```yaml
garden_authoring:
  mode: view | edit
  ai_intensity: off | on_request | assistive | collaborative
  current_draft:
  active_proposal:
  preview:
  pending_changes:
  undo_stack:
  versions:
  recovery:
```

```yaml
ai_proposal:
  proposal_id:
  user_intent_id:
  assumptions:
  scope:
  changes:
  alternatives:
  preserved_entities:
  removed_entities:
  reversible:
  status:
  provenance:
```

---

## 24. Alpha authoring set

1. Explicit View/Edit switch.
2. Manual creation path.
3. User-editable brief.
4. AI on request.
5. Draft workspace.
6. Before/after preview.
7. Partial acceptance.
8. Immediate undo.
9. Version history.
10. Trash and recovery.
11. Provenance.
12. AI intensity setting.

---

## 25. Alpha experiments

### A — Direct generation vs editable brief

Measure:

- fit;
- authorship;
- correction effort;
- trust.

### B — Auto-apply vs proposal

Measure speed, anxiety and perceived control.

### C — Whole-result vs partial acceptance

Measure ownership and usefulness.

### D — Visible assumptions

Measure clarity and correction quality.

### E — Version labels

Compare AI-generated, literal and user-authored labels.

### F — Manual-only session

Verify Garden remains complete without AI.

---

## 26. Candidate principles

1. AI proposes; user commits.
2. View and Edit are always distinct.
3. Complex changes begin as drafts.
4. Preview shows losses as well as gains.
5. Reversibility is default.
6. AI output is decomposable.
7. Assumptions are visible and editable.
8. Manual creation is complete.
9. Rejected proposals do not return.
10. Provenance is preserved.
11. Restoration creates history, not erasure.
12. Bulk changes require scope review.
13. Editing language remains non-judgmental.
14. AI intensity is user-controlled.
15. User effort can support ownership.

---

## 27. What Garden must not claim

- AI knows the best form of the garden;
- generated means improved;
- faster creation always means better creation;
- user correction is failure;
- full automation increases ownership;
- a beautiful preview justifies hidden loss;
- old versions are outdated;
- more AI involvement means more value;
- AI-generated symbolism reflects the user;
- manual creation is an inferior mode.

---

## 28. Claim Registry

| Claim | Confidence | Status |
|---|---:|---|
| Explicit preview and undo can support control | high | foundation |
| AI auto-apply is necessary for convenience | low | rejected |
| Editable briefs may improve fit | medium | Alpha hypothesis |
| Partial acceptance may increase ownership | medium | Alpha hypothesis |
| Manual mode must remain complete | normative/product boundary | required |
| Provenance supports trust and recovery | high | foundation |
| User effort is always desirable | low | rejected |
| Draft-first flow may reduce anxiety for large changes | medium | Alpha hypothesis |
| AI explanations should expose assumptions and trade-offs | high | design foundation |
| Restoring should preserve prior history | high | foundation |

---

## 29. Verdict

Garden should not make the user approve a finished world created by someone else.

It should let the person shape possibilities, compare them, keep parts, reject parts and remain visible as the author.

> **AI can help imagine the garden. Only the person decides what grows into reality.**
