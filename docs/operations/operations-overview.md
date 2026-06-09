---
description: What operating a Frugal AI stack involves, and where each component's operations live.
icon: gauge
---

# Operations overview

Operating a Frugal AI service means keeping each layer healthy: starting and stopping it, updating it, backing up data, reviewing logs, and recovering from failure. This page maps what is operated and where the guidance lives.

## What is operated

| Component | Operations | Where |
| --- | --- | --- |
| Local AI chat service (Open WebUI and Ollama) | Start and stop, update, back up, restore, troubleshoot | [Local AI chat service operations](open-webui-ops.md) |
| Gateway (LiteLLM) | Run, keys, redaction services, audit log | The gateway section of the [chat service runbook](open-webui-ops.md) |
| Coding agent (OpenCode) | Update the agent, manage gateway keys, review actions and the audit log, keep the workspace scoped | Notes below; full runbook is further work |
| Curriculum advisor (Dify) | Containers, document ingestion, embedding model, backups | The guide's troubleshooting covers development use; full runbook is further work |
| Serving engines (vLLM, SGLang) | Capacity, concurrency, monitoring, and recovery at pilot scale | Further work |

## Coding agent operations

Until a full runbook exists, operate the [coding agent](../getting-started/coding-agent.md) by keeping OpenCode updated, storing the gateway key in the host environment, reviewing the agent's actions and the gateway audit log, and keeping the agent scoped to a project directory with `edit` and `bash` set to ask.

## Further work

Full runbooks for the coding agent, for the curriculum advisor's Dify deployment, and for pilot-scale serving engines are not yet written. Add them when those paths are operated in a pilot, alongside the [production environment](../components/environments/production.md).
