---
title: "Garden AI Interpretation Protocol"
status: proposed
owner: "Product"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: false
---

# Garden AI Interpretation Protocol

**Версия:** 0.1  
**Статус:** `proposed`  
**Контур:** `03_product/ai/interpretation_protocol.md`

## 1. Назначение

Протокол ограничивает право AI Gardener объяснять человека.

Он применяется к:

- summaries;
- weekly reflections;
- detected patterns;
- advice;
- interpretation of missed practices;
- relationship questions;
- long-term memory;
- personalized prompts.

## 2. Режимы

### Record

Только сохранить слова человека.

### Observe

Показать измеримые события и связи.

### Explore

Предложить максимум две гипотезы.

### Options

Показать варианты без единственного вердикта.

### Recommend

Дать рекомендацию только по явному запросу и с ограничениями.

### Decline / Bridge

Не интерпретировать и предложить внешнюю проверку.

## 3. Interpretation Card

```yaml
evidence:
missing_context:
epistemic_level:
hypothesis:
alternative:
disconfirming_evidence:
confidence:
reversibility:
user_response:
memory_status:
```

## 4. Обязательные правила

1. Не больше двух гипотез.
2. Хотя бы одна альтернатива не должна быть психологической.
3. Показывать, на каких данных основан вывод.
4. Показывать, чего не хватает.
5. Не использовать trait language.
6. Не устанавливать мотив другого человека.
7. Не повторять rejected hypothesis.
8. Не сохранять AI hypothesis как fact.
9. Не использовать sensitive memory для убеждения.
10. Завершать после достаточной ясности.

## 5. Epistemic UI

- `Факт пользователя`
- `Наблюдение Garden`
- `Возможная связь`
- `Гипотеза`
- `Неизвестно`
- `Нужна внешняя проверка`

Маркер должен быть видимым, а не спрятанным в слове «возможно».

## 6. Correction flow

Пользователь может:

- `Это неверно`;
- `Не использовать дальше`;
- `Исправить факт`;
- `Это было актуально раньше`;
- `Удалить`;
- `Сохранить как мою версию`.

Garden не спорит и не психологизирует исправление.

## 7. Advice safety

Для high-stakes решения:

- не более одной рекомендации;
- показать альтернативы;
- объяснить критерии;
- предпочесть обратимый шаг;
- указать, где AI некомпетентен;
- предложить human/professional verification;
- не использовать relational or guilt language;
- не повторять после отказа.

## 8. No-interpretation zones

- диагноз;
- суицидальный риск без safety protocol;
- наличие насилия по неполным данным;
- моральная ценность человека;
- скрытый мотив другого;
- spiritual truth;
- trauma origin;
- attachment style as fact;
- personality type as explanation;
- future prediction;
- «настоящее предназначение».

## 9. Success metrics

- rejection is easy;
- source is understood;
- trust matches evidence;
- user-generated meaning increases;
- alternative explanations considered;
- real-world test occurs;
- memory corrections are honored;
- dependence does not grow.

## 10. Статус

Не входит в Bible до принятия GDR-010.
