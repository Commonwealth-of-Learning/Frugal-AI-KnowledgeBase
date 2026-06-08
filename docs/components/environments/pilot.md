---
description: Controlled shared-use assumptions before production.
icon: users
---

# Pilot environment

_Scope: a deployment environment, not a [stack layer](../../concepts/how-the-stack-fits-together.md); it applies across all layers._

A pilot environment is a controlled shared setup for testing Frugal AI with a small group before production. It validates governance, support, data handling, quality, and operations under real use.

## At a glance

| Question | Answer |
| --- | --- |
| Current role | Defines assumptions for controlled shared use before production. |
| Best fit | Small educator or staff pilot with named owners, limited users, and agreed data rules. |
| Hardware fit | NVIDIA DGX Spark or a measured equivalent for the selected workload. |
| Main caution | A pilot is not production; scope, access, and recovery rules must be explicit. |

## When to use it

Use this environment when:

- More than one person needs access.
- The service has a named owner and support path.
- Data rules, acceptable use, and human review are agreed.
- Backup and restore have been tested.
- Pilot success criteria are written before launch.

## Defaults

| Setting | Default | Rationale |
| --- | --- | --- |
| Hardware | [NVIDIA DGX Spark](../hardware/nvidia-dgx-spark.md) or measured equivalent | Provides more memory headroom than the first Mac mini path. |
| Runtime | [Ollama](../runtimes/ollama.md) or another measured local runtime | Keeps inference local while allowing pilot measurement. |
| Interface | [Open WebUI](../frameworks/open-webui.md) or a governed pilot interface | Provides account-based access and a familiar chat surface. |
| Users | Small named group | Keeps support and risk manageable. |
| Data | Approved pilot data only | Prevents uncontrolled learner or institutional data exposure. |
| Updates | Scheduled window | Avoids surprising pilot users. |
| Backups | Tested before launch | Confirms recovery before shared use. |

## Governance and operations

| Area | Minimum decision |
| --- | --- |
| Owner | Role or team accountable for the pilot. |
| Access | Who can use the service and how accounts are removed. |
| Data | What can be entered, uploaded, retained, and exported. |
| Review | When human review is required before reuse of outputs. |
| Logs | What is kept, who can see it, and retention period. |
| Support | Who responds to incidents, quality issues, and access requests. |

## What changes before production

Before production, add:

- security review;
- service monitoring;
- incident response;
- lifecycle and model update policy;
- capacity and concurrency testing;
- accessibility and language review;
- formal data protection approval.

## Related pages

- [Development environment](development.md)
- [NVIDIA DGX Spark](../hardware/nvidia-dgx-spark.md)
- [Open WebUI](../frameworks/open-webui.md)
- [Local AI chat service operations](../../operations/open-webui-ops.md)
