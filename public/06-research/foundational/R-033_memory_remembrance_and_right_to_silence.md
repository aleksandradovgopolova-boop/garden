---
title: "R-033 — Память, воспоминания и право на тишину"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-033 — Память, воспоминания и право на тишину

**Версия:** 0.1  
**Дата:** 17 июля 2026  
**Статус:** design research / memory, remembrance and forgetting

## Главный вопрос

> Что Garden должен помнить, что может забывать и кто имеет право решать это — без превращения Garden во второй мозг, граф знаний, архив жизни или систему интеллектуального управления заметками?

## Жёсткая граница

Garden не является second brain, knowledge graph, note-taking system, personal wiki, semantic network, universal memory assistant или проектом «Нити».

> **Memory in Garden supports lived experience. It does not become an information system.**

Связи допустимы только для поддержки места, ритуала, объекта и пользовательского воспоминания. Они не становятся самостоятельной моделью продукта.

## History и Memory

History отвечает: что произошло в продукте?

Memory отвечает: что человек хочет сохранить как часть собственного опыта?

History может фиксировать создание места, перемещение объекта или восстановление snapshot. Memory может хранить: «Здесь я впервые почувствовала спокойствие».

## Memory is not Event

Воспоминание может относиться к месту, объекту, ритуалу, человеку, фотографии, звуку, сезону или периоду. Но Garden не обязан превращать это в сеть сущностей.

### Alpha model

- one primary place;
- optional ritual;
- optional object;
- optional date or period;
- no free-form graph.

## Garden does not create memories

Garden может создать запись, карточку, snapshot или контейнер, но не само воспоминание.

> **Garden can preserve a memory. It cannot manufacture one.**

## AI и ложный смысл

AI может описать наблюдаемое: «На фотографии четыре человека и закат».

AI не может утверждать без слов пользователя:

- «Это был счастливый день»;
- «Это важное воспоминание»;
- «Здесь ты чувствовала себя свободной»;
- «Этот момент изменил твою жизнь».

## Слои памяти

```yaml
garden_memory:
  memory_id:
  user_title:
  date_or_period:
  primary_place_id:
  ritual_id:
  object_id:
  media:
  original_note:
  later_reflections:
  visibility:
  provenance:
```

Все содержательные поля могут быть пустыми.

## Переосмысление без переписывания

Позднее понимание добавляется к старой записи, но не заменяет её.

```yaml
memory_reflection:
  reflection_id:
  memory_id:
  created_at:
  user_text:
  relation: adds_context | changes_view | contradicts | preserves
```

> **New understanding is added to the past. It does not replace the past.**

## Тишина и забывание

Garden различает:

- Silence — память давно не открывали;
- Hidden — пользователь убрал её из обзора;
- Archived — сохранил вне активного пространства;
- Forgotten by choice — решил отпустить;
- Deleted — удалил с recovery period, где это возможно.

Inactivity never changes memory status.

## Нет рейтинга важности

Garden не вычисляет:

- важнейшее воспоминание;
- определяющий период;
- любимого человека;
- самое значимое место;
- «забытое, но ценное» содержание.

Не ранжирует по частоте, свежести, количеству связей или насыщенности медиа.

## Нет автоматического resurfacing

В Alpha нет:

- «В этот день»;
- случайных воспоминаний;
- автоматических годовщин;
- эмоциональных flashbacks;
- «возможно, ты забыла это».

Допустимы только пользовательские действия: поиск, открытие через место или ритуал, явно включённое напоминание, запрос по периоду.

## Поиск

Search is primary.

Он может находить запросы вроде:

- «вечер с дождём»;
- «место, где я снова начала читать»;
- «пицца в июле».

Semantic retrieval должен быть основан на пользовательском тексте, метаданных и наблюдаемом содержимом медиа с обозначением неопределённости.

Он не строит скрытую теорию пользователя.

## Связи

Допустимы локальные связи:

- memory belongs to place;
- memory relates to ritual;
- memory contains object;
- reflection belongs to memory.

Не допускаются как ядро:

- arbitrary semantic linking;
- auto-generated concept graph;
- backlinks as product center;
- cluster maps;
- automatic ontology;
- «related thoughts» everywhere.

> **Garden remembers context, not an abstract graph of knowledge.**

## Память места и ритуала

Место может содержать одну память, несколько или ни одной. Оно не неполно без контента.

Ритуал может иметь отдельные выбранные occurrences или не иметь истории вообще. Garden не превращает его в дневник по умолчанию.

## AI role

AI может:

- транскрибировать пользовательское аудио;
- описывать видимое;
- искать;
- суммировать выбранный материал;
- предлагать буквальные теги;
- находить дубликаты;
- помогать экспортировать.

AI не может:

- выводить эмоциональную истину;
- ранжировать важность;
- писать автобиографический смысл;
- генерировать ностальгию;
- строить историю жизни;
- связывать воспоминания в скрытый нарратив;
- предлагать травматическую интерпретацию.

## Literal tags

Безопасные теги: rain, evening, kitchen, music, book, winter, photo.

Теги healing, turning point, grief, love, breakthrough, loneliness требуют явного авторства пользователя.

## Забывание по выбору

Пользователь может скрыть, архивировать, исключить из поиска, экспортировать и удалить память.

Garden не спрашивает, почему.

Нет guilt copy и предупреждений вроде «А точно ли это не важно?».

## Болевые воспоминания

Garden не показывает потенциально болезненный контент неожиданно.

- no random resurfacing;
- preview for anniversary reminders;
- user-controlled sensitivity;
- hide from suggestions;
- hide from global search where needed.

Garden не является терапией и не интерпретирует травму.

## Trigger Round

### Human-centric — «А что если ничего не объяснять?»
Memory may exist with only media, date and place. **Accepted.**

### Storytelling — «А что если история нелинейна?»
Later reflections coexist with original notes. **Accepted architecture.**

### Innovation — «А что если поиск станет главным?»
Search replaces feed-based resurfacing. **Accepted Alpha direction.**

### Business Design — «А что если бросить вызов главному тренду?»
Reject automatic “On this day” engagement loops. **Accepted boundary.**

### Naming — «А что если назвать буквально?»
Concrete titles: «Дождь после работы», «Пицца дома», «Первая прогулка у воды». **Accepted.**

### Rejected

Automatic semantic graph building is rejected because it moves Garden toward knowledge management and overlaps with «Нити».

## Alpha memory set

1. Manual creation.
2. One primary place.
3. Optional ritual or object link.
4. Photo, audio or text.
5. Later reflections.
6. Literal and grounded semantic search.
7. Hide, archive, export and delete.
8. No feed.
9. No “On this day”.
10. No graph view.
11. No automatic related memories.

## Candidate principles

1. Garden preserves memory; it does not manufacture it.
2. History and memory are distinct.
3. Later understanding is additive.
4. Silence is not forgetting.
5. Inactivity does not reduce importance.
6. No importance ranking.
7. No automatic resurfacing.
8. Search is primary.
9. Connections remain local and purposeful.
10. No knowledge graph.
11. No second-brain behavior.
12. Emotional meaning belongs to the user.
13. Literal description precedes interpretation.
14. Forgetting may be chosen.
15. Painful memories are never surfaced by surprise.

## Verdict

Garden не должен становиться машиной, которая помнит всё вместо человека.

> **Garden holds what the person chooses to keep. It does not turn a life into a database.**
