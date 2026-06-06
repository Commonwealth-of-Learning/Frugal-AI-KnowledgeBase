---
date: 2026-06-05
topic: frugal-ai-knowledge-base-redesign
---

# Frugal AI Knowledge Base Redesign

## Problem Frame

The repository contains a practical Frugal AI knowledge base in `reference/`, but the GitBook-facing `docs/` tree is still generic platform template content with broken placeholder links. The redesign should turn `docs/` into a polished, minimal GitBook showcase for Frugal AI without porting the full knowledge base.

The first public slice should prove the documentation model through one complete path: setting up a local offline chat service with the supporting hardware, runtime, model, framework, environment, stack, and operations pages needed to understand and maintain it.

Research inputs:
- Commonwealth of Learning frames Frugal AI around inclusive, responsible, local, capacity-building AI, with emphasis on efficiency, sovereignty, local ownership, and avoiding cloud dependency.
- GitBook documentation favors clear page hierarchy, Markdown-native pages, concise headings, practical examples, and LLM-ready docs.
- Goose, Dify, and NVIDIA Spark docs all lead with short, concrete quickstarts or playbooks before deeper reference material.

---

## Actors

- A1. New local AI builder: Wants to get a private local chat service running with minimal conceptual overhead.
- A2. Institutional evaluator: Wants to understand whether the stack supports sovereignty, offline operation, cost control, and practical education use.
- A3. Docs maintainer: Needs a repeatable content pattern for adding future guides without bloating navigation.
- A4. AI assistant / LLM reader: Needs clear hierarchy, short sections, stable page titles, and practical examples to retrieve the right answer.

---

## Key Flows

- F1. Build the first offline chat service
  - **Trigger:** A reader lands on the docs and wants to run a local AI chat service.
  - **Actors:** A1
  - **Steps:** Start from the welcome page, choose Quickstart, verify prerequisites, set up Ollama and the model, start Open WebUI, verify the service, then use the ops page for restart or troubleshooting.
  - **Outcome:** The reader has a working offline chat service and understands which pages support the guide.
  - **Covered by:** R1, R2, R3, R5, R6

- F2. Evaluate Frugal AI fit
  - **Trigger:** A policymaker, educator, or technical lead wants to understand why this stack is framed as Frugal AI.
  - **Actors:** A2
  - **Steps:** Read the welcome page, skim principles, inspect the offline chat architecture, review component limits and safeguards, and understand what is intentionally out of scope.
  - **Outcome:** The evaluator can explain the value proposition and limits without reading the full reference corpus.
  - **Covered by:** R1, R4, R7, R8, R10

- F3. Extend the docs after the showcase
  - **Trigger:** A maintainer wants to add RAG, agents, pilot deployment, or production deployment later.
  - **Actors:** A3
  - **Steps:** Reuse the same guide -> stack -> components -> runbook pattern, add only pages needed by the new path, and keep deep reference material outside the first-level navigation until it supports a guide.
  - **Outcome:** The docs remain navigable as the knowledge base grows.
  - **Covered by:** R2, R3, R8, R9

---

## Requirements

**Navigation and scope**
- R1. Replace the generic GitBook template pages in `docs/` with a Frugal AI documentation slice centered on one runnable path: an offline chat service.
- R2. Do not port all `reference/` content into `docs/`; include only pages required to make the offline chat guide coherent and credible.
- R3. Use a GitBook structure that starts with a short Welcome, Quickstart, and Guide path, then exposes supporting concepts, component cards, and operations pages.
- R4. Keep the sovereign education architecture as a framing page or concept summary, not as the main entry point for a first-time builder.

**Showcase content set**
- R5. The minimum guide path must include an offline chat service guide derived from `reference/guides/01-offline-chat-service.md`.
- R6. Supporting pages must include the Mac Mini 24 GB environment, Ollama runtime, Qwen3.5-9B model card, Open WebUI framework card, development environment, and Open WebUI operations runbook.
- R7. Include a compact Frugal AI principles page that explains local control, offline capability, open-source preference, cost discipline, data sovereignty, and teacher/institutional capacity.
- R8. Keep broader pages such as Dify, agentic frameworks, LM Studio, DGX Spark, large model cards, RAG, and production deployment out of the first showcase unless they are linked as "coming next" or "not in this path."

**Page patterns**
- R9. Each guide should follow a consistent pattern: outcome, time, prerequisites, architecture or component map, steps, verification, troubleshooting, and next step.
- R10. Each component card should follow a consistent pattern: what it is, when to use it, requirements, frugal fit, compatibility, limits, and links.
- R11. Each runbook should follow a consistent pattern: scope, start/stop, health checks, maintenance, backup/recovery, troubleshooting, and escalation notes.

**Tone and style**
- R12. Use a practical, calm, institution-friendly voice: direct enough for builders, sober enough for education and public-sector readers.
- R13. Prefer short paragraphs, numbered steps, verification tables, and concrete commands over abstract explanation.
- R14. Distinguish tested values from estimates wherever performance, memory, or hardware limits are discussed.
- R15. Use British/Commonwealth spelling consistently where natural, matching the current `reference/` tone: "optimised", "localised", "quantisation", "artefact".
- R16. Include a dedicated editorial review pass across all rewritten `docs/` pages for consistent tone, simplified language, repeated terminology, heading hierarchy, and unnecessary jargon.

**GitBook affordances**
- R17. Preserve useful GitBook blocks from the template only where they improve scanning: cards for entry points, hints for warnings or success states, tabs only for genuine platform variants, and stepper blocks for procedural flows.
- R18. Remove placeholder platform concepts, broken links, fake deployment examples, and generic SaaS language from `docs/`.
- R19. Keep headings clear and hierarchical so published GitBook `.md`, `llms.txt`, and MCP exposure remain useful to AI readers.

---

## Acceptance Examples

- AE1. **Covers R1, R2, R3.** Given a reader opens the GitBook docs, when they scan the sidebar, they see a compact Frugal AI path rather than a full mirror of every `reference/` page.
- AE2. **Covers R5, R6, R9.** Given a reader follows the offline chat guide, when they need context on the model, runtime, or hardware, each linked supporting page exists in `docs/` and answers that specific question.
- AE3. **Covers R12, R13, R14.** Given a page mentions memory footprint or tokens per second, when the number is estimated, the page labels it as estimated instead of presenting it as measured.
- AE4. **Covers R17, R18.** Given the implementation is complete, when searching `docs/` for template terms like "workspace", "deploy", "custom domain", or broken GitBook page IDs, those placeholder concepts are gone unless they are genuinely relevant to Frugal AI.
- AE5. **Covers R12, R13, R15, R16.** Given the first content draft is complete, when the editorial pass runs, every page uses the same voice, plain-language terminology, consistent spelling, and a predictable page pattern.

---

## Success Criteria

- A first-time reader can understand the Frugal AI thesis and reach a working offline chat service path within two clicks from the welcome page.
- The `docs/` sidebar contains a small, coherent GitBook information architecture rather than a reference dump.
- The guide, component cards, and runbook use visibly consistent page structures and voice.
- The docs are LLM-friendly: stable headings, concise sections, practical examples, and no broken placeholder links.
- A downstream implementation plan can map each required page to source material in `reference/` without inventing product scope.

---

## Scope Boundaries

- Do not port the entire `reference/` tree into `docs/`.
- Do not build RAG, Dify, multi-agent, DGX Spark, or production-serving documentation in the first showcase.
- Do not convert the knowledge base into a policy-only or academic publication; it must remain practical and build-oriented.
- Do not add unverified new benchmark claims during the docs rewrite.
- Do not redesign GitBook styling beyond Markdown/GitBook content structure.
- Do not remove `reference/`; treat it as source material and a deeper working library.

---

## Recommended GitBook Structure

```text
docs/
  README.md
  SUMMARY.md
  getting-started/
    quickstart.md
    offline-chat-service.md
  concepts/
    frugal-ai-principles.md
    how-the-stack-fits-together.md
  components/
    hardware/mac-mini-24gb.md
    runtimes/ollama.md
    models/qwen-3.5-9b.md
    frameworks/open-webui.md
    environments/development.md
  operations/
    open-webui-ops.md
  reference/
    glossary.md
```

Sidebar recommendation:

```markdown
# Table of contents

* [Welcome](README.md)

## Start here
* [Quickstart](getting-started/quickstart.md)
* [Offline chat service](getting-started/offline-chat-service.md)

## Concepts
* [Frugal AI principles](concepts/frugal-ai-principles.md)
* [How the stack fits together](concepts/how-the-stack-fits-together.md)

## Components
* [Mac Mini 24 GB](components/hardware/mac-mini-24gb.md)
* [Development environment](components/environments/development.md)
* [Ollama](components/runtimes/ollama.md)
* [Qwen3.5-9B](components/models/qwen-3.5-9b.md)
* [Open WebUI](components/frameworks/open-webui.md)

## Operations
* [Open WebUI operations](operations/open-webui-ops.md)

## Reference
* [Glossary](reference/glossary.md)
```

---

## Key Decisions

- Use the offline chat service as the showcase path: it is the smallest complete Frugal AI workflow already represented in `reference/`.
- Put builder docs before policy framing: the site should earn trust by helping users run something, then explain why the architecture matters.
- Keep component cards short and linked from the guide: they support decision-making without interrupting the procedural flow.
- Keep the first GitBook slice intentionally small: this prevents a navigation dump and gives future guides a repeatable expansion pattern.
- Use a sober field-guide tone: practical commands and verification steps, with clear acknowledgement of constraints and estimates.

---

## Dependencies / Assumptions

- GitBook Git Sync will consume the `docs/` tree as the published space.
- The `reference/` folder remains available as source material during planning and implementation.
- The current offline chat path remains Mac Mini 24 GB + Ollama + Qwen3.5-9B + Open WebUI unless planning uncovers a factual issue.
- External product facts may need verification during implementation where source pages have changed since this brainstorm.

---

## Outstanding Questions

### Resolve Before Planning

- None.

### Deferred to Planning

- [Affects R6][Needs research] Verify whether `qwen3.5:9b` and the current Qwen3.5-9B claims in `reference/` are accurate against upstream model/runtime sources before publishing.
- [Affects R16][Technical] Confirm which GitBook blocks render correctly from repository-authored Markdown in this project’s Git Sync setup.
- [Affects R17][Technical] Decide whether old placeholder docs should be deleted, replaced in place, or left as redirects if GitBook has already indexed them.

---

## Next Steps

-> `/ce-plan` for structured implementation planning.
