---
description: Dense multimodal alternative model for the local AI chat service path.
icon: brain
---

# Qwen3.5-9B

_Layer: [Inference](../../concepts/how-the-stack-fits-together.md) (model)._

Qwen3.5-9B is the smaller alternative model for the local AI chat service path; it was the documented default until [Gemma 4 12B](gemma-4-12b.md) replaced it (2026-06-12). It remains a practical local option: small enough to leave extra headroom on the documented 24 GB Mac mini path, and capable enough for general chat, explanation, light coding help, and simple visual tasks.

## At a glance

- **Current role** — Alternative model for the local AI chat service path; the documented default until 2026-06-12.
- **Best fit** — A private local chat service where a smaller download and more memory headroom matter.
- **Prefer it when** — Memory is tight, the download must stay small, or a task needs the family's source-listed coverage of up to 201 languages; the [model comparison](../../concepts/inference-layer.md) sets out the trade-offs against [Gemma 4 12B](gemma-4-12b.md).
- **Local fit** — Fits the documented 24 GB Mac mini path with the guide's 8K context setting.
- **Model type** — Dense 9B multimodal model. Dense means there is no separate total-versus-active parameter count to explain.
- **Inputs** — Text and image in Ollama; upstream sources also describe video-style visual inputs.
- **Languages** — Source-listed multilingual support across many languages; Qwen lists up to 201.
- **Agentic readiness** — Native function calling supports single read-only tools of the kind the [math tutor](../../getting-started/math-tutor.md) uses; small models can miss tool calls, so set Function Calling to Native when tools are not called reliably.
- **Main caution** — The source-listed 256K and 1M context figures are not the guide default. Larger contexts can sharply increase memory use and latency.

## Good for

- Local chat: a compact alternative for running the local AI chat service pattern with extra memory headroom.
- General assistance: explanation, summarisation, drafting, and local knowledge-base support.
- Light coding assistance: code explanation, small edits, debugging support, and test-writing prompts, with human review.
- Basic multimodal work: image-based questions, document screenshots, and visual reasoning where the runtime supports them.
- Long-context experiments after memory and latency are measured beyond the guide's 8K setting.

## Not suitable for

- Full 256K or 1M-token local contexts on the 24 GB path without separate measurement.
- Audio or speech workflows; this card covers the text and visual model path.

The [Inference layer](../../concepts/inference-layer.md) lists the cautions shared by every model, including production serving, sensitive data, and autonomous actions.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Runs without a cloud API key once downloaded. |
| Resource use | Ollama lists `qwen3.5:9b` at 6.6 GB, but context and visual inputs can add memory pressure. |
| Hardware | Fits the 24 GB Mac mini development path with an 8K context. |
| Replaceability | Can be swapped later if a guide needs a different model profile. |
| Governance | Apache 2.0 licence is permissive, but institutional data rules and model-use policy still apply. |

<details>

<summary><strong>Reference settings</strong></summary>

These settings separate the Frugal AI guide baseline from Unsloth's Qwen3.5 reference profiles. The current first path uses Ollama and an 8K local guide context; Unsloth settings should be treated as llama.cpp-compatible GGUF reference settings until tested in the documented path.

| Profile | Context | Temperature | Top-p | Top-k | Min-p | Penalty | Thinking mode | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Frugal AI guide setting | 8K | Runtime default | Runtime default | Runtime default | Runtime default | Runtime default | Not configured by the guide | Current guide |
| Non-thinking, general tasks | Up to 262,144 tokens | 0.7 | 0.8 | 20 | 0.0 | Presence 1.5; repeat disabled or 1.0 | Disabled by default for Qwen3.5 Small | Unsloth |
| Non-thinking, reasoning tasks | Up to 262,144 tokens | 1.0 | 0.95 | 20 | 0.0 | Presence 1.5; repeat disabled or 1.0 | Disabled by default for Qwen3.5 Small | Unsloth |
| Thinking, general tasks | Up to 262,144 tokens | 1.0 | 0.95 | 20 | 0.0 | Presence 1.5; repeat disabled or 1.0 | Explicitly enabled in supported runtimes | Unsloth |
| Thinking, precise coding tasks | Up to 262,144 tokens | 0.6 | 0.95 | 20 | 0.0 | Presence 0.0; repeat disabled or 1.0 | Explicitly enabled in supported runtimes | Unsloth |

Reference notes:

- Unsloth lists 32,768 tokens as an adequate output length for most Qwen3.5 queries. The first path does not set this as a generation limit.
- Unsloth lists `presence_penalty = 0.0 to 2.0` as an option for reducing repetitions, while noting that higher values may reduce performance.
- Unsloth states that Qwen3.5 Small models, including 9B, have reasoning disabled by default in its GGUF flow.
- Unsloth currently states that its Qwen3.5 GGUFs do not work in Ollama because of separate vision projection files. This does not remove the Ollama `qwen3.5:9b` registry tag this card documents, but it does mean Unsloth GGUF settings need a llama.cpp-compatible backend until separately tested.

</details>

## Technical details

| Field | Value |
| --- | --- |
| Model ID | `Qwen/Qwen3.5-9B` |
| Ollama tag | `qwen3.5:9b` |
| Source | [Hugging Face model page](https://huggingface.co/Qwen/Qwen3.5-9B) |
| Architecture | Dense hybrid Gated DeltaNet and Gated Attention model with a vision encoder |
| MoE status | Dense checkpoint. The Qwen3.5 family includes sparse MoE models, but this 9B card and config list FFN layers rather than routed-expert fields. |
| Model licence | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Local guide context | 8K, chosen for a comfortable development setup |

<details>

<summary><strong>Source confidence</strong></summary>

| Claim | Value | Confidence |
| --- | --- | --- |
| Parameter count | 9B | Source-listed by Hugging Face |
| Layers | 32 | Source-listed by Hugging Face |
| Hidden dimension | 4096 | Source-listed by Hugging Face |
| Token embedding | 248,320, padded | Source-listed by Hugging Face |
| Upstream context window | 262,144 tokens native, extensible up to 1,010,000 tokens | Source-listed by Hugging Face |
| Ollama context window | 256K tokens | Source-listed by Ollama |
| Ollama size | 6.6 GB | Source-listed by Ollama |
| Unsloth 9B memory bands | 5.5 GB, 6.5 GB, 9 GB, 13 GB, and 19 GB for 3-bit, 4-bit, 6-bit, 8-bit, and BF16 | Source-listed by Unsloth for Qwen3.5 GGUF-style use |

Do not treat source benchmark tables as local performance claims. Measure speed, memory use, quality, and failure modes on the target machine before increasing context length or using this model for production work.

</details>

## Limits

- Source-listed context limits are not the same as the Frugal AI guide setting.
- Ollama currently lists `qwen3.5:9b` with text and image input. Other runtime variants may expose different modality support.
- Unsloth's Qwen3.5 GGUF guidance is runtime-specific and should not be copied into the Ollama path without testing.
- Thinking mode and long answers can increase latency and token use.
- Coding output still requires review, testing, and security checks before use in production systems.

## Used by

An alternative model for the [Local AI chat service](../../getting-started/offline-chat-service.md) pattern: the guide's model-profile step transfers directly (`FROM qwen3.5:9b`, 8K context, profile name `qwen3.5-dev`). The documented path uses [Gemma 4 12B](gemma-4-12b.md).

## Links

- [Hugging Face: Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)
- [Hugging Face config: Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/config.json)
- [Ollama: qwen3.5](https://registry.ollama.com/library/qwen3.5)
- [Unsloth: Qwen3.5 local guide](https://unsloth.ai/docs/models/qwen3.5)
