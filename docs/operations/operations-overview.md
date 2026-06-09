---
description: What operating a Frugal AI stack involves, and where each component's operations live.
icon: gauge
---

# Operations overview

Operating a Frugal AI service means keeping each layer healthy: starting and stopping it, updating it, backing up data, reviewing logs, and recovering from failure. This page maps what is operated now and what needs its own runbook before a pilot.

## What is operated

| Component | Operations | Where |
| --- | --- | --- |
| Local AI chat service (Open WebUI and Ollama) | Start and stop, update, back up, restore, troubleshoot | [Local AI chat service operations](open-webui-ops.md) |
| Gateway (LiteLLM) | Run, keys, redaction services, audit log | The gateway section of the [chat service runbook](open-webui-ops.md) |
| Coding agent (OpenCode) | Update the agent, manage gateway keys, review actions and the audit log, keep the workspace scoped | Development notes below; create a runbook before repeated team use |
| Curriculum advisor (Dify) | Containers, document ingestion, embedding model, backups | The guide covers development use; create a runbook before a shared pilot |
| Serving engines (vLLM, SGLang) | Capacity, concurrency, monitoring, and recovery at pilot scale | Create a pilot runbook before shared inference |

## Coding agent operations

Until a full runbook exists, operate the [coding agent](../getting-started/coding-agent.md) by keeping OpenCode updated, storing the gateway key in the host environment, reviewing the agent's actions and the gateway audit log, and keeping the agent scoped to a project directory with `edit` and `bash` set to ask.

## Runbook gate

Create a separate runbook when a component moves beyond a single maintainer's development machine. The runbook should name:

- the service owner and support contact;
- start, stop, update, backup, restore, and rollback steps;
- health checks with expected results;
- where logs and audit records live;
- access, key rotation, and data-retention rules;
- the condition that triggers escalation to the [pilot](../components/environments/pilot.md) or [production](../components/environments/production.md) environment guidance.
