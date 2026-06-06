---
description: Dense multimodal model for local coding, reasoning, and agentic workflows.
icon: brain
---

# Gemma 4 12B

Gemma 4 12B is a dense, unified multimodal model from Google DeepMind. It is a candidate model for future Frugal AI paths that need stronger coding, reasoning, agentic, and multimodal capability than the first offline chat path.

This model is not used by the current [Offline chat service](../../getting-started/offline-chat-service.md) guide. It should be treated as a candidate model until a local Frugal AI guide measures memory use, speed, quality, and operational fit.

## Identity

| Field | Value |
| --- | --- |
| Model ID | `google/gemma-4-12B` |
| Instruction-tuned variant | `google/gemma-4-12B-it` |
| Ollama tag | `gemma4:12b` |
| Source | [Hugging Face model page](https://huggingface.co/google/gemma-4-12B) |
| Architecture | Dense, unified, encoder-free multimodal transformer |
| MoE status | Not MoE. Gemma 4 26B A4B is the MoE model in the family. |
| Modality, upstream | Text, image, audio, and video-style frame inputs with text output |
| Modality, Ollama tag | Text and image, source-listed |
| Model licence | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Local guide context | Not set. Start with a smaller context until measured locally. |

## Source confidence

| Claim | Value | Confidence |
| --- | --- | --- |
| Parameter count | 11.95B | Source-listed by Hugging Face |
| Layers | 48 | Source-listed by Hugging Face |
| Context window | 256K tokens | Source-listed by Hugging Face and Ollama |
| Sliding window | 1024 tokens | Source-listed by Hugging Face |
| Vocabulary size | 262K | Source-listed by Hugging Face |
| Ollama size | 7.6 GB | Source-listed by Ollama |
| Unsloth hardware guidance | Not listed for 12B | Unsloth lists E2B, E4B, 26B-A4B, and 31B variants |
| Memory use in Frugal AI path | Not measured | Needs local validation |

Do not treat source benchmark tables as local performance claims. Measure speed, memory use, and quality on the target machine before using this model in a guide.

## Reference settings

These settings are starting points for evaluation, not guide defaults. The current Frugal AI knowledge base path does not use this model.

| Profile | Context | Temperature | Top-p | Top-k | Min-p | Penalty | Thinking mode | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Frugal AI guide setting | Not set | Not set | Not set | Not set | Not set | Not set | Not set | Candidate model only |
| Gemma 4 family default | Start at 32K locally; source maximum is 256K for this card | 1.0 | 0.95 | 64 | Not listed | Disabled or 1.0 unless looping appears | Optional through Gemma 4 thinking control | Unsloth and Hugging Face |

Reference notes:

- Unsloth lists Google's Gemma 4 default sampling settings as `temperature = 1.0`, `top_p = 0.95`, and `top_k = 64`.
- Unsloth recommends starting local inference at 32K context for responsiveness, then increasing after measurement.
- The Gemma 4 end-of-sentence token is listed as `<turn|>`.
- For multimodal prompts, Unsloth recommends placing media before text. Visual token budgets range from 70 or 140 for fast captioning to 1120 for OCR, document parsing, handwriting, and small text.
- Unsloth's hardware table does not list Gemma 4 12B. Do not reuse its E2B, E4B, 26B-A4B, or 31B memory figures for this 12B card.

## Why this model fits a future path

- It is a dense 12B-class model, which makes it simpler to reason about than a MoE model with active and total parameter counts.
- Google describes Gemma 4 12B as small enough for local use on systems with 16 GB VRAM or unified memory, but the Frugal AI knowledge base should still validate it on the documented hardware.
- It adds stronger coding, reasoning, function-calling, and multimodal capability than the current first-path model.
- It is available through common local tooling, including Hugging Face Transformers and Ollama.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Designed for local execution and listed in Ollama as `gemma4:12b`. |
| Resource use | Ollama lists the model at 7.6 GB, but context and multimodal inputs can add memory pressure. |
| Replaceability | Can be evaluated as an alternative to the current local chat model when a guide needs coding or multimodal tasks. |
| Governance | Apache 2.0 licence is permissive, but institutional data rules and model-use policy still apply. |

## Good for

- Coding assistance: code generation, completion, correction, and local developer workflows.
- Agentic workflows: native function calling, system-role support, and configurable thinking mode support structured tool use.
- Multimodal understanding: image understanding, document or screen interpretation, OCR-style tasks, audio input, and video analysis through frame sequences.
- Long-context work: source-listed 256K context support for the 12B model class.
- Multilingual tasks: Google lists 35+ languages for out-of-the-box use and pre-training across 140+ languages.

## Not suitable for

- The current offline chat guide without a separate measured setup path.
- Production serving without concurrency, latency, security, and lifecycle testing.
- Sensitive learner or institutional data without local governance and human review.
- Low-memory deployments that cannot absorb context growth or multimodal input overhead.
- Tasks requiring guaranteed code correctness, security review, or formal assessment decisions without expert validation.

## Limits

- Gemma 4 12B is a dense model. The MoE option in the family is Gemma 4 26B A4B, not this model.
- Ollama currently lists `gemma4:12b` with text and image input. Upstream materials describe broader audio and video-style capabilities, but runtime support may differ.
- Multimodal inputs can increase memory and latency beyond the base model size.
- Thinking mode and function calling need application-layer support and testing before use in agentic workflows.
- Unsloth's Gemma 4 reference settings are family-level defaults for local GGUF-style inference, not measured Frugal AI guide settings for the 12B checkpoint.
- Coding output still requires review, testing, and security checks before use in production systems.

## Used by

No public Frugal AI guide uses this model yet. Candidate future paths include local coding support, multimodal course-material review, and teacher-in-the-loop agentic workflows.

## Links

- [Hugging Face: google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)
- [Hugging Face: google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)
- [Google Developers Blog: Gemma 4 12B developer guide](https://developers.googleblog.com/gemma-4-12b-the-developer-guide/)
- [Google launch post: Introducing Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)
- [Ollama: gemma4](https://registry.ollama.com/library/gemma4)
- [Unsloth: Gemma 4 local guide](https://unsloth.ai/docs/models/gemma-4)
