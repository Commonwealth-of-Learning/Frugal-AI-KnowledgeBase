---
description: Dense multimodal model used by the first local AI chat service path.
icon: brain
---

# Gemma 4 12B

_Layer: [Inference](../../concepts/how-the-stack-fits-together.md) (model)._

Gemma 4 12B is a dense, unified multimodal model from Google DeepMind. It is the model used in the first local AI chat service path: capable of general chat, coding support, reasoning, and multimodal work, while still fitting the documented 24 GB Mac mini path at the guide's 8K context setting.

## At a glance

- **Current role** — Used by the first local AI chat service and the guides built on it.
- **Best fit** — Local chat, coding support, multimodal course-material review, and teacher-in-the-loop workflows.
- **Prefer it when** — Following the documented guides; it is the baseline the first path assumes. The [model comparison](../../concepts/inference-layer.md#choose-a-model) lists when [Qwen3.5-9B](qwen-3.5-9b.md) or a candidate model is the better fit.
- **Local fit** — Fits the documented 24 GB Mac mini path with the guide's 8K context setting; the stack was measured at about 9.3 GB total (Ollama about 8.4 GB plus Open WebUI about 0.9 GB) on a reference Apple Silicon Mac on 2026-07-15, leaving headroom on 24 GB.
- **Model type** — Dense 12B multimodal model. Dense means each request uses the same model weights rather than routed experts.
- **Inputs** — Ollama lists text and image. Upstream sources describe text, image, audio, and video-style frame inputs.
- **Languages** — Google lists 35+ languages out of the box and pre-training across 140+.
- **Agentic readiness** — Source-listed native function calling, system-role support, and configurable thinking mode; needs backend-specific testing before agentic use.
- **Main caution** — Runtime support differs. Audio, video, thinking mode, and function calling need backend-specific testing.

## Good for

- First-path local chat: the model the local AI chat service runs, for general assistance, explanation, and document-style tasks.
- Coding assistance: code generation, completion, correction, and local developer workflows.
- Agentic workflows: native function calling, system-role support, and configurable thinking mode support structured tool use.
- Multimodal understanding: image understanding, document or screen interpretation, and OCR-style tasks now, with audio input and video analysis through frame sequences where the runtime supports them.
- Long-context work: source-listed 256K context support for the 12B model class.
- Multilingual tasks: Google lists 35+ languages for out-of-the-box use and pre-training across 140+ languages.

## Not suitable for

- Contexts well beyond the guide's 8K setting on the 24 GB path without separate measurement; the source-listed 256K maximum is not a guide default.
- Low-memory deployments that cannot absorb context growth or multimodal input overhead.

The [Inference layer](../../concepts/inference-layer.md#shared-model-cautions) lists the cautions shared by every model.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Designed for local execution and listed in Ollama as `gemma4:12b`. |
| Resource use | Ollama lists the model at 7.6 GB, but context and multimodal inputs can add memory pressure. |
| Hardware | Expected to fit the 24 GB Mac mini development path with the guide's 8K context. |
| Replaceability | Can be swapped if a guide needs a different model profile; [Qwen3.5-9B](qwen-3.5-9b.md) is the smaller documented alternative. |
| Governance | Apache 2.0 licence is permissive, but institutional data rules and model-use policy still apply. |

<details>

<summary><strong>Reference settings</strong></summary>

The first row is the Frugal AI guide setting; the source-listed rows are starting points for evaluation, not guide defaults.

| Profile | Context | Temperature | Top-p | Top-k | Thinking mode | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Frugal AI guide setting | 8K | Runtime default | Runtime default | Runtime default | Not configured by the guide | Current guide |
| Gemma 4 family default | Start at 32K locally; source maximum is 256K for this card | 1.0 | 0.95 | 64 | Optional through Gemma 4 thinking control | Unsloth and Hugging Face |

Reference notes:

- Unsloth lists Google's Gemma 4 default sampling settings as `temperature = 1.0`, `top_p = 0.95`, and `top_k = 64`.
- Unsloth recommends starting local inference at 32K context for responsiveness, then increasing after measurement.
- Unsloth labels this checkpoint as Gemma 4 12B Unified. The "Unified" label refers to the encoder-free multimodal architecture.
- The Gemma 4 end-of-sentence token is listed as `<turn|>`.
- For multimodal prompts, Unsloth recommends placing image and video content before text, and audio content after text. Visual token budgets range from 70 or 140 for fast captioning to 1120 for OCR, document parsing, handwriting, and small text.

</details>

## Technical details

| Field | Value |
| --- | --- |
| Model ID | `google/gemma-4-12B` |
| Instruction-tuned variant | `google/gemma-4-12B-it` |
| Unsloth model | `unsloth/gemma-4-12b`, labelled Gemma 4 12B Unified |
| Ollama tag | `gemma4:12b` |
| Source | [Hugging Face model page](https://huggingface.co/google/gemma-4-12B) |
| Architecture | Dense, unified, encoder-free multimodal transformer |
| MoE status | Not MoE. Gemma 4 26B A4B is the MoE model in the family. |
| Model licence | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) |

<details>

<summary><strong>Source confidence</strong></summary>

_Sources checked: 2026-06-13._

| Claim | Value | Confidence |
| --- | --- | --- |
| Parameter count | 11.95B | Source-listed by Hugging Face |
| Layers | 48 | Source-listed by Hugging Face |
| Context window | 256K tokens | Source-listed by Hugging Face and Ollama |
| Sliding window | 1024 tokens | Source-listed by Hugging Face |
| Vocabulary size | 262K | Source-listed by Hugging Face |
| Ollama size | 7.6 GB | Source-listed by Ollama |
| Unsloth label | Gemma 4 12B Unified | Source-listed by Unsloth model card |
| Unsloth dense-model row | 11.95B parameters, 48 layers, 1024-token sliding window, 256K context, 262K vocabulary, text/image/audio support | Source-listed by Unsloth model card |

Do not treat source benchmark tables as local performance claims. Measure speed, memory use, and quality on the target machine before using this model in a guide.

</details>

## Limits

- Gemma 4 12B is a dense model. The MoE option in the family is Gemma 4 26B A4B, not this model.
- Ollama currently lists `gemma4:12b` with text and image input. Upstream materials describe broader audio and video-style capabilities, but runtime support may differ.
- Multimodal inputs can increase memory and latency beyond the base model size.
- Thinking mode and function calling need application-layer support and testing before use in agentic workflows.
- Unsloth's Gemma 4 reference settings are source-listed defaults, not measured Frugal AI guide settings for the 12B Unified checkpoint.
- Coding output still requires review, testing, and security checks before use in production systems.

## Used by

Follow [Local AI chat service](../../getting-started/offline-chat-service.md) to create the local `gemma4-dev` profile.

## Links

- [Hugging Face: google/gemma-4-12B](https://huggingface.co/google/gemma-4-12B)
- [Hugging Face: google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it)
- [Google Developers Blog: Gemma 4 12B developer guide](https://developers.googleblog.com/gemma-4-12b-the-developer-guide/)
- [Google launch post: Introducing Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)
- [Ollama: gemma4](https://ollama.com/library/gemma4)
- [Unsloth Hugging Face: gemma-4-12b](https://huggingface.co/unsloth/gemma-4-12b)
- [Unsloth: Gemma 4 local guide](https://unsloth.ai/docs/models/gemma-4)
