---
description: A developer-first reference for building sovereign, local-first AI for education, layer by layer.
icon: hand-wave
---

# Welcome to Frugal AI Knowledge Base

The Frugal AI knowledge base is a build reference for sovereign, local-first AI in education. It shows how to assemble AI services from open, inspectable layers that an institution can run, govern, and own — starting on a single machine and growing only as far as a task needs.

Frugal AI reframes AI as durable institutional infrastructure rather than an externally sourced service, prioritising efficiency, sovereignty, and local ownership. In practice it is local-first, open, and capacity-building infrastructure: predictable cost, data kept under local control, resilience without constant connectivity, and skills that stay with the institution. It continues a long Commonwealth of Learning technology tradition, from [Aptus](https://www.col.org/projects/aptus/) — open-source hardware that brings learning to communities without grid power or the internet — to [teacher-in-the-loop AI](https://jl4d.org/index.php/ejl4d/article/view/1934).

{% hint style="info" %}
The first build is intentionally small: one local chat service on a single machine. It is a development path and does not imply pilot or production readiness.
{% endhint %}

## The Frugal AI stack

Every build in the knowledge base is a path through one layered model. The layers are substitutable and optional; the smallest useful system uses only the lower layers.

```text
Application      chat, coding, agents, search
Gateway          sovereignty envelope: routing, compliance, guardrails
Orchestration    loop, tools, memory, retrieval        (optional)
Inference        local runtimes -> serving engines
Infrastructure   compute, OS, containers, storage
```

Read top to bottom it is the request path; read bottom to top it is the build order. See [The Frugal AI stack](concepts/how-the-stack-fits-together.md) for the full model.

## Governance has one home: the gateway

The gateway is the boundary every model request passes through, so it is where sovereignty is enforced: what may leave the institution, what stays local, what is logged, and what is redacted. Concentrating governance at one layer — the sovereignty envelope — keeps compliance, observability, and guardrails in a single inspectable place rather than scattered across the system. In the first build the envelope is closed: the service runs fully local with no external traffic.

## Where to start

Different goals have different starting points.

| Frugal AI | Start with | Go deeper |
| --- | --- | --- |
| Understand Frugal AI | [The Frugal AI stack](concepts/how-the-stack-fits-together.md) and [Frugal AI principles](concepts/frugal-ai-principles.md) | [Commonwealth of Learning: Frugal AI](https://www.col.org/frugal) |
| Assess it for a ministry | [Frugal AI principles](concepts/frugal-ai-principles.md), the [Gateway layer](concepts/gateway-layer.md), and the [Sovereign education-AI reference architecture](reference/sovereign-education-ai-reference-architecture.md) | [COL Frugal AI](https://www.col.org/frugal); the [Roadmap to Sovereign GenAI](https://www.col.org/news/frugal-ai-a-roadmap-to-sovereign-genai-for-education/) |
| Assess it for an institution | [Frugal AI principles](concepts/frugal-ai-principles.md) and the [Pilot environment](components/environments/pilot.md) | [COL Frugal AI](https://www.col.org/frugal) |
| Build with it | [Quickstart](getting-started/quickstart.md), then the learning path below | [Example applications](concepts/example-applications.md) |

## The first build: Local AI chat service

The first complete build stops at the frugal floor: infrastructure, inference, and an application, with the gateway local-only and no orchestration.

| Layer | Component |
| --- | --- |
| Application | [Open WebUI](components/frameworks/open-webui.md) |
| Inference | [Ollama](components/runtimes/ollama.md) with [Qwen3.5-9B](components/models/qwen-3.5-9b.md) |
| Infrastructure | [Mac mini 24 GB](components/hardware/mac-mini-24gb.md) |

## Learning path

The guides are tiered by level. One education example — a mathematics use case — runs through them, with the [curriculum advisor](getting-started/curriculum-advisor.md) showing the same layers carrying a second application.

| Level | Start with | What it adds | Estimated time |
| --- | --- | --- | --- |
| Beginner | [Local AI chat service](getting-started/offline-chat-service.md), after the [Quickstart](getting-started/quickstart.md) | A private local chat on one machine: the frugal floor. | About 75 minutes across both guides. |
| Intermediate | [Math tutor](getting-started/math-tutor.md), the [Curriculum advisor](getting-started/curriculum-advisor.md), then the [AI gateway](getting-started/ai-gateway.md) | Tools for exact computation, retrieval over approved documents, and a governed boundary with controlled cloud burst. | About 95 minutes across the three guides, plus model downloads. |
| Advanced | [Coding agent](getting-started/coding-agent.md), then the [Manim animator](getting-started/manim-animator.md) | An agent that writes and runs code, animating the mathematics through the gateway. | About 70 minutes across both guides, plus the Manim install. |

These levels match the Start here, Build further, and Advanced sections in the sidebar; [Example applications](concepts/example-applications.md) maps each guide to an application, a tier, and the layers.

## What this path proves

| Proof point | Why it matters |
| --- | --- |
| A useful AI service runs locally. | Prompts and chat history can stay on the machine. |
| Open layers form a complete stack. | Runtime, model, and interface remain inspectable and replaceable. |
| Modest hardware supports a first build. | Memory use stays visible and values are labelled as estimates. |
| Operations are part of the build. | Start, update, backup, and recovery are documented from the start. |

## Guardrails before scale

| Area | Minimum question |
| --- | --- |
| Data | What may be entered, uploaded, retained, or exported? |
| Access | Who can use the service, and how is access removed? |
| Human review | Which outputs need educator or institutional review before learners see them? |
| Compliance | Which national, privacy, security, and procurement rules apply? |
| Operations | Who owns support, updates, backups, and incident response? |

## Frugal AI principles

1. Keep data local by default.
2. Prefer open, inspectable components.
3. Match model size to available hardware.
4. Concentrate governance at the gateway.
5. Build local skills before scaling.

Read [Frugal AI principles](concepts/frugal-ai-principles.md) for the full framing, grounded in the [Commonwealth of Learning Frugal AI](https://www.col.org/frugal) programme.

## From the Commonwealth of Learning

This knowledge base is the technical companion to COL's Frugal AI programme. For the strategy, policy, and latest news, go to COL directly:

- [Frugal AI programme](https://www.col.org/frugal) — COL's overview, approach, and key resources.
- [Gaborone to New Delhi Compact](https://www.col.org/wp-content/uploads/2026/02/Gaborone-to-New-Delhi-Compact.pdf) — the teacher-led, localised-AI commitment, presented at the India AI Impact Summit 2026.
- [Frugal AI: A Roadmap to Sovereign GenAI for Education](https://www.col.org/news/frugal-ai-a-roadmap-to-sovereign-genai-for-education/).
- [COL news](https://www.col.org/news/) — ongoing Frugal AI updates.

## Scope, and what comes next

The learning path above builds the layered model end to end, but it remains a development path. Out of scope across the knowledge base: a production or shared-campus deployment, and a full ministry or national reference architecture. Still ahead, added only when their supporting components, safeguards, and operations pages exist: pilot and production serving (shared multi-user access, security review, incident response, lifecycle management) and further example applications from the [example applications](concepts/example-applications.md) matrix.
