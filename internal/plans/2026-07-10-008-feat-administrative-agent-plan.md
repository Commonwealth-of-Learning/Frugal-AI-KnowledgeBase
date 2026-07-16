---
title: "Increment 6 — Administrative Agent: Tier 2 Agentic Work, the Harness Decision, and the Skill Registry"
type: feat
status: draft
date: 2026-07-10
origin: internal/gap-review-2026-06-12.md
---

# Increment 6 — Administrative Agent: Tier 2 Agentic Work, the Harness Decision, and the Skill Registry

## Overview

Fill the example matrix's last empty row: an administrative agent doing routine staff tasks under human approval. This is the stakeholder-relevant agent example — the case ministries and institutions actually ask about — and the first **Tier 2** worked example (teacher- and staff-only output, post-hoc audit with publish controls), complementing the Tier 1 builds. The increment deliberately bundles three deferred decisions recorded in CLAUDE.md and the naming registry, because they resolve together here:

1. **The harness decision** — reuse OpenCode, or build on a standalone open harness (Pi's `pi-agent-core` is the candidate). If standalone: add the `Harness:` role label to the naming registry and audit prefix list, create the Pi component card under Orchestration, and update the orchestration layer's "a standalone harness build is not a documented path yet" line.
2. **The skill registry** — this build produces the first reusable written skills, so it decides the format: a plain reviewed `skills/` directory of Markdown files is the frugal default; evaluate Pi's skill ecosystem and other open formats against it. Update the forward line in coding-agent step 3 when decided.
3. **The coding-agent runbook** — the guide will recommend repeated team use of an agent, which is the operations-policy gate: the coding agent (and this new agent) must be covered in the operations overview by a runbook, not a further-work marker.

Scope discipline: one agent, one routine task class, Tier 2 only. The advanced matrix cell (multi-step workflows) stays *further work* unless the intermediate cell lands early.

## Decisions to make first (spike iteration)

- **Task selection.** Criteria: no learner personal data, staff-only output, file tools only (no network tools), demonstrable fully local, obviously useful. Candidates, in rough order of fit: drafting routine correspondence from bullet points; tidying and summarising an attendance or enrolment CSV into a term summary; compiling a staff newsletter from provided items; drafting minutes from meeting notes. Pick one for the guide; the others become prompt variations in a closing section.
- **Harness.** Criteria: governance parity with the documented path (review-first permissions, scoped directory, ask-before-side-effects), OpenAI-compatible endpoint so model calls route through the gateway, effort to reach a working guide, and what it teaches (capacity-building value of an inspectable loop). Reusing OpenCode is the low-risk default; `pi-agent-core` is the ownership-maximal option the orchestration layer already points at.
- **Skill format.** Start from plain Markdown in a reviewed `skills/` directory unless the harness choice makes another format clearly better. The registry is version control plus review, not a new system.
- **Model.** Default to Gemma 4 12B through the gateway; the task class is drafting and reshaping text, which a local model should handle — this build should *not* need cloud burst, which is itself a point worth demonstrating. Label as expected until tried.

## Governance (the point of the build)

- **Tier 2**: output reaches staff, not learners — post-hoc audit and publish controls rather than pre-release approval. State plainly that anything forwarded to learners re-enters Tier 1.
- Cross-reference the reference architecture's Appendix A Tier 2 self-assessment indicators (post-hoc audit sampling, publish controls) per plan-009 decision D6 — the knowledge base has no Tier 2 worked example yet, so this build is where those indicators gain one.
- The three governance surfaces, mapped as in the coding-agent guide: local actions gated (review-first, scoped to a working folder of copies, never the system of record), model egress through the gateway (envelope closed for this build), no network tools at all.
- Memory and retention: apply the orchestration layer's memory bullet — say what the agent's working folder and any session history retain, and who clears them.
- Data rule stated up front: the working folder contains no learner personal data; staff records used in examples are synthetic.

## Pages to create or modify

- Create `docs/getting-started/administrative-agent.md` — the guide (Advanced group, **before** Manim animator, per plan-009 decision D6, so the fully-local Advanced path completes before the credential-dependent Manim build): outcome, fit and limits, skill file, task run under review, verification, Tier 2 governance section, troubleshooting.
- Create `docs/operations/coding-agent-ops.md` — runbook covering the coding agent and this build (start/stop, health, audit-log review, working-folder hygiene, recovery).
- Modify `docs/concepts/example-applications.md` — fill the administrative agent intermediate cell; keep the advanced cell *further work*.
- Modify `docs/operations/operations-overview.md` — runbook rows for both agents.
- Modify `docs/SUMMARY.md`, landing routing table (a "Automate routine staff work" row), and `internal/tools/editorial_audit.py` required entries.
- If the standalone harness is chosen: create `docs/components/orchestration/pi.md` (`Harness: Pi`), register the label, extend the audit prefix list, update the orchestration layer line and the coding-agent alternatives note.

## Audit coupling

New required SUMMARY entries for the guide and runbook; the `Harness:` prefix only if that path is chosen. The guide-hint and layer-tag checks apply automatically. Per-increment tone resync against the editorial guide's source inputs, as established in plan-007.

## Minimum vs deferred

Minimum: spike decisions recorded here; the guide on the chosen harness; matrix cell filled; runbook and operations rows; audit and navigation updates. Deferred: the advanced multi-step cell; the Pi card if OpenCode is chosen (the deferral note then stays in the registry); any skill-registry tooling beyond a reviewed directory.

## Iterations

1. Spike and decide: task, harness, skill format; update this plan's status and record decisions.
2. Build and verify the task end to end on the chosen harness; write the guide.
3. Runbook and operations rows for both agents.
4. Cards, labels, and registry updates if the standalone harness was chosen.
5. Cross-links (example matrix, landing routing, orchestration layer), audit updates, tone resync, commit per iteration.
