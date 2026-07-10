---
description: Plain-language terms used in the Frugal AI knowledge base.
icon: bookmark
---

# Glossary

Plain-language definitions for Frugal AI concepts, components, and governance terms.

Terms are grouped by theme and alphabetical within each group.

## Frugal AI and the stack

<details>

<summary><strong>Agent (AI agent)</strong></summary>

An application that takes actions rather than only answering: it reads, writes, and runs things through tools, under scoped permissions and human review. In this knowledge base an agent is an Application-layer subtype, not a separate layer; the coding agent is the worked example.

</details>

<details>

<summary><strong>Agent loop (harness)</strong></summary>

The orchestration that runs an agent: it assembles context, calls tools, and keeps memory between steps. Whoever operates the loop sees what the agent sees while it works, so Frugal AI keeps the loop under institutional control, governed as the Application layer's governance surfaces describe.

</details>

<details>

<summary><strong>Agentic</strong></summary>

Describes work done by agents: workflows where a model plans, calls tools, and takes steps in a loop rather than returning a single answer. Model cards use "agentic readiness" for the features this needs, such as reliable function calling.

</details>

<details>

<summary><strong>Edge device</strong></summary>

A computing device located at the point of use, such as a school, instead of in a central data centre. Edge devices can support local processing and offline operation.

</details>

<details>

<summary><strong>Frugal AI</strong></summary>

Frugal AI treats AI as durable institutional infrastructure rather than an externally sourced service. It optimises for local control, predictable cost, lower energy use, intermittent connectivity, open components, and long-term institutional capacity.

</details>

<details>

<summary><strong>Frugal floor</strong></summary>

The smallest complete build in this knowledge base: infrastructure, inference, and an application, with the gateway local-only and no orchestration. It is the architecture at its minimum, not a cut-down version.

</details>

<details>

<summary><strong>Gateway</strong></summary>

The single boundary every model request passes through, where routing, redaction, audit logging, and approved destinations are enforced. In this knowledge base it is the operational form of the sovereignty envelope and the privacy airlock.

</details>

<details>

<summary><strong>Model Context Protocol (MCP)</strong></summary>

An open standard for packaging tools and data sources so agents can use them. An MCP server offers tools an agent can call; in the Frugal AI stack it is an Orchestration-layer component, substitutable like any other. An MCP server can make its own network calls outside the gateway, so it is governed at the application layer: allowlisted, reviewed, and given no network access by default.

</details>

<details>

<summary><strong>Ollama</strong></summary>

The local runtime used in this path to download, run, and serve the model.

</details>

<details>

<summary><strong>Open WebUI</strong></summary>

The browser chat interface used in this path. It connects to Ollama and stores its data locally.

</details>

<details>

<summary><strong>Orchestration</strong></summary>

The layer that coordinates more than a single model reply: tools, retrieval, and multi-step workflows. It is optional; the first chat build runs without it.

</details>

<details>

<summary><strong>RAG</strong></summary>

Retrieval-Augmented Generation: a technique that grounds AI outputs in retrieved documents from a knowledge base. RAG can improve accuracy and support citation of sources.

</details>

<details>

<summary><strong>Stack</strong></summary>

A tested combination of hardware, environment, runtime, model, application interface, and operations practices.

</details>

## Models and inference

<details>

<summary><strong>Context window</strong></summary>

The amount of text a model can consider at one time. Larger context windows can handle longer conversations or documents, but they also use more memory.

</details>

<details>

<summary><strong>Embedding model</strong></summary>

A model that turns text into numeric vectors so passages with similar meaning can be found. Retrieval-augmented generation uses one to search an approved knowledge base.

</details>

<details>

<summary><strong>LLM</strong></summary>

Large Language Model: an AI model with billions of parameters that can generate, transform, or reason over text and other inputs. Frontier LLMs are often served through cloud infrastructure; smaller or quantised LLMs may run locally.

</details>

<details>

<summary><strong>Local inference</strong></summary>

Running an AI model on a local machine instead of sending prompts to a remote cloud API.

</details>

<details>

<summary><strong>Mixture of Experts (MoE)</strong></summary>

A model design where only a fraction of the parameters — the active parameters — run for any given token, so total size is large but compute per token stays smaller. Contrast with a dense model, where every parameter is used.

</details>

<details>

<summary><strong>Model card</strong></summary>

A short reference page that explains what a model is, what it fits, what it needs, and what its limits are.

</details>

<details>

<summary><strong>Quantisation</strong></summary>

A way to reduce model size and memory use by storing weights with fewer bits. Smaller quantised models fit on modest hardware, but quality can vary.

</details>

<details>

<summary><strong>Runtime</strong></summary>

The software that loads the model, runs inference, and exposes an interface for applications.

</details>

<details>

<summary><strong>Serving engine</strong></summary>

Inference software built for many simultaneous users on GPU hardware, such as vLLM, used at pilot and production scale. Contrast with a local runtime, which suits a single developer.

</details>

<details>

<summary><strong>SLM</strong></summary>

Small Language Model: an AI model with fewer parameters than larger frontier models. SLMs are more suitable for modest hardware and edge deployment, but usually have reduced capability compared with larger models.

</details>

## Sovereignty and governance

<details>

<summary><strong>Audit log</strong></summary>

A record of what the gateway did with each request: where it was routed, what was redacted, and when. It supports review and incident response, and is the record behind indicators such as token sovereignty and personal-data leakage.

</details>

<details>

<summary><strong>Cloud burst</strong></summary>

Temporary use of cloud computing resources for tasks that exceed local processing capacity. In a sovereign AI design, cloud burst needs governance controls for data minimisation, audit logging, jurisdiction, deletion, and fallback to local processing.

</details>

<details>

<summary><strong>Data sovereignty</strong></summary>

The ability for an institution or country to control where its data is stored, processed, accessed, and governed.

</details>

<details>

<summary><strong>DPI</strong></summary>

Digital Public Infrastructure: shared digital systems such as identity, payments, and data exchange that enable public and private services at population scale. Examples include India's Aadhaar, Unified Payments Interface, and National Digital Education Architecture.

</details>

<details>

<summary><strong>Guardrail</strong></summary>

A policy enforced on a request or response, such as masking personal data or blocking learner free text. In this knowledge base guardrails are enforced at the gateway.

</details>

<details>

<summary><strong>Learner-facing content</strong></summary>

Any content intended to be shown directly to learners or used for assessment, feedback, or progression decisions.

</details>

<details>

<summary><strong>Minimum Government Baseline</strong></summary>

The set of safeguards the reference architecture expects any public deployment to meet before adding optional modules: availability, privacy, security, auditability, and a scalability pathway. The development build does not meet it; the pilot and production environments establish it.

</details>

<details>

<summary><strong>Privacy airlock</strong></summary>

A control layer that detects, redacts, or masks personal data before it is processed by a model or sent to an external service. It is the enforcement point of the sovereignty envelope, sometimes called simply the airlock.

</details>

<details>

<summary><strong>Quasi-identifier</strong></summary>

A combination of attributes that may re-identify a person in a small population. Examples include school, grade, and a rare characteristic when used together.

</details>

<details>

<summary><strong>Redaction</strong></summary>

Detecting and masking personal data in a prompt before a model sees it, keeping the original only in protected logs. It is the core action of the privacy airlock.

</details>

<details>

<summary><strong>Risk tier</strong></summary>

The level of human oversight a task needs, from the reference architecture's risk-tiered teacher-in-the-loop: Tier 1 (high; learner-facing; approval before release), Tier 2 (medium; teacher-only drafts), and Tier 3 (low; automated with logging). When classification is uncertain, use the higher tier.

</details>

<details>

<summary><strong>Sensitive topics</strong></summary>

Content areas defined nationally or institutionally as requiring heightened care, especially in learner-facing materials. Examples may include health, religion, conflict history, identity, or locally sensitive public issues.

</details>

<details>

<summary><strong>Sovereign AI</strong></summary>

National strategic and technical control over AI infrastructure, including data ownership, hosting, model access, and alignment policy.

</details>

<details>

<summary><strong>Sovereign operation</strong></summary>

Operation of AI systems under national jurisdiction and policy control. This includes in-country governance of knowledge bases and audit logs, plus a defined sovereignty envelope for any external processing.

</details>

<details>

<summary><strong>Sovereignty envelope</strong></summary>

The boundary that defines what data may be processed externally, what must stay in-country, and what controls apply. In this knowledge base it is drawn at the gateway, and kept closed in a fully local build.

</details>

<details>

<summary><strong>Teacher-in-the-Loop</strong></summary>

A workflow design that requires teacher oversight of AI-generated content. The level of oversight is calibrated to the risk level of the task.

</details>

<details>

<summary><strong>Token sovereignty</strong></summary>

The share of inference processed locally rather than sent to an external provider. The reference architecture suggests it as a monitoring indicator; the gateway audit log is the record behind it.

</details>

## Operations and resilience

<details>

<summary><strong>Offline-first</strong></summary>

Designed to keep working without a continuous internet connection. Some setup steps, such as downloading a model, may still need internet access.

</details>

<details>

<summary><strong>Runbook</strong></summary>

An operations page that explains how to start, stop, check, update, back up, restore, and troubleshoot a service.

</details>

<details>

<summary><strong>Store-and-forward</strong></summary>

A synchronisation method where data is stored locally when connectivity is unavailable and transmitted when connection is restored.

</details>
