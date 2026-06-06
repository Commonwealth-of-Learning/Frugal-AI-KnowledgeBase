---
description: See the first Frugal AI path and prepare your local machine.
icon: bolt
---

# Quickstart

This quickstart shows the smallest useful Frugal AI path in the Frugal AI knowledge base: a private offline chat service on a local Mac.

You will run an open-weight model with Ollama, connect Open WebUI, and verify that chat works without a cloud API key.

{% hint style="success" %}
Expected time: about 45 minutes on a Mac Mini or Apple Silicon Mac with 24 GB memory.
{% endhint %}

## What you will build

| Layer | Component | Purpose |
| --- | --- | --- |
| Hardware | [Mac Mini 24 GB](../components/hardware/mac-mini-24gb.md) | Local machine with enough memory for a light model and chat interface. |
| Environment | [Development environment](../components/environments/development.md) | Single-user setup for learning and testing. |
| Runtime | [Ollama](../components/runtimes/ollama.md) | Runs the model locally and exposes an API. |
| Model | [Qwen3.5-9B](../components/models/qwen-3.5-9b.md) | Light multimodal model for local chat and document-style tasks. |
| Framework | [Open WebUI](../components/frameworks/open-webui.md) | Browser-based chat interface. |
| Operations | [Open WebUI operations](../operations/open-webui-ops.md) | Start, stop, update, back up, and troubleshoot the service. |

## Before you start

You need:

- Apple Silicon Mac with 24 GB memory or more.
- macOS 15 or later.
- 20 GB free disk space.
- Terminal access.
- Docker Desktop.
- Homebrew, recommended for installing command-line tools.

If you are preparing a fresh Mac, install the basics first:

```bash
brew install curl jq git ollama
brew install --cask docker
```

Open Docker Desktop once after installing it so it can finish its first-run setup.

## Build path

1. Read [How the stack fits together](../concepts/how-the-stack-fits-together.md) if you want the architecture first.
2. Follow [Offline chat service](offline-chat-service.md) to run the model and chat interface.
3. Use [Open WebUI operations](../operations/open-webui-ops.md) when you need to restart, update, or back up the service.

## What is not covered yet

This first path does not cover RAG, Dify, multi-agent workflows, DGX Spark, or production serving. Those need their own guide paths because they add new components, risks, and operations work.
