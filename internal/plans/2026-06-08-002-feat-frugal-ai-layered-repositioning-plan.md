---
title: Frugal AI KB Layered Repositioning
type: feat
status: active
date: 2026-06-08
origin: Direction-setting brainstorm, 2026-06-08
relates-to: internal/plans/2026-06-08-001-feat-frugal-ai-docs-improvement-plan.md
---

# Frugal AI KB Layered Repositioning

## Overview

Reposition the Frugal AI knowledge base around an explicit layered architecture model, with the local AI chat service as the first vertical slice. The knowledge base shifts from a single small chat path to a developer/technical-first reference for building sovereign, local-first AI systems layer by layer. The work is incremental: each increment adds exactly one layer or one breadth dimension, and the published surface never advertises pages that do not yet exist.

This plan is the strategic spine. The content-quality backlog in `2026-06-08-001` (model-card accuracy, multilingualism, COL alignment, cost model, glossary consolidation, governance habits) remains valid and folds into the increments below.

## Decisions Locked (2026-06-08)

- **Sequence:** settle the model first, then the landing page.
- **Scope:** reposition now, build incrementally; mark unbuilt layers as planned.
- **Audience:** developer/technical-first on the public surface; stakeholder framing on dedicated pages and lower sections.
- **Reference architecture:** defer the annex revision to a later increment.
- **Apex:** Application is the top layer; an agent is an Application subtype, not its own layer.
- **Orchestration:** the public name for the layer above inference; reserve "harness" for prose.
- **Gateway = sovereignty envelope:** the gateway is a concrete layer in the request path and the single governance home; it is the operational form of the annex's privacy-airlock and cloud-burst controls.
- **Minimum-doc discipline:** showcase the design with the fewest pages; do not add a card per runtime or model.

## The Model

A Frugal AI system is assembled from substitutable, optional layers, governed at one boundary:

```text
Application        chat, coding, agents (subtype), search
Gateway            sovereignty envelope: routing, compliance, observability, guardrails
Orchestration      loop, tools, memory, retrieval, context        (optional)
Inference          local runtimes -> serving engines
Infrastructure     compute, OS, containers, storage, networking
```

Top-down is the request path; bottom-up is the build order. Layers are optional: the frugal floor is Infrastructure plus Inference plus Application, with the gateway local-only and no orchestration. The local chat service is exactly this floor.

## Architecture Model vs Information Architecture

The layer model is the spine of the build and components section only. Principles, operations, governance, and the reference annex are orthogonal sections and are not forced into layers.

## Increment Ladder

### Increment 0 — Showcase the design (first build)

Goal: make the layered model legible and credible on the existing slice, without new runtime or model pages.

- **Architecture page** — rework `docs/concepts/how-the-stack-fits-together.md` into "The Frugal AI stack": the four layers, gateway-as-sovereignty-envelope, request-path versus build-order, and the chat slice mapped to layers as the frugal floor. *(core)*
- **Landing page** — rework `docs/README.md`: developer-first, leads with the stack, routes by layer and by the running slice, gateway = sovereignty envelope as the governance hook. *(core)*
- **Principles** — light edit `docs/concepts/frugal-ai-principles.md`: add the sovereignty-envelope principle and "degrade to a minimal slice".
- **Layer labels** — tag the existing component pages by layer and reflect the grouping in `docs/SUMMARY.md`; re-point, not rewrite, the chat guide and operations pages.

Out (named, not built): LM Studio, llama.cpp, vLLM, and SGLang cards; coding and agent application pages; a gateway implementation guide; new model cards; the full component-tree reorganisation; the annex revision.

### Increment 1 — Orchestration layer

Add the orchestration layer page and the first orchestration slice (retrieval over approved OER, or a tool-using teacher assistant), with source governance and named human review.

### Increment 2 — Gateway as a running layer

Make the sovereignty envelope real: a router enforcing redaction, audit logging, approved destinations, and controlled cloud burst. Turns governance from concept into enforcement.

### Increment 3 — Inference breadth

Add serving engines (vLLM, SGLang) for pilot-scale throughput and alternative local runtimes (LM Studio, llama.cpp), mapped to development versus pilot environments.

### Increment 4 — Application breadth

Add coding assistance and agent applications on the same lower layers, with agent governance. Headline example: an OpenCode coding agent (open-source, terminal-first, local via Ollama) as the concrete agent (Application subtype) and a vivid gateway example, since it can route to cloud providers. Decision 2026-06-08: OpenCode was evaluated for Increment 1 and deferred here, because it is a finished coding agent rather than a neutral orchestration substrate for a teacher assistant.

### Increment 5 — Annex revision

Raise the sovereign education-AI reference architecture to high-level abstraction, relocating technical detail (RAG, MCP, layer specifics) into the now-existing layer pages.

## Guidance Staging

Pages lead, guidance follows, consistent with the editor-workflow's own rule.

**Now, before the architecture page (enabling):**

- Add the layer vocabulary to `internal/naming-registry.md`.
- Record the developer-first audience decision in `internal/editorial-guide.md` (note plus pointer; full rewrite deferred).

**After Increment 0 ships (derive from the real pages):**

- Rewrite the editorial guide audience model, landing-page pattern, and page-type taxonomy (add a "layer overview" type; introduce orchestration and gateway).
- Update the editor-workflow naming gate and page-classification table.
- Add a "Layer:" field to the component templates; extract a "layer overview" template from the architecture page.

**Not yet (no instance to template from):**

- Orchestration-page and gateway-page templates — wait for Increments 1 and 2.

## Audit Coupling

`internal/tools/editorial_audit.py` hardcodes the required `SUMMARY.md` entries and chat-path names. Any navigation change — for example re-grouping the sidebar by layer in Increment 0 — must update the audit's required-entries list in the same change, or the audit fails. Treat the audit as guidance-as-code that moves with navigation.

## Relationship to Plan 001

Plan 001 is the content-quality backlog on existing pages. Its items map into increments: COL alignment and the cost model inform the landing and principles (Increment 0); glossary consolidation and the audience split inform Increment 0; multilingualism and teacher-in-the-loop depth inform Increments 1 and 5; the governance-habit fixes inform Increment 2.

## Risks & Dependencies

| Risk | Mitigation |
|------|------------|
| Guidance rewritten before the model is proven in a page | Stage guidance: thin enabling slice now, bulk after Increment 0. |
| Sidebar re-grouping breaks the editorial audit | Update `editorial_audit.py` required entries in the same change. |
| Layered framing inflates the KB with empty layer pages | Minimum-doc discipline; name unbuilt layers as future and build per increment. |
| Gateway built as theatre before any egress exists | Keep the gateway a concept in Increment 0; implement in Increment 2. |
| Developer-first lead loses the ministry audience | Keep stakeholder framing on dedicated pages and lower sections. |

## Sources & References

- Direction-setting brainstorm, 2026-06-08.
- `internal/handoff-2026-06-08.md`, `internal/editorial-guide.md`, `internal/editor-workflow.md`, `internal/naming-registry.md`.
- Related plan: `internal/plans/2026-06-08-001-feat-frugal-ai-docs-improvement-plan.md`.
- COL Frugal page: `https://www.col.org/frugal`.
