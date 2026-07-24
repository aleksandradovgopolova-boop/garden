---
title: "R-029 — Изменение мира и пределы автоматической эволюции"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-029 — Изменение мира и пределы автоматической эволюции

**Версия:** 0.1  
**Дата:** 17 июля 2026  
**Статус:** design research  
**Контур:** World / Time / Objects / Safety

## Главный вопрос

> Что в Garden имеет право меняться само — и где живая изменчивость мира начинает отнимать у человека авторство, стабильность, память и чувство безопасности?

## Главный вывод

Garden различает:

1. perceptual change;
2. ambient change;
3. reversible configuration;
4. user-authored persistent change;
5. history change;
6. system-authored persistent change.

Последняя категория запрещена в Alpha по умолчанию.

> **The world may vary on its own. It may not rewrite itself without the user.**

## Почему изменение кажется живым

Изменчивость создаёт ощущение времени, глубины, независимости и природного ритма. Но она же может создавать потерю контроля, страх пропустить, эмоциональный долг, attachment anxiety и необратимую потерю значимого состояния.

Garden выбирает жизнь без долга.

## Типы изменений

### Perceptual

Камера, масштаб, фокус, цветовой режим. Мир не меняется.

### Ambient

Свет, облака, ветер, дождь, туман, отражения, звук, вода, ambient wildlife. После окончания мир остаётся прежним.

### Reversible configuration

Время суток, сезон, weather preset, вариант композиции, frozen ambience.

### User-authored persistent

Человек размещает объект, создаёт место, меняет путь, переименовывает, связывает память или сохраняет вариант.

### History

Появляются snapshot, epoch, note, ritual history, provenance и version.

### System-authored persistent

Система сама выращивает дерево, разрушает объект, заращивает путь, удаляет предмет, создаёт следы отсутствия или необратимую сезонную трансформацию.

**Alpha:** запрещено.

## Жизнь без структурной эволюции

Garden может ощущаться живым через:

- свет;
- воду;
- облака;
- ветер;
- звук;
- животных;
- малые вариации поверхности.

Для этого не требуются старение, смерть, разрушение, рост, ресурсы или maintenance.

> **Variation is enough for aliveness; decay is not required.**

## Рост

Автономного биологического роста в Alpha нет.

Позднее допустимы только:

- user-triggered stage change;
- preview;
- freeze;
- variant;
- snapshot;
- reversible return.

## Разрушение и neglect

Garden не симулирует увядание, сорняки как наказание, грязь, сломанные объекты, заброшенные места, исчезающие воспоминания, больных животных или мёртвые растения.

Эстетическая патина допустима только по выбору пользователя, без связи с отсутствием и с возможностью отмены.

## Погода и сезоны

Погода может меняться ambiently, но не имеет разрушительных последствий, не блокирует контент и не зависит от настроения или ритуалов.

Сезоны могут менять свет, палитру, поверхность, звук, fictional foliage и вероятность погоды. Они не удаляют объекты, не убивают растения, не закрывают места и не создают FOMO.

## Объекты и места

Объекты не меняются из-за выполнения или пропуска ритуала.

Места не становятся neglected, abandoned, overgrown, unsafe или inaccessible из-за отсутствия.

## Видимость изменений

Пользователь видит:

- что изменилось;
- когда;
- почему;
- кто инициировал;
- временно ли;
- можно ли отменить.

```yaml
world_change:
  change_id:
  initiated_by: user | system_ambient | collaborator | migration
  scope:
  temporary:
  reversible:
  previous_state:
  new_state:
  timestamp:
  explanation:
```

## Режимы эволюции мира

- **Stable** — минимум ambient variation.
- **Living** — меняются свет, погода, животные и звук.
- **Curated** — пользователь создаёт именованные сцены.
- **Manual** — ничего не меняется без прямого выбора.
- **Frozen** — текущее состояние сохраняется.

Ни один режим не содержит decay.

## Reversibility

Изменение должно быть:

- undoable;
- recoverable from history;
- preservable as variant;
- exportable;
- permanent only by explicit choice.

## Product updates

Обновление продукта не должно молча менять пользовательский мир.

Нужно сохранять layout, object identity, названия, user meaning и историю. Существенная визуальная миграция требует объяснения и, где возможно, legacy rendering.

> Product evolution must not impersonate the evolution of the user’s garden.

## AI

AI может предложить вариант, preview, альтернативную сцену и объяснить последствия.

AI не может применять изменения молча, заполнять пустоту, «улучшать» мир, старить его или трактовать трансформацию как личностный рост.

## Trigger Round

### Human-centric
**Карточка:** «А что если идея ограничивает выбор?»  
**Гипотеза:** запретить все autonomous persistent changes в Alpha.  
**Результат:** accepted boundary.

### Графический дизайн
**Карточка:** «А что если упростить до крайности?»  
**Гипотеза:** жизнь мира только через свет, погоду, воду, звук и животных.  
**Результат:** Alpha experiment.

### Инновации
**Карточка:** «А что если до решения всего один клик или тап?»  
**Гипотеза:** one-click named scene presets.  
**Результат:** candidate.

### Сторителлинг
**Карточка:** «А что если повествование скачет во времени?»  
**Гипотеза:** открывать прошлые состояния как snapshots, а не линейную эволюцию.  
**Результат:** accepted direction.

### Бизнес-дизайн
**Карточка:** «А что если бросить вызов главному тренду?»  
**Гипотеза:** отказ от live-service decay и retention-driven evolution.  
**Результат:** strategic hypothesis.

## Alpha experiments

1. Static vs ambient living world.
2. Ambient variation vs autonomous growth.
3. Manual vs one-click presets.
4. Freeze mode.
5. Snapshot time travel.
6. Migration preserving authored world.

## Принципы

1. Мир может варьироваться, не переписывая себя.
2. Нет autonomous decay.
3. Нет autonomous growth в Alpha.
4. Отсутствие ничего не меняет.
5. Ambient change не влияет на ресурсы.
6. Сезоны и погода контролируются пользователем.
7. Persistent change требует авторства.
8. Изменения видимы.
9. Reversibility — default.
10. Snapshots сохраняют прошлое.
11. Product update не редизайнит сад молча.
12. AI предлагает, но не трансформирует.
13. Frozen mode полноценен.
14. Aliveness не требует loss.
15. History accumulates without replacing the past.

## Verdict

Garden не должен доказывать, что он живой, отнимая что-либо у человека.

> **The world may change around the user. It must not change the user’s world without them.**
