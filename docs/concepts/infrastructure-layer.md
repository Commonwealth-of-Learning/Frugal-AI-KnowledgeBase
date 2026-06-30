---
description: The infrastructure layer — compute, operating system, containers, storage, and networking that everything else runs on.
icon: network-wired
---

# Infrastructure layer

This page describes the Infrastructure layer of [The Frugal AI stack](how-the-stack-fits-together.md). Infrastructure is what everything else runs on: compute, operating system, containers, storage, and networking. It is the bottom layer and the first thing to secure.

## What the layer provides

- Compute: the processor and memory that run models and services. On the first path this is a single development machine.
- Operating system and containers: a stable base, and isolated, reproducible services.
- Storage: space for models, data, and backups, kept under local control.
- Networking: local access by default, with deliberate, governed choices about any external connection.

## Frugal practice

Start with modest, available hardware and add capacity only when a measured need appears. Match the machine to the model, keep data on local storage, and treat any network exposure as a deliberate decision rather than a default. Reusing hardware over several years controls cost and reduces waste.

## Hardware in this knowledge base

| Hardware | Role |
| --- | --- |
| [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) | The documented development machine for the first path. |
| [NVIDIA DGX Spark](../components/hardware/nvidia-dgx-spark.md) | A higher-capability candidate for development and pilot workloads. |

## Start from the machine

The documented first path assumes one machine, but readers arrive with different hardware. This table maps what is available to the closest documented path; rows without a path are honest gaps, and the guide pattern transfers to them only with local measurement.

| The machine available | Closest documented path | Notes |
| --- | --- | --- |
| Apple Silicon Mac with 24 GB memory or more | [Quickstart](../getting-started/quickstart.md), then [Local AI chat service](../getting-started/offline-chat-service.md) | The documented first path. 7B-12B class models fit at the guide's 8K context, per the [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) memory budget (comfortable through 9B, usually fine at 12B). |
| Apple Silicon Mac with 16 GB | No documented path yet *(further work)* | The guide pattern transfers with a smaller model tag and a short context, but fits are unmeasured; check the [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) memory budget before relying on it. |
| Windows or Linux machine, 16-32 GB | No documented path yet *(further work)* | [Ollama](../components/runtimes/ollama.md) runs on macOS, Linux, and Windows, and [LM Studio](../components/runtimes/lm-studio.md) on Mac and Windows, so the components transfer; the guides' macOS-specific steps (Homebrew, Docker Desktop) need local substitution. |
| GPU workstation or server | No documented path yet; pilot serving is planned | [NVIDIA DGX Spark](../components/hardware/nvidia-dgx-spark.md) is the candidate hardware profile, and serving engines such as [vLLM](../components/runtimes/vllm.md) belong to the [pilot environment](../components/environments/pilot.md); a pilot serving guide is further work. |
| Less than 16 GB, or low-power devices | Not covered | Below the measured comfort of the documented path. Smaller-model paths need their own guide and measurement before being documented. |

## How this connects

The infrastructure sets the memory budget that decides which models and engines fit; see the [Inference layer](inference-layer.md). The [development](../components/environments/development.md) and [pilot](../components/environments/pilot.md) environments describe the assumptions for each stage.

## Related pages

- [The Frugal AI stack](how-the-stack-fits-together.md)
- [Hardware: Mac mini 24 GB](../components/hardware/mac-mini-24gb.md)
- [Inference layer](inference-layer.md)
- [Development environment](../components/environments/development.md)
