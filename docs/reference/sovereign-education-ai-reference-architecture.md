---
description: Plain-language summary of COL's sovereign education-AI reference architecture.
icon: landmark
---

# Sovereign education-AI reference architecture

This page summarises COL's Technical Annex for a sovereign education-AI reference architecture. The annex is a discussion and adaptation resource for ministries of education, especially in Small Island Developing States and low- and middle-income countries.

The architecture is not a single product or procurement specification. It is an options menu for designing education AI services that keep data, policy, and governance under national or institutional control.

{% hint style="info" %}
This page is a short knowledge-base adaptation, not a full reproduction of the source PDF. Use the [original COL technical annex](https://www.col.org/wp-content/uploads/2026/02/Technical-Annex-for-Sovereign-Education.pdf) as the authoritative source.
{% endhint %}

## At a glance

| Question | Answer |
| --- | --- |
| Intended reader | Ministries, public institutions, regulators, education technology teams, and teacher education partners. |
| Main use | Plan, assess, or procure sovereign Frugal AI systems for education. |
| Core idea | Local and hybrid AI services can support education while protecting data, sovereignty, and teacher oversight. |
| Scope boundary | High-stakes automated decisions, such as certification or student progression, are outside the baseline. |
| Current status | Reference resource for discussion and adaptation. |

## What problem it addresses

Education systems need ways to benefit from AI without surrendering control over education data, policy, cost, availability, or jurisdiction. Commercial AI services can be quick to procure, but they may introduce dependency risks, unpredictable costs, data-governance issues, and connectivity problems.

The annex proposes a sovereignty-by-design baseline: keep national control where it matters most, use local infrastructure where practical, and allow tightly governed hybrid options only when they add clear value.

## Design principles

| Principle | Meaning |
| --- | --- |
| Teacher-led accountability | AI supports professional work; learner-facing or high-risk outputs require teacher oversight. |
| Sovereign operation | Education data, logs, and governance rules remain under national or institutional control. |
| Frugal resilience | Systems should support low bandwidth, intermittent connectivity, and local fallback. |
| Local relevance | Outputs should be grounded in national curricula, languages, pedagogies, and approved sources. |
| Safety-by-design | Risk classification, traceability, incident reporting, and correction mechanisms are built in. |

## Minimum government baseline

Public deployments that process education data or produce content for learners need safeguards before optional advanced features are added.

| Baseline area | Minimum expectation |
| --- | --- |
| Availability | Defined service levels for intermittent connectivity and offline use. |
| Privacy | Data minimisation, personal-data redaction, and controlled log retention. |
| Security | Role-based access, encryption, patch management, and incident response readiness. |
| Auditability | Tamper-evident logs and versioned model, configuration, and knowledge-base records. |
| Scalability | A clear path from controlled pilot to wider deployment. |

## Architecture layers

| Layer | Purpose | Minimum components |
| --- | --- | --- |
| Access and identity | Control access and accountability. | Role-based access, least privilege, administrator MFA, and tenancy where needed. |
| Teacher-in-the-loop workflow | Keep pedagogy in the lead. | Risk-tiered approval, feedback capture, and audit trail. |
| Application services | Deliver education value safely. | Lesson planning, assessment drafting, OER adaptation, and ministry drafting support. |
| Knowledge layer | Ground outputs in approved sources. | Vetted knowledge base, ingestion, versioning, retrieval rules, and citations. |
| Privacy airlock | Minimise and protect personal data. | Detection and redaction, context minimisation, policy filters, and retention control. |
| Model layer | Provide localised intelligence and cost control. | Locally hostable models for routine tasks and controlled cloud burst for specific complex tasks. |
| Infrastructure | Support resilience and continuity. | Hub or edge nodes, offline caching, synchronisation, and DPI-compatible registries where available. |
| Operations | Provide continuous assurance. | Model registry, evaluation, monitoring, incident response, and audit reporting. |

## Hosting options

| Topology | Best fit | Main consideration |
| --- | --- | --- |
| Ministry hub with district nodes | National or multi-district scale. | Central governance with district-level inference, caching, and offline support. |
| Public university shared service | Countries where public universities can host digital services. | Builds local technical capacity while ministry governance remains explicit. |
| School edge devices | Remote, high-outage, or low-connectivity contexts. | Strong resilience, but device management becomes important. |
| Hybrid local and cloud burst | Cases that need both sovereignty and additional capability. | External processing needs a defined sovereignty envelope and fallback to local processing. |

## Hybrid use and sovereignty envelope

The annex treats local processing as the default for routine workflows. Controlled cloud burst may be considered for narrowly defined complex tasks, but only with clear controls.

A sovereignty envelope should define:

- which data may be processed externally, if any;
- which data must remain in-country or within institutional systems;
- what redaction, minimisation, and aggregation are required;
- which providers, jurisdictions, audit logs, and deletion rules apply;
- what fallback exists when connectivity or external services fail.

The default protected categories include learner data, staff data, sensitive administrative records, and small-population combinations that could re-identify people.

## Risk-tiered teacher oversight

The annex uses a risk-tiered model so human review is strongest where learner harm is most likely.

| Tier | Use case | Oversight rule |
| --- | --- | --- |
| Tier 1: High risk | Learner-facing content, assessment material, sensitive topics, or high-consequence communication. | Teacher or authorised human approval before learner release. |
| Tier 2: Medium risk | Teacher-only planning drafts, internal notes, and resource scaffolding. | Immediate teacher access, publish controls, and periodic quality audit. |
| Tier 3: Low risk | Non-instructional automation such as formatting or administrative templates. | Automated release with logging. |

When classification is uncertain, use the higher tier. Any output that will be shown to learners belongs in Tier 1.

## Data protection and security

The privacy airlock is a control layer before model processing. It should reduce unnecessary data exposure and support audit and redress.

Minimum controls include:

- data minimisation by default;
- personal-data detection and redaction;
- special care for small-school or island-context quasi-identifiers;
- defined retention and deletion periods;
- restricted log access;
- tamper-evident audit trails;
- role-based access, administrator MFA, encryption, patching, and incident response.

## Implementation risks

| Risk | Mitigation pattern |
| --- | --- |
| Procurement delay | Start with a controlled pilot, university partnership, or regional shared service. |
| Quality gap | Match model capability to task, use approved knowledge sources, and validate hybrid options through pilots. |
| Pilot-to-scale gap | Build teacher training, support, and scale criteria into the pilot from the start. |
| Capacity burden | Use phased implementation and build local skills progressively. |

## Monitoring and evaluation

The annex suggests 12-month indicators that can be adapted to national monitoring frameworks.

| Domain | Example indicator |
| --- | --- |
| Teacher uptake | Active teachers per month and usage frequency. |
| Teacher oversight | Share of Tier 1 drafts edited and Tier 2 audit pass rate. |
| Language coverage | Coverage of core learning resources in local languages. |
| Frugal performance | Latency, offline availability, and cloud-burst frequency. |
| Scale readiness | Teacher training completion and support ticket volume. |

Telemetry should be privacy-preserving: collect only what is necessary, aggregate results, restrict access, and avoid learner free text unless explicitly authorised and protected.

## Pilot blueprint

A pilot plan should specify:

- pilot scope, subjects, levels, cohorts, and scale-up path;
- hosting topology and data-flow diagram;
- risk-tier classification and review schedule;
- approved knowledge sources, language coverage, licensing, and provenance;
- teacher capacity-building plan;
- privacy airlock, safeguards, publish controls, and incident escalation;
- baseline indicators, targets, data collection method, and early-warning thresholds;
- governance roles, steering committee, reporting schedule, and scale-up criteria;
- timeline from setup through month 6 and month 12 review.

## Glossary of key terms

The annex uses these terms when describing a sovereign education-AI pilot.

| Term | Meaning |
| --- | --- |
| Sovereign AI | An approach where a nation retains strategic and technical control over AI infrastructure, including data ownership, hosting environments, model weights, and alignment policies, reducing long-term vendor lock-in. |
| Frugal AI | Deployment of highly optimised open-source AI models on lower-specification, consumer-grade, or edge hardware to support predictable costs and technical sustainability in resource-constrained settings. |
| Teacher-in-the-Loop | A pedagogical and operational framework where automated systems remain assistive tools and educators review, modify, or approve AI-generated content before it reaches learners. |
| Retrieval-Augmented Generation | A technical architecture that improves model outputs by retrieving content from an authoritative, pre-vetted knowledge base before generating a response. |
| Privacy airlock | A data-processing layer that intercepts outbound requests and scans, redacts, or masks personally identifiable information before data moves to an external network or cloud endpoint. |
| Cloud bursting | An operational design where routine tasks are handled locally and highly complex reasoning or processing tasks are routed to external cloud infrastructure within a secure sovereignty envelope. |
| Edge device or node | Localised hardware, such as a school server, desktop computer, or micro-hub, that can run model inference and host applications without requiring an active internet connection. |
| Store-and-forward synchronisation | A network communication method where data or logs are collected locally during offline periods and transmitted to a central hub when a network connection becomes available. |

For a broader list of terms, see the [Glossary](glossary.md).

## Self-assessment checklist for ministries

This diagnostic checklist helps technical teams assess baseline readiness and architectural fit before a localised, sovereign education-AI pilot.

### Data sovereignty and infrastructure lifecycle

- [ ] **Data jurisdiction:** Student and teacher interaction logs are legally bound to remain within national geographic boundaries or contractually protected sovereign cloud instances.
- [ ] **Connectivity profile:** Power and network reliability in the target region have been mapped to determine whether school edge nodes, district hubs, or both are required.
- [ ] **Hardware assessment:** Consumer-grade or existing institutional hardware can run small, optimised open-source models locally.

### Knowledge layer and content integrity

- [ ] **Vetted source access:** National syllabi, textbooks, and teacher guides are available in clean digital text formats for a retrieval knowledge base.
- [ ] **Version control:** A designated authority updates, patches, and approves source knowledge repositories when the national curriculum changes.
- [ ] **Open licensing default:** Procurement and generation guidelines define how publicly funded outputs use open licences where appropriate.

### Pedagogical oversight and risk management

- [ ] **Workflow enforcement:** The software architecture prevents high-risk learner-facing generated content from being distributed until an authorised teacher approves it.
- [ ] **User interface design:** Teacher interfaces use structured, task-specific forms where possible instead of relying only on open-ended prompt fields.
- [ ] **Auditability:** The system saves distinct versions of raw AI output and final teacher-edited output so model accuracy and human modification rates can be reviewed.

### Operational capacity and policy

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
