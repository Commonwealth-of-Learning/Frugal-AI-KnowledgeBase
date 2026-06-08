---
description: Multimodal Mixture of Experts model for agentic coding, tool use, and long-context evaluation.
icon: brain
---

# Qwen3.6-35B-A3B

_Layer: [Inference](../../concepts/how-the-stack-fits-together.md) (model)._

Qwen3.6-35B-A3B is a multimodal Mixture of Experts model from Qwen. It is a candidate model for future Frugal AI paths that need stronger agentic coding, repository-level reasoning, tool calling, visual understanding, and long-context work than the current first local AI chat service path.

## At a glance

| Question | Answer |
| --- | --- |
| Current role | Candidate model for future Frugal AI paths. |
| Best fit | Agentic coding, tool use, repository-level reasoning, and multimodal evaluation. |
| Local fit | Better suited to a measured higher-memory path than the current 24 GB Mac mini first path. |
| Model type | MoE model: 35B total parameters with about 3B active per token (Ollama labels the same model 36B). The full package still affects memory use. |
| Inputs | Text, image, and video-style visual inputs upstream; Ollama lists vision, tools, and thinking labels. |
| Main caution | Ollama lists the Q4_K_M package at 24 GB, before context, runtime, interface, and visual-input overhead. |

## Good for

- Agentic coding: frontend workflows, repository-level reasoning, code repair, and terminal-agent style tasks.
- Tool use: local agents where the application layer controls tool permissions, state, and audit logs.
- Multimodal understanding: images, screenshots, documents, diagrams, and video-frame style inputs.
- Long-context work: source-listed 262K native context and YaRN-based extension for specialised long-horizon tasks.
- Complex reasoning: source benchmark tables emphasise coding-agent, general-agent, STEM, and vision-language evaluations.

## Not suitable for

- The current local AI chat service guide without a separate measured setup path.
- Low-memory deployments where the 24 GB Ollama package leaves little room for context, runtime, and interface overhead.
- Production serving without concurrency, latency, security, and recovery testing.
- Sensitive learner or institutional data without local governance and human review.
- Autonomous agentic actions with real side effects unless permissions, audit logs, rollback, and human approval are designed into the workflow.
- Tasks requiring guaranteed code correctness, security review, or formal assessment decisions without expert validation.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Available as an open-weight Hugging Face model and as an Ollama tag. |
| Resource use | Ollama lists the Q4_K_M package at 24 GB, before context and visual-input overhead. |
| Hardware | Better suited to future higher-memory or carefully measured paths than the current 24 GB first path. |
| Replaceability | Can be evaluated as a higher-capability alternative when a guide needs agentic coding, tools, or multimodal reasoning. |
| Governance | Apache 2.0 licence is permissive, but institutional data rules and model-use policy still apply. |

## Reference settings

These settings are source-listed starting points for evaluation. They are not Frugal AI guide defaults.

| Profile | Context | Temperature | Top-p | Top-k | Min-p | Penalty | Thinking mode | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Thinking, general tasks | Up to 262,144 tokens | 1.0 | 0.95 | 20 | 0.0 | Presence 1.5; repetition 1.0 | Default mode | Hugging Face |
| Thinking, precise coding tasks | Up to 262,144 tokens | 0.6 | 0.95 | 20 | 0.0 | Presence 0.0; repetition 1.0 | Default mode | Hugging Face |
| Instruct or non-thinking mode | Up to 262,144 tokens | 0.7 | 0.80 | 20 | 0.0 | Presence 1.5; repetition 1.0 | Disabled through API parameters | Hugging Face |

Reference notes:

- Hugging Face states that Qwen3.6 models operate in thinking mode by default.
- Qwen3.6 does not officially support the older Qwen soft switch tokens for thinking and non-thinking mode.
- Qwen lists 32,768 output tokens as adequate for most queries and 81,920 tokens for highly complex benchmark tasks.
- Qwen advises maintaining at least 128K context to preserve thinking capability, but local Frugal AI paths still need memory and latency measurement before using high context.
- Sampling support varies by inference framework.

## Technical details

| Field | Value |
| --- | --- |
| Model ID | `Qwen/Qwen3.6-35B-A3B` |
| Ollama tag | `qwen3.6:35b-a3b` |
| Source | [Hugging Face model page](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) |
| Architecture | Hybrid Gated DeltaNet and Gated Attention model with a vision encoder |
| MoE status | 35B total parameters and 3B activated |
| Experts | 256 total, with 8 routed and 1 shared expert activated |
| Model licence | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) |

## Source confidence

| Claim | Value | Confidence |
| --- | --- | --- |
| Total and active parameters | 35B total, 3B activated | Source-listed by Hugging Face |
| Ollama parameter label | 36B | Source-listed by Ollama |
| Layers | 40 | Source-listed by Hugging Face |
| Hidden dimension | 2048 | Source-listed by Hugging Face |
| Token embedding | 248,320, padded | Source-listed by Hugging Face |
| Native context window | 262,144 tokens | Source-listed by Hugging Face |
| Extended context | Up to 1,010,000 tokens with RoPE scaling techniques such as YaRN | Source-listed by Hugging Face |
| Ollama size | 24 GB, Q4_K_M quantisation | Source-listed by Ollama |

Do not treat source benchmark tables as local performance claims. Measure speed, memory use, quality, and failure modes on the target machine before using this model in a guide.

## Limits

- The active 3B parameter count does not remove the memory cost of the larger model package, KV cache, vision encoder, or long context.
- Ollama lists a 24 GB Q4_K_M package, which is already close to the full memory of the current 24 GB Mac mini path before runtime overhead.
- Qwen's maximum-context serving examples target larger serving setups such as SGLang or vLLM with tensor parallelism. Local Ollama behaviour needs separate testing.
- Video support and frame sampling are runtime-specific.
- Thinking mode can increase token use and latency. Preserve-thinking behaviour should be evaluated before use in agentic workflows.
- Coding output still requires review, testing, and security checks before use in production systems.

## Links

- [Hugging Face: Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- [Hugging Face config: Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/blob/main/config.json)
- [Qwen blog: Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b)
- [Ollama: qwen3.6:35b-a3b](https://ollama.com/library/qwen3.6:35b-a3b)
