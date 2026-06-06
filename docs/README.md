---
description: Plan, build, and govern local Frugal AI services for education.
icon: hand-wave
---

# Welcome to Frugal AI Knowledge Base

Frugal AI helps education systems use AI without giving up control of data, cost, infrastructure, and institutional decision-making.

The Frugal AI knowledge base is a practical starting point for partner institutions and ministries across the Commonwealth. It follows COL's Frugal AI framing: inclusive, responsible, open, locally governed, and focused on building long-term capacity.

{% hint style="info" %}
The first path is intentionally small. It shows how a local AI chat service can be built before pilot or production decisions are made.
{% endhint %}

## First-time here

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h4><i class="fa-seedling" style="color:$primary;">:seedling:</i></h4></td><td><strong>Frugal AI principles</strong></td><td>10 min - Review the sovereignty, openness, cost, and capacity-building frame.</td><td><a href="concepts/frugal-ai-principles.md">frugal-ai-principles.md</a></td></tr><tr><td><h4><i class="fa-bolt" style="color:$primary;">:bolt:</i></h4></td><td><strong>Quickstart</strong></td><td>10 min - See the first path and what the local build proves.</td><td><a href="getting-started/quickstart.md">quickstart.md</a></td></tr><tr><td><h4><i class="fa-comments" style="color:$primary;">:comments:</i></h4></td><td><strong>Local AI chat service</strong></td><td>30-45 min - Build the first local service in a development environment.</td><td><a href="getting-started/offline-chat-service.md">offline-chat-service.md</a></td></tr><tr><td><h4><i class="fa-users" style="color:$primary;">:users:</i></h4></td><td><strong>Pilot environment</strong></td><td>10 min - Review the minimum governance and operations decisions for shared use.</td><td><a href="components/environments/pilot.md">pilot.md</a></td></tr></tbody></table>

## Why this matters

Many education systems need AI tools that respect national priorities, institutional policies, and learner trust. Frugal AI treats AI as durable local infrastructure, not only as an external service subscription.

| Priority | What it means |
| --- | --- |
| Sovereign AI | Models, data, and operations can be governed by the institution or country. |
| Open technologies | Open-source software and open-weight models reduce lock-in and improve inspectability. |
| Data ownership | Prompts, chat history, files, and backups stay under local rules. |
| Compliance | Deployment choices can align with national regulation, procurement, privacy, and security requirements. |
| Guardrails | Access, human review, logging, backup, and acceptable-use rules are part of the design. |
| Local capacity | Teams learn how the service works and how to adapt it over time. |

## Choose a path

| Reader need | Start with | Why |
| --- | --- | --- |
| Understand the approach | [Frugal AI principles](concepts/frugal-ai-principles.md) | Sovereignty, openness, cost, resilience, and capacity framing. |
| Build a small local service | [Quickstart](getting-started/quickstart.md) | Fast orientation before any commands are run. |
| Review technical layers | [How the stack fits together](concepts/how-the-stack-fits-together.md) | A simple map of hardware, environment, runtime, model, interface, and operations. |
| Plan controlled shared use | [Pilot environment](components/environments/pilot.md) | Minimum decisions for access, data, support, backups, and human review. |
| Maintain the service | [Local AI chat service operations](operations/open-webui-ops.md) | Routine start, stop, backup, update, and recovery tasks. |

## Guardrails before scale

Shared services need clear rules before a pilot or production rollout.

| Area | Minimum question |
| --- | --- |
| Data | What information may be entered, uploaded, retained, or exported? |
| Access | Who can use the service, and how is access removed? |
| Human review | Which outputs require educator or institutional review before use? |
| Compliance | Which national, institutional, privacy, security, and procurement rules apply? |
| Operations | Who owns support, updates, backups, monitoring, and incident response? |

## The first local path

The first documented path builds a private local AI chat service for learning, testing, and demonstration. It is a development path, not a shared pilot or production service.

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
| Environment | [Development environment](components/environments/development.md) |
| Runtime | [Ollama](components/runtimes/ollama.md) |
| Model | [Qwen3.5-9B](components/models/qwen-3.5-9b.md) |
| Framework | [Open WebUI](components/frameworks/open-webui.md) |

## What this path proves

| Proof point | Why it matters |
| --- | --- |
| A useful AI service can run locally. | Sensitive prompts and chat history can stay under institutional control. |
| Open components can form a complete stack. | Runtime, model, and interface layers remain inspectable and replaceable. |
| Modest hardware can support a first build. | Small teams can test the approach before larger procurement or pilot decisions. |
| Operations are part of the build. | Backup, update, recovery, and support questions are visible from the beginning. |

## Frugal AI principles

The practical pages follow four principles:

1. Keep data local by default.
2. Prefer open, inspectable components.
3. Match model size to available hardware.
4. Build local skills and operational confidence before scaling.

Read [Frugal AI principles](concepts/frugal-ai-principles.md) for the full framing.

The framing is grounded in [COL's Frugal AI approach](https://www.col.org/frugal/), which emphasises inclusive and responsible AI, open education as a public good, data sovereignty, trusted governance, and local capability.

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
| [Pilot environment](components/environments/pilot.md) | Account management, backups, monitoring, support ownership, and acceptable-use rules. |
| Teacher-in-the-loop workflows | Review points, quality criteria, feedback loops, and educator guidance. |
| Production readiness | Security review, incident response, lifecycle management, and service ownership. |
