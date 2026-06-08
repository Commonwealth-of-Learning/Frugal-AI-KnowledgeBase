---
description: The gateway layer — the sovereignty envelope made real, one boundary that redacts, routes, logs, and governs every model request.
icon: shield-halved
---

# Gateway layer

This page describes the Gateway layer of [The Frugal AI stack](how-the-stack-fits-together.md). The gateway is the boundary every model request passes through, which makes it the single place to enforce what may leave the institution and what must stay local. It is the operational form of the sovereignty envelope and the privacy airlock in the [sovereign education-AI reference architecture](../reference/sovereign-education-ai-reference-architecture.md).

## From policy to running layer

In the first chat slice the gateway is only a policy: nothing leaves because nothing is configured to leave. A running gateway makes that boundary enforceable in software. Every application sends requests to one endpoint; the gateway decides where each request goes, what is removed before a model sees it, and what is recorded.

## What the gateway does

- One endpoint: applications use a single API, and the model or provider behind it can change without changing the application.
- Redaction: personal data is detected and masked before a prompt reaches a model, with the original kept only in protected logs.
- Routing: requests go to a local model by default, and to an approved external provider only when policy allows.
- Audit: requests, routes, and redactions are logged for review.
- Approved destinations: only the providers configured in the gateway can be reached.

## The sovereignty envelope

The gateway is where the envelope is drawn. A fully local build keeps the envelope closed: every request stays on the machine. When a task genuinely needs a larger external model, controlled cloud burst sends only de-identified, narrowly scoped content to an approved provider, with redaction applied first and a local fallback when connectivity fails. Learner free text and identifiers are blocked by default.

## When the gateway is worth running

For a single local model used by one application, the gateway is optional: governance is simple because nothing leaves. The gateway earns its place as soon as there is more than one model or application, or any external routing. That is the point where governance needs one home rather than many.

## Frugal practice

Run the gateway locally alongside the rest of the stack. Start with one endpoint, redaction, and logging, all local. Add an external destination only when a task needs it, and keep the local model as the default and the fallback.

## First slice: the AI gateway

The [AI gateway](../getting-started/ai-gateway.md) guide puts a local gateway in front of the chat service: a single endpoint, personal-data redaction, audit logging, and optional controlled cloud burst to one approved provider.

## Related pages

- [The Frugal AI stack](how-the-stack-fits-together.md)
- [AI gateway](../getting-started/ai-gateway.md)
- [Sovereign education-AI reference architecture](../reference/sovereign-education-ai-reference-architecture.md)
- [Frugal AI principles](frugal-ai-principles.md)
