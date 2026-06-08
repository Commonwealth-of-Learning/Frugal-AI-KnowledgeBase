---
description: Local development hardware for the first Frugal AI path.
icon: desktop
---

# Mac mini 24 GB

_Layer: [Infrastructure](../../concepts/how-the-stack-fits-together.md)._

The current first path uses a Mac mini with 24 GB unified memory and an Apple M4 or newer chip as the documented development machine. It is small, quiet, relatively low cost, and capable of running a light local model with a browser chat interface.

## At a glance

- **Current role** — Development hardware for the first local AI chat service path.
- **Best fit** — Small local models, short guide contexts, and single-user testing.
- **CPU or chip** — Apple M4 or newer. Current source-listed Mac mini options include M4 and M4 Pro.
- **Memory** — 24 GB unified memory.
- **Main caution** — Larger models and long contexts can exceed available memory.

## When to use it

Use this profile for:

- A single-user development machine.
- Offline-capable local inference.
- A practical first build before pilot or production planning.
- A machine that can run Ollama, Docker, and a 7B-9B class model at the same time.

## Specifications

| Field | Value |
| --- | --- |
| Environment fit | Development. |
| CPU or chip | Apple M4 or newer; current Apple source lists M4 and M4 Pro Mac mini configurations. |
| Memory | 24 GB unified memory. |
| Storage | 512 GB SSD or larger is recommended for local models and container data. |
| Network assumption | Local operation; internet access is useful for initial downloads and updates. |
| Source | [Apple Mac mini technical specifications](https://www.apple.com/ca/mac-mini/specs/) |

## Memory budget

| Use | Expected allocation | Confidence |
| --- | --- | --- |
| macOS and system services | About 6 GB | Estimated planning value |
| Runtime and app overhead | About 2 GB | Estimated planning value |
| Available for model and context | About 16 GB | Estimated planning value |

These are expected planning values. Check the machine with Activity Monitor and `ollama ps`.

## What fits comfortably

| Model class | Quantisation | Context | Fit |
| --- | --- | --- | --- |
| 7B-9B | Q4 | 8K | Comfortable |
| 7B-9B | Q4 | 32K | Usually fine |
| 14B | Q4 | 8K | Usually fine |
| 14B | Q4 | 32K | Tight |
| 70B+ | Any | Any | Not suitable |

## Frugal fit

| Factor | Fit |
| --- | --- |
| Cost discipline | A small desktop machine is enough for the first documented build. |
| Local control | Prompts, chat history, runtime, model, and interface can run on the local machine. |
| Operational load | Suitable for a small team learning the stack before pilot planning. |
| Replaceability | The same guide pattern can move to larger local hardware when model size, concurrency, or pilot requirements increase. |

## Limits

- Unified memory is shared by the CPU, GPU, operating system, Docker, browser, and model.
- Large context windows increase memory use through the key-value cache.
- Docker and browser tabs can make a comfortable setup feel tight.
- This profile is not a shared pilot or production service profile.

## Source confidence

| Claim | Confidence |
| --- | --- |
| M4 and M4 Pro Mac mini chip options | Source-listed by Apple. |
| 24 GB unified memory option | Source-listed by Apple. |
| Development fit and memory budget | Frugal AI planning estimate. |

## Used by this guide

The [Local AI chat service](../../getting-started/offline-chat-service.md) uses this hardware with:

- [Ollama](../runtimes/ollama.md)
- [Qwen3.5-9B](../models/qwen-3.5-9b.md)
- [Open WebUI](../frameworks/open-webui.md)
