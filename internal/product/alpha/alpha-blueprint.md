---
title: "Garden Alpha Blueprint v2"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# Garden Alpha Blueprint v2

**Дата:** 16 июля 2026  
**Статус:** `draft for validation`  
**Основание:** Living Canon v1

---

## 1. Что проверяет Alpha

Alpha проверяет не только метод ритуалов.

Он проверяет целостный минимальный опыт Garden:

> человек приносит важное, создаёт ритуал, превращает его в объект собственного сада, живёт его в реальности и возвращается, чтобы изменить, продолжить, завершить или отпустить.

Две неразделимые гипотезы:

1. Garden помогает перейти от смысла к бережному действию без давления.
2. Личный визуальный сад создаёт чувство владения, красоты и эмоциональной ценности без превращения в score.

---

## 2. Целевая ситуация

Первый пользователь:

- взрослый 18+;
- имеет одну текущую тему или направление;
- уже размышляет о себе;
- пробовал заметки, habits или generic AI;
- не ищет терапию;
- не находится в high-risk сценарии;
- хочет небольшое действие без жёсткой системы;
- ценит визуальную среду и собственное пространство.

Job:

> «Помоги мне превратить то, что важно сейчас, в один живой ритуал и дать ему место в моём саду без чувства, что я снова должна идеально что-то выполнять».

---

## 3. Alpha promise

> **Создай один ритуал для того, что важно сейчас. Посади его в своём саду. Живи его в удобном ритме и меняй без чувства провала.**

---

## 4. Что входит в Alpha

### Обязательно

- Current Direction;
- Ritual Creation;
- Meaningful Minimum;
- Support Choice;
- Visual Garden Space;
- Ritual Object;
- Placement;
- Bounded Review;
- Continue / Adapt / Rest / Complete / Release;
- Memory confirmation;
- export/delete;
- literal labels;
- privacy explanation.

### Не входит

- full social graph;
- community;
- leaderboards;
- passive sensing;
- wearables;
- clinical features;
- AI friend;
- full content library;
- marketplace;
- employer use;
- multiplayer farm;
- autonomous agents;
- public profiles;
- monetization loops.

---

## 5. Core entities

### Current Direction

```yaml
direction_id:
title:
user_words:
why_now:
known:
assumed:
unknown:
context:
```

### Ritual

```yaml
ritual_id:
direction_id:
title:
meaning:
primary_form:
meaningful_minimum:
alternative_form:
frequency_type:
context:
resources:
support_mode:
review_time:
lifecycle_status:
```

### Garden Object

```yaml
object_id:
ritual_id:
object_type:
appearance:
position:
customization:
user_meaning:
transformation_history:
archive_state:
```

### Review

```yaml
review_id:
ritual_id:
event_anchor:
facts:
context:
user_meaning:
ai_hypotheses:
choice:
memory_decision:
```

---

## 6. Core loop

### Step 1 — Bring something important

Prompt:

> «Что сейчас хочется не просто понять, а дать этому место в жизни?»

### Step 2 — Clarify

Garden separates:

- факт;
- потребность;
- контекст;
- неизвестное;
- влияние других людей/систем.

### Step 3 — Create ritual

Prompt:

> «Какое маленькое действие могло бы выразить это в реальной жизни?»

The user chooses:

- full form;
- meaningful minimum;
- alternative;
- timing;
- support.

### Step 4 — Give it a form in the garden

The user chooses:

- plant;
- object;
- place;
- path;
- water element;
- structure;
- symbolic item.

### Step 5 — Place it

The user chooses where it lives.

No AI automatic placement.

### Step 6 — Live outside the app

Garden closes the session.

### Step 7 — Return at chosen time

No daily requirement.

### Step 8 — Bounded review

Garden asks:

- Что произошло?
- Что помогло?
- Что изменилось?
- Что было не под твоим контролем?
- Что теперь хочется сделать?

### Step 9 — Choose lifecycle

- Continue;
- Adapt;
- Rest;
- Complete;
- Release.

### Step 10 — Garden transformation

User chooses whether the object:

- stays;
- changes;
- moves;
- becomes decorative;
- goes to archive;
- disappears.

---

## 7. Minimum visual experience

Alpha needs one garden screen.

### Required

- one viewport;
- free placement;
- 6–10 object templates;
- 3–5 environment customization options;
- empty space;
- basic animation;
- day/night or light variation;
- no hidden performance state;
- no decay;
- user-controlled transformation.

### Optional

- ambient sound;
- weather;
- small discoveries;
- object descriptions;
- ritual history on tap.

### Not allowed

- plant wilting after absence;
- forced harvest;
- timers;
- locked objects;
- energy;
- currency;
- streak reward;
- comparative rarity.

---

## 8. First object set

Potential mappings:

- tree;
- flower;
- path;
- bench;
- pond;
- lantern;
- greenhouse;
- stone circle;
- bridge;
- small house.

User chooses the meaning.

No fixed mapping such as:

- sleep = house;
- creativity = flower;
- relationships = bridge.

Garden may offer examples, not ontology.

---

## 9. AI role

Modes:

- Clarify;
- Ritual Design;
- Review;
- Fresh View;
- Safety Boundary.

AI does not:

- auto-name identity;
- auto-transform the garden;
- assign object meaning;
- infer emotional health;
- push daily return;
- claim causality;
- create a secret profile.

---

## 10. Support modes

- none;
- one reminder;
- chosen check-in;
- preparation message;
- user-initiated only.

Default: no support until chosen.

No:

- escalating reminders;
- “we missed you”;
- guilt;
- social notification;
- disappearing reward.

---

## 11. Measurement modes

### M0 — No tracking

Only ritual setup and review.

### M1 — Event note

User records only when useful.

### M2 — Chosen check-in

Limited cadence.

### M3 — Experiment

Specific question and end date.

Alpha default: M0 or M1.

No score.

---

## 12. Alpha screens

### Screen 1 — Welcome

- human premise;
- boundaries;
- privacy;
- not therapy;
- not habit tracker.

### Screen 2 — What matters now

- direction input;
- fact/context prompts.

### Screen 3 — Create ritual

- action;
- meaningful minimum;
- support;
- cadence.

### Screen 4 — Choose garden form

- object selection;
- appearance;
- meaning.

### Screen 5 — Place in garden

- free placement;
- preview;
- edit.

### Screen 6 — Garden home

- visual world;
- ritual objects;
- no score;
- no task list by default.

### Screen 7 — Ritual detail

- meaning;
- form;
- support;
- history;
- lifecycle.

### Screen 8 — Review

- bounded reflection;
- lifecycle choice;
- transformation.

### Screen 9 — Memory and privacy

- what Garden remembers;
- edit/delete.

### Screen 10 — Archive

- completed/released rituals;
- restore/delete.

---

## 13. Research design

### Stage 0 — concept and visual comprehension

5–8 participants.

Test:

- Do people understand ritual?
- Do they feel ownership?
- Do they read visual state as score?
- Is the garden too childish?
- Is the world emotionally attractive?
- Does literal mode remain clear?

### Stage 1 — concierge prototype

12–18 participants.

Duration: up to 14 days.

No daily requirement.

Each participant:

- creates one direction;
- creates one ritual;
- places one object;
- chooses support;
- returns once or twice;
- completes one review.

### Stage 2 — comparator

Compare:

- Garden;
- plain note + reminder;
- generic AI chat;
- habit tracker.

---

## 14. Primary outcomes

- real-world action or intentional non-action;
- sense of ownership;
- emotional value;
- clarity;
- low pressure;
- adaptation;
- completion;
- calibrated trust;
- value beyond comparator;
- desire to customize the garden.

---

## 15. Guardrails

- guilt;
- anxiety after absence;
- interpreting garden as score;
- attachment to AI rather than space;
- rumination;
- false pattern acceptance;
- unwanted disclosure;
- pressure to decorate;
- feeling childish;
- visual overload;
- dependence;
- replacement of source change with coping.

---

## 16. Success signals

- user says “это мой сад”;
- user freely changes the object;
- user completes or releases ritual without shame;
- user returns because of ownership/delight, not fear;
- user understands AI hypothesis as hypothesis;
- user acts outside the app;
- user can explain what Garden does not know;
- user can leave without loss.

---

## 17. Kill criteria

Stop or redesign if:

- garden feels like hidden progress score;
- users fear objects will deteriorate;
- ritual language feels obligatory;
- visual layer adds no value;
- simple note performs equally;
- users primarily seek AI friendship;
- privacy boundaries are misunderstood;
- value requires daily return;
- users feel judged;
- deletion is incomplete;
- researchers need broad access to raw data;
- safety reviewers reject the setup.

---

## 18. Technical minimum

- encrypted storage;
- no provider training;
- no raw text in analytics;
- explicit model provider;
- source-aware memory;
- full deletion;
- role-based research access;
- no social graph;
- no passive data;
- deterministic lifecycle states;
- user-controlled garden layout.

---

## 19. Alpha team roles

- Product owner;
- UX researcher;
- Product designer;
- Visual/game designer;
- AI interaction designer;
- Privacy reviewer;
- Security reviewer;
- Safety/clinical advisor;
- Engineer;
- Research operations owner.

No one person can waive safety gates.

---

## 20. DoD before recruitment

- Living Canon accepted;
- clickable garden prototype;
- data-flow diagram;
- DPIA draft;
- consent;
- participant information;
- crisis boundary;
- researcher-access policy;
- AI response protocol;
- deletion test;
- adverse-event log;
- interview guide;
- analysis plan;
- owner and safety sign-off.
