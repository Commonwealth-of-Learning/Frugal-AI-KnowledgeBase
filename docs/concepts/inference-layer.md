---
description: The inference layer — local runtimes for development and serving engines for pilot-scale concurrency, all behind one OpenAI-compatible interface.
icon: microchip
---

# Inference layer

This page describes the Inference layer of [The Frugal AI stack](how-the-stack-fits-together.md). Inference is what runs a model and serves predictions. The layer is substitutable: the same model can run on different engines, and applications do not change, because each engine exposes an OpenAI-compatible endpoint that the [gateway](gateway-layer.md) routes to.

## A dev-to-serving gradient

The inference layer spans two tiers.

| Tier | Engines | Environment | Hardware |
| --- | --- | --- | --- |
| Local and development | [Ollama](../components/runtimes/ollama.md) (default), [LM Studio](../components/runtimes/lm-studio.md), and llama.cpp | [Development](../components/environments/development.md) | [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) |
| Serving and pilot | [vLLM](../components/runtimes/vllm.md) and SGLang | [Pilot](../components/environments/pilot.md) | GPU hardware such as [NVIDIA DGX Spark](../components/hardware/nvidia-dgx-spark.md) |

## Local runtimes

Ollama is the default local runtime for the first path. LM Studio is a graphical alternative on Mac and Windows. Both wrap the llama.cpp engine, and on Apple Silicon both can use MLX, Apple's acceleration path for unified memory, for faster local inference.

A local runtime is the right tier for a single developer, a demonstration, or an offline device. It is not built for many simultaneous users.

## Serving engines

vLLM and SGLang are built to serve many requests at once on GPU hardware. vLLM has the broadest hardware and model support and the most production experience. SGLang is strong on throughput at smaller scale, stays stable under high concurrency, and has native structured output, which suits agent workloads. Both expose an OpenAI-compatible endpoint, so adopting one is an endpoint change behind the gateway.

## Match the engine to the machine

Serving engines need GPU servers, which carry cost, export, and availability constraints in many Commonwealth contexts. The frugal default is a local runtime on modest hardware. A serving engine is a deliberate step taken for a pilot with real concurrency, not the starting point. The model is matched to the machine, and so is the engine.

## Choose a model

The three models in this knowledge base are all open-weight, Apache 2.0 licensed, multimodal, and multilingual. What decides a choice between them is the memory band of the available machine, the language coverage a task needs, and how much agentic strength a workflow demands. The dense Gemma 4 12B is the model the documented first path uses; the dense Qwen3.5-9B is the smaller alternative it replaced as the default; the Mixture of Experts (MoE) Qwen3.6-35B-A3B is a candidate for higher-memory machines. Sizes below are source-listed Ollama download sizes; expected fits still need local measurement.

| Model | Role | Type and size | Hardware fit | Prefer it for |
| --- | --- | --- | --- | --- |
| [Gemma 4 12B](../components/models/gemma-4-12b.md) | First-path default | Dense 12B; 7.6 GB download | The documented [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) path at the guide's 8K context | The baseline the guides assume: local chat, document tasks, the [math tutor](../getting-started/math-tutor.md)'s read-only tool calling, coding support, and out-of-the-box coverage of 35+ languages. |
| [Qwen3.5-9B](../components/models/qwen-3.5-9b.md) | Alternative | Dense 9B; 6.6 GB download | The 24 GB path at an 8K context, with more headroom | A smaller download when memory is tight, and the family's source-listed coverage of up to 201 languages. |
| [Qwen3.6-35B-A3B](../components/models/qwen-3.6-35b-a3b.md) | Candidate | MoE; 35B total, about 3B active; 24 GB download | Beyond the 24 GB path; a higher-memory machine such as the [NVIDIA DGX Spark](../components/hardware/nvidia-dgx-spark.md) | Agentic coding, repository-level reasoning, and long-context work on a measured higher-memory path. |

Each model card carries the full picture: reference settings, source confidence, and model-specific limits.

For public deployments, the [sovereign education-AI reference architecture](../reference/sovereign-education-ai-reference-architecture.md) adds selection criteria beyond machine fit: licensing checks, security due diligence, and evaluation against local language and curriculum requirements.

An interactive comparison tool for choosing between open-weight models is further work; until it exists, this table and the model cards are the comparison.

## Shared model cautions

Every model in this knowledge base shares the same cautions, whatever its card says:

- Not for production serving without concurrency, latency, security, and recovery testing.
- Not for sensitive learner or institutional data without local governance and human review.
- Not for autonomous agentic actions with real side effects unless permissions, audit logging, rollback, and human approval are designed in.
- Not for tasks needing guaranteed correctness, security, or formal assessment decisions without expert validation.
- Not for a given language or curriculum on the strength of source-listed language counts alone — counts indicate coverage, not quality; evaluate a candidate on local-language and curriculum samples during piloting, before any learner-facing use.

Each model card lists only its model-specific cautions in addition to these.

## How this connects

Because every engine here speaks the OpenAI API, moving a model from a local runtime in development to a serving engine in a pilot is a change at the [gateway](gateway-layer.md), not in the application. The [development](../components/environments/development.md) and [pilot](../components/environments/pilot.md) environments describe the assumptions for each tier.

## Related pages

- [The Frugal AI stack](how-the-stack-fits-together.md)
- [Runtime: Ollama](../components/runtimes/ollama.md)
- [Serving engine: vLLM](../components/runtimes/vllm.md)
- [Gateway layer](gateway-layer.md)
- [Sovereign education-AI reference architecture](../reference/sovereign-education-ai-reference-architecture.md)
