---
title: "S-009 — Prototype Build Plan"
status: accepted
owner: "Engineering"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: true
---

# S-009 — Prototype Build Plan

## Delivery scope clarification — 2026-10-05

This document describes the broader Alpha or later AI research round. The owner-approved first cycle is [First Place and Return](../../delivery/current/first-place-return-spec.md). AI, Ritual, Memory and versioned Undo are deferred from that first cycle. Its acceptance and participant criteria take precedence for the first round; these broader scenarios are retained for later work.

## Goal

Build a functional coded prototype covering the first-place and AI-preview vertical slice.

## Recommended implementation

- responsive web app;
- local mock persistence first;
- deterministic mock AI before live model integration;
- component-driven development;
- no production backend in Sprint 1.

## Sprint 0 — Foundation

- repository;
- routing;
- token system;
- accessibility baseline;
- domain types;
- mock data;
- event logger;
- test harness.

## Sprint 1 — First Place

- Welcome;
- First Place Setup;
- Place Renderer;
- Atmosphere controls;
- fixed Object library;
- placement;
- save draft/commit distinction;
- Garden Home;
- direct return.

## Sprint 2 — Ritual and Memory

- Ritual Editor;
- Ritual Detail;
- Occurrence;
- Memory Editor;
- Memory Detail;
- local search;
- context cards.

## Sprint 3 — AI Co-creation

- request composer;
- scope selector;
- assumption panel;
- deterministic proposal generator;
- Preview;
- visual/text/structural diff;
- partial Apply;
- version;
- Undo.

## Sprint 4 — Rights and Recovery

- history;
- snapshot;
- offline state;
- errors;
- privacy;
- export;
- deletion.

## Sprint 5 — Research hardening

- instrumentation;
- task reset;
- seeded prototype accounts;
- facilitator mode;
- bug fixing;
- accessibility pass;
- performance pass.

## Build constraints

- no game engine;
- no live collaboration;
- no social layer;
- no semantic graph;
- no autonomous AI;
- no real push notifications;
- no production payment or marketplace.

## Quality gate

Before testing:
- all core tasks can be completed by keyboard;
- Preview never mutates committed state;
- Undo is visible;
- local drafts survive refresh;
- error states are demonstrable;
- analytics contain no private text.

## Build principle

> The prototype should be real enough to reveal product mistakes, but small enough to change without defending sunk cost.
