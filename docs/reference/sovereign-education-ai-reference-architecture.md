---
description: Markdown adaptation of COL's sovereign education-AI reference architecture.
icon: landmark
---

# Technical Annex: Sovereign Education-AI Reference Architecture

**Teacher-led, localised, and Frugal AI for equitable education**

This reference is based on COL's Technical Annex for a sovereign education-AI reference architecture. It is written for ministries and public education partners, especially in Small Island Developing States and low- and middle-income countries.

The annex is not a single product, procurement specification, or deployment guide. It is a reference architecture and options menu for education AI services that keep data, policy, and governance under national or institutional control.

{% hint style="info" %}
This page is a Markdown adaptation for the Frugal AI knowledge base, not a full reproduction of the source PDF. Use the [original COL technical annex](https://www.col.org/wp-content/uploads/2026/02/Technical-Annex-for-Sovereign-Education.pdf) as the authoritative source.
{% endhint %}

## Annex profile

| Field | Detail |
| --- | --- |
| Developed by | Commonwealth of Learning as a reference resource. |
| Purpose | Reference architecture and options menu for sovereign Frugal AI in education. |
| Intended audience | Senior officials, EMIS and ICT units, curriculum authorities, teacher education institutions, public universities, and regulators. |
| Status | For discussion and adaptation. |
| Version and date | v1, February 2026. |
| Scope note | Teacher-support and system enablement. High-stakes automated decision-making, such as student progression or certification, is out of scope. |

## Document conventions

The annex defines a Minimum Government Baseline for public deployments that process education data or produce content intended for learners. Components beyond that baseline are optional modules.

## Contents

1. [Executive Summary for Ministers and Officials](#1-executive-summary-for-ministers-and-officials)
2. [Design Principles and Options](#2-design-principles-and-options)
3. [Reference Architecture](#3-reference-architecture-layered-model)
4. [Hosting Topologies and Hybrid Options](#4-hosting-topologies-and-hybrid-options)
5. [Governance Guardrails](#5-governance-guardrails-risk-tiered-teacher-in-the-loop)
6. [Implementation Challenges and Mitigations](#6-implementation-challenges-and-mitigations)
7. [Policy Alignment](#7-policy-alignment)
8. [Monitoring and Evaluation](#8-monitoring-and-evaluation)
9. [Pilot Blueprint Template](#9-pilot-blueprint-template)
10. [Glossary of Key Terms](#10-glossary-of-key-terms)
11. [Appendix A: Self-Assessment Checklist for Ministries](#appendix-a-self-assessment-checklist-for-ministries)

## 1. Executive Summary for Ministers and Officials

The annex provides a structured set of options and guidelines for deploying AI in education while maintaining national control over education data and policy.

### What problem does this address?

Education systems need ways to benefit from AI without surrendering control over education data, policy, availability, cost, or jurisdiction. Commercial AI subscriptions can be procured quickly, but they introduce dependency risks. Fully sovereign systems are feasible, but require deliberate capacity-building.

This architecture sets out a sovereignty-by-design baseline: national control where it matters most, with pragmatic options for capability and scale.

### What choices do countries have?

The annex can be used in several ways:

- adopt the full architecture as a starting point for national implementation;
- adapt selected components to fit existing systems and capacity;
- combine local processing with controlled cloud access for complex tasks;
- evaluate vendor proposals and procurement decisions;
- set the architecture aside where another approach better fits national circumstances.

### What about the quality gap?

Quality is managed through task specialisation, approved knowledge sources, and hybrid options. Local models can support routine education workflows with predictable latency, predictable costs, offline continuity, and data residency. Where additional capability is needed, controlled cloud burst can be used within a defined sovereignty envelope.

### How does this scale?

Scale depends on risk-tiered teacher oversight. Low-risk tasks can be automated with logging. Teacher-only drafts can use post-hoc audit and publish controls. Learner-facing outputs default to strict approval before release.

## 2. Design Principles and Options

### 2.1 Guiding principles

| Principle | Meaning |
| --- | --- |
| Teacher-led accountability | AI assists professional tasks; teachers maintain oversight through a risk-tiered workflow. |
| Sovereign operation | Education data and audit logs remain under national jurisdiction and policy control. |
| Frugal resilience | Systems operate offline-first and use store-and-forward synchronisation where connectivity is intermittent. |
| Local relevance | Workflows align with national curricula, languages, and pedagogies. |
| Safety-by-design | Learner safeguards include incident reporting, traceability, correction mechanisms, and human oversight. |

### 2.2 Minimum Government Baseline

| Baseline area | Minimum expectation |
| --- | --- |
| Availability | Defined service levels for intermittent connectivity and offline use. |
| Privacy | Data minimisation, personal-data redaction, and controlled log retention. |
| Security | Role-based access control, encryption, patch management, and incident response readiness. |
| Auditability | Tamper-evident logs and versioned knowledge-base, model, and configuration records. |
| Scalability | A clear path from controlled pilot to wider deployment. |

Optional modules such as cloud burst, advanced tuning, and DPI integration should be added only after the baseline safeguards are demonstrably in place.

## 3. Reference Architecture (Layered Model)

| Layer | Objective | Core components |
| --- | --- | --- |
| A. Access and identity | Controlled access and accountability. | Role-based access, least privilege, administrator MFA, and school or district tenancy where needed. |
| B. Teacher-in-the-loop workflow | Pedagogy leads technology. | Risk-tiered approval, feedback capture, and audit trail. |
| C. Application services | Deliver education value safely. | Lesson planning, assessment drafting, OER adaptation, and ministry drafting support. |
| D. Knowledge layer | Ground outputs in approved sources. | Vetted knowledge base, ingestion and versioning, retrieval policies, and citation display. |
| E. Privacy airlock | Minimise and protect personal data. | Personal-data detection and redaction, context minimisation, policy filters, and retention control. |
| F. Model layer | Provide localised intelligence and cost control. | Locally hostable models for routine tasks and controlled cloud burst for complex tasks. |
| G. Infrastructure | Support resilience and continuity. | Edge or hub nodes, offline caching, store-and-forward sync, and DPI-compatible registries where available. |
| H. Operations | Provide continuous assurance. | Model registry, evaluation pipelines, monitoring, incident response, and audit reporting. |

### 3.1 Interface expectations

Procurement and implementation should account for:

- versioning and provenance for knowledge ingestion and retrieval;
- consistent audit logging across applications, models, and knowledge services;
- offline-first synchronisation with retention and minimisation rules;
- integration with EMIS, LMS, and DPI systems using national data exchange standards where available;
- import and export of approved education artefacts, such as lesson plans, rubrics, and assessment items;
- audit log export in a machine-readable format for oversight.

### 3.2 DPI compatibility

Where national Digital Public Infrastructure already exists, the architecture should integrate rather than rebuild. Identity, credentialing, registries, and data exchange can align with national DPI frameworks and legal requirements.

## 4. Hosting Topologies and Hybrid Options

### 4.1 Reference hosting topologies

| Topology | Contexts where it may fit | Considerations |
| --- | --- | --- |
| A. Ministry hub with district nodes | National or multi-district scale. | Central governance, district inference and caching, and support for offline schools through periodic sync. |
| B. Public university shared service | Countries where public universities can host public digital services. | Builds national capacity while the ministry retains governance and audit control. |
| C. School edge devices | Remote areas and high-outage contexts. | Local inference and content access with strong resilience, but device management is required. |
| D. Hybrid local and cloud burst | Countries balancing sovereignty with additional capability. | Local processing for routine tasks; controlled cloud access for complex reasoning; defined data-governance controls. |

### 4.2 The hybrid model

Local processing is the default for routine tasks:

- formatting and document preparation;
- basic quiz and question generation;
- translation and localisation;
- fact retrieval from approved knowledge bases;
- administrative task support.

Controlled cloud burst can be considered for narrowly defined complex tasks:

- complex mathematical reasoning and problem-solving;
- computationally intensive drafting support;
- tasks requiring frontier model capability.

Cloud burst requires data minimisation before transmission, approved providers, audit logging, jurisdictional controls, deletion rules, and local fallback when connectivity fails.

### 4.3 Open-source options

Open-source components can reduce dependency and support sovereign operation. Selection still requires procurement review, licence checks, security due diligence, and evaluation against local language and curriculum needs.

Categories to assess include:

- open-weight models suitable for local inference;
- model servers for CPU, GPU, and offline packaging;
- document ingestion, vector search, and retrieval services;
- safety and moderation filters;
- observability, logging, and dashboard tools.

### 4.4 Sovereignty envelope

A sovereignty envelope defines what data may be processed externally, what must remain in-country, and what controls apply.

| Area | Minimum decision |
| --- | --- |
| Data classification | Define learner, sensitive, internal, and public content categories. |
| Transformation | Specify redaction, minimisation, and aggregation before external processing. |
| Permitted payloads | Limit cloud burst to de-identified or curriculum-only prompts by default. |
| Prohibited payloads | Block learner free text, identifiers, quasi-identifiers, and special-category data by default. |
| Contractual controls | Require deletion commitments, sub-processor disclosure, breach notification, audit rights, and exit rights. |

## 5. Governance Guardrails: Risk-Tiered Teacher-in-the-Loop

The annex avoids a one-size-fits-all approval model. Human oversight is calibrated to the risk of the task.

### 5.1 Risk-tiered approval framework

| Risk tier | Use cases | Approval requirement | Rationale |
| --- | --- | --- | --- |
| Tier 1: High risk | Learner-facing content, assessment items, marking guidance, sensitive topics, or high-consequence communications. | Mandatory teacher or authorised human approval before learner release. | Direct learner impact requires strict gating. |
| Tier 2: Medium risk | Teacher-only planning drafts, internal notes, resource scaffolding, and OER adaptation drafts. | Immediate release to the teacher with publish controls and periodic quality audit. | Supports teacher efficiency without direct learner release. |
| Tier 3: Low risk | Non-instructional automation, formatting, and administrative templates that do not reach learners. | Automated release with logging. | Low consequence tasks can be handled efficiently. |

When classification is uncertain, use the higher tier. Any output shown to learners belongs in Tier 1.

### 5.2 Privacy airlock and data sovereignty envelope

When a workflow requires cloud burst, the privacy airlock and sovereignty envelope should apply before data leaves the local system.

Minimum controls include:

- data minimisation to remove unnecessary context;
- personal-data redaction before model processing;
- special protection for small-population quasi-identifiers;
- approved providers or sovereign cloud endpoints where external processing is used;
- non-retention, deletion, and audit commitments for education data logs.

## 6. Implementation Challenges and Mitigations

Sovereign education-AI deployments are programmes, not single procurements. Predictable challenges should be managed in the pilot design.

| Challenge | Operational impact | Mitigation pattern |
| --- | --- | --- |
| Infrastructure and power volatility | Cloud-dependent systems can fail during network outages or power disruption. | Offline-first local inference and store-and-forward synchronisation. |
| Quality gap of smaller models | Small local models may not match frontier systems on open-ended tasks. | Curriculum-grounded retrieval, task-model fit, evaluation, and controlled cloud burst for specific needs. |
| Teacher literacy and workload | Complex prompt-based interfaces can increase workload and reduce adoption. | Structured, task-specific interfaces and teacher professional development. |
| Data residency compliance | External infrastructure may conflict with national data protection rules. | In-country hosting, public university services, district hubs, or sovereign cloud controls. |
| Pilot-to-scale gap | Successful pilots may stall without support, governance, and training plans. | Scale criteria, helpdesk planning, cascade training, and governance review from the start. |

## 7. Policy Alignment

The architecture is intended to align technical design with national policy, education governance, and international AI principles.

### 7.1 Curriculum standards

Retrieval-Augmented Generation helps align outputs with approved national syllabi, teacher guides, textbooks, and locally vetted source material.

### 7.2 Open Educational Resources

Publicly funded content can be structured for open licensing where national policy allows. This supports reuse, adaptation, and reduced vendor lock-in.

### 7.3 Data protection and privacy laws

The architecture supports data minimisation, local governance, audit trails, and redress. Raw model output and teacher-edited output can be tracked separately to support provenance and quality review.

### 7.4 International alignment

The annex maps to policy themes in UNESCO guidance, OECD AI principles, NIST AI risk management, and DPI approaches. The main alignment areas are human-centred governance, transparency, security, evaluation, and public-interest infrastructure.

## 8. Monitoring and Evaluation

The annex suggests 12-month indicators for pilot review and scale decisions. Countries should adapt indicators to national monitoring frameworks.

| Evaluation area | Core metric | Example target | Verification method |
| --- | --- | --- | --- |
| Pedagogical oversight | Teacher approval for high-risk learner-facing content. | 100 percent before release. | Workflow and audit logs. |
| Content quality | Share of AI output modified by teachers during review. | Locally defined threshold. | Version comparison between model output and final asset. |
| Technical resilience | Local service availability during outages. | Locally defined uptime target. | Edge node and client logs. |
| Retrieval quality | Outputs with valid citations from approved knowledge sources. | High citation validity for RAG tasks. | Evaluation pipeline and sample review. |
| Privacy and safety | Personal-data leakage through external endpoints. | Zero incidents. | Privacy airlock tests and audit review. |
| Incident response | Time to log, triage, and remediate reported issues. | Locally defined service level. | Helpdesk and incident registers. |
| Cost predictability | Variance from budgeted monthly operating cost. | Low variance. | Infrastructure and cloud-burst cost reports. |
| Token sovereignty | Share of inference processed locally. | Majority local processing. | Model layer usage analytics. |

Telemetry should be privacy-preserving: collect only what is necessary, aggregate results, restrict access, and avoid learner free text unless explicitly authorised and protected.

## 9. Pilot Blueprint Template

This template can guide a 3-to-6 month proof-of-concept deployment.

### 9.1 Project identification and governance

Define:

- target jurisdiction, district, or region;
- participating schools, institutions, or hubs;
- lead implementing agency;
- technical integration partner;
- steering committee and reporting schedule.

### 9.2 Hosting architecture selection

Select the topology based on local connectivity, power reliability, technical capacity, and data rules:

- ministry hub with district nodes;
- public university shared service;
- school edge devices;
- hybrid local and cloud burst.

### 9.3 Knowledge layer ingestion scope

List the approved, version-controlled documents that populate the initial knowledge base. Examples include national syllabi, approved textbook chapters, teacher guides, and ministry training manuals. Unvetted web scraping should not be used under the baseline.

### 9.4 Risk-tiering workflow configuration

Define how the system classifies each task and enforces the required review route:

```text
User draft request
  -> system assigns risk tier
  -> Tier 1: high-risk learner-facing content requires approval
  -> Tier 2: teacher-only draft stays in workspace with publish controls
  -> Tier 3: low-risk administrative task is logged and saved
```

### 9.5 Phased implementation milestones

| Phase | Duration | Core activities | Success criteria |
| --- | --- | --- | --- |
| Setup | Weeks 1-4 | Hardware provisioning, local model installation, knowledge layer compilation, and vectorisation. | The system operates offline in a controlled test environment. |
| Alpha test | Weeks 5-8 | Closed testing with master teachers, interface validation, and synthetic privacy-airlock tests. | Personal-data redaction and usability checks meet pilot thresholds. |
| Field pilot | Weeks 9-16 | Live deployment in pilot schools, store-and-forward synchronisation, and observation of oversight workflows. | Monitoring indicators are logged and major incidents are escalated. |
| Review | Weeks 17-20 | Audit log review, cost analysis, token distribution review, and adaptation roadmap. | Evaluation report is ready for ministry scale-up decision. |

## 10. Glossary of Key Terms

The terms used in this annex — Sovereign AI, Frugal AI, Teacher-in-the-Loop, Retrieval-Augmented Generation, privacy airlock, cloud burst, edge device, and store-and-forward synchronisation — are defined in the knowledge base's canonical [Glossary](glossary.md), which is the single source for these definitions.

## Appendix A: Self-Assessment Checklist for Ministries

This diagnostic checklist helps technical teams assess readiness before a localised, sovereign education-AI pilot.

### A.1 Data sovereignty and infrastructure lifecycle

- [ ] **Data jurisdiction:** Student and teacher interaction logs are legally bound to remain within national geographic boundaries or contractually protected sovereign cloud instances.
- [ ] **Connectivity profile:** Power and network reliability in the target region have been mapped to determine whether school edge nodes, district hubs, or both are required.
- [ ] **Hardware assessment:** Consumer-grade or existing institutional hardware can run small, optimised open-source models locally.

### A.2 Knowledge layer and content integrity

- [ ] **Vetted source access:** National syllabi, textbooks, and teacher guides are available in clean digital text formats for a retrieval knowledge base.
- [ ] **Version control:** A designated authority updates, patches, and approves source knowledge repositories when the national curriculum changes.
- [ ] **Open licensing default:** Procurement and generation guidelines define how publicly funded outputs use open licences where appropriate.

### A.3 Pedagogical oversight and risk management

- [ ] **Workflow enforcement:** The software architecture prevents high-risk learner-facing generated content from being distributed until an authorised teacher approves it.
- [ ] **User interface design:** Teacher interfaces use structured, task-specific forms where possible instead of relying only on open-ended prompt fields.
- [ ] **Auditability:** The system saves distinct versions of raw AI output and final teacher-edited output so model accuracy and human modification rates can be reviewed.

### A.4 Operational capacity and policy

- [ ] **Technical partnership:** A public university, research centre, or internal agency can support local model configuration and deployment.
- [ ] **Data privacy alignment:** The pilot structure complies with national data protection rules for data minimisation and log management.
- [ ] **Budget predictability:** The compute architecture keeps monthly operational costs predictable and reduces exposure to commercial subscription volatility.

## How this connects to the Frugal AI knowledge base

The current Frugal AI knowledge base starts with a small development path: a local AI chat service on documented hardware. The COL annex describes a broader ministry-level reference architecture.

| Knowledge base page | How it relates |
| --- | --- |
| [Frugal AI principles](../concepts/frugal-ai-principles.md) | Gives the local-control, open-technology, and capacity-building frame. |
| [Pilot environment](../components/environments/pilot.md) | Introduces the controlled shared-use stage before production. |
| [NVIDIA DGX Spark](../components/hardware/nvidia-dgx-spark.md) | Candidate hardware profile for development and pilot workloads needing more memory headroom. |
| [Local AI chat service operations](../operations/open-webui-ops.md) | Shows how operations, backup, update, and recovery are documented even in the first path. |

## Source

- [Technical Annex: Sovereign Education-AI Reference Architecture](https://www.col.org/wp-content/uploads/2026/02/Technical-Annex-for-Sovereign-Education.pdf), Commonwealth of Learning, February 2026.
