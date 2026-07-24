---
title: "R-021 — Цвет как система мира Garden"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-021 — Цвет как система мира Garden

**Версия:** 0.1  
**Дата:** 16 июля 2026  
**Статус:** design research / colour system  
**Контур:** Garden Atlas → Beauty / Light / Materials / Accessibility

---

## 1. Главный вопрос

> Как создать цветовую систему Garden, которая делает мир красивым, узнаваемым и доступным, но не превращает цвет в психологическую диагностику, универсальную символику или скрытую шкалу успеха?

---

## 2. Главный вывод

Цвет нельзя проектировать только через названия оттенков и эмоциональные ассоциации.

Восприятие цвета зависит как минимум от:

- hue;
- lightness or brightness;
- chroma or saturation;
- размера цветового поля;
- соседних цветов;
- освещения;
- адаптации зрения;
- материала и текстуры;
- экрана;
- культурного и предметного контекста;
- особенностей цветового зрения.

CIE подчёркивает, что perceived colour описывается через hue, lightness/brightness and colourfulness/saturation/chroma, а само восприятие зависит от окружения, размера, структуры, адаптации наблюдателя и прошлого опыта.

### Garden position

> **Цвет — это свойство мира и интерфейса, а не вывод о человеке.**

---

## 3. Почему «зелёный успокаивает» — плохая дизайн-основа

Утверждения вроде:

- зелёный успокаивает;
- синий вызывает доверие;
- красный означает опасность;
- жёлтый делает счастливее;
- бежевый является уютным,

слишком грубы.

Research on colour and psychological functioning показывает:

- эффекты зависят от контекста задачи;
- один цвет связан с несколькими, иногда противоположными эмоциями;
- hue нельзя отделять от saturation and lightness;
- культурный опыт меняет ассоциации;
- эффект цвета в лаборатории не равен устойчивому эффекту цифрового мира.

Систематический обзор исследований color–emotion associations показывает повторяющиеся связи, но не простое соответствие «один цвет — одна эмоция». Например, красный связывался как с любовью и возбуждением, так и с гневом и враждебностью.

### Следствие

Garden не создаёт таблицу:

```text
green = calm
blue = reflection
red = problem
yellow = joy
grey = inactivity
```

---

## 4. Hue, lightness and chroma

### Hue

Категория цветового тона.

Hue полезен для:

- эстетического характера;
- различения групп;
- пользовательской настройки;
- поддержания мира.

Hue не должен быть единственным информационным каналом.

### Lightness

Perceived lightness особенно важна для:

- читаемости;
- визуальной иерархии;
- границ;
- распознавания объектов;
- контраста.

Светлота часто оказывает на UX более практическое влияние, чем название оттенка.

### Chroma / saturation

Высокая насыщенность может:

- привлекать внимание;
- создавать энергию;
- усиливать визуальный вес.

Низкая насыщенность может:

- снижать конкуренцию элементов;
- поддерживать сложные композиции;
- ощущаться тихо.

Но пастельный цвет не гарантирует спокойную эмоциональную реакцию. Исследование 2025 года не обнаружило устойчивого способа, которым пастельные цвета сами по себе модулировали эмоции.

---

## 5. Цвет существует в окружении

Один и тот же цвет воспринимается иначе:

- на светлом и тёмном фоне;
- в маленькой и большой области;
- рядом с комплементарным оттенком;
- при разном уровне освещения;
- на матовой или блестящей поверхности;
- в UI и на объекте мира.

CIE отдельно отмечает влияние размера стимула на perceived lightness, chroma and even hue.

### Garden implication

Palette review must happen:

- on full garden scenes;
- in context panels;
- in mobile;
- in reduced-motion mode;
- in different light settings;
- on actual object sizes.

Palette swatches alone are insufficient.

---

## 6. Object-context problem

Люди могут предпочитать цвет абстрактно и не предпочитать его для конкретного объекта.

Исследования показывают, что most/least preferred colours vary depending on the object being coloured.

### Garden example

A dark purple may feel beautiful as:

- evening sky;
- flower;
- fabric;
- UI accent.

The same colour may feel unnatural or distracting as:

- water;
- grass;
- large background;
- body text.

### Requirement

Color tokens need semantic context:

```yaml
world:
  sky:
  terrain:
  vegetation:
  water:
  structures:
ui:
  background:
  surface:
  text:
  border:
  focus:
state:
  selected:
  disabled:
```

Not one generic `purple-500` applied everywhere.

---

## 7. Cultural variation

Color-emotion and color-preference studies show both shared patterns and cultural variation.

Differences may involve:

- language;
- symbolic traditions;
- object associations;
- gender norms;
- religion;
- history;
- national context;
- commercial conventions.

Even when a cross-cultural pattern exists on average, it does not justify assigning meaning to an individual.

### Garden rule

Color preference is selected or observed in the current design task, not inferred from:

- gender;
- country;
- age;
- diagnosis;
- personality;
- mood.

---

## 8. Colour-vision diversity

Garden must support people who:

- have red–green colour-vision differences;
- distinguish some hues differently;
- need stronger luminance contrast;
- use high-contrast modes;
- experience light sensitivity;
- use monochrome or reduced-colour settings.

Research on red–green dichromats demonstrates that colour preference patterns can differ reliably from trichromatic observers.

### Requirement

Do not define “accessible palette” as one simulated screenshot.

Testing needs:

- automated contrast checks;
- colour-vision simulations;
- real participants;
- non-colour cues;
- large-scene testing.

---

## 9. Use of color and contrast

WCAG requires that colour is not the only visual means of conveying information. Text and essential interface elements must meet contrast requirements; non-text UI components and states also need sufficient contrast against adjacent colours.

### Garden consequences

Lifecycle status cannot be shown only through:

- green;
- yellow;
- grey;
- red.

It needs:

- label;
- icon;
- shape or pattern;
- accessible description.

Selected objects need more than a coloured glow.

Paths, controls and object boundaries must remain perceivable under different colour conditions.

---

## 10. Color must not become moral state

Forbidden mappings:

- green = good / active;
- red = bad / failed;
- grey = neglected;
- black = crisis;
- bright = healthy;
- dark = depressed;
- saturated = productive;
- faded = inactive.

### Allowed

Colour may indicate:

- current selection;
- interactive focus;
- user-selected aesthetic family;
- object material;
- time of day;
- explicit category chosen by the user.

Even in these cases, colour must not be the only cue.

---

## 11. Garden is allowed to be dark

A dark visual world is not automatically:

- sad;
- unhealthy;
- dangerous;
- premium;
- masculine;
- inaccessible.

A light world is not automatically:

- hopeful;
- safe;
- feminine;
- minimal;
- calm.

Garden should allow:

- dawn;
- daylight;
- dusk;
- night;
- overcast;
- high-contrast literal mode.

All must preserve usability and dignity.

---

## 12. Multiple aesthetic worlds

Garden needs one visual grammar, not one fixed palette.

### Shared grammar

- compatible value structure;
- stable hierarchy;
- consistent materials;
- predictable interactive colours;
- accessible text contrast;
- controlled accents.

### Possible palette families

#### Meadow Light

- warm light terrain;
- muted green vegetation;
- soft mineral neutrals;
- limited warm accents.

#### Woodland Shade

- darker terrain;
- moss and bark range;
- cool ambient light;
- brighter accessible focus accents.

#### Evening Garden

- deep blue-violet environment;
- warm lanterns;
- restrained vegetation chroma;
- high-contrast UI surfaces.

#### Stone and Water

- neutral mineral world;
- desaturated plants;
- cool water;
- quiet accent colour.

#### Wild Colour

- higher chroma flowers and objects;
- neutral interface;
- user-controlled density.

These are design hypotheses, not psychological profiles.

---

## 13. User control

User may choose:

- world palette;
- time/light mode;
- accent;
- colour intensity;
- high contrast;
- reduced colour;
- automatic system mode;
- object appearance.

User does not choose:

> “calm personality palette”.

### Copy

Not:

> «Какая энергия вам подходит?»

Better:

> «В каком цвете вам приятнее видеть сад?»

---

## 14. Colour and hierarchy

Garden should use colour sparingly for priority.

Primary hierarchy should also use:

- size;
- position;
- typography;
- spacing;
- shape;
- depth;
- motion.

Otherwise the garden becomes:

- noisy;
- difficult for colour-vision-diverse users;
- emotionally overcoded;
- interface-like rather than spatial.

---

## 15. Colour and interaction

### Focus

- visible outline;
- sufficient contrast;
- not colour-only;
- consistent across palettes.

### Selection

- outline + handle + label;
- no ambiguous ambient glow alone.

### Destructive action

- label and confirmation;
- icon;
- position;
- colour as secondary cue.

### Safety

Safety mode may use high contrast and direct structure, but red is not used as an emotional alarm unless the specific control convention requires it.

---

## 16. Colour and world history

Past rituals and archived objects should not be automatically faded to imply lesser value.

Archive can use:

- changed context;
- separate space;
- label;
- static presentation.

Not:

- grey = dead history.

---

## 17. Colour and monetization

Forbidden:

- premium palettes being the only visually dignified options;
- free garden deliberately dull;
- rare colour as status ranking;
- limited-time palette FOMO;
- paywalling high-contrast or accessibility themes.

Paid cosmetics may exist only after Alpha and separate ethical review.

Accessibility and core aesthetic dignity stay available to all.

---

## 18. Colour QA matrix

Every palette must be tested for:

### Technical

- WCAG text contrast;
- non-text contrast;
- focus visibility;
- disabled-state comprehension;
- colour-vision simulations;
- light/dark system behavior.

### Spatial

- full garden;
- dense and empty scenes;
- water;
- paths;
- object overlap;
- day/night.

### Human

- preference;
- ownership;
- fatigue;
- childishness;
- cultural fit;
- emotional overinterpretation;
- readability;
- glare.

### Ethical

- Does any colour imply success/failure?
- Is a dark preference pathologized?
- Does the palette create status?
- Is accessible mode aesthetically inferior?
- Is mood inferred?

---

## 19. Alpha experiments

### Experiment A — One canonical palette vs palette families

Measure:

- ownership;
- beauty;
- choice burden;
- consistency;
- cultural fit.

### Experiment B — Colour-coded lifecycle vs neutral lifecycle

Compare:

- coloured status;
- label + shape + subtle colour.

Measure moral interpretation and comprehension.

### Experiment C — Light vs dark garden

Test both without mood framing.

### Experiment D — Saturation control

Allow:

- quiet;
- balanced;
- vivid.

Do not name them by personality.

### Experiment E — High-contrast dignity

Test whether accessible variant feels like the same designed world rather than a technical fallback.

---

## 20. Candidate colour-system principles

1. Lightness before hue for hierarchy.
2. Colour never acts alone.
3. No moral colour coding.
4. Palette families, not personality palettes.
5. User preference before demographic inference.
6. World colour and UI colour are separate systems.
7. Full-scene testing over swatches.
8. Dark and light worlds are equal.
9. Accessibility themes remain beautiful.
10. Saturation is a controllable resource.
11. Archive is not automatically grey.
12. No premium dignity or colour FOMO.

---

## 21. What Garden must not claim

- green is universally calming;
- blue universally builds trust;
- red universally creates danger;
- pastel palettes improve wellbeing;
- a dark palette indicates sadness;
- colour preference reveals personality;
- cultural averages describe individuals;
- accessible palettes are emotionally neutral;
- digital colour effects reproduce real environmental effects.

---

## 22. Claim Registry

| Claim | Confidence | Status |
|---|---:|---|
| Perceived colour depends on hue, lightness/brightness, chroma/saturation and context | high | foundation |
| Colour alone should convey UI meaning | rejected | accessibility boundary |
| Colour-emotion associations show both recurring patterns and contextual/cultural variation | high | foundation |
| Green universally calms users | low | rejected |
| Pastel colours reliably reduce emotional arousal | low | rejected |
| Colour preferences vary by object context | high | foundation |
| Colour-vision diversity can alter preference and discrimination | high | foundation |
| A single canonical palette will maximize belonging | unknown | Alpha question |
| Palette choice can increase ownership | medium-low | product hypothesis |
| Accessible variants can remain aesthetically strong | normative/design principle | required |

---

## 23. Verdict

Garden should not choose colours to control emotion.

It should use colour to:

- create a coherent world;
- support perception;
- make interaction visible;
- allow aesthetic ownership;
- express materials, light and atmosphere;
- provide several dignified ways of seeing the same garden.

> **The user chooses the colour of the world. Garden does not use that colour to decide what the user feels.**
