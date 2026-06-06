---
description: Local runtime for running open-weight models.
icon: terminal
---

# Ollama

Ollama is the local runtime used in the first Frugal AI path. It downloads models, runs them locally, and exposes an API that tools such as Open WebUI can connect to.

## At a glance

| Question | Answer |
| --- | --- |
| Current role | Runs the local model for the first Frugal AI path. |
| Best fit | Local model testing and development on a single machine. |
| Main caution | Model size and context length still need to fit available memory. |

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

For the offline chat path, install it with:

```bash
brew install ollama
```

## Limits

- Ollama is best for development, demos, and simple pilot use.
- High-concurrency production serving needs a different runtime plan.
- Model names, tags, and sizes can change; check the Ollama model library before publishing precise values.

## Used by this guide

The [Local AI chat service](../../getting-started/offline-chat-service.md) uses Ollama with [Qwen3.5-9B](../models/qwen-3.5-9b.md).

## Links

- [Ollama](https://ollama.com)
- [Ollama qwen3.5 library](https://registry.ollama.com/library/qwen3.5)
