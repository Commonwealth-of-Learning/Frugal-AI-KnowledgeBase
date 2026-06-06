---
description: The operating principles behind the local AI path.
icon: seedling
---

# Frugal AI principles

Frugal AI is a practical way to deploy AI within real institutional limits. It favours local control, open components, modest hardware, and operational skills over dependency on remote services.

The Commonwealth of Learning frames Frugal AI as inclusive, responsible, capacity-building AI for education. In this knowledge base, that means starting with a small service that an institution can run, inspect, and improve locally.

## Principles

### Keep data local by default

Prompts, uploaded files, and chat history should stay on the local machine unless there is a clear reason to send data elsewhere.

Local does not mean risk-free. It still needs access control, backups, and clear rules for sensitive information.

### Prefer open, inspectable components

Use open-weight models and open-source runtimes where practical. This helps institutions understand what they are running and reduces dependency on a single vendor.

Some useful tools may not be fully open source. When that happens, the docs should say so and explain the trade-off.

### Match the model to the machine

A smaller model that runs reliably is better than a larger model that exhausts memory or needs constant tuning. Frugal AI starts with the memory budget, then chooses the runtime, model, and context window.

### Build local capacity

The goal is not only to install software. The goal is to help a local team understand how the service runs, how to recover it, and when it is not suitable.

### Keep teachers and institutions in control

For education use, AI should support professional judgement rather than replace it. Higher-risk uses need human review, versioned sources, and audit trails.

## What this first path proves

The offline chat service demonstrates the smallest useful version of the pattern:

- A local machine provides the infrastructure.
- Ollama runs the model.
- Qwen3.5-9B provides the intelligence layer.
- Open WebUI provides the chat interface.
- The operations page explains how to keep it running.

This is a development path, not a full ministry deployment.

## What comes later

RAG, agentic workflows, shared pilot services, and production deployments add new responsibilities. Each should get its own guide only when the knowledge base includes the supporting components, safeguards, and operations pages.
