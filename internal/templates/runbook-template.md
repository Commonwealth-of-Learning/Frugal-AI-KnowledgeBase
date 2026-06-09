# Runbook Template

Thin scaffold. The canonical structure is the live exemplar: `docs/operations/open-webui-ops.md`. Heading patterns are owned by `internal/editorial-guide.md` (Runbooks); when this file and the editorial guide disagree, follow the editorial guide and update this file.

## Heading pattern

```text
---
description: Operations scope for the service.
icon: gitbook-icon-name
---
# Service name operations         (service-level name from the naming registry)
Intro: what this runbook operates; development/pilot/production scope; what it is not.
## Scope                          (service, environment, data, owner)
## Deployment profiles
## Start, stop, and restart
## Health checks                  (Check | Command or action | Expected result)
## Maintenance                    (updates, cleanup, backup)
## Recovery                       (numbered scenario steps, each verified)
## Troubleshooting                (Symptom | Cause | Fix)
## Escalation notes
## When to move beyond            (transition gate to pilot decisions)
```

## Reminders

- Use the service-level public name, not the implementation tool, as the runbook title.
- One command per table row or block; every procedure ends in a verification with an expected result.
- Backup rows state what is covered (full volume vs one database file), location, frequency, and sensitivity.
- Recovery scenarios name an owner; escalation notes record what changed, output, data affected, and follow-up owner.
- End with the transition gate: what a pilot must decide (accounts, backups, update windows) before scaling past this runbook.
