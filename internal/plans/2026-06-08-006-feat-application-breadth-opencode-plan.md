---
title: "Increment 4 — Application Breadth: OpenCode Coding Agent"
type: feat
status: active
date: 2026-06-08
origin: internal/plans/2026-06-08-002-feat-frugal-ai-layered-repositioning-plan.md
---

# Increment 4 — Application Breadth: OpenCode Coding Agent

## Overview

Broaden the Application layer with its first agent: an OpenCode coding agent running on the local stack. This makes the agent subtype concrete — the chat and teacher-assistant slices are not agents — and is a vivid gateway example, because the agent's model calls route through the gateway and can burst to an approved provider under the sovereignty envelope. It is developer and maintainer facing, the most technical application in the knowledge base, consistent with the developer-first repositioning.

Scope discipline: one application (an OpenCode coding agent) plus the Application layer overview. Do not add other applications such as search or non-coding agents in this increment.

## Decision (confirmed 2026-06-08)

Depth: full parallel — an Application layer overview, an OpenCode coding-agent guide, and an OpenCode component card.

## Why OpenCode, and Where It Sits

OpenCode is an open-source, terminal-first coding agent, also available for the IDE and desktop. It reads, writes, and edits files, runs shell commands, and surfaces editor diagnostics, with Plan and Build modes that add a review step before it changes files. It is multi-provider and runs local models through an OpenAI-compatible endpoint. In the stack it is an Application — the agent subtype — bundling its own orchestration, on top of Inference and Infrastructure, with its model calls routed through the Gateway.

## Two Governance Surfaces (the key insight)

An agent has two distinct control points, and the slice must address both.

- What the agent does locally: file edits and shell commands are real side effects. Controls: Plan mode for a review step before changes, a scoped working directory, and human approval before changes are applied. This makes the model cards' caution about autonomous agentic actions concrete.
- What leaves the institution: the agent's model calls. Control: route OpenCode through the gateway, so redaction, approved destinations, and audit logging apply, and any cloud burst stays inside the envelope.

The gateway governs egress; the agent's own controls govern local actions. Both are required.

## Model and Hardware Fit

Coding agents want stronger coding models than the first chat path. On the 24 GB Mac mini a smaller model runs but with reduced coding-agent reliability; stronger local coding models, such as a 30B-class coder, need more memory, which connects to the inference-breadth and pilot-hardware story. The frugal pattern is a local model by default, with controlled cloud burst through the gateway for harder tasks. Coding-quality expectations are labelled honestly: the slice demonstrates the agent and governance pattern, not state-of-the-art coding.

## Recommended Approach

- Route OpenCode at the gateway's OpenAI-compatible endpoint rather than at Ollama directly, so model calls are governed and cloud burst is available under the envelope.
- Default to a local coding-capable model; enable controlled cloud burst only for harder tasks.
- Use Plan mode, a scoped working directory, and human approval for the agent's local actions.

## Pages to Create or Modify

- Create `docs/concepts/application-layer.md` — Application layer overview: what applications are, agents as a subtype, and the two governance surfaces. Completes the set of layer overviews.
- Create `docs/getting-started/coding-agent.md` — guide: install OpenCode, point it at the gateway or a local model, set Plan mode and a scoped workspace, run a small task, review and apply, with governance and troubleshooting.
- Create `docs/components/applications/opencode.md` — component card (Application: OpenCode).
- Modify `docs/concepts/how-the-stack-fits-together.md` — link the Application row to the overview and note agents as a subtype.
- Modify `docs/SUMMARY.md` — add the overview, guide, and card.
- Modify `internal/tools/editorial_audit.py` — add the required entries and add `applications` to `COMPONENT_PARTS`.

## Audit Coupling

A new component-type folder, `components/applications/`, requires adding `applications` to `COMPONENT_PARTS`, as was done for `gateways`. Add the guide and the component card to `REQUIRED_SUMMARY_ENTRIES`. The application-layer overview is a concept page and is not a required entry.

## Minimum vs Deferred

Minimum: the application-layer overview, the OpenCode guide, and the OpenCode card; navigation and audit updates.

Deferred: other applications such as search or non-coding agents; a strong-coding-model pilot setup; deep OpenCode customisation.

## Verification

- The guide runs OpenCode against the gateway endpoint, uses Plan mode, and applies a change only after review.
- The governance section names both surfaces: local actions and model egress.
- The component card includes "## At a glance" and a layer tag; the audit passes with updated required entries and `COMPONENT_PARTS`.
- Build-time check: verify OpenCode's local and OpenAI-compatible endpoint configuration against current OpenCode documentation before writing the steps.

## Sources

- OpenCode documentation: agents, models and providers, and local models through an OpenAI-compatible endpoint. Reviewed June 2026.
