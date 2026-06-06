---
description: Build a local, low-cost AI service with open components and clear operational limits.
icon: hand-wave
---

# Frugal AI

Frugal AI treats AI as local institutional infrastructure, not a remote service dependency. It prioritises offline operation, open components, data sovereignty, and practical capacity building.

This GitBook is a small working path through the knowledge base. It shows how to run a private offline chat service on a Mac Mini using Ollama, Qwen3.5-9B, and Open WebUI.

{% hint style="info" %}
This first path is intentionally small. Broader RAG, agentic, pilot, and production deployments remain in the deeper `reference/` library until they are ready for their own guides.
{% endhint %}

## Start here

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h4><i class="fa-bolt" style="color:$primary;">:bolt:</i></h4></td><td><strong>Quickstart</strong></td><td>See what you will build, what you need, and where each part fits.</td><td><a href="getting-started/quickstart.md">quickstart.md</a></td></tr><tr><td><h4><i class="fa-comments" style="color:$primary;">:comments:</i></h4></td><td><strong>Offline chat service</strong></td><td>Build a private ChatGPT-like service that runs on your local machine.</td><td><a href="getting-started/offline-chat-service.md">offline-chat-service.md</a></td></tr><tr><td><h4><i class="fa-sitemap" style="color:$primary;">:sitemap:</i></h4></td><td><strong>How the stack fits together</strong></td><td>Understand the hardware, runtime, model, framework, and operations layers.</td><td><a href="concepts/how-the-stack-fits-together.md">how-the-stack-fits-together.md</a></td></tr></tbody></table>

## What this path gives you

| Outcome | Why it matters |
| --- | --- |
| Local chat service | Prompts and chat history stay on your machine. |
| Open-weight model | You can inspect, replace, and operate the model without a cloud API key. |
| Clear memory budget | The guide explains what fits on a 24 GB Mac Mini and where estimates are used. |
| Operations runbook | You can start, stop, update, back up, and troubleshoot the service after setup. |

## Frugal AI principles

The practical docs follow four principles:

1. Keep data local by default.
2. Prefer open, inspectable components.
3. Match model size to available hardware.
4. Build local skills and operational confidence before scaling.

Read [Frugal AI principles](concepts/frugal-ai-principles.md) for the full framing.
