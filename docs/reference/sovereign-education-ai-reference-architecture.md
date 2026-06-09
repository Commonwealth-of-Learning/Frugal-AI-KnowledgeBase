---
description: How COL's sovereign education-AI reference architecture maps onto the Frugal AI knowledge base stack.
icon: landmark
---

# Sovereign education-AI reference architecture

**Teacher-led, localised, Frugal AI for equitable education**

This page connects COL's Technical Annex for a sovereign education-AI reference architecture to the builds in this knowledge base. The annex is not a product, a procurement specification, or a deployment guide: it is a reference architecture and an options menu for education-AI services that keep data, policy, and governance under national or institutional control, written especially for Small Island Developing States and low- and middle-income countries.

{% hint style="info" %}
This page abstracts the annex rather than reproducing it. The [original COL technical annex](https://www.col.org/wp-content/uploads/2026/02/Technical-Annex-for-Sovereign-Education.pdf) is the authoritative source for the full tables, the pilot blueprint, and the ministry self-assessment checklist.
{% endhint %}

## How to read this page

The annex is written for ministries and public-education partners; this knowledge base is developer-first. This page is the bridge between them. A developer reads it to see which governance requirement each build satisfies. An official reads it to see how the annex's architecture maps onto a real, running build.

## The annex in brief

- **Developed by** — Commonwealth of Learning, as a reference resource.
- **Purpose** — A reference architecture and options menu for sovereign, Frugal AI in education; countries may adopt, adapt, or set aside as appropriate.
- **Audience** — Senior officials, EMIS and ICT units, curriculum authorities, teacher-education institutions, public universities, and regulators.
- **Status** — v1, February 2026; for discussion and adaptation.
- **Scope** — Teacher support and system enablement. High-stakes automated decisions, such as student progression or certification, are out of scope.

## Two views of one system

The annex and this knowledge base describe the same kind of system through different lenses. The annex organises by **governance concern** into eight layers (A–H). The knowledge base organises by the **request and build path** into four layers plus a gateway. They are not in conflict; the crosswalk below maps one onto the other.

| Annex layer (governance view) | Knowledge base realisation (build view) | State in the first build |
| --- | --- | --- |
| A. Access and identity | Single-user, localhost-bound | Minimal; role-based access, MFA, and SSO are pilot-scale further work |
| B. Teacher-in-the-loop workflow | Cross-cutting; named human review in every learner-facing guide | Present, governed by the risk tiers below |
| C. Application services | [Application layer](../concepts/application-layer.md) — chat, math tutor, curriculum advisor, coding agent, animator | Covered |
| D. Knowledge layer (RAG) | [Orchestration layer](../concepts/orchestration-layer.md) — Dify, the curriculum advisor | Covered |
| E. Privacy airlock | [Gateway layer](../concepts/gateway-layer.md) — LiteLLM with personal-data redaction | Covered |
| F. Model layer | [Inference layer](../concepts/inference-layer.md) for local models, plus the gateway for cloud-burst control | Covered; split across two knowledge base layers |
| G. Infrastructure | [Infrastructure layer](../concepts/infrastructure-layer.md) — Mac mini, DGX Spark | Covered |
| H. Operations | [Operations](../operations/operations-overview.md) — overview and the chat-service runbook | Partial; model registry and evaluation pipelines are further work |

The knowledge base makes one main interpretive choice: it concentrates governance at a single **Gateway layer**. The annex's Layer E (privacy airlock), its §4.4 sovereignty envelope, and the cloud-burst control inside Layer F are all realised in one place — the gateway — rather than spread across the stack. This is the operational meaning of the phrase "the gateway is the sovereignty envelope" used throughout the knowledge base.

## Governance: risk-tiered teacher-in-the-loop

The annex's central mechanism calibrates human oversight to the risk of the task, so safety is strict where it matters without making every output wait for approval.

| Risk tier | Use cases | Approval requirement |
| --- | --- | --- |
| Tier 1: high | Any output intended for learners; assessment and marking; sensitive topics. | Mandatory teacher approval before learner release. |
| Tier 2: medium | Teacher-only drafts not intended for learners; planning and scaffolding. | Immediate release to the teacher, with publish controls and periodic audit. |
| Tier 3: low | Non-instructional automation that does not reach learners. | Automated release with logging. |

When classification is uncertain, the higher tier applies. Every learner-facing build in this knowledge base — the [math tutor](../getting-started/math-tutor.md) and the [curriculum advisor](../getting-started/curriculum-advisor.md) — sits in **Tier 1**: a teacher approves output before any learner sees it.

## The sovereignty envelope and privacy airlock

When a workflow needs an external model, the annex requires a sovereignty envelope: data classification, redaction and minimisation before anything leaves, permitted and prohibited payloads, and contractual controls. In this knowledge base that is enforced at the [gateway](../concepts/gateway-layer.md): redaction first, approved destinations only, learner free text and identifiers blocked by default, and a local fallback when connectivity fails. The [AI gateway](../getting-started/ai-gateway.md) guide is the running build.

## Minimum Government Baseline

The annex defines a Minimum Government Baseline — availability under intermittent connectivity, privacy controls, a security baseline, auditability, and a scalability pathway — that any public deployment is expected to meet before adding optional modules such as cloud burst or DPI integration. The first build in this knowledge base is a development path and does not meet this baseline; the [pilot](../components/environments/pilot.md) and [production](../components/environments/production.md) environments are where the baseline is established before scale.

## Hosting and hybrid options

The annex offers four reference topologies — a ministry hub with district nodes, a public-university shared service, school edge devices, and a hybrid of local processing with controlled cloud burst — chosen by connectivity, institutional capacity, and data rules. This knowledge base documents the single-machine development path and points to the [pilot environment](../components/environments/pilot.md) for shared use. The annex holds the full topology table.

## The quality gap and the Frugal AI Challenge

The annex treats the local-model quality gap as a programme problem, managed by task-model fit, curriculum-grounded retrieval, and controlled cloud burst for narrowly defined hard tasks. It also proposes a Frugal AI Challenge: "the best Mathematics Tutor that runs on an Aptus Pi or equivalent edge device, without internet."

The knowledge base's through-line is a working answer to that framing: a [math tutor](../getting-started/math-tutor.md) that computes exactly and offline, a [gateway](../getting-started/ai-gateway.md) for controlled cloud burst on genuinely hard problems, and a [Manim animator](../getting-started/manim-animator.md) for the visual case. The COL [Aptus](https://www.col.org/projects/aptus/) tradition — open-source hardware that brings learning to communities without grid power or the internet — is the heritage this continues.

## Monitoring and evaluation

The annex suggests 12-month indicators for pilot review and scale decisions, to be adapted to national frameworks. Two map directly onto what the stack already produces: **token sovereignty** — the share of inference processed locally — and **personal-data leakage through external endpoints** are both measured by the [gateway](../concepts/gateway-layer.md) audit log, which records every route and redaction. The annex holds the full indicator set; telemetry should stay privacy-preserving, aggregated, and free of learner free text unless explicitly authorised.

## Glossary

The annex's key terms — sovereign operation, Frugal AI, teacher-in-the-loop, retrieval-augmented generation, privacy airlock, cloud burst, edge device, quasi-identifier, and store-and-forward synchronisation — are defined in the knowledge base's canonical [Glossary](glossary.md), the single source for these definitions.

## Source

- [Technical Annex: Sovereign Education-AI Reference Architecture](https://www.col.org/wp-content/uploads/2026/02/Technical-Annex-for-Sovereign-Education.pdf), Commonwealth of Learning, February 2026.
