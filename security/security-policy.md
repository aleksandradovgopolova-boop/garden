---
title: "security/security-policy.md"
status: draft
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: false
---

# Security disclosure policy

## Как сообщить об уязвимости

Use GitHub private vulnerability reporting: https://github.com/aleksandradovgopolova-boop/garden/security/advisories/new . It is enabled for this repository. Include reproduction steps, affected commit and impact. Do not include secrets in public issues.

## Политика ответа

The repository owner reviews private reports. No response SLA has been committed. Coordinate public disclosure with the owner after remediation.

## Поддерживаемые версии

Current main is a documentation repository. The AI Ops installation PR is an unreleased change; no Garden application release is supported yet.

## Границы

Garden source, repository tooling and configuration are in scope. Upstream Kit and WowRepo defects should also be reported to their maintainers.
