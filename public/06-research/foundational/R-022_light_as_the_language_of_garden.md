---
title: "R-022 — Свет как язык Garden"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-022 — Свет как язык Garden

**Версия:** 0.1  
**Дата:** 16 июля 2026  
**Статус:** design research / lighting system  
**Контур:** Garden Atlas → Light / Time / Accessibility

---

## 1. Главный вопрос

> Как использовать свет для глубины, атмосферы, времени и ориентации в Garden, не превращая его в психологическую оценку, скрытый таймер или источник визуального и сенсорного дискомфорта?

---

## 2. Главный вывод

Свет в Garden должен проектироваться как две связанные, но независимые системы:

### World Light

- небо;
- солнце;
- рассеянное освещение;
- тени;
- локальные источники;
- отражения;
- глубина;
- ощущение времени и погоды.

### Interface Light

- контраст текста;
- поверхности;
- focus states;
- выбранные объекты;
- навигация;
- accessibility.

### Основной принцип

> **Атмосфера мира никогда не должна разрушать читаемость интерфейса.**

---

## 3. Brightness, lightness и luminance

Эти понятия не равны друг другу.

### Luminance

Физически измеримая величина света, приходящего от поверхности или экрана в направлении наблюдателя.

### Brightness

Перцептивное ощущение того, насколько область кажется излучающей или отражающей много света.

### Lightness

Оценка яркости поверхности относительно белого или аналогично освещённой области.

CIE colour and appearance models подчёркивают, что brightness and lightness являются перцептивными атрибутами, зависящими от условий наблюдения и адаптации.

### Для Garden

Нельзя считать, что один RGB-токен создаёт одинаковое ощущение света:

- на разных экранах;
- в тёмной комнате;
- на солнце;
- на маленьком и большом объекте;
- рядом с разными фонами.

---

## 4. Свет как структура пространства

Свет помогает увидеть:

- глубину;
- границы;
- расстояние;
- материал;
- форму;
- путь;
- иерархию.

В Garden свет может:

- отделять место от места;
- направлять взгляд;
- поддерживать ориентиры;
- обозначать вход;
- создавать защищённый уголок;
- делать воду и материалы различимыми.

### Запрет

Свет не должен:

- автоматически выделять «правильный» ритуал;
- подсвечивать пропущенный объект;
- создавать скрытый priority score;
- вести пользователя к engagement-цели продукта.

---

## 5. Свет и атмосфера

Атмосфера создаётся сочетанием:

- направления;
- мягкости;
- контраста;
- цвета;
- движения;
- локальных источников;
- видимости горизонта;
- тумана;
- отражений.

### Возможные режимы

- dawn;
- daylight;
- overcast;
- dusk;
- night;
- lantern light;
- user-created local light.

Эти режимы являются эстетическими.

Они не означают:

- начало;
- продуктивность;
- спокойствие;
- грусть;
- завершение;
- crisis.

---

## 6. Дневной свет как inspiration, не обещание

Систематический обзор 2024 года по daylight in indoor environments включил 33 исследования и нашёл перспективные, но неоднородные данные о restorative outcomes. Авторы отдельно подчёркивают роль visual discomfort и недостаточную ясность механизмов.

### Garden conclusion

Можно использовать качества daylight:

- изменение;
- мягкие градиенты;
- направление;
- отражение;
- естественную вариативность.

Нельзя утверждать:

- что цифровой рассвет восстанавливает внимание;
- что солнечный паттерн улучшает настроение;
- что экранный свет воспроизводит физиологические эффекты реального дневного света.

---

## 7. Circadian claims

Реальный свет влияет на circadian biology через спектр, интенсивность, длительность и время воздействия.

Но Garden является экранным продуктом и не должен заявлять:

- circadian optimization;
- улучшение сна;
- гормональную регуляцию;
- лечение нарушений ритма.

### Rule

Garden can synchronize aesthetic light with local time only as:

- optional ambience;
- user-controlled behavior;
- non-medical feature.

It cannot present this as a health intervention.

---

## 8. Реальное время и право пользователя

Возможные режимы:

### Fixed

User selects one light scene.

### Manual

User changes the light at any time.

### Local-time

Garden follows device time after opt-in.

### Gentle cycle

A fictional slow cycle independent of real time.

### Rules

- no automatic lock;
- no removal of content at night;
- no “too late” state;
- no forced dawn;
- no reward for opening at a particular time;
- night-shift users must not receive incorrect day-language.

---

## 9. Night mode is not merely dark mode

A night garden requires:

- readable values;
- controlled local lights;
- preserved path visibility;
- reduced glare;
- visible focus;
- no crushed shadows;
- no inaccessible low-contrast text.

### Equal-status principle

Night is not:

- premium;
- dangerous;
- sad;
- less functional;
- a reward state.

It is a complete aesthetic world.

---

## 10. Overcast and diffuse light

Overcast light can provide:

- low directional contrast;
- clear material readability;
- quiet atmosphere;
- reduced hard-shadow complexity.

But it can also appear:

- flat;
- lifeless;
- low-contrast.

### Garden use

Use subtle value separation, material variation and depth cues.

Do not make overcast the visual language of inactivity.

---

## 11. Dappled and moving light

Moving light through leaves or water can make the world feel alive.

A 2026 Journal of Environmental Psychology study investigated motion types in abstract light patterns and stress recovery, showing that this remains an emerging research area rather than an established interface rule.

### Risks

- distraction;
- visual fatigue;
- motion sickness;
- flicker-like effects;
- reduced text readability;
- performance cost.

### Rule

- ambient movement is optional;
- low amplitude;
- slow;
- never behind reading content;
- disabled in reduced-motion mode;
- no essential information carried by movement.

---

## 12. Glare and discomfort

Digital Garden may create discomfort through:

- very bright local lights on dark scenes;
- abrupt transitions;
- saturated bloom;
- reflections;
- flashing water;
- high dynamic range without control;
- white modals over night scenes.

### Requirements

- cap local contrast;
- provide brightness control;
- smooth transitions;
- avoid bloom over text;
- test HDR and SDR;
- provide neutral interface surfaces;
- allow static light.

---

## 13. Shadows

Shadows create:

- depth;
- grounding;
- object separation;
- time and direction.

But deep or dynamic shadows can:

- hide controls;
- reduce object recognition;
- imply danger;
- create visual noise.

### Garden rules

- interactive objects stay legible;
- important controls never exist only in shadow;
- shadows do not encode lifecycle;
- user can reduce scene contrast.

---

## 14. Local light sources

Potential objects:

- lantern;
- window;
- candle-like glow;
- fire;
- reflected water light;
- bioluminescent fictional object.

### Safety and cultural caution

- open fire is symbolic/aesthetic, not a suggested real ritual;
- candles require no mystical or therapeutic claim;
- culturally identifiable lanterns require provenance;
- local lights do not become rewards for completion.

### User ownership

The user places and controls local lights.

---

## 15. Light and materials

Different materials need distinct light behavior:

- water reflects and transmits;
- stone has weight and texture;
- wood absorbs and scatters;
- glass transmits and reflects;
- fabric softens;
- foliage creates layered translucency.

### Product consequence

Material identity cannot rely only on texture assets. Lighting and shading are part of object readability.

---

## 16. Light transitions

Transitions should:

- be predictable;
- allow interruption;
- avoid abrupt full-screen changes;
- respect reduced motion;
- preserve focus;
- not block interaction.

### Duration categories

- immediate for accessibility-critical state;
- short for UI;
- slow and optional for atmosphere.

No transition should be long merely to appear cinematic.

---

## 17. Motion and accessibility

W3C guidance states that non-essential interaction-triggered motion should be disableable, and `prefers-reduced-motion` can be used to honour user settings.

### Garden requirements

- reduced-motion mode;
- static-light option;
- pause/stop for auto-moving ambient content;
- no parallax requirement;
- no camera drift;
- no flashing;
- no light pulses used as reminders;
- no automatic zoom to active ritual.

---

## 18. Light and focus

The selected object must remain visible across:

- day;
- dusk;
- night;
- overcast;
- colour-vision modes;
- high contrast.

Selection uses:

- outline;
- handle;
- label;
- optional controlled glow.

Glow alone is insufficient.

---

## 19. Interface surfaces over the world

Panels and modals must not inherit uncontrolled world lighting.

### UI surface rules

- defined surface tokens;
- stable text contrast;
- limited translucency;
- backdrop blur optional;
- no glassmorphism that harms readability;
- night/day variants tested separately.

### Principle

> The interface can belong to the world without becoming visually submerged in it.

---

## 20. Safety mode

Safety mode:

- removes atmospheric transitions;
- uses neutral high-contrast surfaces;
- disables ambient motion;
- avoids metaphorical light language;
- keeps direct information visible.

Not:

> «В саду стало темнее».

Better:

> direct literal safety message.

---

## 21. Light must not moralize

Forbidden mappings:

- bright = successful;
- dark = failed;
- sunrise = growth;
- sunset = completion;
- shadow = hidden trauma;
- spotlight = important life direction;
- extinguished lantern = neglected ritual;
- storm flash = crisis inference.

Allowed:

- user-selected aesthetic;
- actual or fictional time;
- object material;
- navigation and focus;
- explicit user-authored symbolism.

---

## 22. Light architecture

```yaml
world_light:
  scene:
    dawn:
    daylight:
    overcast:
    dusk:
    night:
  global:
    intensity:
    direction:
    softness:
    colour_temperature:
  local_sources:
    type:
    position:
    intensity:
    radius:
    user_controlled:
  ambient_motion:
    enabled:
    speed:
    amplitude:

ui_light:
  surface_day:
  surface_night:
  text:
  border:
  focus:
  overlay:

accessibility:
  reduced_motion:
  static_light:
  high_contrast:
  max_brightness:
  transition_speed:
```

---

## 23. Alpha experiments

### A — Fixed vs local-time light

Test:

- ownership;
- comfort;
- incorrect assumptions;
- perceived pressure;
- night-shift fit.

### B — Static vs gentle motion

Test:

- vitality;
- distraction;
- fatigue;
- reduced-motion preference.

### C — Dusk/night usability

Test:

- object recognition;
- text contrast;
- path legibility;
- glare.

### D — Local lights

Test whether user-placed lights:

- increase ownership;
- create hierarchy;
- become interpreted as rewards.

### E — World/UI separation

Compare:

- deeply translucent panels;
- stable opaque/translucent hybrid surfaces.

---

## 24. Candidate principles

1. World light and UI light are separate.
2. Light creates space, not judgment.
3. Real-time sync is optional.
4. Night is a complete world.
5. No circadian or therapeutic claims.
6. Motion is optional and slow.
7. Glare is a design failure.
8. Accessibility overrides cinematic effect.
9. Local lights belong to the user.
10. Light never encodes success or failure.
11. Materials require lighting-specific treatment.
12. Safety mode is literal and stable.

---

## 25. What Garden must not claim

- that screen daylight restores cognition;
- that dawn mode improves mood;
- that night mode supports sleep;
- that warm light is emotionally safe;
- that cool light increases focus;
- that dynamic light is biophilic treatment;
- that local-time sync is circadian design;
- that darkness reflects internal state.

---

## 26. Verdict

Light should make Garden feel alive without making the user feel watched, interpreted or timed.

> **The world may change its light. It must never use light to tell the person what their life means.**
