# Frugal AI Editorial Guide

Internal maintainer guide. Do not add this file to `docs/SUMMARY.md` or the root `SUMMARY.md`.

This guide translates the tone and writing style of Commonwealth of Learning Frugal AI material into a practical style guide for the Frugal AI knowledge base.

## Source Inputs

- [COL Frugal page](https://www.col.org/frugal/)
- [Frugal AI: A Blueprint for Digital Sovereignty in Commonwealth Education](https://www.col.org/news/frugal-ai-a-blueprint-for-digital-sovereignty-in-commonwealth-education/), 28 November 2025
- [Frugal AI: A Roadmap to Sovereign GenAI for Education](https://www.col.org/news/frugal-ai-a-roadmap-to-sovereign-genai-for-education/), 13 February 2026
- [COL Connections, April 2026, Vol. 31 No. 1](https://oasis.col.org/server/api/core/bitstreams/51a0562e-d4d1-4cd6-9011-18963b498475/content), especially the Frugal AI focus and tech trends sections

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

## Unified Knowledge Base Voice

Write as a practical institutional field guide. The knowledge base should be direct enough for builders, sober enough for education leaders, and clear enough for readers who are evaluating risk, cost, and capacity.

The voice should be:

- Practical: explain what to do, what it depends on, and how to verify it.
- Institution-friendly: respect governance, procurement, privacy, accessibility, and public accountability.
- Local-first: treat local control, offline operation, and open components as design choices with trade-offs.
- Capacity-focused: show how implementation builds internal skill, not only how it delivers a tool.
- Evidence-aware: separate tested facts, estimates, assumptions, and future possibilities.
- Teacher-centred: position AI as support for educators and institutions, not a replacement for professional judgement.

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

Use British and Commonwealth spelling where natural: "optimised", "localised", "specialised", "centre", "licence" as a noun, and "licensing" as a verb.

Use "cloud dependency" carefully. Do not imply that all cloud use is wrong. Say what risk is being managed: cost volatility, bandwidth reliance, data jurisdiction, vendor lock-in, or governance complexity.

Treat affordability as one part of sovereignty. Avoid reducing Frugal AI to cost-cutting.

State limits. If a setup is for development, say so. If performance is estimated, label it as an estimate. If a claim needs local validation, say what to test.

Keep people in the loop. When AI affects learners, assessment, content, or institutional decisions, name the human review point.

Use examples from education. Prefer scenarios such as local chat, course search, teacher support, OER adaptation, administrative helpdesk, and Moodle support.

## Page Patterns

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
- Avoids hype, deficit framing, and vendor-hostile language.
- Keeps headings clear enough for both human readers and LLM retrieval.
- Links to the next practical page rather than ending in abstract framing.

## Publication Guardrail

This file is internal guidance. Keep it outside the GitBook publishing surface:

- Do not link it from `docs/SUMMARY.md`.
- Do not link it from the root `SUMMARY.md`.
- Do not move it into `docs/`.
- If a public-facing style note is later needed, create a separate, shorter page written for readers rather than maintainers.
