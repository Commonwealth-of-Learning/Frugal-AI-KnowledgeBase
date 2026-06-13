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

## Start from the task

| Task | Start with | What it gives |
| --- | --- | --- |
| Understand the model | [The Frugal AI stack](concepts/how-the-stack-fits-together.md) | The layer map, the gateway boundary, and the frugal floor. |
| Assess it for a ministry | [Gateway layer](concepts/gateway-layer.md), then the [reference architecture](reference/sovereign-education-ai-reference-architecture.md) | The governance pattern and the policy baseline. |
| Assess it for an institution | [Pilot environment](components/environments/pilot.md) | The questions to settle before shared use. |
| Match the build to the machine available | [Infrastructure layer](concepts/infrastructure-layer.md) | The closest documented path for the hardware at hand, and what is not covered yet. |
| Build the first service | [Quickstart](getting-started/quickstart.md), then [Local AI chat service](getting-started/offline-chat-service.md) | A private local chat service in about 75 minutes across both guides. |
| Add education workflows | [Math tutor](getting-started/math-tutor.md), [Curriculum advisor](getting-started/curriculum-advisor.md), then [AI gateway](getting-started/ai-gateway.md) | Exact computation, retrieval over approved documents, and controlled cloud burst. |
| Try agentic work | [Coding agent](getting-started/coding-agent.md), then [Manim animator](getting-started/manim-animator.md) | A reviewed coding agent that writes and runs code through the governed stack. |

## The first build: Local AI chat service

The first complete build stops at the frugal floor: infrastructure, inference, and an application, with the gateway local-only and no orchestration.

| Layer | Component |
| --- | --- |
| Application | [Open WebUI](components/applications/open-webui.md) |
| Inference | [Ollama](components/runtimes/ollama.md) with [Gemma 4 12B](components/models/gemma-4-12b.md) |
| Infrastructure | [Mac mini 24 GB](components/hardware/mac-mini-24gb.md) |

The first build proves a useful service can run locally, with prompts and chat history on the machine, components that remain inspectable, and operations documented from the start. [Example applications](concepts/example-applications.md) shows how the same floor supports a math tutor, curriculum advisor, coding agent, and future administrative workflows.

## From the Commonwealth of Learning

This knowledge base is the technical companion to COL's Frugal AI programme. For the strategy, policy, and latest news, go to COL directly:

- [Frugal AI programme](https://www.col.org/frugal) — COL's overview, approach, and key resources.
- [Gaborone to New Delhi Compact](https://www.col.org/wp-content/uploads/2026/02/Gaborone-to-New-Delhi-Compact.pdf) — the teacher-led, localised-AI commitment, presented at the India AI Impact Summit 2026.
- [Frugal AI: A Roadmap to Sovereign GenAI for Education](https://www.col.org/news/frugal-ai-a-roadmap-to-sovereign-genai-for-education/).
- [COL news](https://www.col.org/news/) — ongoing Frugal AI updates.

## Scope and next work

The build path remains a development path. Out of scope for the current public guides: production or shared-campus deployment, high-stakes automated decisions, and national-scale implementation. Pilot serving, production operations, and further example applications will be added only when their supporting components, safeguards, and operations pages exist.
