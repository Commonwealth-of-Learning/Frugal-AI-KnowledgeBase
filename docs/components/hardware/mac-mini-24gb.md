---
description: Local development hardware for the first Frugal AI path.
icon: desktop
---

# Mac mini 24 GB

The current first path uses a Mac mini with 24 GB unified memory as the documented development machine. It is small, quiet, relatively low cost, and capable of running a light local model with a browser chat interface.

## At a glance

| Question | Answer |
| --- | --- |
| Current role | Development hardware for the first local AI chat service path. |
| Best fit | Small local models, short guide contexts, and single-user testing. |
| Main caution | Larger models and long contexts can exceed available memory. |

## When to use it

Use this profile for:

- A single-user development machine.
- Offline-capable local inference.
- A practical first build before pilot or production planning.
- A machine that can run Ollama, Docker, and a 7B-9B class model at the same time.

## Memory budget

| Use | Expected allocation |
| --- | --- |
| macOS and system services | About 6 GB |
| Runtime and app overhead | About 2 GB |
| Available for model and context | About 16 GB |

These are expected planning values. Check the machine with Activity Monitor and `ollama ps`.

## What fits comfortably

| Model class | Quantisation | Context | Fit |
| --- | --- | --- | --- |
| 7B-9B | Q4 | 8K | Comfortable |
| 7B-9B | Q4 | 32K | Usually fine |
| 14B | Q4 | 8K | Usually fine |
| 14B | Q4 | 32K | Tight |
| 70B+ | Any | Any | Not suitable |

## Limits

- Unified memory is shared by the CPU, GPU, operating system, Docker, browser, and model.
- Large context windows increase memory use through the key-value cache.
- Docker and browser tabs can make a comfortable setup feel tight.

## Used by this guide

The [Local AI chat service](../../getting-started/offline-chat-service.md) uses this hardware with:

- [Ollama](../runtimes/ollama.md)
- [Qwen3.5-9B](../models/qwen-3.5-9b.md)
- [Open WebUI](../frameworks/open-webui.md)
