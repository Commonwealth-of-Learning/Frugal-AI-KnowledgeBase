# Gap review — documentation and workflow

Date: 2026-06-12. Scope: all of `docs/` (35 pages), `docs/SUMMARY.md`, `.gitbook.yaml`, `.gitignore`, and the editorial machinery (`internal/editor-workflow.md`, `internal/editorial-guide.md`, `internal/naming-registry.md`, `internal/templates/`, `internal/tools/editorial_audit.py`), checked against the 2026-06-09 reviews and the plan-007 outcomes. Method: full inventory, audit run from both roots (clean, both passes), git history since 2026-06-09, and targeted cross-checks of every deferred item. Findings only; no public pages were edited.

Baseline: the 2026-06-09 reviews' recommendations are nearly all implemented. The five plan-007 iterations, the navigation fixes, the principles rewrite, and the stub retirement landed cleanly. The gaps below are what remains, plus what those changes themselves left behind.

## A. Stale workflow pointers (defects; fix first)

**A1. The concept exemplar points at a deleted public page.** `internal/editor-workflow.md` (Exemplar Pages) and `internal/templates/concept-page-template.md` both name `docs/concepts/frugal-ai-principles.md` as the live concept exemplar. That page moved to `internal/frugal-ai-principles.md` on 2026-06-09 (commit eb1774f). The concept page type now has no public exemplar, and a maintainer following the workflow would copy structure from an internal page whose framing is deliberately not public. The audit's link checker covers `docs/` pages only, so it cannot catch this. Fix: designate a public concept exemplar (`docs/concepts/application-layer.md` or `gateway-layer.md` are the strongest candidates) and update both files.

**A2. The workflow's role-label example block is stale against the naming registry.** Step 10 of the workflow still shows `Agent: OpenCode` (renamed to `Coding Agent:` on 2026-06-09, when the registry and audit were updated) and omits `Platform: Dify`. Anyone using the workflow's block rather than the registry would reintroduce the old label. Fix: sync the block with the registry's approved set, or replace it with a pointer to the registry so the list lives in one place.

**A3. The handoff document is three days and fifteen commits out of date.** `internal/handoff-2026-06-08.md` (base head 475a334) predates plan-007's five iterations, the principles internalisation, the reference-page v2 rebuild, the legacy-stub retirement, and the navigation fixes. It is the only onboarding document in the repository (the local decision log is gitignored), so a new maintainer would inherit a materially wrong picture: it still describes a "framework" component card, legacy stubs, and a pre-agentic KB. Fix: refresh it, or add a superseded-by header pointing at the current state and keep it as a dated snapshot.

**A4. The stub-retirement decision was reversed but the record was not.** The decision log recorded "user declined content-file deletion 2026-06-09; stubs stay", yet commit 5eb7ec9 (same day, later) deleted the ten stubs, added twelve redirects to `.gitbook.yaml`, and moved `frameworks/open-webui.md` to `components/applications/`. The published result is correct; the stale record is the risk, since future sessions would avoid the area or re-propose the work. Relatedly, the workflow still lists "Legacy stub" as a page type (step 1) and keeps the stub rule in step 10; harmless, but both can be cut now the mechanism is redirects.

## B. Content gaps (public docs)

**B1. The administrative agent row is still empty.** Both cells of the example-matrix row remain *further work*. The 2026-06-09 review called it the example ministries will ask about first, and everything it depends on now exists: the three governance surfaces, MCP framing, Dify orchestration, and the human-approval vocabulary. This is the largest open content gap and the natural next build increment (a plan-008).

**B2. Runbook debt is now the operations overview's main content.** Three of the five rows in "What is operated" are promissory: the coding agent ("create a runbook before repeated team use"), Dify ("before a shared pilot"), and the serving engines ("before shared inference"). Only the chat-service runbook exists. The coding-agent runbook is the most urgent of the three: OpenCode is the builder's tool the capacity-building story depends on, and "repeated team use" is exactly what that story prescribes. The interim notes on the overview page are good but are not a runbook by the page's own gate.

**B3. No pilot serving guide.** `how-the-stack-fits-together.md` says "a pilot guide is further work"; the pilot environment page poses the readiness questions but no guide shows a pilot build (vLLM behind the gateway is the implied path). The curriculum advisor's advanced cell (Dify multi-step at pilot scale) is blocked on the same gap. These two can be one increment.

**B4. SGLang and llama.cpp are load-bearing mentions without cards.** `inference-layer.md` presents SGLang as a peer of vLLM ("adopting one is an endpoint change behind the gateway") and the operations overview lists it in the operated-class table, but no card exists; llama.cpp is named as the engine both local runtimes wrap, also without a card. This is consistent with the policy of adding cards only when a path needs them, but the SGLang case is close to the line: a reader comparing serving engines has a card for one side only. Decide explicitly (card at pilot-guide time, or a one-line "no card yet" marker) rather than leaving it implicit.

**B5. One unverified claim remains on the agent page.** `use-with-an-ai-agent.md` still carries "confirm the endpoints on the published domain before relying on them". A single check of `<site URL>/llms.txt` on the published GitBook domain closes it; until then the page documents a capability nobody has observed.

**B6. Minor vocabulary drift on the production checklist.** The Human review bullet says "teacher-only outputs" without tying it to the tier scheme used everywhere else (Tier 2 is the teacher-only band). One phrase; low priority.

## C. Process and tooling gaps (internal)

**C1. The audit roadmap has one item left.** Of the five checks proposed on 2026-06-09, four are implemented (internal links, second person, layer tags, guide hints). The confidence-label heuristic (warn when memory or performance figures appear without measured / source-listed / expected / estimated labels) was not built, and the final-pass checklist still carries it manually. Lowest-value of the five by design; either build it warn-only or strike it from the roadmap so the list reads as done.

**C2. The MCP-server role-label decision is unrecorded.** The 2026-06-09 review said to register the agentic role-label set before any page uses it. MCP now appears in the orchestration layer, the glossary, and the OpenCode card, but the naming registry records no decision on whether `MCP server:` becomes a sidebar role or stays prose-only inside Orchestration. No page breaches the gate yet; one registry line closes it pre-emptively.

**C3. The annex v2 change file has no owner or decision route.** `internal/annex-v2-proposed-changes.md` collects the v2 highlighted changes "for COL review" with no named reviewer, date, or record of what happens on acceptance (which appendices, if any, flow back into the public reference page). As the v2 draft evolves at COL, this file silently stales. Add an owner line and a review-by date, or fold it into the next increment's plan.

**C4. Repository hygiene.** `internal/tools/__pycache__/editorial_audit.cpython-310.pyc` is tracked and `.gitignore` has no `__pycache__/` entry, so the binary will churn with every Python version change. `internal/superpowers/` (a 2026-06-06 spec and plan pair) is superseded by the editor workflow it designed; mark it historical or move it under a dated archive heading. Tracked `.DS_Store` files remain by standing decision.

## Suggested order

1. Same-day fixes, no content risk: A1 exemplar repointing · A2 label sync · A4 record correction and workflow stub-type cut · C2 registry line · C4 pycache ignore.
2. One-time checks: B5 published-endpoint verification · C3 owner line on the annex file.
3. Onboarding: A3 handoff refresh (worth doing before any new increment, so the next session starts from a true picture).
4. Next build increment (plan-008): B1 administrative-agent guide, with the B2 coding-agent runbook alongside it (the guide will recommend repeated team use, which is the runbook gate).
5. Following increment: B3 pilot serving guide + curriculum advisor advanced cell, with the B4 SGLang decision and the remaining B2 runbooks (Dify, serving engines) inside it.

The pattern across A1 to A4 is the one structural weakness this review found: the public docs have an audit that keeps them consistent, but the internal machinery that produces them has no equivalent check, so renames and moves land in the registry and the audit yet miss the workflow, the templates, and the handoff. Extending the audit's link checker to resolve `docs/` paths referenced from `internal/` files would catch most of this class automatically.
