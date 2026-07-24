---
title: "R-024 — Время и сезоны Garden"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-024 — Время и сезоны Garden

**Версия:** 0.1  
**Дата:** 16 июля 2026  
**Статус:** design research / temporal architecture  
**Контур:** Garden Atlas → Time and Seasons / Memory / World

---

## 1. Главный вопрос

> Как Garden может давать ощущение времени, истории и сезонности, не превращая календарь в систему давления, отсутствие — в нарушение, а мир — в набор ограниченных событий и дедлайнов?

---

## 2. Главный вывод

Garden должен различать несколько видов времени:

- календарное;
- переживаемое;
- событийное;
- памятное;
- мировое;
- пользовательское.

Продуктам обычно удобно работать только с календарным временем:

- сегодня;
- вчера;
- пропущено;
- серия;
- просрочено;
- осталось два дня.

Но человеческий опыт организован сложнее. Восприятие длительности зависит от внимания, нагрузки, контекста и количества событий. Память также сегментирует непрерывный опыт на эпизоды и границы событий.

### Garden position

> **Время в Garden должно добавлять историю, а не создавать долг.**

---

## 3. Calendar time

Календарное время нужно для:

- выбранных reminders;
- review;
- экспорта;
- синхронизации;
- истории изменений;
- юридических и технических журналов.

Но оно не должно становиться главным эмоциональным языком мира.

### Не показывать по умолчанию

- «Вы отсутствовали 17 дней»;
- «Последняя активность»;
- «Ритуал просрочен»;
- «Серия прервана»;
- «Вы потеряли сезон».

### Показывать по запросу

- точную дату события;
- дату создания;
- дату review;
- системный audit trail.

---

## 4. Subjective time

Исследования time perception показывают, что субъективная длительность не является прямой копией физического времени.

На оценку влияют:

- внимание ко времени;
- working-memory load;
- эмоциональный контекст;
- новизна;
- количество событий;
- ожидание;
- ретроспективная реконструкция.

### Garden implication

Нельзя говорить:

> «Прошло достаточно времени, чтобы ритуал стал частью жизни».

Календарь не доказывает:

- интеграцию;
- привычку;
- значимость;
- восстановление;
- готовность.

---

## 5. Event time

Люди воспринимают поток опыта через события и их границы.

Event boundaries могут:

- разделять эпизоды в памяти;
- влиять на temporal order;
- увеличивать субъективную дистанцию между событиями;
- помогать структурировать последовательность.

### Garden translation

История может быть организована не только по датам, но и по событиям:

- до появления пруда;
- после переезда;
- когда был создан первый ритуал;
- период мастерской;
- до завершения проекта;
- время тихой поляны.

### Ограничение

Это пользовательская навигация и narrative device, а не более точная научная модель жизни.

---

## 6. Epochs of the Garden

`Epoch` — пользовательски определённый период истории сада.

```yaml
epoch_id:
name:
start_event:
end_event_optional:
user_description:
places:
rituals:
objects:
snapshot:
calendar_dates_visible:
```

### Примеры

- «Когда появился пруд»;
- «После переезда»;
- «Лето книги»;
- «Период тихих вечеров»;
- «До мастерской».

### Правила

- эпоху создаёт пользователь;
- AI может предложить название только по запросу;
- календарные даты остаются доступными;
- эпоха не становится психологической стадией;
- AI не объявляет новый «сезон жизни» автоматически.

---

## 7. World time

Сад может иметь собственное атмосферное время:

- свет;
- облака;
- ветер;
- погоду;
- сезон;
- рост декоративной среды;
- появление независимой жизни.

World time не зависит от:

- выполнения ритуалов;
- streak;
- регулярности входа;
- пользовательского score.

---

## 8. Time modes

### Timeless

Одна выбранная атмосфера сохраняется.

Примеры:

- вечная весна;
- вечный вечер;
- пасмурный сад;
- ночь с фонарями.

### Manual

Пользователь меняет:

- сезон;
- свет;
- погоду;
- атмосферу.

### Local Year

Сад следует локальному календарю после opt-in.

### Slow Year

Сезоны меняются медленнее реального года.

### Fictional Cycle

Независимый цикл мира.

### Personal Epochs

Визуальные изменения привязаны к пользовательским решениям и событиям, но не к performance.

---

## 9. Seasonality

Seasonality может давать:

- изменение;
- узнаваемый ритм;
- визуальную историю;
- разнообразие;
- новые точки зрения.

Она не должна создавать:

- FOMO;
- limited-time rewards;
- утрату объектов;
- обязательный вход;
- сезонную тревогу;
- коммерческое давление.

### Rule

> Every seasonal element must remain accessible later or be purely ambient.

---

## 10. Seasonal events

Alpha не использует seasonal events.

Позже допустимы:

- атмосферные изменения;
- новые optional scenes;
- архивируемые visual states;
- пользовательское переключение.

Недопустимы:

- «Успей собрать»;
- предмет только за ежедневный вход;
- disappearing ritual;
- exclusive social status;
- countdown;
- платное продление сезона.

Исследования deceptive design in games identify time pressure and FOMO as common manipulative patterns; daily engagement rewards can also become burdensome rather than supportive.

---

## 11. Absence

После долгого отсутствия:

- сад остаётся целым;
- ритуалы не портятся;
- объекты не исчезают;
- животные не страдают;
- накопленного долга нет;
- система не перечисляет пропущенные дни.

### Return experience

Garden opens normally.

Possible neutral copy:

> «Сад остался таким, каким ты его оставила».

Or no copy at all.

### Never

- «Мы скучали»;
- «Ты давно не заходила»;
- «Пока тебя не было…» with loss;
- backlog of missed reviews;
- forced catch-up.

---

## 12. Does the world change while the user is away?

Yes, but only in bounded ambient ways.

Allowed:

- light cycle;
- clouds;
- weather;
- gentle seasonal state if selected;
- independent animal movement;
- non-persistent ambient variation.

Not allowed without user choice:

- permanent object transformation;
- new ritual state;
- archive;
- decay;
- memory creation;
- paid-resource consumption;
- irreversible world change.

### Principle

> The world may live without the user. It may not make decisions about the user.

---

## 13. Pause time

The user can freeze:

- season;
- light;
- weather;
- ambient cycle;
- animation.

This is not cheating.

### Reasons

- aesthetic preference;
- sensory comfort;
- grief;
- attachment to a scene;
- accessibility;
- device constraints;
- dislike of change.

No explanation required.

---

## 14. Calendar visibility

Calendar data has three levels.

### Hidden by default

No dates on garden canvas.

### Available contextually

Ritual detail and archive may show dates.

### Export/audit

Exact timestamps remain available.

### User preference

- exact dates;
- month/year;
- relative labels;
- epochs;
- minimal time.

---

## 15. Memory and temporal distance

Event boundaries can make episodes feel further apart in memory and affect temporal ordering. Recent work continues to show that event structure matters for retrospective duration and distance judgments.

### Garden caution

Visual epochs and garden transformations may alter how people remember sequence and distance.

Garden should not:

- present a generated timeline as objective memory;
- reorder events to create a cleaner story;
- compress quiet periods;
- automatically label turning points;
- hide contradictions.

### User control

- edit epoch boundaries;
- remove AI-created groupings;
- see exact dates;
- preserve ungrouped events;
- mark uncertainty.

---

## 16. Time and autobiographical identity

Autobiographical memory contributes to continuity, but Garden must not turn history into a final identity narrative.

### Allowed

> «Ты назвала этот период “Лето книги”».

### Not allowed

> «Это был период, когда ты наконец стала собой».

### Right to rename

The user can change the name of an epoch later.

---

## 17. Time and ritual lifecycle

Lifecycle is not based only on elapsed time.

### Active

Not defined by recent completion.

### Resting

Chosen, not inferred after inactivity.

### Integrated

Confirmed by the user.

### Completed

Chosen because the ritual’s role is complete.

### Released

Chosen because support is no longer desired.

### Rule

No automatic state transition based on time alone, except explicitly authorized technical expiration.

---

## 18. Reminders

Reminder time belongs to the support contract.

Requirements:

- exact user choice;
- easy snooze or disable;
- no escalation;
- no guilt;
- no automatic compensation for missed reminders;
- timezone-aware;
- quiet hours;
- accessibility.

### Missed reminder

No new state is created.

---

## 19. Time zones and life patterns

Garden must support:

- travel;
- migration;
- daylight-saving changes;
- night shifts;
- irregular schedules;
- multiple homes;
- different calendars where feasible.

### Rule

Device time does not define the person’s correct rhythm.

---

## 20. Seasons and culture

Seasons differ by:

- hemisphere;
- climate;
- latitude;
- local ecology;
- cultural calendar;
- personal experience.

A four-season temperate model is not universal.

### Garden options

- four-season;
- wet/dry;
- local;
- fictional;
- manual;
- timeless.

### Language

Avoid:

> «Весна — время роста».

This is a cultural metaphor, not a universal human fact.

---

## 21. Time and grief

People may want a garden state to remain unchanged after:

- loss;
- separation;
- major transition;
- completion;
- migration.

Garden should allow:

- freeze;
- snapshot;
- memorial place;
- private archive;
- no automatic seasonal shift.

But it must not claim to treat grief or decide when change should resume.

---

## 22. Time and children/ageing

Age-related differences in time perception and memory exist, but Garden does not infer a preferred temporal model from age.

User control remains primary.

---

## 23. Temporal architecture

```yaml
garden_time:
  mode:
    timeless:
    manual:
    local_year:
    slow_year:
    fictional_cycle:
  timezone:
  calendar_visibility:
  season_model:
  frozen:
  ambient_progression:
  user_override:

epochs:
  enabled:
  user_created:
  ai_suggestions:
  exact_dates_visible:
  ungrouped_events_allowed:

ritual_time:
  cadence:
  reminder:
  review:
  lifecycle_time_rules:
    automatic_transition: false

absence:
  permanent_world_changes: false
  backlog: false
  decay: false
  guilt_copy: false
```

---

## 24. Alpha experiments

### A — Calendar-first vs Epoch-first history

Measure:

- comprehension;
- memory confidence;
- emotional value;
- perceived truthfulness;
- narrative pressure.

### B — Timeless vs Local Year

Measure:

- ownership;
- realism;
- pressure;
- cultural fit;
- night-shift mismatch.

### C — Garden after 10-day absence

Show unchanged world.

Measure:

- relief;
- expectation;
- guilt;
- trust;
- perceived liveliness.

### D — Ambient change without permanent change

Test clouds/light/animals while preserving objects.

### E — Freeze time

Check whether freeze feels empowering, unnatural or confusing.

### F — Seasonal FOMO comprehension

Show ethical ambient season and a typical limited-time event as comparator.

---

## 25. Candidate principles

1. Time adds history, not debt.
2. Calendar remains available but not dominant.
3. Events and epochs are user-defined.
4. No automatic narrative turning points.
5. Seasons are optional and culturally configurable.
6. No time-based decay.
7. No FOMO.
8. Absence creates no backlog.
9. World may live but not decide for the user.
10. Freeze time is a legitimate control.
11. Lifecycle does not change on elapsed time alone.
12. Exact dates remain accessible for truthfulness.
13. Garden supports irregular rhythms.
14. Quiet periods are not compressed or treated as empty.

---

## 26. What Garden must not claim

- that subjective time can be inferred from usage;
- that an epoch is an objective life stage;
- that spring represents growth;
- that winter represents rest;
- that a ritual integrates after a fixed number of days;
- that AI can identify turning points reliably;
- that event-based memory is more truthful than dates;
- that seasonal visuals improve wellbeing;
- that time away means disengagement or decline.

---

## 27. Claim Registry

| Claim | Confidence | Status |
|---|---:|---|
| Subjective duration depends on attention and context | high | foundation |
| Event boundaries structure memory and temporal judgments | high | foundation |
| Calendar time is psychologically unimportant | rejected | false simplification |
| Epoch navigation may support meaningful history | low-medium | product hypothesis |
| AI can identify true life chapters | low | rejected |
| Daily rewards can become burdensome and manipulative | medium-high | guardrail |
| Seasonal FOMO is necessary for game engagement | rejected | product choice |
| User-controlled time modes may increase ownership | low | Alpha hypothesis |
| Absence without decay may reduce guilt | low-medium | Alpha hypothesis |
| Exact dates should remain available | normative/integrity | required |

---

## 28. Verdict

Garden should know what time it is when the user needs accuracy.

But it should not use time as a judge.

The garden may have:

- days;
- light;
- seasons;
- weather;
- history;
- epochs;
- memories.

Yet none of these creates an obligation to return.

> **Time in Garden does not take anything away. It only offers ways to notice what changed — and the right to leave everything as it is.**
