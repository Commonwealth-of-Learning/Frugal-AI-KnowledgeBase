---
description: Local runtime for running open-weight models.
icon: terminal
---

# Ollama

_Layer: [Inference](../../concepts/how-the-stack-fits-together.md) (runtime)._

Ollama is the local runtime used in the first Frugal AI path. It downloads models, runs them locally, and exposes an API that tools such as Open WebUI can connect to.

On Apple Silicon, Ollama now uses the MLX engine for faster local inference. For alternatives and the move to serving engines for shared use, see the [Inference layer](../../concepts/inference-layer.md) overview.

## At a glance

- **Current role** — Runs the local model for the first Frugal AI path.
- **Best fit** — Local model testing and development on a single machine.
- **Main caution** — Model size and context length still need to fit available memory.

## When to use it

Use Ollama for:

- A simple local model runtime.
- Offline-capable development and demonstrations.
- Apple Silicon support without manual GPU driver work.
- An API endpoint for local tools.

## What it provides

| Capability | Why it matters |
| --- | --- |
| Model management | Pull, list, run, and remove local models. |
| Local API | Open WebUI can connect to `http://localhost:11434`. |
| Quantised models | Smaller model files fit on modest hardware. |
| Metal support on macOS | Apple Silicon acceleration works through the runtime. |

## Requirements

- macOS, Linux, or Windows.
- Enough memory for the selected model and context window.
- Disk space for downloaded model files.

For the local AI chat service path, install it with:

```bash
brew install ollama
```

## Limits

- Ollama is best for development, demos, and simple pilot use.
- High-concurrency production serving needs a different runtime plan.
- Model names, tags, and sizes can change; check the Ollama model library before publishing precise values.

## Used by this guide

The [Local AI chat service](../../getting-started/offline-chat-service.md) uses Ollama with [Gemma 4 12B](../models/gemma-4-12b.md).

## Links

- [Ollama](https://ollama.com)
- [Ollama gemma4 library](https://registry.ollama.com/library/gemma4)
