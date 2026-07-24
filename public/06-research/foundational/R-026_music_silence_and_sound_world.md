---
title: "R-026 — Музыка, тишина и звуковой мир Garden"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-026 — Музыка, тишина и звуковой мир Garden

**Версия:** 0.1  
**Дата:** 17 июля 2026  
**Статус:** design research / soundscape and auditory UX  
**Контур:** Garden Atlas → Sounds / Accessibility / World

---

## 1. Главный вопрос

> Как звук может делать Garden живым, пространственным и узнаваемым, не управляя эмоциями человека, не перегружая внимание, не превращаясь в повторяющийся soundtrack и не становясь обязательным каналом интерфейса?

---

## 2. Главный вывод

Garden должен различать четыре звуковых слоя:

1. **Ambient soundscape** — ветер, вода, листья, дождь, животные и пространство.
2. **Music** — опциональный художественный слой.
3. **Interaction sound** — короткая обратная связь на действия.
4. **Accessibility audio** — speech, earcons and assistive cues.

Они имеют разные цели и отдельные настройки.

### Основной принцип

> **Звук создаёт присутствие, но не определяет, что человек должен чувствовать.**

---

## 3. Acoustic environment и soundscape

ISO 12913 различает:

- **acoustic environment** — физические звуки в среде;
- **soundscape** — то, как эта акустическая среда воспринимается человеком в конкретном контексте.

Следовательно, «правильный» набор звуков не существует независимо от:

- человека;
- ситуации;
- задачи;
- громкости;
- повторения;
- времени;
- культурных ассоциаций.

### Для Garden

Нельзя проектировать звук только как библиотеку файлов:

```text
birds.mp3
water.mp3
wind.mp3
```

Нужно проектировать восприятие целой сцены.

---

## 4. Тишина

Тишина является полноценным режимом Garden.

Она не означает:

- отсутствие работы дизайнера;
- пустоту;
- плохое состояние сада;
- выключенный «настоящий опыт»;
- неполную подписку.

### Silent Garden

Все функции доступны без звука:

- создание;
- навигация;
- размещение;
- review;
- lifecycle;
- safety;
- уведомления.

### Правило

> Ни один смысл, статус или необходимое действие не передаётся только звуком.

---

## 5. Natural sounds

Метаанализ 2024 года по natural sounds и stress reduction обнаружил в целом более благоприятные результаты по части физиологических показателей по сравнению с тишиной, но эффекты были неоднородными, а по психологическим показателям преимущества были непоследовательны.

### Garden conclusion

Можно использовать звуки:

- воды;
- ветра;
- листьев;
- птиц;
- дождя.

Нельзя обещать:

- снижение стресса;
- восстановление внимания;
- улучшение сна;
- терапевтический эффект.

Цифровой soundscape является художественной средой, не лечением.

---

## 6. Ambient soundscape

Ambient sound should feel:

- spatial;
- sparse;
- variable;
- non-demanding;
- consistent with the scene.

### Layers

```yaml
ambience:
  air:
  foliage:
  water:
  weather:
  animals:
  distant_world:
  human_made_optional:
```

### Rules

- layers independently adjustable;
- no short obvious loops;
- no constant high-frequency detail;
- sound density configurable;
- quiet moments remain;
- no sound reacts morally to ritual states.

---

## 7. Repetition and auditory fatigue

Even pleasant sound becomes tiring when:

- loop length is short;
- timing is predictable;
- the same bird call repeats;
- frequency range is dense;
- volume never changes;
- silence never occurs;
- the listener cannot control it.

### Garden requirements

- procedural or long-form variation;
- randomized but ecologically plausible intervals;
- minimum silence windows;
- species-call limits;
- session-aware repetition protection;
- persistent user volume settings.

### No-go

A three-minute ambient loop repeated indefinitely.

---

## 8. Music

Music can influence emotion and be used intentionally for emotion regulation. Reviews also show that effects vary by:

- personal preference;
- familiarity;
- task;
- lyrics;
- arousal;
- context;
- individual differences.

Background music can have beneficial, null or detrimental effects on cognition. Lyrics are often more disruptive for language-related tasks.

### Garden position

Music is:

- optional;
- explicitly chosen;
- separate from ambient sound;
- never automatically personalized through inferred mood;
- not presented as therapeutic.

### Alpha

No continuous default soundtrack.

Possible:

- 2–3 optional instrumental pieces;
- user-provided or external music integration later;
- no lyrics in focused review by default;
- full silence remains equal-status.

---

## 9. Music must not steer the person

Forbidden:

- sad music after a difficult review;
- uplifting music after completion;
- tense music during “important” decisions;
- personalized mood correction;
- soundtrack based on inferred emotions;
- music that signals success or failure.

Allowed:

- user-selected scene music;
- aesthetic theme;
- explicit ritual-specific choice;
- manual playback.

### Principle

> The user may use music to shape their experience. Garden does not use music to shape the user.

---

## 10. Interface sounds

Interaction sounds can communicate:

- placement;
- selection;
- save;
- undo;
- opening;
- closing.

They should be:

- short;
- quiet;
- materially consistent;
- optional;
- non-celebratory;
- accompanied by visual feedback.

### Examples

- soft stone placement;
- paper fold for archive;
- subtle wood contact;
- quiet water touch.

### Avoid

- reward fanfare;
- victory chime;
- streak sound;
- sad failure tone;
- casino-like sparkle;
- escalating notification cue.

---

## 11. Auditory icons and earcons

### Auditory icon

A recognizable real-world sound representing an action.

Example:

- paper movement for archive.

### Earcon

An abstract musical or tonal cue learned through use.

These can support fast interaction and accessibility, but users may need to learn their meaning.

### Garden rule

- use sparingly;
- provide text/visual equivalent;
- allow preview and disable;
- do not rely on cultural universality;
- no hidden emotional meaning.

---

## 12. Accessibility audio

Audio can support users through:

- screen readers;
- spoken labels;
- earcons;
- spatial orientation;
- confirmation cues.

But ambient sound must not interfere with assistive audio.

### Requirements

- separate ambience and assistive channels;
- automatic ambience ducking during speech;
- full keyboard/list navigation;
- captions or labels for informative sounds;
- monaural compatibility;
- no essential spatial-audio-only information;
- hearing-device testing where possible.

---

## 13. Spatial audio

Spatial audio may help:

- locate water;
- understand place boundaries;
- feel depth;
- identify movement.

Risks:

- headphone dependence;
- motion sickness or disorientation;
- inaccessible meaning;
- inconsistent device support;
- privacy concerns in public spaces.

### Alpha

Simple stereo positioning only.

No core navigation depends on spatial audio.

---

## 14. Sound and materials

Material sounds should match visual behavior.

- stone sounds weighted;
- wood sounds muted;
- ceramic sounds clear but not sharp;
- paper sounds light;
- water responds softly;
- fabric is nearly silent.

One sound family should not be reused across incompatible materials.

### Rule

Sound supports material recognition but never becomes the sole cue.

---

## 15. Animal sound

Ambient creatures:

- do not call for the user;
- do not sound distressed;
- do not announce rarity;
- do not trigger notifications;
- do not repeat too frequently.

Separate controls:

- birds;
- insects;
- frogs;
- aquatic ambience.

No surprise close or loud calls.

---

## 16. Weather sound

Weather can include:

- light rain;
- distant rain;
- wind;
- leaf movement;
- soft thunder only by explicit choice.

### Forbidden by default

- sudden thunder;
- storm alarm;
- strong low-frequency rumble;
- sound tied to user “state”;
- weather audio that overrides quiet mode.

---

## 17. Notification sound

Garden notifications are external to the garden soundscape.

Requirements:

- off by default or selected during support setup;
- no emotional character;
- no creature call;
- no garden distress;
- no escalating sequence;
- respects OS settings and quiet hours.

### Not allowed

- bird reminding the user;
- wilting sound;
- “garden needs you” cue;
- sound after missed ritual.

---

## 18. Review mode

Focused review should default to:

- silence;
- or very low, explicitly selected ambience.

Music is off unless chosen.

Why:

- language processing;
- emotional sensitivity;
- accessibility;
- reduced manipulation.

### Exit

When review ends, audio does not play a success sound.

---

## 19. Safety mode

Safety mode:

- disables music and decorative audio;
- preserves assistive speech;
- uses only necessary interface feedback;
- avoids calming-sound promises;
- never masks urgency with ambient sound.

---

## 20. Personalization

User may control:

- master volume;
- ambience;
- music;
- interface sounds;
- animal sounds;
- weather;
- speech;
- sound density;
- dynamic range;
- stereo/spatial effects.

Garden does not infer preferences from:

- diagnosis;
- age;
- culture;
- mood;
- personality.

---

## 21. Dynamic range and comfort

Garden must avoid:

- sudden volume changes;
- loud transients;
- bass-heavy effects;
- high-frequency fatigue;
- sound masking of speech;
- default maximum volume.

### Provide

- loudness normalization;
- dynamic-range control;
- gentle fades;
- preview;
- safe default level;
- device-level respect.

---

## 22. Privacy

Sound settings may reveal:

- accessibility needs;
- environment;
- habits;
- device use.

Garden should not:

- activate microphone for ambience;
- infer location from sound;
- analyze surrounding audio;
- store listening behavior for psychological profiling.

Microphone use requires a separate, explicit use case and GDR.

---

## 23. Sound architecture

```yaml
soundscape:
  master:
  ambience:
    air:
    foliage:
    water:
    weather:
    animals:
    distant_world:
  music:
    enabled:
    selected_track:
    volume:
  interaction:
    enabled:
    material_feedback:
    navigation_feedback:
  accessibility:
    speech:
    earcons:
    ducking:
  comfort:
    dynamic_range:
    max_volume:
    reduced_density:
    mono:
```

---

## 24. Alpha sound set

### Ambient

- soft air;
- one foliage layer;
- one water layer;
- sparse fictional bird;
- optional light rain.

### Interaction

- place object;
- move;
- save;
- undo;
- archive.

### Music

- off by default;
- maximum 2–3 optional instrumental environments.

### Modes

- Silent;
- Minimal;
- Living;
- Custom.

These are density settings, not personality types.

---

## 25. Alpha experiments

### A — Silence vs ambient sound

Measure:

- liveliness;
- comfort;
- fatigue;
- ownership;
- distraction.

### B — Short loop vs variable soundscape

Measure repetition detection and irritation.

### C — Music vs no music in review

Measure clarity, emotional pressure and preference.

### D — Material interaction sounds

Measure comprehension and delight without reward interpretation.

### E — Sound density

Test Silent, Minimal and Living.

### F — Accessibility coexistence

Test screen reader plus ambience and audio ducking.

---

## 26. Candidate principles

1. Silence is a complete mode.
2. Ambient, music, interface and accessibility audio are separate.
3. Sound never carries essential meaning alone.
4. No therapeutic claims.
5. No emotion inference or correction.
6. No short obvious loops.
7. User controls every sound layer.
8. Review defaults to silence.
9. Interface sound confirms, never rewards obedience.
10. Animals never call for the user.
11. Safety mode removes decorative audio.
12. Accessibility speech has priority.
13. No microphone-based profiling.
14. Quiet is part of the world.

---

## 27. What Garden must not claim

- nature sounds reliably reduce stress for every user;
- music improves focus;
- a soundtrack regulates emotion safely;
- bird sounds are universally pleasant;
- spatial audio improves wellbeing;
- silence means disengagement;
- sound preference reveals personality;
- Garden music is music therapy;
- ambient audio reproduces being in nature.

---

## 28. Claim Registry

| Claim | Confidence | Status |
|---|---:|---|
| Soundscape is a perceptual construct in context, distinct from physical acoustic environment | high | foundation |
| Natural sounds may support some stress-related outcomes on average | medium | limited evidence |
| Natural sounds are always better than silence | low | rejected |
| Music can influence emotion regulation | high | foundation, contextual |
| Background music reliably improves cognitive performance | low | rejected |
| Repetition can create auditory fatigue | high by auditory-design practice | foundation |
| Variable ambience will increase ownership | low | Alpha hypothesis |
| Interface sounds can support recognition | medium-high | design foundation |
| Audio-only information is accessible | rejected | accessibility boundary |
| Silence is an equal-status experience | normative/product principle | required |

---

## 29. Verdict

Garden should have a sound world, but it should never require the person to hear it.

Its best sound may sometimes be:

- water at a distance;
- one bird;
- leaves;
- a quiet object placed;
- or nothing.

> **Тишина — не пустой Garden. Это Garden, который ничего не требует от слуха.**
