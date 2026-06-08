---
title: Increment 2 — Gateway: The Sovereignty Envelope as a Running Layer
type: feat
status: active
date: 2026-06-08
origin: internal/plans/2026-06-08-002-feat-frugal-ai-layered-repositioning-plan.md
---

# Increment 2 — Gateway: The Sovereignty Envelope as a Running Layer

## Overview

Turn the gateway from a concept into a running layer: a self-hosted LLM gateway in the request path between the applications and the models, enforcing a single API, PII redaction, audit logging, routing, and approved destinations. This is where the sovereignty envelope and the annex's privacy airlock become enforceable in software rather than asserted by the absence of egress.

Frugal framing: build the gateway local-first. Phase 2a runs it with no external egress, proving the envelope on local traffic. Phase 2b (optional) adds one approved cloud-burst destination, governed by the same envelope.

## Decisions (confirmed 2026-06-08)

- Phase scope: 2a and 2b — local enforcement plus controlled cloud burst.
- Gateway: LiteLLM.

## Recommended Approach

Anchor on **LiteLLM**, a self-hosted open-source AI gateway and proxy: a unified OpenAI-compatible endpoint over local Ollama and, optionally, cloud providers, with built-in guardrails and PII redaction (Presidio), audit logging, and routing with fallback. Rationale: most widely adopted and documented, native Ollama support, the exact envelope feature set, and it runs locally alongside the existing stack.

Alternatives recorded, not built: Bifrost (Apache 2.0, high performance), Portkey open-source gateway, Kong AI Gateway, and LLM Router Cloud.

## The Gateway Is Optional Until Requests Diverge or Leave

For the simplest single-model local chat, the gateway is an optional simplification: governance is trivial because nothing leaves and access is handled in the application. The gateway becomes the governance home as soon as there are multiple models or applications, or any external routing. Present it that way, consistent with "layers are optional".

## Layer Mapping (after this increment)

Request path: Application to Gateway (LiteLLM) to Orchestration and Inference. Open WebUI connects to the gateway's OpenAI-compatible endpoint instead of Ollama directly; the gateway forwards to Ollama, and in Phase 2b to an approved external provider.

## What the Gateway Enforces

- One OpenAI-compatible endpoint for all applications.
- PII redaction before the model sees a prompt, with originals only in protected audit logs.
- Audit logging of requests, routes, and redactions.
- Routing between local models, and an approved-destination allowlist.
- Phase 2b: controlled cloud burst for de-identified payloads only, with audit logging and local fallback.

## Pages to Create or Modify

- Create `docs/concepts/gateway-layer.md` — Gateway layer overview: the sovereignty envelope made real.
- Create `docs/getting-started/ai-gateway.md` — build guide: deploy LiteLLM in front of Ollama, repoint Open WebUI, enable redaction and audit logging, verify (2a); an optional 2b section for cloud burst.
- Create `docs/components/gateways/litellm.md` — component card (Gateway: LiteLLM).
- Modify `docs/operations/open-webui-ops.md` — gateway operation: start and stop, configuration, key management, log review, and redaction policy.
- Modify `docs/concepts/how-the-stack-fits-together.md` — note the gateway is now a running component, not only a policy.
- Modify `docs/getting-started/offline-chat-service.md` — optional note that the chat service can connect through the gateway.
- Modify `docs/SUMMARY.md` — add a `## Gateway` group (between Orchestration and Application) plus the guide.
- Modify `internal/tools/editorial_audit.py` — add the new required entries, and add `gateways` to `COMPONENT_PARTS` (see audit coupling).

## Audit Coupling

Two changes this time. New `SUMMARY.md` entries (the gateway guide and the LiteLLM component card) require updating `REQUIRED_SUMMARY_ENTRIES`. A new component-type folder, `components/gateways/`, requires adding `gateways` to the audit's `COMPONENT_PARTS` set, so the component card receives the "## At a glance" check that other component cards get.

## Governance and Safeguards (centrepiece)

This increment operationalises the annex's sovereignty envelope and privacy airlock:

- redaction at the boundary; approved destinations; audit logging; local fallback;
- Phase 2b cloud burst only for de-identified, narrowly defined tasks, with learner free text and identifiers blocked by default;
- ties to risk-tiered teacher-in-the-loop for any learner-facing output.

## Minimum vs Deferred

Minimum (2a): LiteLLM in front of Ollama; single endpoint; PII redaction; audit logging; Open WebUI repointed; the gateway overview, guide, and component card; operations additions; no egress.

Deferred: Phase 2b cloud burst (optional this increment); RBAC, virtual keys, budgets, SSO, and multi-team management (pilot scale); advanced guardrails such as prompt-injection and topic filters.

## Verification

- Open WebUI works through the gateway; chat is unchanged for the user.
- A prompt containing a test identifier is redacted before the model; the original appears only in the protected log.
- The audit log records the request and the route taken.
- Phase 2b: cloud burst routes only de-identified payloads to the approved destination, with local fallback when offline.
- The editorial audit passes with the updated required entries and `COMPONENT_PARTS`.

## Sources

- LiteLLM proxy, guardrails, and Ollama provider documentation; open-source LLM-gateway comparisons. Reviewed June 2026.
