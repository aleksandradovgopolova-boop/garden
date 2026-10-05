---
title: "Garden Measurement Model"
status: proposed
owner: "Product"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: false
---

# Garden Measurement Model

**Версия:** 0.1  
**Статус:** `proposed`  
**Контур:** `03_product/measurement/measurement_model.md`

---

## 1. Основной принцип

> Measure less. Explain more. Stop when the measurement no longer supports a decision.

Garden не требует данных для существования практики.

---

## 2. Measurement modes

### M0 — No tracking

Практика существует без записей и score.

### M1 — Event record

- happened;
- adapted;
- intentionally skipped;
- not recorded.

### M2 — Context note

Одна добровольная заметка или выбранный context tag.

### M3 — Temporary experiment

Ограниченный срок, вопрос и заранее определённые данные.

### M4 — Periodic reflection

Редкий review, ориентированный на решение.

### M5 — Research mode

Отдельное согласие, protocol, burden monitoring и research governance.

Переход вверх только по явному выбору.

---

## 3. Measurement Contract

```yaml
measurement_id:
question:
purpose:
decision_supported:
mode:
frequency:
recall_period:
data_fields:
derived_outputs:
known_limits:
attention_effect:
visibility:
retention:
review_date:
pause_control:
delete_control:
status:
```

---

## 4. Event semantics

`not_recorded` хранится отдельно от `did_not_happen`.

`adapted` не считается partial failure.

`intentionally_skipped` не получает negative score.

`completed` завершает measurement by default.

---

## 5. Derived Observation Card

```yaml
observation:
source_events:
period:
recorded_n:
missing_n:
exceptions:
within_or_between_person:
association_only:
alternative_explanations:
user_confirmed:
expires_at:
```

---

## 6. Display rules

Каждый график:

- показывает пропуски;
- не соединяет отсутствующие точки как наблюдения;
- показывает период;
- позволяет скрыть trend line;
- не использует red/green moral encoding;
- не показывает normative benchmark по умолчанию;
- не делает причинный заголовок;
- позволяет открыть raw events;
- показывает изменение определения шкалы;
- имеет текстовое описание ограничений.

---

## 7. Prohibited scores

- Garden Score;
- Flourishing Score;
- Self-Care Score;
- Balance Score;
- Emotional Stability;
- Reliability of Commitment;
- Personality Risk;
- Compliance Likelihood;
- Relationship Health;
- Hidden Vulnerability Segment.

---

## 8. Permitted calculations

С ограничениями:

- count;
- duration;
- frequency;
- missingness;
- range;
- user-defined average;
- simple co-occurrence;
- change relative to explicitly selected period.

Любой расчёт имеет purpose, provenance и expiry.

---

## 9. Pattern threshold

Pattern feedback возможен, если:

- минимум 6 записанных событий;
- минимум 3 события каждого сравниваемого типа, если применимо;
- показаны missing data;
- есть минимум одно исключение или явно указано его отсутствие;
- не заявляется причинность;
- пользователь может отвергнуть;
- решение обратимо.

Порог является safety hypothesis и требует эмпирической настройки.

---

## 10. Metrics for Garden

### Human value

- clarity;
- agency;
- real-life action;
- adaptation;
- completion;
- transfer;
- honest reporting;
- reduced need for tracking.

### Measurement safety

- burden;
- unwanted prompts;
- response manipulation;
- compulsive checking;
- false pattern acceptance;
- difficulty stopping;
- distress from graphs;
- correction and deletion success.

### Product metrics not used as success alone

- DAU;
- number of records;
- data completeness;
- time in dashboard;
- score improvement;
- number of tracked practices.

---

## 11. Exit

Measurement can be paused, deleted or completed without affecting the practice itself.

Garden does not create empty-bed, wilted-plant or lost-progress states after exit.

---

## 12. Status

Не входит в Garden Bible до принятия GDR-011.
