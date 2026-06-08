---
description: The operating principles behind the local AI path.
icon: seedling
---

# Frugal AI principles

Frugal AI is a practical way to deploy AI within real institutional limits. It favours local control, open components, modest hardware, and operational skills over dependency on remote services.

The Commonwealth of Learning frames Frugal AI as inclusive, responsible, capacity-building AI for education. In the Frugal AI knowledge base, that means starting with a small service that an institution can run, inspect, and improve locally. It continues a long COL tradition of frugal educational technology, from Aptus, open-source hardware that brings learning to communities without grid power or the internet.

## Principles

### Keep data local by default

Prompts, uploaded files, and chat history should stay on the local machine unless there is a clear reason to send data elsewhere.

Local does not mean risk-free. It still needs access control, backups, and clear rules for sensitive information.

### Concentrate governance at the gateway

When a request could leave the institution, route it through one governed boundary: the sovereignty envelope. Redaction, approved destinations, logging, and guardrails belong at that single layer rather than scattered across the system. A fully local service keeps the envelope closed, with no external traffic.

### Prefer open, inspectable components

Use open-weight models and open-source runtimes where practical. This helps institutions understand what they are running and reduces dependency on a single vendor.

Some useful tools may not be fully open source. When that happens, the page should say so and explain the trade-off.

### Match the model to the machine

A smaller model that runs reliably is better than a larger model that exhausts memory or needs constant tuning. Frugal AI starts with the memory budget, then chooses the runtime, model, and context window. See [Cost and sustainability](cost-and-sustainability.md) for the cost and energy case.

### Degrade to a minimal build

A Frugal AI system should run at its smallest useful size: infrastructure, inference, and an application, with no orchestration and the gateway closed to external traffic. Layers are added only when a task needs them, so the approach still works on a single machine or an offline school device.

### Build local capacity

The goal is not only to install software. The goal is to help a local team understand how the service runs, how to recover it, and when it is not suitable.

### Reach learners in their languages

Open models increasingly support many languages, which matters for inclusive, equitable education across the Commonwealth. Where AI reaches learners, treat language coverage and accessibility as design choices, and review quality in low-resource languages rather than assuming it.

### Keep teachers and institutions in control

For education use, AI should support professional judgement rather than replace it. Higher-risk uses need human review, versioned sources, and audit trails.

## What this first path proves

The [Local AI chat service](../getting-started/offline-chat-service.md) demonstrates the smallest useful version of the pattern:

- A local machine provides the infrastructure.
- Ollama runs the model.
- Qwen3.5-9B provides the intelligence layer.
- Open WebUI provides the chat interface.
- The operations page explains how to keep it running.

This is a development path, not a full ministry deployment.

## What comes later

RAG, agentic workflows, shared pilot services, and production deployments add new responsibilities. Each should get its own guide only when the knowledge base includes the supporting components, safeguards, and operations pages.
