---
description: Light local model used by the offline chat service.
icon: brain
---

# Qwen3.5-9B

Qwen3.5-9B is the model used in the first offline chat path. It is small enough for local development on a 24 GB Mac while still supporting text and image input in the upstream model family.

## Identity

| Field | Value |
| --- | --- |
| Model ID | `Qwen/Qwen3.5-9B` |
| Ollama tag | `qwen3.5:9b` |
| Size in Ollama | 6.6 GB, source-listed |
| Context in Ollama | 256K, source-listed |
| Input in Ollama | Text and image |
| Local guide context | 8K, chosen for a comfortable development setup |

Sources:

- [Hugging Face model page](https://huggingface.co/Qwen/Qwen3.5-9B)
- [Ollama qwen3.5 library](https://registry.ollama.com/library/qwen3.5)

## Why this model fits the first path

- It is a light model for a local Mac setup.
- Ollama publishes a ready-to-run `qwen3.5:9b` tag.
- It supports long-context use upstream, while the guide uses a smaller context to manage memory.
- It is capable enough for general chat, explanation, and document-style tasks in a development setting.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Runs without a cloud API key once downloaded. |
| Memory | Source-listed model size is 6.6 GB in Ollama. |
| Hardware | Fits the 24 GB Mac Mini development path with an 8K context. |
| Replaceability | Can be swapped later if a guide needs a different model. |

## Limits

- The 256K context listed by Ollama is not the default used in this guide. Larger context windows consume more memory.
- Speed depends on hardware, context size, memory pressure, and runtime settings.
- Treat local speed values as expected values until measured on your machine.
- Check licence and institutional policy before using any model with sensitive data.

## Used by this guide

Follow [Offline chat service](../../getting-started/offline-chat-service.md) to create the local `qwen3.5-dev` profile.
