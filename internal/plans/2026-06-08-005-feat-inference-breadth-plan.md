---
title: "Increment 3 — Inference Breadth: Dev Runtimes to Serving Engines"
type: feat
status: active
date: 2026-06-08
origin: internal/plans/2026-06-08-002-feat-frugal-ai-layered-repositioning-plan.md
---

# Increment 3 — Inference Breadth: Dev Runtimes to Serving Engines

## Overview

Broaden the Inference layer to show it is substitutable along a dev-to-serving gradient: local single-node runtimes for development, and serving engines for pilot-scale concurrency on GPU hardware. All speak the OpenAI API, so the gateway routes to any of them and applications do not change. This maps the layer onto the Development and Pilot environments and reinforces matching the engine, not only the model, to the machine.

Scope discipline: add an Inference layer overview and a minimal set of component cards. Do not add a runnable serving guide yet; serving engines need GPU hardware (such as DGX Spark) that the knowledge base has not measured.

## Decision (confirmed 2026-06-08)

Breadth depth: an overview plus two cards — a vLLM serving-engine card and an LM Studio dev-runtime card. SGLang and llama.cpp are named in the overview without separate cards.

## What the Research Establishes

- Serving engines (vLLM, SGLang) are open-source, OpenAI-compatible, and run on NVIDIA GPUs — pilot and production scale, not the Mac mini. vLLM leads on hardware and model breadth and production maturity. SGLang leads on throughput at smaller scale, stability under high concurrency, and native structured output and prefix sharing for agent workloads.
- Local runtimes (Ollama, LM Studio, llama.cpp) are single-node and developer-oriented. Ollama and LM Studio wrap llama.cpp; on Apple Silicon the fast path is MLX, which Ollama now uses. LM Studio is the GUI-first alternative on Mac and Windows.
- All expose OpenAI-compatible endpoints, so the gateway routes to any of them and applications stay unchanged.

## The Dev-to-Serving Gradient (the spine)

| Tier | Engines | Environment | Hardware |
| --- | --- | --- | --- |
| Local and development | Ollama (default), LM Studio, llama.cpp; MLX on Apple Silicon | Development | Mac mini 24 GB |
| Serving and pilot | vLLM, SGLang | Pilot | GPU hardware such as DGX Spark |

## Frugal and Sovereignty Note

Serving engines require GPU servers, which carry cost, export, and availability constraints for Small Island Developing States and low- and middle-income countries. The frugal default stays a local single-node runtime; a serving engine is a deliberate pilot-scale step, not the starting point. This mirrors how premium hardware is treated elsewhere in the knowledge base.

## Layer Mapping and Routing

The gateway (LiteLLM) routes by an OpenAI-compatible endpoint, so moving a model from Ollama in development to vLLM or SGLang in a pilot is an endpoint change behind the gateway, not an application change.

## Pages to Create or Modify

- Create `docs/concepts/inference-layer.md` — Inference layer overview: the gradient, OpenAI-compatible substitutability, environment and hardware mapping, gateway routing, and the frugal default.
- Create `docs/components/runtimes/vllm.md` — component card (Serving engine: vLLM). *(if the depth includes it)*
- Create `docs/components/runtimes/lm-studio.md` — component card (Runtime: LM Studio). *(if the depth includes it)*
- Optional full breadth: `docs/components/runtimes/sglang.md` and `docs/components/runtimes/llama-cpp.md`.
- Modify `docs/concepts/how-the-stack-fits-together.md` — link the Inference row to the overview.
- Modify `docs/components/runtimes/ollama.md` — note the alternatives and the MLX Apple Silicon path.
- Modify `docs/SUMMARY.md` — add the overview and the new cards under the Inference group.
- Modify `internal/tools/editorial_audit.py` — add the new component cards to the required entries.

## Audit Coupling

New component cards live under `components/runtimes/`, which is already in `COMPONENT_PARTS`, so no change there is needed. Add the new card entries to `REQUIRED_SUMMARY_ENTRIES`. The inference-layer overview is a concept page and, like the other layer overviews, is not a required entry.

## Minimum vs Deferred

Minimum: the inference-layer overview plus the chosen cards; navigation and audit updates; cross-links from the Ollama card.

Deferred: a runnable serving guide, until pilot GPU hardware is measured; SGLang and llama.cpp cards, unless full breadth is chosen; MLX as its own card; any benchmark figures.

## Verification

- The overview maps engines to environments and hardware and states the OpenAI-compatible routing point.
- New component cards include "## At a glance" and a layer tag.
- The editorial audit passes with updated required entries; links resolve; British spelling; no direct second person.

## Sources

- vLLM and SGLang serving-engine comparisons; Ollama, LM Studio, llama.cpp, and MLX local-runtime comparisons. Reviewed June 2026.
