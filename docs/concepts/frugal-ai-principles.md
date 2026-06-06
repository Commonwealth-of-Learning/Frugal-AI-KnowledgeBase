---
description: The operating principles behind the local AI path.
icon: seedling
---

# Frugal AI principles

Frugal AI helps an institution run useful AI services without giving up control of its data, costs, or day-to-day operations.

It starts with a clear education task, then chooses the smallest reliable model, runtime, and infrastructure needed to support that task. In the Frugal AI knowledge base, the first example is a local AI chat service that a small team can run, inspect, and maintain.

Frugal AI is not cheap AI. It is local-first, open where practical, and designed to build institutional capacity over time.

## The problem

Cloud AI services can be useful, especially for early experimentation. They also introduce risks that grow as AI becomes part of everyday teaching, learning, and administration:

- Cost can rise unpredictably with usage, licensing, and model changes.
- Reliable bandwidth becomes a condition for basic service.
- Student, staff, and institutional data may cross unclear jurisdictions.
- Local teams may remain dependent on external vendors for core capability.
- Innovation can fragment into pilots that cannot be scaled or maintained.

Frugal AI manages these risks by designing for local control, open components, offline resilience, and local capacity from the start.

## Definition

Frugal AI is a design approach for deploying AI with minimal resource intensity and maximum local control.

In practice, this means:

- define the education task first;
- choose the smallest reliable model and runtime for that task;
- prefer open-source tools and open-weight models where practical;
- run inference on local infrastructure when the data or service requires it;
- keep teachers, institutional owners, and local technical teams in the workflow;
- document the limits, operating costs, and support responsibilities before scaling.

## Why it matters

Frugal AI connects technical choices to public-interest education outcomes.

| Outcome | What it means in practice |
| --- | --- |
| Data sovereignty | Sensitive education data stays under institutional or national control unless there is a clear, approved reason to move it. |
| Operational resilience | Core services can keep working when connectivity is limited, expensive, or temporarily unavailable. |
| Economic resilience | Institutions move from open-ended subscription exposure toward more predictable investment in local infrastructure and support. |
| Local expertise | Teams learn by deploying, maintaining, auditing, and improving the system rather than only consuming an external service. |
| Teacher agency | AI supports educator judgement. Teachers remain reviewers, validators, and contextual experts for learner-facing materials. |
| Digital public value | Open components, shared recipes, and modular designs make it easier for institutions to adapt and improve systems together. |

## Principles

### Start from the education task

Do not start by asking for the largest model the hardware can run. Start with the job to be done.

Name the users, the data involved, the risk level, and the expected output. A local chat assistant for staff experimentation has different requirements from a learner-facing tutor, a teacher resource workflow, or an administrative helpdesk.

### Keep data local by default

Prompts, uploaded files, chat history, course materials, and learner records should stay on local or institutionally governed infrastructure unless there is a documented reason to send them elsewhere.

Local does not mean automatically safe. A local system still needs access control, backups, retention rules, update plans, and clear handling for sensitive information.

### Prefer open and inspectable components

Use open-source tools and open-weight models where practical. This helps institutions understand what they are running, adapt it to local needs, and reduce dependency on a single vendor.

Open-weight does not always mean open source. Model licences, data-use terms, and deployment restrictions still need to be checked before a pilot becomes an institutional service.

### Match the model to the machine

A smaller model that runs reliably is often more useful than a larger model that exhausts memory, fails under load, or needs constant tuning.

Frugal AI starts with the memory budget, the expected number of users, and the quality needed for the task. It then chooses the runtime, model, quantisation, context window, and interface.

### Design offline-first where resilience matters

Offline-first means the core service can run locally and synchronise only when connectivity is available. This matters for small states, rural campuses, disaster-prone regions, and institutions where bandwidth is unreliable or expensive.

Offline-first is not the same as never using the cloud. A hybrid design may be reasonable for updates, backups, or temporary demand spikes. The important point is that cloud use should be deliberate, governed, and reversible.

### Build capacity through delivery

Frugal AI should leave local teams stronger after each deployment. The team should know how to start the service, stop it, update it, back it up, restore it, review logs, test quality, and decide when the system is not suitable.

Implementation is part of the training model. Teams build capability by operating the system, not only by attending a workshop about it.

### Keep teachers and institutions in the loop

AI should support professional judgement, not replace it. For learner-facing resources, teachers should review, refine, and approve outputs before they reach learners.

This is the Teacher-in-the-Loop principle: educators act as co-designers, validators, and quality filters. The same logic applies to institutional workflows. A human owner must be accountable for what the system is allowed to do.

### Govern AI as public infrastructure

Education AI affects trust, inclusion, privacy, assessment, accessibility, language, and cultural context. Treat it as infrastructure that needs governance, not as a tool that can be installed and forgotten.

At minimum, each service should document:

- who owns the service;
- what data it can use;
- who can access it;
- how outputs are reviewed;
- what logs are retained;
- how incidents are handled;
- when the system must be paused or escalated.

### Keep the architecture modular

Start with a small service that works. Add retrieval, agents, learning-management-system integration, analytics, and multi-user access only when the supporting safeguards and operations are ready.

A modular design lets an institution improve one layer at a time: hardware, runtime, model, interface, content sources, monitoring, or governance.

## Trade-offs

Frugal AI is not a shortcut around institutional responsibility.

| Choice | Benefit | Responsibility |
| --- | --- | --- |
| Local inference | Keeps sensitive data closer to institutional control. | Requires local security, backups, hardware planning, and support ownership. |
| Open-weight models | Reduces vendor lock-in and supports adaptation. | Requires licence review, quality testing, and model lifecycle management. |
| Smaller models | Fits modest hardware and lowers operating cost. | May need better prompts, retrieval, human review, or narrower tasks. |
| Offline-first design | Keeps core services available during connectivity gaps. | Requires update, sync, and recovery plans. |
| Teacher-in-the-loop workflows | Protects professional judgement and learner context. | Requires time, mentoring, quality criteria, and institutional recognition. |
| Modular growth | Makes pilots easier to maintain and improve. | Requires discipline not to add features before governance is ready. |

## How the first path applies this

The [Local AI chat service](../getting-started/offline-chat-service.md) is the smallest useful version of the pattern in the Frugal AI knowledge base.

| Principle | How the current path applies it | What it does not prove yet |
| --- | --- | --- |
| Local control | A local machine runs the runtime, model, and chat interface. | It is not a hardened multi-user institutional deployment. |
| Open components | Ollama, Open WebUI, and an open-weight model keep the stack inspectable and replaceable. | Licences and governance still need review before formal deployment. |
| Matched resources | The model is selected for the Mac mini with 24 GB unified memory development environment. | It does not establish performance for classrooms, campuses, or ministries. |
| Operational capacity | The operations page explains routine start, stop, health checks, and recovery. | It does not replace a full service desk, monitoring, or incident plan. |
| Human oversight | The service is suitable for experimentation and reviewed use. | It is not an automated assessment, tutoring, or decision system. |
| Modular growth | The same pattern can later support RAG, LMS support, or helpdesk workflows. | Those paths need their own data governance and quality controls. |

## Not Frugal AI

Avoid calling a system Frugal AI if it:

- sends sensitive education data to external services by default;
- depends on a vendor that the institution cannot inspect, replace, or govern;
- runs a model too large for the local team to operate reliably;
- treats teachers as optional reviewers for learner-facing content;
- starts a pilot without a maintenance owner, backup plan, or exit path;
- uses local hosting as a label while leaving data, costs, or control outside institutional reach.

## Source framing

This page adapts the Commonwealth of Learning framing from:

- [COL Frugal](https://www.col.org/frugal/)
- [Frugal AI: A Blueprint for Digital Sovereignty in Commonwealth Education](https://www.col.org/news/frugal-ai-a-blueprint-for-digital-sovereignty-in-commonwealth-education/)
- [Frugal AI: A Roadmap to Sovereign GenAI for Education](https://www.col.org/news/frugal-ai-a-roadmap-to-sovereign-genai-for-education/)
- [Gaborone to New Delhi Compact for AI in education](https://www.col.org/news/gaborone-to-new-delhi-compact-for-ai-in-education-launched-at-india-ai-impact-summit/)
- [Beyond the Classroom: Frugal AI in TVET as a roadmap in skills training](https://www.col.org/news/beyond-the-classroom-frugal-ai-in-tvet-as-a-roadmap-in-skills-training/)
- [Teacher-in-the-loop AI places educators at the centre](https://www.col.org/news/teacher-in-the-loop-ai-places-educators-at-the-centre-of-how-artificial-intelligence-is-designed-applied-and-validated-in-education/)
- [COL Connections, April 2026](https://oasis.col.org/server/api/core/bitstreams/51a0562e-d4d1-4cd6-9011-18963b498475/content)
