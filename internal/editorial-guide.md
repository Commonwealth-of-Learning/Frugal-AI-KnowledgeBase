# Frugal AI Editorial Guide

Internal maintainer guide. Do not add this file to `docs/SUMMARY.md` or the root `SUMMARY.md`.

This guide translates the tone and writing style of Commonwealth of Learning Frugal AI material into a practical style guide for the Frugal AI knowledge base.

For the repeatable page review process, use `internal/editor-workflow.md`.

For approved public names, sidebar labels, hardware names, service names, and reader-friendly term explanations, use `internal/naming-registry.md`.

## Source Inputs

- [COL Frugal page](https://www.col.org/frugal/)
- [Frugal AI: A Blueprint for Digital Sovereignty in Commonwealth Education](https://www.col.org/news/frugal-ai-a-blueprint-for-digital-sovereignty-in-commonwealth-education/), 28 November 2025
- [Frugal AI: A Roadmap to Sovereign GenAI for Education](https://www.col.org/news/frugal-ai-a-roadmap-to-sovereign-genai-for-education/), 13 February 2026
- [COL Connections, April 2026, Vol. 31 No. 1](https://oasis.col.org/server/api/core/bitstreams/51a0562e-d4d1-4cd6-9011-18963b498475/content), especially the Frugal AI focus and tech trends sections
- [NVIDIA DGX Spark build page](https://build.nvidia.com/spark)
- [Dify Docs introduction](https://docs.dify.ai/en/use-dify/getting-started/introduction)
- [Claude Platform docs home](https://platform.claude.com/docs/en/home)
- [Docker Docs home](https://docs.docker.com/)

## Source Tone And Style

### COL Frugal Page

Tone: institutional, values-driven, multilateral, and calm. The page presents Frugal AI as part of a longer COL technology tradition rather than as a new product launch.

Style: short thematic sections, broad policy framing, repeated emphasis on inclusion, equity, responsible governance, open education, local capacity, and digital public goods.

Use this for: framing pages, principles pages, and introductions that need to connect practical AI deployment to public value.

Avoid carrying over: broad institutional language without a concrete next step.

### Blueprint Article

Tone: strategic and persuasive, aimed at education leaders who need to understand why cloud-first AI creates cost, privacy, sustainability, and capacity risks.

Style: clear problem-to-solution structure. It names barriers first, then introduces a three-part blueprint, then shows what the blueprint enables for students, staff, and leadership.

Use this for: decision briefs, architecture overviews, and pages that need to explain why local-first deployment matters.

Avoid carrying over: claims that sound complete or universal before implementation limits are stated.

### Roadmap Article

Tone: sober, architectural, governance-minded, and teacher-centred. It is more precise than promotional copy and treats AI as long-term institutional infrastructure.

Style: definition first, risk framing second, strategic pillars third, then a classroom-centred example. It uses memorable framing sparingly, then explains the operating model behind it.

Use this for: core concept pages, reference architecture pages, teacher-in-the-loop guidance, and governance sections.

Avoid carrying over: slogan-like lines unless the page immediately turns them into operational guidance.

### COL Connections PDF

Tone: accessible, optimistic, trend-aware, and magazine-like. It makes the same themes easier to scan through focus sections, tips, examples, and short summaries.

Style: narrative hooks, practical sidebars, "top five" lists, concise examples, and strong transitions from policy to classroom or institutional use.

Use this for: quickstart introductions, summaries, callouts, and scannable guidance.

Avoid carrying over: hype words, urgency without evidence, or claims that overpromise speed, scale, or impact.

## Documentation Site Patterns

### NVIDIA DGX Spark

Tone: developer-facing, action-oriented, and workflow-led. The page starts from a concrete local AI outcome, then routes readers into time-boxed playbooks.

Style: short headlines, compact descriptions, visible time estimates, and playbook cards. It uses "First Time Here?" as a routing device before exposing a larger catalogue.

Use this for: landing-page entry cards, quickstart labels, and future guide indexes where each path has a clear task, time estimate, and outcome.

Avoid carrying over: large catalogues before the Frugal AI knowledge base has enough complete paths to support them.

### Dify Docs

Tone: concise, product-definition first, and low-friction. The introduction uses a short definition followed by a small set of routing choices.

Style: minimal prose, clear section labels, and simple next-step cards such as quick start, concepts, self-hosting, and tutorials.

Use this for: a short landing-page definition, clean routing cards, and first-page navigation that keeps the reader moving.

Avoid carrying over: broad platform categories that do not exist yet in the Frugal AI knowledge base.

### Claude Platform Docs

Tone: build-oriented and lifecycle-aware. The home page routes readers by build surface and then by stages such as getting started, building, evaluating, shipping, and operating.

Style: short framing copy, direct calls into core workflows, and progressive disclosure from quickstart to production concerns.

Use this for: organising Frugal AI content around a lifecycle: orient, build, evaluate, operate, then scale.

Avoid carrying over: code-forward landing-page patterns. The Frugal AI knowledge base landing page should route to procedural guides rather than present code immediately.

### Docker Docs

Tone: task-led and question-led. The home page starts with common reader questions and broad entry points such as getting started, guides, manuals, and reference.

Style: simple question prompts, featured topics, and clear content types.

Use this for: reader-path tables and "start from the task" framing.

Avoid carrying over: broad product documentation structure before the knowledge base has multiple mature product areas.

### Combined Landing-Page Pattern

The Frugal AI knowledge base landing page should:

- open with one grounded definition for partner institutions and ministries;
- route first-time readers into time-boxed next steps;
- explain why sovereign AI, open technologies, data ownership, compliance, guardrails, and local capacity matter;
- separate stakeholder, builder, pilot, and maintainer needs;
- name guardrails before moving into technical detail;
- show the first stack as a compact layer map lower on the page;
- state what the first path proves;
- state what is out of scope;
- mark future paths as future work until supporting pages exist.

It should not:

- open with technical stack detail before the institutional purpose is clear;
- show long shell scripts or custom code snippets;
- imply production readiness before operations and governance pages exist;
- expose a large catalogue of future topics as if the pages already exist.

## Unified Knowledge Base Voice

Write as a practical institutional field guide. The knowledge base should be direct enough for builders, sober enough for education leaders, and clear enough for readers who are evaluating risk, cost, and capacity.

The voice should be:

- Practical: explain what to do, what it depends on, and how to verify it.
- Institution-friendly: respect governance, procurement, privacy, accessibility, and public accountability.
- Local-first: treat local control, offline operation, and open components as design choices with trade-offs.
- Capacity-focused: show how implementation builds internal skill, not only how it delivers a tool.
- Evidence-aware: separate tested facts, estimates, assumptions, and future possibilities.
- Teacher-centred: position AI as support for educators and institutions, not a replacement for professional judgement.

## Audience Model

> **Repositioning note (2026-06-08, see `internal/plans/2026-06-08-002-feat-frugal-ai-layered-repositioning-plan.md`):** The public surface is moving to a developer/technical-first lead. The first screen of landing and architecture pages now states the architecture and the build path, with stakeholder framing (purpose, risk, cost, governance) carried on dedicated pages and lower sections. The stakeholder-first instruction below is superseded for those pages and will be rewritten once Increment 0 ships; until then, follow the plan's audience decision.

Write for two audiences at once.

Education stakeholders need to understand purpose, risk, cost, governance, institutional fit, and the role of human oversight without reading commands.

Developers and maintainers need exact component names, model IDs, runtime tags, settings, commands, verification steps, and source links.

The first screen of a public page should answer the stakeholder question: what is this, why does it matter, and what are the limits? Developer details should remain available lower on the page.

## Core Message

Frugal AI is not cheap AI. It is a local-first, open, and capacity-building approach to AI infrastructure for education. Its purpose is to help institutions control data, costs, reliability, and expertise while still giving learners and educators useful AI services.

When writing, connect every technical choice back to at least one of these outcomes:

- Data and institutional control
- Predictable cost and reduced vendor dependency
- Offline or low-connectivity resilience
- Open-source or open-weight adaptability
- Teacher-in-the-loop or human oversight
- Local skills and long-term maintainability
- Alignment with public-interest education

## Writing Rules

Start with the reader's decision or task. Explain the problem before the principle.

Use short paragraphs. One idea per paragraph is usually enough.

Prefer concrete nouns and verbs. Say "run the model locally", "check the service", or "keep data on the institution's server" instead of abstract phrases such as "enable transformational capability".

Avoid direct second person in public docs. Prefer "the institution", "the local team", "the operator", "the guide", or imperative steps with no subject. Use direct second person only when removing it would make a safety warning or procedural instruction unclear.

Use British and Commonwealth spelling where natural: "optimised", "localised", "specialised", "centre", "licence" as a noun, and "licensing" as a verb.

Use "cloud dependency" carefully. Do not imply that all cloud use is wrong. Say what risk is being managed: cost volatility, bandwidth reliance, data jurisdiction, vendor lock-in, or governance complexity.

Treat affordability as one part of sovereignty. Avoid reducing Frugal AI to cost-cutting.

State limits. If a setup is for development, say so. If performance is estimated, label it as an estimate. If a claim needs local validation, say what to test.

Leave out empty or unverifiable sections. If a template section has no verified content, remove the section instead of writing that the information is unavailable, cannot be found, or has not been verified.

Keep people in the loop. When AI affects learners, assessment, content, or institutional decisions, name the human review point.

Use examples from education. Prefer scenarios such as local chat, course search, teacher support, OER adaptation, administrative helpdesk, and Moodle support.

Use the site name consistently. In public-facing copy, call the site the "Frugal AI knowledge base". Avoid substituting "GitBook", "docs", "documentation site", or "this knowledge base" when referring to the published reader experience. Use "GitBook" only when discussing the publishing platform or GitBook-specific syntax.

Use the naming registry before drafting or revising public pages. Service names, hardware names, model names, runtime names, interface names, and sidebar labels should match `internal/naming-registry.md`.

Prefer service-level names over tool-level names when naming guides and runbooks. Use `Local AI chat service` for the current first build guide and `Local AI chat service operations` for the operations page.

Use exact product names where precision matters: `Ollama`, `Open WebUI`, `Qwen3.5-9B`, `Qwen3.6-35B-A3B`, and `Gemma 4 12B`.

Explain unfamiliar technical terms on first use. Expand `Mixture of Experts` before using `MoE`, and explain `runtime`, `interface`, `context window`, and `open-weight model` when they first appear on a page for general readers.

Use `Mac mini 24 GB` for the current hardware card and `Mac mini with 24 GB unified memory` on first mention. Use `GB`, not `Gb`, for memory.

## Technical Writing Style

Use progressive disclosure. Landing pages and concept pages should route and frame. Guides and runbooks should carry procedural detail. Component pages should explain fit, limits, and verification.

Keep code out of landing pages unless the code is the product's main entry point. For the Frugal AI knowledge base, the landing page should point to the quickstart and guide instead of embedding commands.

Avoid customised code samples unless the page is specifically about code. Prefer standard commands, documented tool options, configuration tables, or short excerpts that can be verified locally.

Avoid long shell scripts. A shell block should normally contain one command. Two or three commands are acceptable only when they form one clear step. Longer setup flows should be split into numbered steps with explanations and verification after each step.

Do not use heredocs, generated scripts, or multi-command pipelines in public docs unless there is no simpler documented path. If a long script is unavoidable, move it into a maintained file and link to it from the guide.

For commands, include the expected result or a verification command. A command without a check leaves the operator guessing.

Prefer stable values over environment-specific values. Avoid local usernames, machine names, private paths, tokens, or values copied from a single development workstation.

For configuration, show the smallest meaningful excerpt. Explain the field being changed and the reason for the value.

For errors, write from symptom to cause to fix. Keep troubleshooting entries short and testable.

For time estimates, label them as estimates unless they have been measured in the documented environment.

## Page Patterns

### Landing Pages

Use this order:

1. Grounded definition
2. Partner and ministry context
3. Time-boxed entry cards
4. Why this matters
5. Reader-path table
6. Guardrails before scale
7. First local path
8. Proof points
9. Principles and source grounding
10. Scope boundaries
11. Future paths

Landing pages should not include shell commands, custom code, or long setup instructions. Link to the relevant quickstart or guide instead.

### Guides

Use this order:

1. Outcome
2. Fit and limits
3. Time and prerequisites
4. Component map
5. Steps
6. Verification
7. Troubleshooting
8. Next step

### Concepts

Use this order:

1. Problem
2. Definition
3. Why it matters
4. Practical design principles
5. Trade-offs
6. Example
7. Links to implementation pages

### Component Pages

Use this order:

1. What it is
2. When to use it
3. Requirements
4. Frugal fit
5. Compatibility
6. Limits
7. Verification
8. Links

### Runbooks

Use this order:

1. Scope
2. Start and stop
3. Health checks
4. Maintenance
5. Backup and recovery
6. Troubleshooting
7. Escalation notes

## Preferred Terms

| Prefer | Avoid |
| --- | --- |
| Frugal AI | cheap AI |
| local-first infrastructure | fully cloudless by ideology |
| local inference | on-prem magic |
| open-source tools | free tools as the main argument |
| open-weight models | open models, unless the licence is actually open source |
| data sovereignty | data ownership as a vague slogan |
| digital public goods | proprietary alternative without explanation |
| institutional capacity | upskilling as a generic benefit |
| teacher-in-the-loop | replacing teachers |
| human oversight | human approval theatre |
| operational resilience | always-on claims |
| predictable costs | cost-free |
| governance guardrails | compliance checkbox |

## Style Examples

Weak: "This solution revolutionises education with powerful AI."

Use: "This setup gives an institution a local chat service it can test, govern, and improve without sending routine data to an external provider."

Weak: "Cloud AI is unsafe and expensive."

Use: "Cloud-hosted AI can be useful, but it can also introduce cost volatility, bandwidth dependence, and data jurisdiction questions. Local-first deployment manages those risks where they matter most."

Weak: "Teachers can use AI to automate lesson creation."

Use: "AI can draft lesson materials, but teachers should review, adapt, and approve the output before it reaches learners."

Weak: "Frugal AI is a low-cost AI stack."

Use: "Frugal AI uses only the compute and services needed for a defined education task, with local control and long-term maintainability as design goals."

## Editorial Checklist

Before publishing a knowledge base page, check that it:

- Starts with a clear task, decision, or question.
- Explains why the topic matters for education.
- Connects technical detail to sovereignty, resilience, cost discipline, or capacity.
- Distinguishes tested values from estimates and assumptions.
- Names human oversight where learner-facing or policy-sensitive AI is involved.
- Uses consistent terms: Frugal AI, local-first, open-weight, teacher-in-the-loop, data sovereignty.
- Uses British/Commonwealth spelling.
- Avoids direct second person except where needed for safety or clarity.
- Avoids customised code samples unless the page is specifically about code.
- Avoids long shell scripts and multi-command setup blocks.
- Avoids hype, deficit framing, and vendor-hostile language.
- Keeps headings clear enough for both human readers and LLM retrieval.
- Links to the next practical page rather than ending in abstract framing.

## Publication Guardrail

This file is internal guidance. Keep it outside the GitBook publishing surface:

- Do not link it from `docs/SUMMARY.md`.
- Do not link it from the root `SUMMARY.md`.
- Do not move it into `docs/`.
- If a public-facing style note is later needed, create a separate, shorter page written for readers rather than maintainers.
