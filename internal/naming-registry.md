# Frugal AI Naming Registry

Internal maintainer reference. This file is not published in the Frugal AI knowledge base.

This registry sets naming *principles and patterns*, not a fixed catalogue. Use it as guidance when creating or revising public pages under `docs/` and templates under `internal/templates/`. The current stack appears throughout as a worked example; when the stack changes, update the examples, not the principles.

A small set of these rules is enforced automatically by `internal/tools/editorial_audit.py` and is marked **(audited)** below. Treat audited rules as firm and the rest as sensible defaults that can flex with good reason.

## Principles

- Name each thing one way and reuse that form across prose, navigation, and titles.
- Write the first screen for education stakeholders — purpose, risk, cost, governance, institutional fit, in plain language. Developer detail (exact tags, settings, commands, links) can follow lower on the page.
- Prefer the reader-facing service name over the underlying tool name in titles and navigation.
- Put a detail in a name (memory size, version, capacity) only when it changes whether a documented path works.
- Use British/Commonwealth spelling, and frame the work as Frugal AI rather than "cheap AI".

## Audience

The knowledge base serves two audiences: education stakeholders who need plain-language purpose, risk, cost, governance, and institutional fit; and developers and maintainers who need exact component names, model tags, settings, commands, and source links. The first screen should work for stakeholders.

## Site Name

Refer to the published reader experience as **Frugal AI knowledge base** (lower-case "knowledge base"). The capitalised "Frugal AI Knowledge Base" is allowed only as the landing-page H1 **(audited)**. Reserve `GitBook` for the publishing platform or its syntax; avoid `docs`, `documentation site`, or casual variants when naming the reader experience.

## Page Types

Common page jobs: route readers (landing), complete one practical task (guide), explain a decision or trade-off (concept), describe one component's fit and limits (component card, including model, hardware, runtime, application/interface, and environment variants), operate and recover a service (runbook), and define terms or collect source links (reference). Each page should do one of these jobs.

## Architecture Layers

The knowledge base is organised around a layered model of a Frugal AI system. Use these layer names consistently in prose, navigation, and component grouping. The full rationale lives in the architecture page, "The Frugal AI stack".

| Layer | Role | Public name |
| --- | --- | --- |
| Infrastructure | Compute, operating system, containers, storage, and networking. | `Infrastructure` |
| Inference | Runs the model and serves predictions; local runtimes through to serving engines. | `Inference` |
| Orchestration | The loop, tools, memory, retrieval, and context that turn a model into a workflow. | `Orchestration` (reserve `harness` for prose) |
| Application | What a person uses: chat, search, coding, and agents. | `Application` |
| Gateway | The governed boundary every request passes through: routing, compliance, observability, and guardrails. | `Gateway`, described as the `sovereignty envelope` |

Naming rules for the layers:

- An agent is an `Application` subtype, not a separate layer. Continue to reserve `AI agent` for tool-using paths.
- Describe the gateway as the `sovereignty envelope` when explaining governance; it is the operational form of the privacy-airlock and cloud-burst controls in the reference architecture.
- Layers are optional and substitutable; the smallest build (`Infrastructure` plus `Inference` plus `Application`, gateway local-only) is the frugal floor, not a degraded version.

## Naming Patterns

Use the patterns below; the current-stack values are examples to follow, not the only permitted names.

Services — name by what the reader does, not the tool underneath. Use a reader-facing service name for the build guide (current example: `Local AI chat service`, not "Offline chat service" — **audited**) and `<service name> operations` for its operations page (current example: `Local AI chat service operations`, not "Open WebUI operations" — **audited**). Reserve `AI agent` for future paths involving tool use, workflow actions, or orchestration beyond chat (current example: `Institutional AI agent pilot`).

Applications — name a named AI application by its capability and role, and revisit names as capability grows rather than defaulting to "assistant". Reserve `agent` for applications that take actions (the Application-layer agent subtype). Keep `assistant` only as the generic word for a non-agentic application that answers — not as the name of any application. Current named applications: `Math tutor`, `Curriculum advisor` (renamed from "Curriculum knowledge assistant", 2026-06-08), `Coding agent`, `Manim animator`. The planned example-applications row `Administrative agent` (renamed from "Administrative helpdesk", 2026-06-08) performs routine staff tasks — it acts, so it is correctly an `agent`, not an assistant. The SUMMARY entry for the curriculum guide is **audited**, and a `.gitbook.yaml` redirect preserves the old `curriculum-assistant` URL.

Hardware — include memory only when it is central to whether a path works, and write it as `GB`, not `Gb` (current example: `Mac mini 24 GB`; the "Mac mini" capitalisation and "24 GB" spacing are **audited**). Do not add a spec to a title unless pages need to distinguish configurations.

Components — name each component once and give it a short first-use explanation (current examples: `Ollama`, the local model runtime; `Open WebUI`, the browser chat interface; `Development environment`; `Pilot environment`; and models by their published tag, such as `Gemma 4 12B`, the first-path default since 2026-06-12, or `Qwen3.5-9B`, the alternative it replaced). The first-path Ollama model profile is `gemma4-dev` (8K context); the retired `qwen3.5-dev` profile name stays only on the Qwen3.5-9B card as the alternative pattern.

## Navigation And Titles

In `docs/SUMMARY.md`, give component pages a role prefix that names the kind within its layer — one of `Hardware:`, `Environment:`, `Runtime:`, `Serving engine:`, `Model:`, `Platform:`, `Gateway:`, `Interface:`, `Agent:`, or `Coding Agent:` — and give guide and operations pages their reader-facing service name. Each layer section opens with its `... layer` overview page (for example `Inference layer`), and its component cards nest under that overview. Open WebUI is an `Interface:` (the chat interface in the Application layer), not a framework; OpenCode is labelled `Coding Agent:` in the sidebar (renamed from `Agent:` 2026-06-09); Dify is a `Platform:` in the Orchestration layer. Sidebar labels and H1s should correspond, with two common variations: a component H1 may drop the role prefix (sidebar `Hardware: Mac mini 24 GB`, H1 `Mac mini 24 GB`), and an environment H1 reads as a noun phrase (`Development environment`). The editorial audit enforces this approved set of role prefixes.

The audit also requires a specific set of linked summary entries with exact reader-facing labels. Run `internal/tools/editorial_audit.py` after navigation changes rather than hand-verifying them.

`MCP server:` is not a sidebar role (decision 2026-06-12). MCP servers are described in prose as substitutable Orchestration-layer components (see the orchestration layer page, the glossary, and the OpenCode card); none has its own component card. If an MCP-server card is ever added, register a role label here first, in keeping with the naming gate.

## Reader-Friendly Explanations

Expand technical terms in plain language on first use — for example: runtime ("the software that runs the model"), interface, open-weight model, context window, multimodal, Mixture of Experts, and Model Context Protocol ("MCP, a standard way to supply tools to agents"). Expand "Mixture of Experts" before using "MoE" on the first screen **(audited)**.

## Port Allocations

Every service exposed on a host port is registered here, so that two services never claim the same port as the knowledge base grows. The editorial audit flags a duplicate in this table, and any host port bound in a guide that is missing from it. Ports are the upstream defaults; record a new service here before documenting it.

| Host port | Service |
| --- | --- |
| 80 | Dify dashboard (nginx) |
| 1234 | LM Studio local server (alternative runtime) |
| 3000 | Open WebUI, development path |
| 4000 | LiteLLM gateway |
| 5001 | Presidio anonymiser |
| 5002 | Presidio analyzer |
| 8080 | Open WebUI, integrated image on DGX Spark |
| 11434 | Ollama API |

## Preferred Terms

Prefer the values-aligned framing: Frugal AI over "cheap AI"; local-first over "fully cloudless"; teacher-in-the-loop over "replacing teachers"; and open-weight models over "open models" when a licence point matters. The service titles, the "Mac mini" and "24 GB" forms, the "Frugal AI knowledge base" site name, and avoiding direct second person (`you`, `your`, `yours`) in public pages are all **(audited)**.

The landing hexagon's tier vocabulary is **goals and practices** — not "pillars", "ends", or "principles" (the principles page is internal). Goals: Frugality, Sovereignty, Openness. Practices: Local first, Teacher-in-the-loop, Capacity building, each opposite the goal it makes real. The graphics are generated by `internal/tools/generate_hexagons.py`; edit node names or one-liners there, not in the SVGs.
