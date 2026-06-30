# Guide Template

Thin scaffold. The canonical structure is the live exemplar: `docs/getting-started/math-tutor.md`, including its localisation section. Heading patterns are owned by `internal/editorial-guide.md` (Page Patterns); when this file and the editorial guide disagree, follow the editorial guide and update this file.

## Heading pattern

```text
---
description: One-sentence outcome.
icon: gitbook-icon-name
---
# Guide title                     (service-level name from the naming registry)
Intro: the practical outcome in one short paragraph.
{% hint style="info" %} Level: beginner|intermediate|advanced. Expected time: estimate. Scope note. {% endhint %}
## Fit and limits                  (bold-label list: Good for / Not for / Governance / Caution)
## Prerequisites
## Component map                   (layer -> component table)
## 1. Step name … ## n. Step name  (explain, one command, expected result)
## Verify                          (Check | Expected result table)
## Governance and review
## Troubleshooting                 (Problem | Check | Fix table)
## Next step
```

## Reminders

- The hint box carries both level and expected time; label the time as an estimate unless measured.
- One command per shell block, each followed by its expected result or a verification command.
- "Fit and limits" is a bold-label list (`- **Label** — value`), not a table.
- "Governance and review" names the human review point and where model egress is governed.
- Add a "Localise it" section when the guide's content should be adapted to curriculum, names, or language.
- A new runnable component must appear in `docs/operations/operations-overview.md` (runbook or further work) before the guide is linked.
- Register any new host port in the Port Allocations table in `internal/naming-registry.md`.
