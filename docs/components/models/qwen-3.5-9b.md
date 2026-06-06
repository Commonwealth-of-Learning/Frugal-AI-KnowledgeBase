---
description: Dense multimodal model used by the first offline chat service.
icon: brain
---

# Qwen3.5-9B

Qwen3.5-9B is the model used in the first offline chat path. It is a dense 9B multimodal model in the Qwen3.5 family and provides a practical baseline for local chat on the 24 GB Mac Mini path.

The Frugal AI knowledge base uses a smaller local context than the source-listed maximum. Treat this card as an operational profile, not a local benchmark claim.

## Identity

| Field | Value |
| --- | --- |
| Model ID | `Qwen/Qwen3.5-9B` |
| Ollama tag | `qwen3.5:9b` |
| Source | [Hugging Face model page](https://huggingface.co/Qwen/Qwen3.5-9B) |
| Architecture | Dense hybrid Gated DeltaNet and Gated Attention model with a vision encoder |
| MoE status | Dense checkpoint. The Qwen3.5 family includes sparse MoE models, but this 9B card and config list FFN layers rather than routed-expert fields. |
| Modality, upstream | Text, image, and video-style visual inputs with text output |
| Modality, Ollama tag | Text and image, source-listed |
| Model licence | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Local guide context | 8K, chosen for a comfortable development setup |

## Source confidence

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
| Memory use in first path | Comfortable at 8K context on the documented 24 GB Mac Mini path | Guide setting, not a full 256K measurement |

Do not treat source benchmark tables as local performance claims. Measure speed, memory use, quality, and failure modes on the target machine before increasing context length or using the model for production work.

## Reference settings

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
- Unsloth currently states that its Qwen3.5 GGUFs do not work in Ollama because of separate vision projection files. This does not remove the Ollama `qwen3.5:9b` registry tag used by the first path, but it does mean Unsloth GGUF settings need a llama.cpp-compatible backend until separately tested.

## Why this model fits the first path

- It has a ready-to-run Ollama tag with a small source-listed local size.
- It gives the first path a local multimodal baseline without requiring a cloud API key after download.
- Its dense 9B profile is easier to reason about operationally than a MoE model with separate total and active parameter counts.
- It supports long-context use upstream, while the public guide keeps context smaller to manage memory.
- It is capable enough for general chat, explanation, document-style tasks, and light coding assistance in a development setting.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Runs without a cloud API key once downloaded. |
| Resource use | Ollama lists `qwen3.5:9b` at 6.6 GB, but context and visual inputs can add memory pressure. |
| Hardware | Fits the 24 GB Mac Mini development path with an 8K context. |
| Replaceability | Can be swapped later if a guide needs a different model profile. |
| Governance | Apache 2.0 licence is permissive, but institutional data rules and model-use policy still apply. |

## Good for

- First-path local chat: a compact baseline for running the offline chat service.
- General assistance: explanation, summarisation, drafting, and local knowledge-base support.
- Coding assistance: lightweight code explanation, small edits, debugging support, and test-writing prompts, with human review.
- Agentic prototypes: local tool-use experiments where the application layer controls permissions, state, and side effects.
- Multimodal understanding: image-based questions, document screenshots, visual reasoning, and video-frame style inputs where the runtime supports them.
- Long-context experiments: staged tests beyond the 8K guide setting after memory and latency are measured.
- Multilingual tasks: broad language coverage where local validation confirms quality for the target language.

## Not suitable for

- Production serving without concurrency, latency, security, and recovery testing.
- Full 256K or 1M-token local contexts on the 24 GB path without separate measurement.
- Sensitive learner or institutional data without local governance and human review.
- Tasks requiring guaranteed code correctness, security review, or formal assessment decisions without expert validation.
- Autonomous agentic actions with real side effects unless permissions, audit logs, rollback, and human approval are designed into the workflow.
- Audio or speech workflows; this card covers the text and visual model path.

## Limits

- Qwen3.5-9B is treated here as a dense checkpoint. Family-level Qwen3.5 MoE statements should not be read as this card's MoE status.
- Ollama currently lists `qwen3.5:9b` with text and image input. Other runtime variants may expose different modality support.
- Unsloth's Qwen3.5 GGUF guidance is runtime-specific and should not be copied into the Ollama path without testing.
- Larger context windows can consume much more memory than the 8K guide setting.
- Thinking mode and long answers can increase latency and token use.
- Agentic behaviour depends on the surrounding application, tool permissions, logs, and recovery process.
- Coding output still requires review, testing, and security checks before use in production systems.

## Used by

Follow [Offline chat service](../../getting-started/offline-chat-service.md) to create the local `qwen3.5-dev` profile.

## Links

- [Hugging Face: Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)
- [Hugging Face config: Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/config.json)
- [Ollama: qwen3.5](https://registry.ollama.com/library/qwen3.5)
- [Unsloth: Qwen3.5 local guide](https://unsloth.ai/docs/models/qwen3.5)
