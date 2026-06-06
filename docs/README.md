---
description: Build a local, low-cost AI service with open components and clear operational limits.
icon: hand-wave
---

# Welcome to Frugal AI Knowledge Base

Frugal AI helps institutions run useful AI services locally, with clear control over data, cost, and operations.

The first path builds a local AI chat service that runs on the documented development machine.

{% hint style="info" %}
This first path is intentionally small. Broader RAG, agentic, pilot, and production deployments remain in the deeper `reference/` library until they are ready for their own guides.
{% endhint %}

## First-time here

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h4><i class="fa-bolt" style="color:$primary;">:bolt:</i></h4></td><td><strong>Quickstart</strong></td><td>10 min - Map the build, prerequisites, and supporting pages.</td><td><a href="getting-started/quickstart.md">quickstart.md</a></td></tr><tr><td><h4><i class="fa-comments" style="color:$primary;">:comments:</i></h4></td><td><strong>Local AI chat service</strong></td><td>30-45 min - Set up the local runtime, model, and chat interface.</td><td><a href="getting-started/offline-chat-service.md">offline-chat-service.md</a></td></tr><tr><td><h4><i class="fa-sitemap" style="color:$primary;">:sitemap:</i></h4></td><td><strong>How the stack fits together</strong></td><td>10 min - Review the hardware, environment, runtime, model, interface, and operations layers.</td><td><a href="concepts/how-the-stack-fits-together.md">how-the-stack-fits-together.md</a></td></tr><tr><td><h4><i class="fa-wrench" style="color:$primary;">:wrench:</i></h4></td><td><strong>Local AI chat service operations</strong></td><td>10 min - Start, stop, back up, update, and troubleshoot the local service.</td><td><a href="operations/open-webui-ops.md">open-webui-ops.md</a></td></tr></tbody></table>

## Choose a path

| Reader need | Start with | Why |
| --- | --- | --- |
| Build a local service | [Quickstart](getting-started/quickstart.md) | Fast orientation before running commands. |
| Evaluate the Frugal AI fit | [Frugal AI principles](concepts/frugal-ai-principles.md) | Sovereignty, cost, resilience, and capacity framing. |
| Understand the architecture | [How the stack fits together](concepts/how-the-stack-fits-together.md) | A layer-by-layer map of the first stack. |
| Maintain the service | [Local AI chat service operations](operations/open-webui-ops.md) | Routine start, stop, backup, update, and recovery tasks. |

## The first stack

```text
Mac mini 24 GB
  -> Ollama
  -> Qwen3.5-9B
  -> Open WebUI
  -> Local AI chat service
```

| Layer | Page |
| --- | --- |
| Hardware | [Mac mini 24 GB](components/hardware/mac-mini-24gb.md) |
| Environment | [Development](components/environments/development.md) |
| Runtime | [Ollama](components/runtimes/ollama.md) |
| Model | [Qwen3.5-9B](components/models/qwen-3.5-9b.md) |
| Interface | [Open WebUI](components/frameworks/open-webui.md) |

## What this path proves

| Proof point | Why it matters |
| --- | --- |
| A useful AI service can run locally. | Prompts and chat history can stay on the machine. |
| Open components can form a complete stack. | Runtime, model, and interface layers remain inspectable and replaceable. |
| Modest hardware can support a first build. | The guide labels planning values and keeps memory use visible. |
| Operations are part of the build. | Start, stop, update, backup, and recovery steps are documented from the beginning. |

## Frugal AI principles

The practical docs follow four principles:

1. Keep data local by default.
2. Prefer open, inspectable components.
3. Match model size to available hardware.
4. Build local skills and operational confidence before scaling.

Read [Frugal AI principles](concepts/frugal-ai-principles.md) for the full framing.

## Not in this first path

This first path is not:

- a production deployment;
- a shared campus service;
- a RAG system over institutional documents;
- an automated assessment or decision system;
- a complete ministry or national reference architecture.

## Coming next

Future paths should be added only when the supporting components, safeguards, and operations pages are ready.

| Future path | Additional work required |
| --- | --- |
| RAG with local course materials | Document ingestion, retrieval checks, source governance, and privacy review. |
| Pilot deployment | Account management, backups, monitoring, support ownership, and acceptable-use rules. |
| Teacher-in-the-loop workflows | Review points, quality criteria, feedback loops, and educator guidance. |
| Production readiness | Security review, incident response, lifecycle management, and service ownership. |
