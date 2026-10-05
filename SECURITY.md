---
title: "SECURITY.md"
status: draft
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: false
---

# Current security boundary

Report vulnerabilities through [the disclosure policy](security/security-policy.md). Canonical proposed application security: [security architecture](internal/engineering/security/security-architecture.md).

## 1. Модель угроз

Current assets are public source and GitHub write access. Untrusted repository content and dependencies can influence developer tooling. Human review, branch protection, checksum validation and version pinning limit this risk; they do not prove future application safety.

## 2. Аутентификация

GitHub controls repository authentication. Garden has no application login.

## 3. Авторизация

Protected main requires PRs and checks. Independent reviewer enforcement remains open in issue #8. Canon, publication, production and expanded private-context access require owner approval.

## 4. Классификация данных

The entire repository is public. Raw participant data and confidential material stay outside it. No participant data is supplied to the Kit.

## 5. Управление секретами

Provider configuration references an environment variable; no provider credential is committed. Runtime outputs are ignored. No model API was called during installation.

## 6. Безопасность AI

Kit is development tooling only. Protected paths and manual update PRs are configured. Live AI in Garden remains outside the current slice; its controls are proposed, not implemented.

## 7. Известные пробелы

No application threat model has been validated against running code. WowRepo dependency remediation is tracked in issue #7 before future publication. Independent review is tracked in issue #8. No production security acceptance is claimed.
