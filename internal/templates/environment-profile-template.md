# Environment Profile Template

Thin scaffold. The canonical structure is the live exemplar: `docs/components/environments/development.md` (pilot scope: `docs/components/environments/pilot.md`). Heading patterns are owned by `internal/editorial-guide.md` (Component Pages); when this file and the editorial guide disagree, follow the editorial guide and update this file.

## Heading pattern

```text
---
description: Environment role in the Frugal AI knowledge base.
icon: gitbook-icon-name
---
# Environment name
Intro: one short paragraph; state whether it is development, pilot, or production.
## At a glance
                                  (bold-label list: Current role / Best fit / Hardware fit / Main caution)
## When to use it
## Defaults                       (hardware, runtime, interface, users, data, updates, backups — with rationale)
## Governance and operations      (owner, access, data, review, logs, support — minimum decisions)
## What changes before the next stage
## Related pages
```

## Reminders

- The governance table records minimum decisions, not aspirations; name an accountable owner.
- "What changes before the next stage" is the transition gate; keep it concrete and testable.
- A production profile that is not yet built stays a further-work stub; do not imply readiness.
