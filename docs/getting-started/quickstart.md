---
description: See the first Frugal AI path and prepare the local machine.
icon: bolt
---

# Quickstart

The first path builds a local AI chat service that runs on the documented development machine.

The path runs an open-weight model with Ollama, connects Open WebUI, and verifies that chat works without a cloud API key.

{% hint style="success" %}
Expected time: about 45 minutes on a Mac mini or Apple Silicon Mac with 24 GB memory.
{% endhint %}

## Build outcome

| Layer | Component | Purpose |
| --- | --- | --- |
| Hardware | [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) | Local machine with enough memory for a light model and chat interface. |
| Environment | [Development environment](../components/environments/development.md) | Single-user setup for learning and testing. |
| Runtime | [Ollama](../components/runtimes/ollama.md) | Runs the model locally and exposes an API. |
| Model | [Gemma 4 12B](../components/models/gemma-4-12b.md) | Dense multimodal model for local chat and document-style tasks. |
| Interface | [Open WebUI](../components/applications/open-webui.md) | Browser-based chat interface. |
| Operations | [Local AI chat service operations](../operations/open-webui-ops.md) | Start, stop, update, back up, and troubleshoot the service. |

## Prerequisites

Needed:

- Apple Silicon Mac with 24 GB memory or more. For other hardware, the [Infrastructure layer](../concepts/infrastructure-layer.md) maps what is available to the closest documented path.
- macOS 15 or later.
- 20 GB free disk space.
- Terminal access.
- Docker Desktop.
- Homebrew, recommended for installing command-line tools.

For a fresh Mac, install the basics first:

```bash
brew install curl jq git ollama
brew install --cask docker
```

Open Docker Desktop once after installing it so it can finish its first-run setup.

## Build path

1. Read [The Frugal AI stack](../concepts/how-the-stack-fits-together.md) for the architecture first.
2. Follow [Local AI chat service](offline-chat-service.md) to run the model and chat interface.
3. Use [Local AI chat service operations](../operations/open-webui-ops.md) for restart, update, or backup tasks.

## What is not covered yet

This first path does not cover RAG, Dify, multi-agent workflows, DGX Spark, or production serving. Those need their own guide paths because they add new components, risks, and operations work.
