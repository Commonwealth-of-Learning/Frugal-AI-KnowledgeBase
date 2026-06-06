---
description: Higher-capability local hardware for development and pilot Frugal AI paths.
icon: server
---

# NVIDIA DGX Spark

NVIDIA DGX Spark is a compact Grace Blackwell desktop system for larger local AI development and pilot work. In the Frugal AI knowledge base, it is a higher-capability hardware profile for workloads that exceed the 24 GB Mac mini development path.

## At a glance

| Question | Answer |
| --- | --- |
| Current role | Development and pilot hardware for future Frugal AI paths. |
| Best fit | Larger local models, multimodal evaluation, fine-tuning experiments, and pilot services that need more memory headroom. |
| CPU or chip | NVIDIA Grace Blackwell architecture with integrated GPU and CPU; source-listed CPU is a 20-core Arm processor. |
| Memory | 128 GB unified system memory. |
| Main caution | Suitable pilot use still needs service ownership, access control, backups, monitoring, and workload testing. |

## When to use it

Use this profile for:

- Development work that needs larger models than the current Mac mini path can comfortably support.
- Pilot environments where a local system should serve a small controlled user group.
- Multimodal, coding, retrieval, or agentic evaluation that needs more memory headroom.
- Local experimentation with fine-tuning or model adaptation before a managed deployment decision.

## Specifications

| Field | Value |
| --- | --- |
| Environment fit | Development and pilot. |
| Architecture | NVIDIA Grace Blackwell with integrated GPU and CPU. |
| CPU | 20-core Arm processor with high-performance cores. |
| GPU | NVIDIA Blackwell architecture with 5th generation Tensor Cores and 4th generation RT Cores. |
| Memory | 128 GB LPDDR5x unified system memory. |
| Storage | 1 TB or 4 TB NVMe M.2 with self-encryption. |
| Network | 10 GbE, ConnectX-7, Wi-Fi 7, and Bluetooth 5.4. |
| Form factor | 150 mm x 150 mm x 50.5 mm; 1.2 kg. |
| Source | [NVIDIA DGX Spark hardware overview](https://docs.nvidia.com/dgx/dgx-spark/hardware.html#physical-specifications) |

## Memory planning

NVIDIA lists 128 GB unified system memory for DGX Spark. That gives substantially more local headroom than the 24 GB Mac mini development path, but it is not a substitute for measuring the selected runtime, model, quantisation, context window, concurrency, and visual-input overhead.

Treat 128 GB as planning headroom. A future DGX Spark guide should publish measured memory use for the exact service stack before recommending pilot defaults.

## What fits

| Workload | Fit | Confidence |
| --- | --- | --- |
| 7B-14B local chat and evaluation | Comfortable | Expected from memory headroom |
| Larger open-weight models for pilot evaluation | Candidate fit | Needs model-specific measurement |
| Multimodal evaluation | Candidate fit | Needs model-specific measurement |
| Fine-tuning or adaptation experiments | Candidate fit | Needs workflow-specific measurement |
| Production serving | Not established by this card | Requires production architecture and operations review |

NVIDIA states that DGX Spark supports AI models up to 200 billion parameters, or 405 billion parameters in a dual-Spark configuration. In the Frugal AI knowledge base, that source-listed capability should still be tested against the actual model, quantisation, context, and user load.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Cost discipline | Higher initial cost than the Mac mini path, but still local and reusable across development and pilot work. |
| Local control | Model execution and pilot data can remain on local institutional infrastructure. |
| Operational load | Requires stronger administration than a single-user development machine. |
| Replaceability | Can act as a local pilot step before a larger server, cluster, or managed deployment. |

## Compatibility

| Runtime or framework | Status | Notes |
| --- | --- | --- |
| [Ollama](../runtimes/ollama.md) | Candidate | Requires DGX Spark software validation before documenting a runnable guide. |
| [Open WebUI](../frameworks/open-webui.md) | Candidate | Useful for pilot chat interfaces after account, access, backup, and monitoring decisions are made. |

## Limits

- This card does not define a production reference architecture.
- Pilot use requires access control, logging policy, backup and restore tests, update windows, support ownership, and incident handling.
- Workload claims need local measurement before publication as guide defaults.
- Model licences and data-governance rules still need review before institutional use.

## Current and future use

- The Mac mini remains the documented first development path.
- NVIDIA DGX Spark is the candidate hardware profile for future development and pilot paths.
- Future DGX Spark guides should document the runtime, model, concurrency, monitoring, backup, and recovery assumptions before being linked as a runnable path.

## Source confidence

| Claim | Confidence |
| --- | --- |
| Grace Blackwell architecture, 20-core Arm CPU, 128 GB unified memory, storage, network, and physical specifications | Source-listed by NVIDIA. |
| Development and pilot fit | Frugal AI planning judgement; requires local measurement before guide defaults. |
| Production suitability | Not established by this card. |
