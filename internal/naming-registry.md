# Frugal AI Naming Registry

Internal maintainer reference. This file is not published in the Frugal AI knowledge base.

Use this registry before creating or revising public pages under `docs/` and templates under `internal/templates/`.

## Audience

The Frugal AI knowledge base serves two audiences:

- education stakeholders who need purpose, risk, cost, governance, and institutional fit in plain language;
- developers and maintainers who need exact component names, model tags, settings, commands, and source links.

The first screen of a public page should work for stakeholders. Developer details can appear lower on the page.

## Site Name

| Use | Approved form |
| --- | --- |
| Published reader experience | Frugal AI knowledge base |

Avoid using `GitBook`, `docs`, `documentation site`, or casual variants when referring to the published reader experience. Use `GitBook` only when discussing the publishing platform or GitBook-specific syntax.

## Page Type Names

| Page type | Purpose |
| --- | --- |
| Landing page | Route readers into the Frugal AI knowledge base |
| Guide | Complete one practical task |
| Concept | Explain a decision, principle, or trade-off |
| Component card | Explain fit, limits, and links for one component |
| Model card | Explain model identity, practical fit, settings, and limits |
| Hardware card | Explain local hardware fit, memory budget, and limits |
| Runbook | Operate, maintain, and recover a service |
| Reference page | Define terms or collect source links |

## Service Names

| Use | Approved name | Avoid |
| --- | --- | --- |
| First build guide | Local AI chat service | Offline chat service |
| Operations page | Local AI chat service operations | Open WebUI operations |
| Future tool-using workflow | Institutional AI agent pilot | AI agent for the current chat-only path |

Reserve `AI agent` for future paths that include tool use, workflow actions, agent orchestration, or other agentic behaviour beyond local chat.

## Hardware Names

Hardware names should include memory only when memory is central to whether a documented path works.

Use `GB`, not `Gb`, for memory.

| Use | Approved name | First mention |
| --- | --- | --- |
| Current first path hardware | Mac mini 24 GB | Mac mini with 24 GB unified memory |
| Future higher-capability hardware | NVIDIA DGX Spark | NVIDIA DGX Spark |

Do not include memory in the DGX Spark title unless future pages distinguish multiple DGX Spark memory configurations.

## Component Names

| Component type | Approved name | First-use explanation |
| --- | --- | --- |
| Environment | Development environment | Development environment for local testing |
| Runtime | Ollama | Ollama, the local model runtime |
| Framework | Open WebUI | Open WebUI, the browser chat interface |
| Model | Qwen3.5-9B | Qwen3.5-9B, the first-path local model |
| Model | Qwen3.6-35B-A3B | Qwen3.6-35B-A3B, a future MoE evaluation model |
| Model | Gemma 4 12B | Gemma 4 12B, a future dense multimodal evaluation model |

## Navigation Labels

Use role prefixes for component pages in `docs/SUMMARY.md`:

- `Hardware: Mac mini 24 GB`
- `Environment: Development environment`
- `Runtime: Ollama`
- `Model: Qwen3.5-9B`
- `Model: Qwen3.6-35B-A3B`
- `Model: Gemma 4 12B`
- `Framework: Open WebUI`

Use reader-facing service names for guide and operations pages:

- `Local AI chat service`
- `Local AI chat service operations`

## Title Patterns

| Page type | Sidebar pattern | H1 pattern |
| --- | --- | --- |
| Guide | `Local AI chat service` | `Local AI chat service` |
| Operations | `Local AI chat service operations` | `Local AI chat service operations` |
| Hardware card | `Hardware: Mac mini 24 GB` | `Mac mini 24 GB` |
| Runtime card | `Runtime: Ollama` | `Ollama` |
| Model card | `Model: Qwen3.5-9B` | `Qwen3.5-9B` |
| Framework card | `Framework: Open WebUI` | `Open WebUI` |

## Reader-Friendly Explanations

| Term | First-use explanation |
| --- | --- |
| runtime | the software that runs the model |
| interface | the browser or application people use to chat with the model |
| open-weight model | a model whose weights are available for local use under a specific licence |
| Mixture of Experts | a model design that activates part of a larger model for each token |
| MoE | Use only after `Mixture of Experts` has been expanded |
| context window | the amount of text and other input the model can consider at once |
| multimodal | able to work with more than one input type, such as text and images |

## Discouraged Terms

| Avoid | Prefer |
| --- | --- |
| cheap AI | Frugal AI |
| fully cloudless | local-first |
| Open WebUI operations, as a public service title | Local AI chat service operations |
| Offline chat service, as the public guide title | Local AI chat service |
| Mac Mini | Mac mini |
| Mac mini 24Gb | Mac mini 24 GB |
| open models, when licence is unclear | open-weight models |
| replacing teachers | teacher-in-the-loop |
