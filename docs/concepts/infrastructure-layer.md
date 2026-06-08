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

## How this connects

The infrastructure sets the memory budget that decides which models and engines fit; see the [Inference layer](inference-layer.md). The [development](../components/environments/development.md) and [pilot](../components/environments/pilot.md) environments describe the assumptions for each stage.

## Related pages

- [The Frugal AI stack](how-the-stack-fits-together.md)
- [Hardware: Mac mini 24 GB](../components/hardware/mac-mini-24gb.md)
- [Inference layer](inference-layer.md)
- [Development environment](../components/environments/development.md)
