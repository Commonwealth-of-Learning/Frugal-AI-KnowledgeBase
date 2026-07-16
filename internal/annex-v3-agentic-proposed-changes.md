# Annex v3 — agentic-era proposed changes (KB-originated, for COL review)

_Owner: TBC — assign a COL focal point to receive these proposals for review (plan-009 decision D7; gap-review-2026-06-12 C3). The same owner covers the extracted v2 changes in [annex-v2-proposed-changes.md](annex-v2-proposed-changes.md)._

**Routing rule.** These twelve proposals are **KB-originated input to a future annex revision**, collected here for COL review. They are **NOT applied to the public reference page** `docs/reference/sovereign-education-ai-reference-architecture.md`, which stays a faithful adaptation of COL's authoritative annex — the same convention as `annex-v2-proposed-changes.md`. The single public change the knowledge base makes itself is A1's extension of the KB-authored crosswalk row ("How the annex maps to the knowledge base stack"), which is adaptation commentary, not annex text.

**Difference from the v2 set.** `annex-v2-proposed-changes.md` extracts COL's own highlighted v2 draft, which is entirely non-agentic (task–model fit, M&E measurement, privacy-airlock testing, open-source scan, policy instruments). This collection is a distinct, KB-authored set covering agents, harnesses, loop and tool-egress governance — the areas the KB documents publicly but the annex (v1 and the v2 draft alike) does not yet address. Where an item extends a pending v2 appendix, that is noted (A8 → v2 Appendix E; A12 → v2 Appendix G); reconcile only if COL accepts v2 first.

**Guardrails preserved (as in v2).** No proposal expands into high-stakes automated decisions (certification, progression, grading); cloud burst stays the exception, not the default; teacher approval for learner-facing content is unchanged or strengthened; child-safety and data-protection language is preserved or reinforced.

**Grounding note.** Each proposal cites the KB pages that already document the practice. `internal/frugal-ai-principles.md` (internal-only) informs the arguments in A4 and A11 but must never be cited on a public page.

**Interdependencies.** A1 defines the terms the others use. A2, A3 and A5 are the control set that A8 and A9 then audit. A10 depends on the Section 5 controls (A2/A3) being in place. Suggested order for COL review: A1 first; then A2, A3, A5, A4, A6, A7, A10, A11, A12; then A8 and A9 last. A8 and A9 did not receive an independent adversarial verification pass in the source review (their verifiers could not be re-run) — flagged inline.

---

## A1 — Place agents in the eight-layer model (high)

**Where:** §3 Layer C (Application Services) row; the metadata scope note; §10 glossary.

**What:** Amend Layer C to name agents as a subtype of Application Services — applications that take multi-step actions (plan, call tools, edit files, run commands) under the oversight controls of Layer B and the Section 5 risk tiers — so agents inherit a defined home in the eight-layer model rather than falling outside it. Add an explicit note that an agent's tool or MCP traffic does not pass the Layer E privacy airlock and needs its own allowlist control, so §5.3's "all processing passes through the privacy airlock" is not silently falsified for agents. Clarify the scope note so agentic task execution under review gates is within the baseline, while high-stakes automated decision-making stays out of scope regardless of whether an agent performs it. Add to the annex glossary: agent, agent loop (harness), tool egress, written skill, and Model Context Protocol (MCP) — the pending v2 glossary additions are Quantisation, QAT, and Task–Model Fit only.

**KB grounding:** `docs/concepts/application-layer.md:14-16` (agent as the most capable, most governed application subtype); `docs/reference/glossary.md:16-18` (agent as an Application-layer subtype).

**Public exception applied:** the KB-authored crosswalk row on the reference page now reads "Application Services | Application layer, including agents as an Application-layer subtype." No annex text was changed.

## A2 — The second egress surface: tool/MCP traffic outside the airlock (high)

**Where:** §5.3 (qualify the "all processing passes through the privacy airlock" assertion); §4.4 (extend the envelope); §3 layer table under **Layer C** core components (not Layer E).

**What:** Model-bound processing passes the privacy airlock, but an agent's tools and MCP servers are a second external-processing path that does not. Require the same envelope discipline for tool egress — an allowlist of permitted tools, MCP servers, and destinations; no network access by default; each network-reaching tool reviewed as a component before adoption — and extend the §4.4 permitted/prohibited payload rules to tool traffic. Surface the control under Layer C, not Layer E: the KB crosswalks Layer E (Privacy Airlock) to the gateway, which governs model egress only, and governs tool egress at the application layer (which crosswalks to Layer C), so a Layer E placement would contradict the three-governance-surfaces framing.

**KB grounding:** `docs/concepts/application-layer.md:28`; `docs/getting-started/coding-agent.md:142`; `docs/concepts/gateway-layer.md:38` ("The gateway governs model egress only").

## A3 — Extend risk-tiered oversight from outputs to actions (high)

**Where:** §5.1 risk-tiered approval framework and the tier-classification quick test.

**What:** Where an application acts (edits files, runs commands, calls side-effecting tools), oversight applies per action as well as per output — a plan-only review mode before execution, explicit approval for each side-effecting action, a scoped working directory, and denial outside scope. Extend the quick test: "Does the task involve an agent taking actions with side effects? → per-action approval applies in addition to the output tier." Note the approval step assumes AI literacy: reviewers must be able to see and understand what an agent did before approving it.

**KB grounding:** `docs/getting-started/coding-agent.md:93-97,125,128-134`; `docs/concepts/orchestration-layer.md:47-51`; `docs/README.md:34`; `docs/reference/glossary.md:220-222`.

## A4 — Sovereign operation extends to the agent loop (high)

**Where:** §2.1 Sovereign operation principle; procurement questions in §3.1 and Appendix A (not the §1 executive summary).

**What:** Where agents are used, the agent loop (harness) — the orchestration that assembles context, calls tools, and keeps memory between steps — remains under national or institutional control, because whoever operates it sees everything the agent sees while it works, and residency rules alone do not capture the working knowledge an externally run loop experiences. Frame the stake as delegation capacity: whether an institution has agents working for it, or only works inside someone else's. Add procurement questions: who operates the harness; where its logs and memory accrue, and under what retention and review; whether the model behind it can be substituted without surrendering the loop.

**KB grounding:** `docs/concepts/application-layer.md:18-20`; `docs/concepts/orchestration-layer.md:39`; `docs/README.md:34`. Internal-only argument: `internal/frugal-ai-principles.md:18-26` (do not cite publicly).

## A5 — Agent memory as a named retention surface (medium)

**Where:** §5.3 retention baseline; §2.2 privacy controls.

**What:** For any agentic deployment, define what an agent is permitted to remember across sessions, where that memory is stored, how long it is retained, and who can review it — the same discipline the annex already applies to prompts, outputs, and logs. An agent's working context and memory fall under the same residency and access expectations as stored records, since memory accumulates institutional knowledge even when nothing is stored in the traditional sense.

**KB grounding:** `docs/concepts/orchestration-layer.md:49`; `docs/reference/glossary.md:24-26`.

## A6 — Written skills as a third versioned artefact class (medium)

**Where:** §2.2 auditability list; §3 Layer H registries; §5.1 Tier 2 feedback loop.

**What:** Add written skills and agent instruction files as a third versioned artefact class alongside the knowledge base and model configurations: short written procedures an agent loads into context to direct its behaviour, reviewed and version-controlled like any other configuration. Register them in the Layer H operations registries, and connect them to §5.1's Tier 2 feedback loop — corrections identified through review are folded back into the skill, giving the annex a concrete artefact for "errors identified through audit feed back into system improvement."

**KB grounding:** `docs/getting-started/coding-agent.md:105,115`; `docs/getting-started/manim-animator.md:74`; `docs/concepts/application-layer.md:34`; `docs/reference/glossary.md:112-114`.

## A7 — Staged Tier 1 review as an optional pattern (medium)

**Where:** §5.1 Tier 1 approval gate; §6.3 pilot-to-scale mitigations.

**What:** Describe staged Tier 1 review as an optional pattern for generated artefacts (animations, complex documents, multi-part materials): a plain-language plan or storyboard approved before production begins, and the finished artefact inspected against an explicit checklist at release. Staging moves teacher judgement to the cheapest point in the workflow without weakening the approval-before-learner-release rule — it strengthens it with an earlier review point — and gives §6.3 a concrete mechanism against the review-capacity bottleneck rather than tiering alone.

**KB grounding:** `docs/getting-started/manim-animator.md:78,88-94,101,111`.

## A8 — Layer H components and §8 indicators for agentic use (medium)

_No independent adversarial verification pass in the source review — treat as provisional._

**Where:** §3 Layer H core components; §8 indicator table.

**What:** Add an "Agent oversight" domain to the §8 indicators: completeness of agent action logs (every file edit and command recorded with its approval decision); tool-call audit coverage and allowlist conformance (share of tool calls logged; no tool egress outside the allowlist); per-action approval and rejection rates; a defined review cadence for agent memory. Extend Layer H's core components with agent action logs and a registry of approved tools and MCP servers, parallel to the model and knowledge-base registries. Extends, does not duplicate, the pending v2 Appendix E measurement sheet — reconcile if COL accepts v2 first.

**KB grounding:** `docs/getting-started/coding-agent.md:128-134`; `docs/concepts/orchestration-layer.md:47-51`; `docs/concepts/gateway-layer.md:51`.

## A9 — Appendix A self-assessment subsection for agentic use (medium)

_No independent adversarial verification pass in the source review — treat as provisional._

**Where:** Appendix A, a new subsection after Security or Scale Readiness.

**What:** Add "Agentic use (if agents are deployed)" in the checklist's existing style: each of the three governance surfaces (local actions, model egress, tool egress) has a named control; tools and MCP servers are allowlisted with no network access by default; side-effecting actions require per-action approval with a plan-only review mode available; agent memory retention is documented (what is remembered, where stored, how long retained, who reviews); written skills are versioned and reviewed; agent action logs are tamper-evident; and agents remain single-operator tools until an operational runbook and review workflow exist for shared use.

**KB grounding:** `docs/concepts/gateway-layer.md:38,51`; `docs/concepts/application-layer.md:22-30`; `docs/components/environments/pilot.md:12`.

## A10 — Governed coding agents as a §6.1 capacity mitigation (medium)

**Where:** §6.1 Procurement Paralysis mitigations.

**What:** Add a technical mitigation: governed coding agents as a force-multiplier for the small teams operating the sovereign stack — drafting configurations, scaffolding components, and maintaining documentation under human review. State the required controls directly (not by reference to other proposals): review-first, per-action approval of file edits and commands; model calls routed through the gateway inside the sovereignty envelope; tools allowlisted with no network access by default, since tool egress does not pass the gateway. Note the second-order benefit: a team that operates a readable open-source agent also builds the capacity to govern agents generally.

**KB grounding:** `docs/getting-started/coding-agent.md:26,39-42` (OpenCode's dual role).

## A11 — Agentic workloads strengthen the local-default case (medium)

**Where:** §4.2 hybrid-model rationale; §4.4 envelope corollary.

**What:** Add a paragraph to §4.2: an agent loop consumes many times the tokens of a single reply (retries, tool calls, multi-step work), so per-token cloud pricing turns autonomy into a rationed resource in exactly the contexts this annex serves, while local inference makes the marginal cost of a long-running agent task close to zero once the modest hardware §1 already assumes exists. Corollary in §4.4 envelope vocabulary: burst applies per hard step inside a locally run loop, never to the loop itself, so only the minimised per-step payload crosses the envelope while the run record and the agent's working state fall under the what-must-remain-in-country clause.

**KB grounding:** `docs/getting-started/manim-animator.md:111` (loop and actions gated locally; model calls including controlled burst gateway-governed). Internal-only argument: `internal/frugal-ai-principles.md:58-60` (do not cite publicly).

## A12 — Agent harnesses as a sixth §4.3 open-source category (low)

**Where:** §4.3 open-source options category list (and a matching dated subsection in the pending v2 Appendix G if that is accepted first, since the v2 §4.3 note routes every category to Appendix G).

**What:** Add a sixth category: agent harnesses and coding agents — open-source agent loops that connect to locally served, OpenAI-compatible model endpoints and gate file and command actions behind per-action review. State the selection criteria the KB documents: a codebase readable enough for the local team to study the loop it will govern; support for local OpenAI-compatible endpoints; review-first per-action permission gating — exercised in practice by the documented OpenCode path, and verified (though not documented as paths) for Tau and Pi.

**KB grounding:** `docs/getting-started/coding-agent.md:35-42`.

---

## Source

- `internal/annex-grounded-review-2026-07-15.md` — Part 3 (the twelve agentic annex-update proposals, with per-proposal adversarial verdicts).
- `internal/plans/2026-07-15-009-feat-audit-remediation-plan.md` — WS15 (the collection's scope and routing).
