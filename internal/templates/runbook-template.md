---
description: [Operations scope for the service.]
icon: [gitbook-icon-name]
---

# [Service name] operations

[State what this runbook operates and when it should be used.]

Use the service name from `internal/naming-registry.md`; do not use an implementation tool as the public runbook title when the page operates a broader service.

This is a [development/pilot/production] runbook. It is not [out-of-scope operating model].

## Scope

| Area | Covered |
| --- | --- |
| Service | [Service name] |
| Environment | [Environment profile] |
| Data | [What data is handled] |
| Owner | [Role or team responsible] |

## Start, stop, and restart

| Task | Command or action |
| --- | --- |
| Start [service] | `[one command]` |
| Stop [service] | `[one command]` |
| Restart [service] | `[one command]` |
| Check status | `[one command]` |

## Health checks

| Check | Command or action | Expected result |
| --- | --- | --- |
| [Check 1] | `[one command]` | [Expected result] |
| [Check 2] | [Action] | [Expected result] |

## Maintenance

### Updates

[Explain update responsibility and cadence. Link to component or upstream release notes when needed.]

```bash
[one command]
```

Expected result: [expected output or state].

### Cleanup

[Explain what can be safely removed and what must be retained.]

### Backup

| Item | Location | Frequency | Sensitivity |
| --- | --- | --- | --- |
| [Data item] | [Location] | [Frequency] | [Sensitivity] |

## Recovery

### [Recovery scenario]

1. [Action]
2. [Action]
3. Verify with `[one command]`.

Expected result: [expected state].

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| [Common problem 1] | [Likely cause] | [Smallest safe fix] |
| [Common problem 2] | [Likely cause] | [Smallest safe fix] |

## Escalation notes

Escalate when:

- [Condition 1]
- [Condition 2]
- [Condition 3]

Record:

- what changed;
- command output or error message;
- data affected;
- recovery attempt;
- owner for follow-up.
