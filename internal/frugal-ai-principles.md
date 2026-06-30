---
description: The operating principles behind the local AI path, restated for an era when AI agents act inside institutional systems.
icon: seedling
---

# Frugal AI principles

Frugal AI is a practical way to deploy AI within real institutional limits. It favours local control, open components, modest hardware, and operational skills over dependency on remote services.

The Commonwealth of Learning frames Frugal AI as inclusive, responsible, capacity-building AI for education. In the Frugal AI knowledge base, that means starting with a small service that an institution can run, inspect, and improve locally. It continues a long COL tradition of frugal educational technology, from Aptus, open-source hardware that brings learning to communities without grid power or the internet.

## The agentic shift

AI is moving from systems that answer questions to agents that take actions: reading files, running tools, and carrying out multi-step work inside institutional systems. The knowledge base treats an agent as an [Application subtype](application-layer.md), and the shift changes what sovereignty, cost, and capability mean in practice. Frugal AI was designed before this shift and is positioned for it.

The sovereignty question itself has moved three times:

| Generation | The question | Era |
| --- | --- | --- |
| Data residency | Where does the data sit? | Cloud era |
| Data protection | Who can access the data? | Compliance era |
| Data in action | Who runs the loop that sees and acts on the data? | Agentic era |

An agent runs in a loop, sometimes called its harness: the orchestration that assembles context, calls tools, and keeps memory between steps. Whoever operates that loop sees what the agent sees while it works: prompts, documents, tool outputs, and accumulated memory. That memory compounds into institutional knowledge over time, from curricula and administrative practice to the patterns of daily work. When the loop runs on infrastructure the institution does not control, that knowledge accrues somewhere else. Residency rules do not capture this, because nothing was stored in the traditional sense; it was experienced by someone else's agent.

Owning the loop means deciding locally: what data may enter an agent's context, which tools and systems the agent may touch, what is logged, retained, and remembered and where, and where the model runs, knowing it can be swapped. In the stack, these decisions live in the [Orchestration layer](orchestration-layer.md), the [Gateway](gateway-layer.md), and the [Application layer's three governance surfaces](application-layer.md). Models are increasingly substitutable; the loop is where control sits.

## Principles

### Keep data local by default

Prompts, uploaded files, and chat history should stay on the local machine unless there is a clear reason to send data elsewhere. For an agent, this includes its working context and memory, not only stored files.

Local does not mean risk-free. It still needs access control, backups, and clear rules for sensitive information.

### Concentrate governance at the gateway

When a model request could leave the institution, route it through one governed boundary: the sovereignty envelope. Redaction, approved destinations, logging, and guardrails belong at that single layer rather than scattered across the system. A fully local service keeps the envelope closed, with no external traffic.

The gateway governs model egress. An agent's tools are governed at the application layer, as the [three governance surfaces](application-layer.md) describe.

### Own the loop

The orchestration that runs an agent, with its tools, logs, and memory, stays under institutional control. An aircraft can change engines without handing over the cockpit; in the same way, the model behind an agent can be swapped while the loop, and everything it sees, remains the institution's. Even when a stronger external model is reached through controlled cloud burst, the loop decides what flows out, and the record of what happened stays local.

### Prefer open, inspectable components

Use open-weight models and open-source runtimes where practical. This helps institutions understand what they are running and reduces dependency on a single vendor.

Some useful tools may not be fully open source. When that happens, the page should say so and explain the trade-off.

### Match the model to the machine

A smaller model that runs reliably is better than a larger model that exhausts memory or needs constant tuning. Frugal AI starts with the memory budget, then chooses the runtime, model, and context window.

In the agentic era this principle gains force, because capability increasingly comes from routing, tools, and composition rather than from model size. On many institutional tasks, a small local model with the right tools does more useful work than a larger model without them; the [math tutor](../getting-started/math-tutor.md) is the worked example.

### Make autonomy affordable to run

An agent loop consumes many times the tokens of a single chat reply, because it retries, calls tools, and works in steps. When every step is a metered billing event, autonomy is rationed, and it is rationed hardest in the institutions Frugal AI serves. Local inference changes the equation: once the hardware exists, the marginal cost of a long-running task is close to zero. Agent workloads such as overnight content adaptation or translation drafts can then run without a budget conversation, with teacher review before anything reaches learners.

### Degrade to a minimal build

A Frugal AI system should run at its smallest useful size: infrastructure, inference, and an application, with no orchestration and the gateway closed to external traffic. Layers are added only when a task needs them, so the approach still works on a single machine or an offline school device.

### Build local capacity

The goal is not only to install software. The goal is to help a local team understand how the service runs, how to recover it, and when it is not suitable. The [coding agent](../getting-started/coding-agent.md) doubles as the builder's tool here: the local team uses an agent it governs to extend and maintain the stack itself.

### Reach learners in their languages

Open models increasingly support many languages, which matters for inclusive, equitable education across the Commonwealth. Where AI reaches learners, treat language coverage and accessibility as design choices, and review quality in low-resource languages rather than assuming it.

### Keep teachers and institutions in control

For education use, AI should support professional judgement rather than replace it. Higher-risk uses need human review, versioned sources, and audit trails. With agents the stakes rise, because actions have real effects; the institution should always be the principal of its agents, never merely the subject of someone else's.

## Why this matters now

The divide that matters next is delegation capacity: whether an institution has agents working for it, or only works inside someone else's. In the last decade the question was whether citizens could reach the internet; in this one it is whether institutions command their own agents or rent autonomy by the token. For Commonwealth institutions, and especially for small states, the practical answer starts small: the [Local AI chat service](../getting-started/offline-chat-service.md) is the smallest sovereign loop, and each tier of the learning path grows it only as far as a task needs.

## What this first path proves

The [Local AI chat service](../getting-started/offline-chat-service.md) demonstrates the smallest useful version of the pattern:

- A local machine provides the infrastructure.
- Ollama runs the model.
- Gemma 4 12B provides the intelligence layer.
- Open WebUI provides the chat interface.
- The operations page explains how to keep it running.

This is a development path, not a full ministry deployment.

## What comes later

RAG, agentic workflows, shared pilot services, and production deployments add new responsibilities. Each should get its own guide only when the knowledge base includes the supporting components, safeguards, and operations pages.

## Related pages

- [The Frugal AI stack](how-the-stack-fits-together.md)
- [Application layer](application-layer.md)
- [Example applications](example-applications.md)
- [Use the knowledge base with an AI agent](../reference/use-with-an-ai-agent.md)
