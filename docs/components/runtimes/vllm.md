---
description: GPU serving engine for pilot-scale, multi-user local inference.
icon: server
---

# vLLM

_Layer: [Inference](../../concepts/how-the-stack-fits-together.md) (serving engine)._

vLLM is an open-source serving engine for running open-weight models at pilot and production scale. In the Frugal AI knowledge base it is the Inference layer engine for shared use on GPU hardware, beyond the single-user local runtime path.

## At a glance

- **Current role** — Candidate serving engine for pilot-scale inference.
- **Best fit** — Many simultaneous users on GPU hardware, behind the gateway.
- **Local fit** — Runs on GPU servers such as DGX Spark, not the 24 GB Mac mini development path.
- **Interface** — OpenAI-compatible endpoint, so the gateway and applications do not change.
- **Main caution** — Needs GPU hardware and capacity planning; a pilot-scale step, not the frugal default.

## When to use it

Use vLLM when more than one person needs the service at once and GPU hardware is available, typically at the pilot stage. For single-user development, a local runtime such as Ollama is the frugal choice.

## Requirements

- GPU hardware with enough memory for the chosen model.
- A Linux host with the appropriate GPU drivers.
- Capacity and concurrency testing before shared use.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Runs in-country on local or institutional GPU hardware; no external API required. |
| Resource use | Built for throughput, but needs GPU memory and power beyond a desktop. |
| Replaceability | OpenAI-compatible, so it can be swapped with another engine behind the gateway. |
| Governance | Pairs with the gateway for redaction, routing, and audit logging. |

## Compatibility

- Broad open-weight model support and broad hardware support.
- Routed through the [gateway](../gateways/litellm.md) like any other model endpoint.
- An alternative, SGLang, suits high-concurrency and structured-output workloads.

## Limits

- Not suitable for the 24 GB Mac mini development path.
- Needs measured capacity, latency, and recovery testing before pilot use.
- GPU cost, export, and availability constraints apply in many contexts.

## Used by

A serving engine supports a future pilot path; the current first path uses [Ollama](ollama.md) on the development machine.

## Links

- [vLLM documentation](https://docs.vllm.ai/)
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)
