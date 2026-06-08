---
title: "Increment 1 — Orchestration: Tool-Using Teacher Assistant"
type: feat
status: active
date: 2026-06-08
origin: internal/plans/2026-06-08-002-feat-frugal-ai-layered-repositioning-plan.md
---

# Increment 1 — Orchestration: Tool-Using Teacher Assistant

## Overview

Build the first Orchestration-layer slice: a tool-using teacher assistant that drafts teaching materials with a small set of safe, local tools, under teacher review. This makes the Orchestration layer concrete and becomes the worked example for the orchestration layer overview page. It is the next step up from the frugal floor: the same infrastructure and inference as the chat slice, the gateway still local-only, with orchestration added on top.

Scope discipline (per plan 002): add the orchestration layer page and exactly one orchestration slice. Do not add RAG, Dify, agentic autonomy, or side-effecting tools in this increment.

## Approach (confirmed 2026-06-08)

Anchor the slice on **Open WebUI's native Tools and Functions** (Python, bring-your-own-function), on the existing stack.

- Frugal: no new infrastructure or services; orchestration lives in the Application-layer tool already in use.
- Local-first: tools run locally; the gateway stays closed, with no egress.
- Governed: Open WebUI provides user groups and granular permissions for access control.

Defer **Dify** — a full agentic-workflow platform (API, worker, web, plugin daemon, sandbox, vector database, object store, PostgreSQL, Redis, and a reverse proxy) — to a later, heavier increment, for when multi-step workflows or shared retrieval outgrow Open WebUI's tools. It integrates Ollama locally but is many services to run and govern.

Model: keep **Qwen3.5-9B** (tool-capable in Ollama: vision, tools, thinking). Caveat to document: local tool calling is less reliable than cloud APIs, and the model can emit a tool call as text instead of executing it. The slice needs output validation and, above all, the teacher-in-the-loop review the design already requires. If reliability proves insufficient, a more tool-reliable candidate (Gemma 4 12B native function calling, or Qwen3.6 on higher-memory hardware) is the recorded fallback, not built here.

## Layer Mapping

| Layer | This slice |
| --- | --- |
| Application | Open WebUI teacher assistant workspace. |
| Gateway | Local-only, no egress (unchanged). |
| Orchestration | Open WebUI Tools and Functions: the tool loop, a small tool set, and chat memory. |
| Inference | Ollama with Qwen3.5-9B (tool-capable). |
| Infrastructure | Mac mini 24 GB. |

## Tools (minimum, read-only, no side effects)

The first slice ships one or two safe, education-relevant, side-effect-free tools, for example a lesson-plan or rubric template filler and a simple curriculum date or term planner. Tools that send, publish, write to external systems, or reach learners are deferred to a later increment with stricter governance.

## Governance and Safeguards (load-bearing)

Tie the slice to the reference architecture's risk-tiered teacher-in-the-loop:

- The assistant operates at Tier 2: teacher-only drafts, publish controls, and periodic quality audit. No automatic learner-facing output.
- Named human review before any output reaches learners; Tier 1 (learner-facing) stays gated and out of this slice.
- Audit logging of prompts, tool calls, and outputs; raw output and teacher-edited output tracked separately.
- Gateway local-only: no external egress; the envelope stays closed.
- Tool-call reliability caveat documented; validation on tool output, with teacher review as the backstop.

## Pages to Create or Modify

- Create `docs/concepts/orchestration-layer.md` — Orchestration layer overview (concept): what it is, where it sits, frugal trade-offs, governance through tiered review and the gateway, with the teacher assistant as the worked example. Now justified by a concrete slice.
- Create `docs/guides/teacher-assistant.md` — the build guide (guide pattern): outcome, fit and limits, prerequisites, component map, steps (define a tool or function in Open WebUI, enable tool use, configure access), verification, troubleshooting (including tool-call reliability), and next step.
- Modify `docs/operations/open-webui-ops.md` — add tool and function management, audit-log review, and update considerations.
- Modify `docs/SUMMARY.md` — add an `## Orchestration` group.
- Modify `internal/tools/editorial_audit.py` — add the new pages to the required-entries list (see audit coupling).

## Audit Coupling (applies this time)

Unlike Increment 0, this increment adds new `SUMMARY.md` entries with new labels (the orchestration overview and the teacher assistant guide). The `REQUIRED_SUMMARY_ENTRIES` list in `internal/tools/editorial_audit.py` must be updated in the same change, or the audit will not enforce the new pages.

## Minimum vs Deferred

Minimum: Open WebUI tools and functions; one or two read-only tools; Tier-2 governance; audit logging; named human review; the orchestration overview and the guide; operations additions.

Deferred: side-effecting tools; automated Tier-1 routing; Dify; RAG; multi-step agent autonomy; a tool-reliable model swap.

## Verification

- A tool defined in Open WebUI executes (rather than printing as text) for a sample teacher task; the reliability caveat is documented.
- The governance section names Tier-2 scope, human review, audit logging, and the local-only gateway.
- The editorial audit passes with the updated required entries; links resolve; British spelling; no direct second person.

## Decision (2026-06-08)

Confirmed: build on Open WebUI tools and functions. OpenCode was considered and deferred to the coding-agent Application increment (plan 002, Increment 4), because it is a finished coding agent rather than a neutral orchestration substrate for a teacher assistant. First tool set: one or two read-only education tools.

## Sources

- Open WebUI features and tools documentation; Ollama tool-calling documentation; Qwen3.5 tool-calling reliability reports; Dify self-host documentation. Reviewed June 2026.
