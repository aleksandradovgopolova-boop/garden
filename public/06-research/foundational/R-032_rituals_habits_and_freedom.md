---
title: "R-032 — Ритуалы, привычки и свобода"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-032 — Ритуалы, привычки и свобода

**Версия:** 0.1  
**Дата:** 17 июля 2026  
**Статус:** design research / rituals, habits and behavioral autonomy  
**Контур:** Garden Atlas → Rituals / Time / AI / Safety

---

## 1. Главный вопрос

> Как Garden может помогать человеку замечать, сохранять и развивать значимые повторяющиеся практики, не превращая их в задачи, streak, обязанность, норму или систему управления поведением?

---

## 2. Главный вывод

Garden различает:

1. **Task** — действие с ожидаемым завершением.
2. **Habit** — повторяемое поведение.
3. **Routine** — организованная последовательность действий.
4. **Ritual** — практика, ценность которой может находиться в самом переживании, значении, контексте и повторении.

Эти сущности могут пересекаться, но не являются взаимозаменяемыми.

### Core principle

> **Garden does not manage behavior. It helps people notice and shape meaningful practices.**

---

## 3. Task

Task обычно имеет:

- формулировку;
- ожидаемый результат;
- статус;
- дедлайн или момент завершения;
- понятие done.

Примеры:

- отправить письмо;
- оплатить счёт;
- записаться к врачу.

Garden может хранить связанные действия, но не должен превращать каждый ритуал в task.

---

## 4. Habit

Habit — повторяемое поведение, которое может становиться более автоматическим в определённом контексте.

Примеры:

- пить воду после пробуждения;
- открывать книгу перед сном;
- выходить на прогулку после обеда.

Habit может быть:

- полезной;
- нейтральной;
- нежелательной;
- сознательной;
- автоматической.

Garden не маркирует привычки как хорошие и плохие без пользовательского определения.

---

## 5. Routine

Routine — организованная последовательность.

Например:

```text
вода → зарядка → душ → завтрак
```

Routine может быть:

- практичной;
- временной;
- необходимой;
- устойчивой;
- скучной;
- поддерживающей.

Routine не обязана иметь символическое значение.

---

## 6. Ritual

Ritual может включать:

- повторяемость;
- последовательность;
- предметы;
- место;
- атмосферу;
- время;
- намерение;
- личный смысл.

Пример:

```text
включить лампу
заварить чай
открыть книгу
сесть у окна
```

Для habit tracker это четыре поведения.

Для Garden это может быть одно целостное переживание.

### Principle

> A ritual is not merely a checklist with better language.

---

## 7. Ritual does not require transcendence

Garden не романтизирует каждую практику.

Ритуал может быть:

- бытовым;
- простым;
- смешным;
- неидеальным;
- коротким;
- нерегулярным;
- без глубокой символики.

Человек может назвать ритуалом:

- вечерний чай;
- музыку по дороге;
- пятничную пиццу;
- звонок близкому;
- пять минут тишины.

Система не решает, достаточно ли это «значимо».

---

## 8. No universal definition of completion

Ритуал может завершаться:

- после последнего действия;
- после выбранного времени;
- когда человек сам почувствовал завершение;
- без отдельной точки завершения.

### Garden options

- no completion;
- manual mark;
- soft ending;
- time window;
- user-authored signal;
- retrospective note.

No default threshold.

---

## 9. Absence is not failure

Если ритуал не произошёл, Garden не создаёт отдельное событие failure.

Отсутствие записи означает только:

> в системе нет сохранённого события.

Оно не означает автоматически:

- ритуал пропущен;
- пользователь сорвался;
- последовательность нарушена;
- практика потеряна;
- цель провалена.

### Core rule

> **No event is not the same as a failed event.**

---

## 10. No streak

Garden Alpha does not use:

- daily streak;
- longest streak;
- broken chain;
- recovery token;
- freeze token;
- missed-day warning;
- consistency score.

### Why

Streak changes the meaning of repetition:

from:

> «Я возвращаюсь к практике, когда она мне нужна.»

to:

> «Я продолжаю, чтобы не потерять число.»

Garden may later show descriptive history only by explicit request.

---

## 11. Frequency

Frequency may matter practically.

Examples:

- medication;
- rehabilitation;
- professional training;
- scheduled care.

But those cases differ from personal ritual.

### Garden distinction

```yaml
frequency:
  descriptive:
  planned:
  safety_critical:
```

Personal ritual defaults to descriptive or no frequency.

Safety-critical schedules require a separate domain and must not be romanticized as rituals.

---

## 12. Quality

Garden does not score ritual quality.

No:

- five stars;
- enough/not enough;
- effective/ineffective;
- ideal duration;
- perfect execution;
- AI praise after every occurrence.

Possible user-authored reflection:

- how it felt;
- what changed;
- what was difficult;
- whether to adjust;
- free note.

---

## 13. Duration

Five minutes can be complete.

Two hours can feel unfinished.

Duration is metadata, not value.

### Rule

Garden never implies:

- longer is better;
- more frequent is better;
- more complex is deeper.

---

## 14. Ritual occurrence

An occurrence is a user-recorded instance.

```yaml
ritual_occurrence:
  occurrence_id:
  ritual_id:
  started_at:
  ended_at:
  recorded_at:
  record_mode:
  place_id:
  components_used:
  user_note:
  user_state_note:
  source:
```

All fields except identity and provenance may be optional.

---

## 15. Record modes

- **None** — practice exists without logging.
- **Manual** — user saves an occurrence.
- **Retrospective** — user records later.
- **Lightweight** — one quiet action.
- **Detailed** — optional note and components.
- **Imported** — from another source with provenance.

### Principle

A ritual remains real even when it is not logged.

---

## 16. Ritual lineage

A ritual may evolve.

Example:

```text
tea → book
```

later:

```text
tea → music → book → candle
```

Garden should support lineage:

```yaml
ritual_lineage:
  lineage_id:
  ritual_versions:
  parent_version:
  changed_components:
  changed_meaning:
  preserved_name:
  user_note:
```

### Important distinction

A version records configuration.

Lineage records continuity perceived by the user.

The system does not decide whether a change created a new ritual.

---

## 17. One action in multiple rituals

An action may belong to several contexts.

Example:

`walk` may belong to:

- morning;
- recovery;
- creative thinking;
- time with a close person.

Garden therefore avoids rigid ownership.

```yaml
ritual_component_link:
  component_id:
  ritual_ids:
  role_by_ritual:
```

---

## 18. Components

A ritual may contain:

- action;
- object;
- place;
- person;
- sound;
- light;
- text;
- preparation;
- transition;
- ending.

Components can be:

- required by user;
- optional;
- common;
- remembered;
- no longer used.

Garden does not convert all components into checkboxes.

---

## 19. Ritual and place

A ritual may be:

- tied to one place;
- possible in several places;
- independent of place;
- moved over time.

Place can support ritual recognition, but does not authenticate it.

A ritual performed elsewhere is not invalid.

---

## 20. Ritual and time

A ritual may relate to:

- clock time;
- daypart;
- event;
- season;
- epoch;
- subjective readiness;
- another ritual.

Examples:

- after waking;
- before sleep;
- when returning home;
- during rain;
- when work ends;
- when needed.

Garden does not force calendar schedules.

---

## 21. Ritual lifecycle

```yaml
ritual_state:
  forming:
  lived:
  resting:
  transformed:
  preserved:
  archived:
  ended:
```

All transitions are user-controlled.

### No automatic states

- inactive;
- failed;
- abandoned;
- broken;
- neglected.

---

## 22. Ending a ritual

A ritual may end because:

- it no longer fits;
- circumstances changed;
- the person chooses another form;
- it belonged to an epoch;
- it completed its role.

Ending is not failure.

Garden may preserve:

- history;
- lineage;
- objects;
- memories;
- user explanation.

---

## 23. AI role

AI may help:

- notice repeated patterns in user-provided data;
- ask whether a practice feels meaningful;
- help name or describe;
- suggest alternative forms;
- identify practical friction;
- preserve lineage;
- compare versions.

AI may not:

- declare a ritual from behavior alone;
- prescribe a habit as necessary;
- diagnose avoidance;
- shame inconsistency;
- infer values from repetition;
- optimize frequency without a user-defined goal.

---

## 24. Pattern detection

Pattern detection is sensitive.

Requirements:

- opt-in;
- explain data source;
- show uncertainty;
- ask before creating a ritual;
- allow dismissal;
- no repeated nudging;
- no hidden behavioral profile.

Possible wording:

> «В нескольких записях появляется чай и чтение вечером. Хочешь рассмотреть это как одну практику?»

Not:

> «Мы обнаружили твой вечерний ритуал.»

---

## 25. Suggestions

AI suggestion should be framed as an option.

Examples:

- simplify;
- shorten;
- move;
- split;
- combine;
- pause;
- remove a component;
- create a lighter version.

No default recommendation to intensify.

### Important

“Do less” and “stop” are valid suggestions.

---

## 26. Reflection

Reflection is optional.

Possible prompts:

- Что здесь было важно?
- Что хочется сохранить?
- Что можно убрать?
- Эта практика всё ещё твоя?
- Нужна ли ей другая форма?

Avoid:

- Почему ты не выполнила?
- Что помешало быть последовательной?
- Как повысить дисциплину?
- Как наверстать?

---

## 27. Social rituals

A ritual may include others.

Risks:

- consent;
- unequal expectations;
- exposing private meaning;
- shared history;
- changes by one participant.

Alpha ritual records remain private.

Shared ritual architecture requires separate research.

---

## 28. Metrics

Garden does not use ritual frequency as the north star.

Possible product metrics:

- user-created ritual retained by choice;
- ritual edited;
- ritual archived without friction;
- manual mode use;
- export success;
- perceived autonomy;
- absence guilt;
- usefulness of lineage.

### Guardrails

- streak anxiety;
- perceived judgment;
- unwanted reminders;
- AI overreach;
- pressure to log;
- pressure to intensify.

---

## 29. Trigger Round

### Problem

How can Garden support repetition without converting it into compliance?

### Trigger 1 — Human-centric

**Prompt:** «А что если не создавать привычку?»

**Hypothesis:** Garden first helps notice existing practices and asks whether they deserve form.

**Outcome:** accepted direction.

### Trigger 2 — Storytelling

**Prompt:** «А что если история уже происходит?»

**Hypothesis:** Ritual history may predate creation of the Garden entity.

**Outcome:** accepted architecture through retrospective occurrences.

### Trigger 3 — Business Design

**Prompt:** «А что если бросить вызов главному тренду?»

**Hypothesis:** Garden rejects streak as both product mechanic and strategic position.

**Outcome:** accepted boundary and brand hypothesis.

### Trigger 4 — Innovation

**Prompt:** «А что если убрать понятие выполнения?»

**Hypothesis:** Ritual supports occurrence, experience, preservation, transformation and ending instead of binary completion.

**Outcome:** Alpha experiment.

### Trigger 5 — Naming

**Prompt:** «А что если назвать через действие?»

**Hypothesis:** User can name a ritual through a lived phrase rather than a category.

Examples:

- «Читать у окна»
- «Вернуться к себе после работы»
- «Пицца и музыка в пятницу»

**Outcome:** candidate naming pattern.

### Rejected interpretation

Automatic habit coaching based on inactivity is rejected.

---

## 30. Ritual architecture

```yaml
garden_ritual:
  ritual_id:
  user_name:
  literal_name:
  description:
  components:
  time_relation:
  place_ids:
  lineage_id:
  lifecycle_state:
  record_mode:
  reflection_mode:
  planned_frequency:
  reminders:
  user_meaning:
  provenance:
```

### Invariants

- no streak fields;
- no failed occurrence;
- no quality score;
- no automatic lifecycle transition;
- no inferred meaning;
- no required logging;
- no AI-created ritual without confirmation.

---

## 31. Alpha ritual set

1. Create from scratch.
2. Create retrospectively from an existing practice.
3. Optional place and time relations.
4. Components without mandatory checklist.
5. No completion by default.
6. Quiet manual occurrence.
7. Optional reflection.
8. Lineage and version history.
9. Rest, transform, archive or end.
10. AI pattern suggestion only on request or explicit opt-in.
11. No streak.
12. No consistency score.

---

## 32. Alpha experiments

### A — Completion vs occurrence language

Measure:

- pressure;
- clarity;
- perceived value;
- understanding.

### B — Streak vs descriptive history vs no frequency

Measure guilt, motivation and meaning.

### C — Checklist components vs holistic ritual

Measure usefulness and fragmentation.

### D — Retrospective creation

Test whether users can recognize existing practices without planning a new habit.

### E — Lineage

Measure whether evolution feels more faithful than replacement.

### F — No-log ritual

Test whether users understand that a ritual can exist without recording.

---

## 33. Candidate principles

1. Ritual is not a decorated task.
2. No event is not a failed event.
3. No streak.
4. Logging is optional.
5. Completion is optional.
6. Duration is not value.
7. Quality is not scored.
8. Frequency is not moral.
9. Components need not be checkboxes.
10. One action may belong to several rituals.
11. Lineage preserves continuity without forcing sameness.
12. Ending is not failure.
13. AI notices only with consent.
14. AI does not prescribe meaning.
15. Doing less is a valid evolution.
16. Manual and retrospective creation are equal.
17. Rituals can exist outside Garden.

---

## 34. What Garden must not claim

- repetition proves meaning;
- consistency proves commitment;
- longer rituals are deeper;
- missed days damage a ritual;
- logging is required for awareness;
- AI can discover true rituals from behavior;
- every routine should become a ritual;
- ending means failure;
- frequency reveals values;
- streaks are necessary for motivation;
- rituals are inherently beneficial;
- Garden creates meaning on behalf of the user.

---

## 35. Claim Registry

| Claim | Confidence | Status |
|---|---:|---|
| Habit, routine, task and ritual are distinct but overlapping concepts | high | foundation |
| Streaks are necessary for sustained behavior | low | rejected |
| Logging is necessary for a ritual to exist | rejected | product boundary |
| Holistic ritual representation may reduce fragmentation | medium-low | Alpha hypothesis |
| Retrospective recognition may support authorship | medium | Alpha hypothesis |
| Absence should be recorded as failure | rejected | boundary |
| Ritual lineage may preserve continuity | medium | product hypothesis |
| AI can reliably infer personal meaning from repetition | low | rejected |
| Optional reflection may support adaptation | medium | candidate |
| Ending a ritual can be a legitimate lifecycle event | high | foundation |

---

## 36. Verdict

Garden should not build a better cage for habits.

It should help a person notice the forms of repetition that already carry life, choose what to preserve, change what no longer fits and let go without failure.

> **A ritual is not something Garden makes the person obey. It is something the person may choose to recognize as their own.**
