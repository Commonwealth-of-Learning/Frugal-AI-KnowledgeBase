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

## How this connects

Because every engine here speaks the OpenAI API, moving a model from a local runtime in development to a serving engine in a pilot is a change at the [gateway](gateway-layer.md), not in the application. The [development](../components/environments/development.md) and [pilot](../components/environments/pilot.md) environments describe the assumptions for each tier.

## Related pages

- [The Frugal AI stack](how-the-stack-fits-together.md)
- [Runtime: Ollama](../components/runtimes/ollama.md)
- [Serving engine: vLLM](../components/runtimes/vllm.md)
- [Gateway layer](gateway-layer.md)
