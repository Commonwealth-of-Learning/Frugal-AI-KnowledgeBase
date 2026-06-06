---
description: [How a Frugal AI stack fits together.]
icon: [gitbook-icon-name]
---

# [Stack name]

[Describe the stack in one short paragraph. State the service it supports and the operating scope.]

## Outcome

This stack supports [specific guide or service].

## Layers

| Layer | Page | Decision |
| --- | --- | --- |
| Hardware | [Hardware](../components/hardware/[file].md) | [Why this hardware] |
| Environment | [Environment](../components/environments/[file].md) | [Development/pilot/production assumption] |
| Runtime | [Runtime](../components/runtimes/[file].md) | [Why this runtime] |
| Model | [Model](../components/models/[file].md) | [Why this model] |
| Interface | [Interface](../components/frameworks/[file].md) | [Why this interface] |
| Operations | [Runbook](../operations/[file].md) | [How it is maintained] |

## Operating assumptions

| Assumption | Value | Confidence |
| --- | --- | --- |
| Users | [value] | [planned/tested] |
| Data location | [value] | [planned/tested] |
| Connectivity | [value] | [planned/tested] |
| Memory budget | [value] | [measured/estimated] |
| Support owner | [role/team] | [planned/assigned] |

## Frugal fit

| Principle | How the stack applies it |
| --- | --- |
| Local control | [How data and operation stay local] |
| Open components | [Which layers are inspectable or replaceable] |
| Resource discipline | [How model and hardware are matched] |
| Capacity building | [What the local team learns to operate] |
| Human oversight | [Where review or approval happens] |

## Verification

| Check | Command or action | Expected result |
| --- | --- | --- |
| [Check 1] | `[one command]` | [Expected result] |
| [Check 2] | [Action] | [Expected result] |

## Variants

| Variant | What changes | When to use |
| --- | --- | --- |
| [Variant 1] | [Layer changes] | [Scenario] |

## Limits

- [Limit 1]
- [Limit 2]
- [Limit 3]

## Next step

[Link to the guide or runbook that uses this stack.]
