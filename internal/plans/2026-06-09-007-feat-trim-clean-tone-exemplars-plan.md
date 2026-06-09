---
title: "Increment 5+ — Trim, Tone, Exemplars, Agentic Framing"
type: feat
status: active
date: 2026-06-09
origin: internal/editorial-review-and-roadmap-2026-06-09.md
---

# Increment 5+ — Trim, Tone, Exemplars, Agentic Framing

## Overview

Implements the five-iteration roadmap in `internal/editorial-review-and-roadmap-2026-06-09.md`, grounded in the public-docs review `internal/docs-review-2026-06-09.md`. One commit per iteration; the editorial audit must pass after each.

## Iterations

1. **Trim and clean** — internal link checker in the editorial audit; anchor the `.gitignore` `reference/` pattern; remove stale template-review sections from the editor workflow; thin templates to exemplar pointers. *Decision 2026-06-09: the ten legacy stubs stay in place and the open-webui folder move stays deferred — file deletion is not enabled in this workspace, and the stubs are unlinked and harmless. Revisit only if deletion is enabled later; redirects in `.gitbook.yaml` would then replace them.*
2. **Tone grounding** — refresh editorial-guide Source Inputs against live col.org/frugal; tone-resync line in the workflow; plan-001 leftovers (JL4D citation, Blueprint decision, Compact/alliance paragraph).
3. **Landing and exemplars** — slim `docs/README.md`; time/level hints completed on all guides; glossary theme headings; audit checks for hints and layer tags; exemplar set polished (Quickstart, Local AI chat service, Qwen3.5-9B, Ollama).
4. **Agentic framing** — third egress surface (tool/MCP traffic) in application layer and coding-agent guide; MCP in orchestration layer, glossary, OpenCode card; AGENTS.md step; "Use the knowledge base with an AI agent" reference page; model-card agentic-readiness rows; agentic preferred terms in the editorial guide.
5. **Sweep and visuals** — consistency sweep of worked guides; mermaid diagrams (gateway, coding agent, example matrix); reference page reader's guide. The administrative-agent guide remains further work (next build increment).

## Out of scope

New build guides requiring local verification (administrative agent, pilot/production runbooks).
