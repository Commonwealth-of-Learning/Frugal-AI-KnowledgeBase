---
description: Plain-language terms used in the Frugal AI knowledge base.
icon: bookmark
---

# Glossary

Plain-language definitions for Frugal AI concepts, components, and governance terms.

<details>

<summary><strong>Airlock</strong></summary>

A control layer that detects and removes personal identifiers from data before AI model processing. It reduces privacy exposure by limiting what the model receives.

</details>

<details>

<summary><strong>Cloud burst</strong></summary>

Temporary use of cloud computing resources for tasks that exceed local processing capacity. In a sovereign AI design, cloud burst needs governance controls for data minimisation, audit logging, jurisdiction, deletion, and fallback to local processing.

</details>

<details>

<summary><strong>Context window</strong></summary>

The amount of text a model can consider at one time. Larger context windows can handle longer conversations or documents, but they also use more memory.

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

<summary><strong>Edge device</strong></summary>

A computing device located at the point of use, such as a school, instead of in a central data centre. Edge devices can support local processing and offline operation.

</details>

<details>

<summary><strong>Frugal AI</strong></summary>

AI systems and practices designed for resource-constrained education contexts. Frugal AI optimises for local control, lower cost, lower energy use, poor or intermittent connectivity, open components, and long-term institutional capacity.

</details>

<details>

<summary><strong>Learner-facing content</strong></summary>

Any content intended to be shown directly to learners or used for assessment, feedback, or progression decisions.

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

<summary><strong>Model card</strong></summary>

A short reference page that explains what a model is, what it fits, what it needs, and what its limits are.

</details>

<details>

<summary><strong>Offline-first</strong></summary>

Designed to keep working without a continuous internet connection. Some setup steps, such as downloading a model, may still need internet access.

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

<summary><strong>Quasi-identifier</strong></summary>

A combination of attributes that may re-identify a person in a small population. Examples include school, grade, and a rare characteristic when used together.

</details>

<details>

<summary><strong>Quantisation</strong></summary>

A way to reduce model size and memory use by storing weights with fewer bits. Smaller quantised models fit on modest hardware, but quality can vary.

</details>

<details>

<summary><strong>RAG</strong></summary>

Retrieval-Augmented Generation: a technique that grounds AI outputs in retrieved documents from a knowledge base. RAG can improve accuracy and support citation of sources.

</details>

<details>

<summary><strong>Runbook</strong></summary>

An operations page that explains how to start, stop, check, update, back up, restore, and troubleshoot a service.

</details>

<details>

<summary><strong>Runtime</strong></summary>

The software that loads the model, runs inference, and exposes an interface for applications.

</details>

<details>

<summary><strong>Sensitive topics</strong></summary>

Content areas defined nationally or institutionally as requiring heightened care, especially in learner-facing materials. Examples may include health, religion, conflict history, identity, or locally sensitive public issues.

</details>

<details>

<summary><strong>SLM</strong></summary>

Small Language Model: an AI model with fewer parameters than larger frontier models. SLMs are more suitable for modest hardware and edge deployment, but usually have reduced capability compared with larger models.

</details>

<details>

<summary><strong>Sovereign operation</strong></summary>

Operation of AI systems under national jurisdiction and policy control. This includes in-country governance of knowledge bases and audit logs, plus a defined sovereignty envelope for any external processing.

</details>

<details>

<summary><strong>Stack</strong></summary>

A tested combination of hardware, environment, runtime, model, framework, and operations practices.

</details>

<details>

<summary><strong>Store-and-forward</strong></summary>

A synchronisation method where data is stored locally when connectivity is unavailable and transmitted when connection is restored.

</details>

<details>

<summary><strong>Teacher-in-the-Loop</strong></summary>

A workflow design that requires teacher oversight of AI-generated content. The level of oversight is calibrated to the risk level of the task.

</details>
