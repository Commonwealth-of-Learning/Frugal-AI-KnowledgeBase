---
description: Graphical local runtime for running open-weight models on Mac and Windows.
icon: desktop
---

# LM Studio

_Layer: [Inference](../../concepts/how-the-stack-fits-together.md) (runtime)._

LM Studio is a graphical local runtime for open-weight models on Mac and Windows. In the Frugal AI knowledge base it is an alternative to Ollama for the Inference layer on the development machine, with a built-in model browser and a local OpenAI-compatible server.

## At a glance

| Question | Answer |
| --- | --- |
| Current role | Alternative local runtime for development. |
| Best fit | A graphical, single-user setup on a Mac or Windows machine. |
| Local fit | Runs on the development machine; on Apple Silicon it can use the MLX engine for faster inference. |
| Interface | OpenAI-compatible local server, so the gateway and applications do not change. |
| Main caution | A single-user development tool, not a serving engine for shared use. |

## When to use it

Use LM Studio when a graphical model browser and a desktop application suit the local team better than a command-line runtime. For scripted or headless setups, Ollama remains the default.

## Requirements

- A Mac or Windows machine with enough memory for the chosen model.
- Disk space for downloaded models.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Runs fully local; the local server stays on the machine. |
| Resource use | On Apple Silicon, the MLX engine uses unified memory efficiently. |
| Replaceability | OpenAI-compatible, so it can be swapped with Ollama behind the gateway. |
| Governance | Local-first; pairs with the gateway for redaction and logging. |

## Compatibility

- Open-weight models in GGUF, and MLX models on Apple Silicon.
- Routed through the [gateway](../gateways/litellm.md) like any other model endpoint.

## Limits

- A single-user development tool, not a serving engine for concurrency.
- The feature set and model formats depend on the application version.

## Used by

An alternative runtime for the development path; the documented first path uses [Ollama](ollama.md).

## Links

- [LM Studio documentation](https://lmstudio.ai/docs)
