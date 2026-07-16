---
title: "Increment 7 — Audit Remediation: Example-Audit Fixes and Annex-Grounded Improvements"
type: feat
status: draft
date: 2026-07-15
origin: internal/example-audit-2026-07-15.md + internal/annex-grounded-review-2026-07-15.md
---

# Increment 7 — Audit Remediation: Example-Audit Fixes and Annex-Grounded Improvements

## Overview

Two audits run on 2026-07-15 converge on a single remediation increment. The **example audit** (`internal/example-audit-2026-07-15.md`) built the guides end to end and surfaced three reader-blocking defects — a host `pip install` that fails on the KB's own baseline platform (EX-gateway-install), a math-tutor SymPy tool that silently returns a truthy value for prose instead of erroring (EX-math-silent-true), and a gateway audit log that does not persist or show the masked form the assessor is told to review (EX-gateway-audit-log) — plus audience-discoverability gaps (the governance third step and the IT-deployer path are present but never linked), a cluster of build-guide consistency slips, and one resolved open item: the running stack was measured at ~9.3 GB, confirming the guide's "about 9 GB" and closing the KB's "memory pending local measurement" hedge. The **annex-grounded review** (`internal/annex-grounded-review-2026-07-15.md`) checked the KB against COL's authoritative reference architecture and produced eighteen KB-page improvements (K1–K18) plus twelve agentic-era annex proposals (A1–A12). The plan's shape: **priority-ordered workstreams** (P0 reader-blockers first, then P1 governance-and-audience, then P2 depth-and-consistency, then P3 internal collection), each independently committable, grouped so each public page is edited by a single workstream; the **twelve annex proposals are collected in an internal COL-review artefact, never applied to the public reference page**, following the `internal/annex-v2-proposed-changes.md` routing convention; and a **decisions-for-user list** resolved before the gated work begins.

## Decisions to make first

Each decision below gates one or more workstreams; resolve them before the gated iteration begins. Recorded declines are restated so adjacent work is not misread as reopening them.

- **D2 — Reorder the Build-further tier so AI gateway precedes Curriculum advisor.**
  - *Why:* gateway-first lets the Dify curriculum advisor connect through the sovereignty boundary from birth, closing finding **C1** (Dify's direct-to-Ollama bypass against the "every model request passes through it" claim) structurally rather than with a two-sentence textual patch. Touches only `README.md` wording and intra-tier `SUMMARY.md` order; the math tutor's Next step already points at the gateway. Not itself a recorded decision, but the user's call.
  - *Recommendation:* adopt the reorder — low risk, and the clean fix for C1; otherwise WS3 falls back to the textual reconciliation.
  - *Blocks:* WS3 (C1 structural close vs textual fallback).

- **D4 — Canonical time figure: quickstart 45 min (inclusive) vs README "75 min across both guides" (additive, double-counts the embedded chat build). Exactly one should change.**
  - *Why:* the two figures are inconsistent and one mis-sums the chat build already embedded in the math-tutor timing.
  - *Recommendation:* keep the quickstart 45-minute inclusive figure and reword README so it stops double-counting the embedded chat build.
  - *Blocks:* WS5 (EX-quickstart-time — which figure changes).

- **D3 — Add a dedicated "Operate it" landing row, or extend the existing institution row for IT deployers?**
  - *Why:* the "Operate it" row was deliberately removed on 2026-07-10; AUD-itdeployer-chain restores IT-deployer discoverability. It can either revive that removed row or extend the "Assess it for an institution" row to pilot → operations-overview → chat service + runbook.
  - *Recommendation:* extend the existing institution row (avoids re-litigating the 2026-07-10 removal). Add a dedicated "Operate it" row only if the user explicitly prefers it.
  - *Blocks:* WS5 (AUD-itdeployer-chain shape).

- **D6 — Amend plan-008: sequence the administrative agent before Manim (vs the draft's "after") and add an Appendix A Tier 2 cross-reference.**
  - *Why:* the admin agent is fully local and serves the deployer and governance audiences; sequencing it before Manim lets the fully-local Advanced path complete before the one example that needs reader-supplied cloud burst. Amends the plan-008 draft tracked in CLAUDE.md.
  - *Recommendation:* adopt both amendments; record them in the plan-008 draft, not as new scope here.
  - *Blocks:* the deferred plan-008 sequencing (BL-plan008-admin-agent), not any active work in this plan.

- **D5 — Add "Level: beginner." to the Quickstart page.**
  - *Why:* the Quickstart carries no Level label; the audit exempts it by filename, so this is a one-word conformance call, not a fix.
  - *Recommendation:* add it for conformance with the other guides — harmless and consistent. Low priority.
  - *Blocks:* nothing (standalone conformance; fold into WS5 alongside the README edits if adopted).

- **D1 — End-user / educator scope: serve the teacher-as-reader?**
  - *Why:* the only in-scope bridge today is the math-tutor browser-only sentence; anything more (an educator routing row or an educator-facing AI-literacy guide) reopens the educator routing row declined 2026-06-09. The sanctioned vehicle (AI-literacy guide) is deferred and needs an explicit scope decision.
  - *Recommendation:* keep the educator row declined for this remediation round; add only the in-scope math-tutor browser-only sentence. Route any educator-facing guide to a separate, explicitly-scoped plan — do not fold it into this remediation.
  - *Blocks:* nothing active (the vehicle is deferred); surfaced as a scope decision only.

- **D7 — Annex-feedback owner line: assign a COL owner for the internal annex-proposal collections (v2 and the new v3).**
  - *Why:* `gap-review-2026-06-12` C3 flagged that the internal annex-proposal collections have no named owner line for the COL hand-back; WS15 creates a second such collection (annex-v3), widening the gap.
  - *Recommendation:* name a COL owner and add the owner line to both `internal/annex-v2-proposed-changes.md` and the new `internal/annex-v3-agentic-proposed-changes.md` when WS15 scaffolds it.
  - *Blocks:* WS15 hand-off completeness (not the edits themselves).

- **Declined decisions — restate the boundary; do not schedule (DEC-declined-revisit).**
  - The educator routing row (declined 2026-06-09), re-publishing the internal principles page, the "Operate it" landing row (deliberately removed 2026-07-10), and standalone values pages are all user decisions. Adjacent work exists — K10's infrastructure-resilience half is distinct from the declined Infrastructure build-order note; an educator AI-literacy guide would revive the declined educator row — so the boundary is stated, not assumed. Leave all four declined for this plan; any reversal needs an explicit user scope decision.

## Workstreams

Fifteen workstreams, priority-ordered P0 → P3. Each is independently committable; files touched by more than one workstream carry a sequence note. Every actionable bullet traces to a finding id from the two audits. `verified_mode` is flagged where it matters — real execution (the guide was built and the defect reproduced or the value measured), dry-run (walked but not executed live), analysis (reasoned from the text), or a hybrid where analysis is anchored by a live check.

### WS1 — Gateway envelope: build-guide blockers + governance depth (P0)

*Targets:* `docs/getting-started/ai-gateway.md`, `docs/concepts/gateway-layer.md`, `docs/operations/open-webui-ops.md`, `docs/reference/glossary.md`, `docs/getting-started/manim-animator.md`.

Both audit runs converge on the gateway — the path flagged weakest in the stakeholder review. Merged into one workstream so `ai-gateway.md` and `gateway-layer.md` are each edited once (file cohesion). **Sequence EX-gateway-audit-log first** — it is a stated precondition for AUD-governance-appendixA in WS5 (the log is the assessor's evidence).

- **EX-gateway-audit-log** (P0, real-execution): document a logging config (or `--detailed_debug`) so the gateway audit log the assessor is told to review actually persists and shows the masked form — readiness currently reports "db: Not connected", the default log carries only HTTP status lines, and the masked form appears only with the undocumented `--detailed_debug`. Edit `ai-gateway.md` (lines 8, 148, 159, 173). Honesty precondition for the governance routing path. **Medium severity, M effort.**
- **EX-gateway-install** (P0, real-execution): add venv + interpreter-version guidance for `pip install 'litellm[proxy]'` — on the KB's Homebrew-Python baseline `pip` is not on PATH, `pip3` fails PEP 668, a Python 3.14 venv fails on orjson/pyo3, and only an explicit Python 3.13 venv worked. Edit `ai-gateway.md:60` and, folding cross-cutting finding **C3** (the same host `pip install` pattern recurs on the KB's baseline), `manim-animator.md:47`. **High severity, M effort.** (The `manim-animator.md:47` edit is why WS7 sequences after this workstream.)
- **EX-gateway-presidio** (P2, real-execution): repoint the guide at the maintained Presidio images (`ghcr.io/data-privacy-stack/*`); `mcr.microsoft.com/presidio-*` still pull but are declared end-of-life upstream. Edit `ai-gateway.md`. **Medium severity, S effort.**
- **K1** (P1, adjusted): reword the stale token-sovereignty / personal-data-leakage indicator citation in four places — `gateway-layer.md:19`, `gateway-layer.md:49`, `glossary.md:230`, and the standalone Token sovereignty entry `glossary.md:356-358` — to the annex's actual hooks (tamper-evident audit logging for regulatory review and individual redress; the cloud-burst frequency indicator). Keep the term and definition; reattribute only the sentence. The phrase survives from the pre-rebuild bridge (commit 9d62323). **High severity, S effort.** Coordinate the `glossary.md` edit with WS14 (K17).
- **K4** (P1, confirmed): add retention, secure deletion, log access and redress across the gateway pages — a Governance-and-review bullet in `ai-gateway.md` (define a retention period, delete on schedule, restrict who reads the log), an assessment-table row or trade-offs bullet on `gateway-layer.md` (retention, secure deletion, tamper-evident logs as the basis for individual redress, linking the reference page), and a matching retention line in `open-webui-ops.md`'s gateway section. Closes the Appendix A retention gap on the ministry routing path. **High severity, M effort.** Coordinate the `open-webui-ops.md` edit with WS6 (EX-coding-key-plaintext).
- **K7** (P1, adjusted): add cloud-burst preconditions at concept level on `gateway-layer.md` — (a) one sentence that burst changes where processing happens, not the oversight the output needs (learner-intended output stays Tier 1 whichever route produced it); (b) extend the Frugal-practice line (`:70`) with the annex ordering scoped to deployments beyond development (the dev build deliberately does not meet the baseline per the glossary MGB entry). **Medium severity, S effort.**
- **K8** (P1, confirmed): add the envelope's contractual-controls half to `gateway-layer.md` — one sentence noting §4.4 specifies minimum contractual controls for any approved provider (retention/deletion commitments, breach notification, audit rights, sub-processor disclosure) that sit in the provider agreement, not the configuration. Prevents a ministry reader concluding the envelope is fully satisfied by software. **Medium severity, S effort.**

*Sequence notes:* run `editorial_audit.py` after the commit (Port Allocations, role labels, the five layer sections). `gateway-layer.md` also receives an anchor-link edit in WS5 — fold that edit here or sequence WS5 strictly after this workstream.

### WS2 — Math-tutor SymPy silent-true guard (P0)

*Targets:* `docs/getting-started/math-tutor.md`.

Reader-blocking correctness defect verified by real execution: `sympify('this is not math')` returns `True`, contradicting the guide's "returns an error" claim and a Verify-row prose string that itself errors. A learner-facing Tier 1 tool that silently returns a truthy value is governance-material, not cosmetic. Both items edit one file, so they land in one commit.

- **EX-math-silent-true** (P0, real-execution): guard the SymPy tool against prose parsing to a Python boolean/value, and reword the Verify row so the model prose → SymPy translation is explicit (the folded §1 Verify-row reword). Reconfirmed in a fresh venv. **High severity, S effort.**
- **EX-math-pip-network** (P0 workstream, real-execution): flag that the tool `pip install` needs network, on an otherwise offline-framed guide. **Low severity, S effort.**

*Sequence note:* `math-tutor.md` also receives the shared Tier-1-procedural-gate sentence in WS13 (K12) — coordinate so the Governance-and-review section is edited once, or sequence WS13 last.

### WS3 — Stack-fits governance scoping (two homes) + Dify-bypass reconciliation (P0)

*Targets:* `docs/concepts/how-the-stack-fits-together.md`, `docs/getting-started/curriculum-advisor.md`, `docs/getting-started/ai-gateway.md`.

Both runs touch the page that states the sovereignty invariant; merged so it is reconciled in one pass. Governance-critical.

- **K2** (P0, confirmed): scope `how-the-stack-fits-together.md:43`'s unscoped "governance has one architectural home" sentence to model egress, and add one clause mirroring `README.md:34` (the loop as second home; tool/MCP egress does not pass the gateway), linking the application layer's three governance surfaces. The scoped "one home" phrasings on `gateway-layer.md` and the LiteLLM card are a recorded keep-decision and stay untouched. **High severity, S effort.** No dependency; can proceed.
- **C1** (P0, analysis): reconcile Dify's direct Ollama connection (bypassing the envelope) against the "every model request passes through it" claim in the accumulated stack. Open WebUI is re-pointed through LiteLLM (`ai-gateway.md:83`) but Dify keeps its direct Ollama connection (`curriculum-advisor.md:42`) against `how-the-stack-fits-together.md:41`. **Structural close depends on D2** (gateway-before-curriculum reorder, so Dify connects through the boundary from birth); if D2 is declined, apply the two-sentence textual fallback instead. **Medium severity, M effort.** C1 also edits `curriculum-advisor.md` and `ai-gateway.md` — coordinate with WS10 and WS1.

### WS4 — Annex adaptation §7/§8 table repair (source-verify first) (P1)

*Targets:* `docs/reference/sovereign-education-ai-reference-architecture.md`.

- **K3** (P1, analysis with verify-against-source caveat): three table-dislocation defects on the authoritative annex adaptation since the rebuild commit (6602229) — a Safety & Trust row (`:313`) in the wrong §7 table, "Quarterly" stranded in an OECD column of the Scale row (`:312`), and a reporting-definitions block (`:301-304`) misplaced between the two §7 tables. **Re-obtain the v2 working-draft source first** (`uploads/` is no longer local; the published v1 PDF is a secondary check). **Only if the source is clean** (i.e. a conversion artefact) repair in one pass: move the Safety & Trust row and the reporting-definitions block to §8, recover the genuine OECD cells. **If the source itself carries the defects, do not edit the page** — record the discrepancy for COL in the WS15 annex-feedback collection. This is the one reference-page content edit permitted here because it restores fidelity to source, not an annex change. **High severity, M effort.**

### WS5 — Landing/README routing + time reconciliation (P1)

*Targets:* `docs/README.md`, `docs/reference/sovereign-education-ai-reference-architecture.md`, `docs/concepts/gateway-layer.md`, `docs/components/environments/pilot.md`, `docs/operations/operations-overview.md`.

Grouped because all three routing items edit `docs/README.md` — the landing table is edited once.

- **AUD-governance-appendixA** (P1, analysis): add the missing governance third step by anchor-linking the in-page Appendix A self-assessment checklist (reference page lines 365–411) from the routing row and the `gateway-layer.md` "what is recorded" table. This is **KB-authored navigation on the reference page, NOT an annex content edit**, and it corrects the "checklist is only in the external PDF" misread. **Depends on WS1 (EX-gateway-audit-log)** — the honest log is the assessor's evidence — and its `gateway-layer.md` anchor overlaps WS1's edits (fold into WS1's commit or sequence after WS1). **Medium severity, M effort.**
- **AUD-itdeployer-chain** (P1, analysis): give the under-served IT deployer an entry path by extending the existing "Assess it for an institution" row to `pilot.md` → `operations-overview.md` → chat service + its runbook (the one fully-runbooked unit). Destination pages are good but form no discoverable entry path. **Gated by D3** (extend the institution row vs a dedicated "Operate it" row). Its `pilot.md`/`operations-overview.md` edits overlap WS8 — sequence adjacently. **Medium severity, M effort.**
- **EX-quickstart-time** (P1 workstream, analysis): fix the 45-vs-75-minute double-count on `README.md`. **Gated by D4** (which figure changes). **Medium severity, S effort.**
- *(If D5 adopted:)* add "Level: beginner." to the Quickstart page in the same commit.

*Sequence note:* run `editorial_audit.py` from repo root **and** from inside `docs/`.

### WS6 — Coding-agent correctness and secret-handling (P1)

*Targets:* `docs/getting-started/coding-agent.md`, `docs/operations/open-webui-ops.md`.

All three items edit `coding-agent.md` (one commit).

- **EX-coding-key-plaintext** (P1, real-execution): move the gateway master key out of plaintext `opencode.json` to `{env:VAR}` / host environment — OpenCode supports it and the ops guidance already requires keys in host env (`coding-agent.md:85` vs `open-webui-ops.md:130`). Also edits `open-webui-ops.md` — coordinate with WS1 (K4). **Medium severity, S effort.**
- **EX-coding-node-prereq** (P1, analysis): add Node.js/npm to the coding-agent prerequisites — never a stated prerequisite anywhere in the chain. **Low severity, S effort.**
- **EX-coding-tavily-env** (P1, real-execution): note that a global user config can inject network-capable MCP tools (Tavily MCP + Google AI Search) into a fresh run, contradicting the guide's "adds no tools" claim — environmental, not a KB defect, but material to the tool-egress governance surface. **Low severity, S effort.**

### WS7 — Manim capstone fixes (P1)

*Targets:* `docs/getting-started/manim-animator.md`, `docs/getting-started/ai-gateway.md`.

Both edit `manim-animator.md`. **Sequence after WS1** — EX-gateway-install also edits `manim-animator.md:47` and C2 also touches `ai-gateway.md`; land the gateway edits first to avoid a rebase.

- **EX-manim-squarearea** (P1, analysis): rename `SquareArea` or reword the concept — it reads as "area of a square", not "area under y=x²". **Low severity, S effort.**
- **C2** (P1, analysis + real-execution live-check): state plainly that the capstone's cloud-burst model is reader-supplied (external provider + `CLOUD_BURST_KEY`, no documented acquisition path) — the only example that cannot complete fully locally. The live-built gateway exposes only `gemma4-dev` (live check, audit line 35), so the reader-supplied burst model is not routable from the guide as written (`manim-animator.md:30` → `ai-gateway.md:126,133-138`). **Medium severity, S effort.**

*Sequence note:* WS13's shared K12 sentence lands last on this page.

### WS8 — Operations and pilot annex gaps (P1)

*Targets:* `docs/operations/operations-overview.md`, `docs/components/environments/pilot.md`.

Annex governance-depth additions on the deployer path. Grouped by the two shared files. **Sequence WS8 and WS5's pilot/ops edits adjacently** (AUD-itdeployer-chain routes to both).

- **K5** (P1, adjusted): add a "What to measure" section mapping annex §8 frugal-performance indicators to where observed — latency from service monitoring, offline availability from health checks with connectivity removed, cloud-burst frequency from the gateway audit log — **noting the audit log also records redactions but redaction counts are NOT an §8 indicator**. State remaining §8 domains (teacher uptake/oversight, language coverage, scale readiness) belong to pilot design; restate the telemetry rule faithfully (collect minimum, aggregate, suppress small cohorts, never learner free text). Link `pilot.md:29` success-criteria to the reference page §8 as the starting set. Edits `operations-overview.md` and `pilot.md`. **High severity, M effort.**
- **K6** (P1, adjusted): add a Security row to the pilot Governance-and-operations table — account-level access control with MFA for admin accounts where the interface supports it, encryption in transit beyond localhost, an OS/container patching cadence, documented incident-response procedures. **Reword only the two security items in "What changes before production"** as formal review and hardening of a baseline already present at pilot; **leave the service-monitoring deferral as-is** (a genuine Layer H item). Edits `pilot.md`. **High severity, M effort.**
- **K14** (P1, confirmed): extend the operations runbook gate with three Layer H items — the incident path (detection, triage, remediation, reporting); how audit records are reviewed and reported to the service owner; the model tags, profiles (e.g. `gemma4-dev`) and configuration versions in use, with where changes are recorded. Extends the existing instrument; writes no new runbooks. Edits `operations-overview.md`. **Medium severity, S effort.**
- **K15** (P1, adjusted): add a pilot hosting-topology sentence — pilot design documentation should record which annex topology it approximates (the documented single-node shared pilot most closely approximates topology B; the frugal-floor local build is the shape of topology C), records rather than prescribes. Edits `pilot.md`. **Medium severity, S effort.**

### WS9 — Chat-service guide + Ollama card + gemma card consistency (P2)

*Targets:* `docs/getting-started/offline-chat-service.md`, `docs/components/runtimes/ollama.md`, `docs/components/models/gemma-4-12b.md`.

Frugal-floor cluster; `ollama.md` (touched by C4 and EX-chat-comfortable) lands in one commit. The gemma-4-12b card is touched only by this workstream (EX-memory-measured and EX-chat-comfortable), so its edits land here too.

- **K13** (P2, confirmed): add a synthetic-content note next to the localhost note (`:97`) or in the opening hint — this development build has no redaction layer, so test with synthetic or de-identified content and keep personal data out of prompts; the AI gateway guide adds the redaction airlock. Edits `offline-chat-service.md`. **Medium severity, S effort.**
- **EX-memory-measured** (P2, real-execution): update the expected memory labels to the measured figure — the example build measured the running stack at **~9.3 GB (Ollama 8.4 GB + Open WebUI 934 MiB)**, confirming the guide's "about 9 GB" and **closing the CLAUDE.md-tracked "memory pending local measurement" open item**. Reword the "Memory remains comfortable" row (`offline-chat-service.md:131`) and the expected-values caveat (`:134`), and the gemma-4-12b card's Local-fit line (`gemma-4-12b.md:17`), to state the measured stack use with its Ollama + Open WebUI breakdown (measured 2026-07-15), dropping the "expected/pending"/"to be checked on the machine" hedge. Edits `offline-chat-service.md` and `gemma-4-12b.md`. **Low severity, S effort.**
- **EX-gemma-tag-caution** (P2, real-execution): warn that a bare `gemma4` / `gemma4:latest` (8B) is a different, smaller model than the pinned `gemma4:12b` — the KB pin is correct. Edits `offline-chat-service.md`. **Low severity, S effort.**
- **EX-chat-comfortable** (P2, analysis): reconcile the guide's "comfortable development setup" wording with the Mac-mini card's 12B/8K "Usually fine" rating. Edits `offline-chat-service.md` and `ollama.md`. **Low severity, S effort.**
- **C4** (P2, analysis): unify `registry.ollama.com` → `ollama.com` on the Ollama card (`ollama.md:63`) — a consistency slip against a recorded decision to unify on `ollama.com`. **Low severity, S effort.**

*Sequence note:* the EX-memory-measured card edit is the plan's only model-card edit; keep the gemma card's external `_Sources checked:_` line as-is (external sources are not re-verified) and state the measured value inline as "measured 2026-07-15" — see Audit coupling.

### WS10 — Curriculum-advisor rewrite + citation display (P2)

*Targets:* `docs/getting-started/curriculum-advisor.md`, `docs/concepts/orchestration-layer.md`.

The six example items constitute the §4 curriculum-advisor rewrite; all guide edits land in one `curriculum-advisor.md` commit. **All six example items are dry-run only** (that example was never executed live) — verify against a live Dify build before publishing if possible.

- **EX-curriculum-prereq-link** (P2, dry-run): link the prerequisite floor guide (restores the sibling pattern the math tutor sets). **Medium severity, S effort.**
- **EX-curriculum-llm-name** (P2, dry-run): name the answering LLM (currently never named). **Low severity, S effort.**
- **EX-curriculum-embedding-pull** (P2, dry-run): promote the embedding-model `ollama pull` from Troubleshooting into the numbered steps. **Medium severity, S effort.**
- **EX-curriculum-env-step** (P2, dry-run): add the omitted `.env` copy step to the "in short" Dify summary. **Low severity, S effort.**
- **EX-curriculum-dify-swap** (P2, dry-run): declare the Application-layer swap (Open WebUI → Dify chat app); the guide currently claims only Orchestration substitutability. **Low severity, S effort.**
- **EX-curriculum-memory** (P2, dry-run): quantify memory demand against the 24 GB baseline (currently unquantified). **Low severity, S effort.**
- **K11** (P2, confirmed): enable citation display — add the citation/attribution setting to step 4, a Verify row ("Sources shown — an answer displays which approved document it drew from"), and one clause on `orchestration-layer.md` (`:17` or the tools table `:60`): retrieved answers cite their sources so a reviewer can check them. The review step already assumes citations exist (`:94`). **Medium severity, S effort.**

*Sequence note:* `curriculum-advisor.md` is also touched by WS3 (C1) and WS13 (K12) — coordinate the Governance-and-review and Dify-connection edits; sequence WS13 last.

### WS11 — Example-applications tier lens + prerequisite chain (P2)

*Targets:* `docs/concepts/example-applications.md`.

Both edit one page; one commit. Keeps plan-008's "Tier 2 only" scope intact.

- **K9** (P2, adjusted): add one tier-lens sentence after `:28` — learner-facing cells sit in Tier 1; the administrative row is where lower tiers apply (Tier 2 for staff-only drafts with post-hoc audit and publish-controls, Tier 3 only for purely administrative output automated with logging). **Do NOT describe Tier 2 as automation** (the annex reserves automated release for Tier 3). Add the reference page to Related pages. **Medium severity, S effort.**
- **EX-matrix-prereq-chain** (P2, analysis): add a prerequisite-chain sentence to the matrix. **Low severity, S effort.**

### WS12 — Infrastructure and inference annex depth (P2)

*Targets:* `docs/concepts/infrastructure-layer.md`, `docs/concepts/inference-layer.md`.

Two concept-page annex-grounding additions; both add the reference page to Related pages. K10 is distinct from the declined 2026-06-09 Infrastructure build-order note (see Declined decisions).

- **K10** (P2, adjusted): add the missing Layer G resilience half to `infrastructure-layer.md` — a short further-work paragraph on offline-first service levels, store-and-forward synchronisation (glossary link — currently zero inbound references), and edge/hub topologies for multi-site builds; the documented single-machine path is inherently offline, multi-node paths are not documented yet. **Medium severity, S effort.**
- **K16** (P2, adjusted): add model-selection due-diligence to `inference-layer.md` — (a) a fifth shared caution in the existing "Not for …" style (not for a given language or curriculum on source-listed language counts alone; counts indicate coverage, not quality; evaluate on local-language and curriculum samples during piloting); (b) one sentence in "Choose a model" after `:43` (for public deployments the reference architecture, linked, adds licensing checks, security due diligence, and evaluation against local requirements). **No bare annex section-number citations on public pages**; leaves the comparison-tool further-work line untouched; no card edits. **Medium severity, S effort.**

### WS13 — Tier 1 procedural-gate note across the three learner-facing guides (P2)

*Targets:* `docs/getting-started/math-tutor.md`, `docs/getting-started/curriculum-advisor.md`, `docs/getting-started/manim-animator.md`.

- **K12** (P2, adjusted): add one shared sentence to each Governance-and-review section — in this development path the Tier 1 approval gate is procedural (the teacher operates the single-user interface, learners have no direct access), whereas the reference architecture expects a technically enforced gate before any learner-facing pilot (further work). **Use the annex term "approval gate", NOT "publish-control"** (the annex reserves publish-control for Tier 2 export prevention). **Medium severity, S effort.**

*Sequence note:* **sequence AFTER WS2 (math-tutor), WS7 (manim) and WS10 (curriculum-advisor)** so the shared sentence is the last, coordinated touch on each Governance-and-review section.

### WS14 — Glossary entries + production interoperability item (P2)

*Targets:* `docs/reference/glossary.md`, `docs/components/environments/production.md`.

- **K17** (P2, confirmed): add four glossary entries the page promises as "the single source" but lacks, following the bare-acronym-headword convention — Data residency (Sovereignty-and-governance group, immediately before Data sovereignty, cross-referenced); EMIS ("Education Management Information System:"); OER ("Open Educational Resources:"); Open-weight model (models group; weights published for download and local hosting, licence terms still vary). **The 2026-07-10 "Open weights → Openness" hexagon rename does NOT apply to the technical term "Open-weight model".** Edits `glossary.md`. **Medium severity, S effort.** Coordinate with WS1 (K1 token-sovereignty reattribution) so the two glossary edits do not conflict.
- **K18** (P2, confirmed): add one Interoperability item to the production readiness checklist naming the procurement-relevant behaviours — SSO/role integration, export/import of approved content artefacts, machine-readable audit-log export for oversight, LMS/EMIS integration that does not ingest unnecessary learner records — linking the reference page, none yet documented as a build path (further-work idiom). Edits `production.md`. **Medium severity, S effort.**

### WS15 — Internal annex-v3 agentic proposal collection (COL review, internal-only) (P3)

*Targets:* `internal/annex-v3-agentic-proposed-changes.md` (new), `docs/reference/sovereign-education-ai-reference-architecture.md` (A1 crosswalk row ONLY).

The twelve agentic annex proposals (A1–A12) are KB-originated **input to a future annex v3**, collected for COL review per the `internal/annex-v2-proposed-changes.md` routing convention — **NEVER applied to the public reference page.** The single public exception is A1's KB-authored crosswalk-row extension (legitimate KB commentary, not annex content). Kept separate from the pending v2 set; reconcile A8 with v2 Appendix E and A12 with v2 Appendix G only if COL accepts v2 first. Do NOT cite `internal/frugal-ai-principles.md` publicly (informs A4/A11 argument only). **Order: scaffold first; then A1 (defines the terms all others use); then A2, A3, A5, A4, A6, A7, A10, A11, A12; then A8 and A9 last** (they audit the A2+A3+A5 control set and carry a no-independent-adversarial-pass verification caveat).

- **EX-annex-v3-artefact**: scaffold `internal/annex-v3-agentic-proposed-changes.md` with the routing rule (collected for COL, never applied to the page), the v2-guardrail preservation note (teacher approval unchanged/strengthened; cloud burst non-default; no high-stakes automated decisions), the interdependency map, and the D7 annex-feedback owner line.
- **A1** — agents as a Layer C subtype (Application Services that take multi-step actions), scope-note clarification, and annex glossary terms; the one public exception is extending the "Application Services | Application layer" crosswalk row on the reference page.
- **A2** — the second tool/MCP egress surface (governed at Layer C, not Layer E; §5.3 and §4.4 qualified).
- **A3** — risk-tier oversight extended from outputs to actions (per-action approval, plan-only mode, scoped directory).
- **A4** — the sovereign agent loop (harness under national/institutional control; procurement questions in §3.1 and Appendix A, not §1).
- **A5** — agent memory as a named retention surface (what/where/how long/who reviews).
- **A6** — written skills as a third versioned artefact class (registered in Layer H, tied to §5.1's Tier 2 feedback loop).
- **A7** — staged Tier 1 review as an optional pattern (storyboard-first + release checklist; strengthens approval-before-release).
- **A8** — Layer H components and §8 indicators for agentic use (agent-oversight domain; agent action logs and tool/MCP registry). *No independent adversarial pass.*
- **A9** — an Appendix A "Agentic use (if agents are deployed)" subsection. *No independent adversarial pass.*
- **A10** — governed coding agents as a §6.1 capacity mitigation (controls stated directly, not by reference).
- **A11** — agentic workloads strengthen the annex local-default case (§4.2 token-cost paragraph; §4.4 per-step burst corollary).
- **A12** — agent harnesses as a sixth §4.3 open-source category (exercised by OpenCode; verified for Tau and Pi).

*Audit coupling:* WS15 touches only one public line (A1's crosswalk row), so its audit coupling is limited to that edit.

## Governance

No change in this plan weakens teacher approval or the tier model; several strengthen the governance case that the stakeholder review flagged as the weakest path.

- **Audit-log honesty gates the ministry assessment path.** EX-gateway-audit-log (WS1) is scheduled first because AUD-governance-appendixA (WS5) points the assessor at a log that must actually persist and show the masked form. K4 (WS1) adds the retention/deletion/redress the annex requires around that log; K5 and K14 (WS8) make it reviewable and reportable.
- **Tier vocabulary is preserved exactly.** K9 (WS11), K12 (WS13) and A3/A7 (WS15) use the annex's Tier 1/2/3 vocabulary and the term "approval gate"; Tier 2 is never described as automation (the annex reserves automated release for Tier 3), and "publish-control" is not used for the Tier 1 gate.
- **The three governance surfaces stay intact.** K2 (WS3) and A1/A2 (WS15) keep local actions / model egress via the gateway / tool-MCP egress (which does not pass the gateway) as the framing; K8 (WS1) adds the contractual half of the envelope so a ministry reader does not conclude software alone satisfies it.
- **The tier model is not weakened.** K12 states plainly that this development path's Tier 1 gate is procedural and a technically enforced gate is further work before any learner-facing pilot; the v2-guardrail note in WS15 records that the agentic proposals do not weaken approval-before-learner-release.

## Audit coupling

`internal/tools/editorial_audit.py` must pass **from the repo root AND from inside `docs/`**, plus `git diff --check`, before each commit.

- **New pages / SUMMARY:** this plan creates no new public page, so no new `SUMMARY.md` entries are required (the only new file is the internal `annex-v3` collection, which lives outside `docs/` and is unlinked from public navigation).
- **Guide-hint / Level / layer-tag checks:** apply automatically to every guide edited (WS2, WS6, WS7, WS9, WS10, WS13). If D5 is adopted, the Quickstart Level label is added under the audit's filename exemption — a conformance addition, not a requirement.
- **Port Allocations:** WS1 introduces no new host port (Presidio and LiteLLM ports are already registered); if any edit changes a `-p` binding, register it in the naming registry.
- **Model-card Sources-checked line:** WS9 makes the plan's only model-card edit — updating the gemma-4-12b card's memory figure to the measured value (EX-memory-measured), stated inline as "measured 2026-07-15". The card's external `_Sources checked:_` line is left unchanged (external source values were not re-verified), so the regex-enforced `_Sources checked: YYYY-MM-DD._` line still parses. WS12's K16 deep-links the shared cautions rather than editing cards.
- **Role labels / five layer sections / glossary grouping:** WS14's glossary additions must respect the four theme-group headings and bare-acronym-headword convention; WS1/WS3 must keep the approved role-label prefixes and the five layer sections.

## Minimum vs Deferred

**Minimum viable remediation:** the three P0 reader-blockers (WS1 EX-gateway-audit-log + EX-gateway-install, WS2 EX-math-silent-true, WS3 K2/C1), the P1 governance-and-audience set (WS1 K4/K7/K8, WS4 K3 if source is clean, WS5 routing, WS6 coding-agent, WS7 manim, WS8 ops/pilot), and the internal annex-v3 scaffold with at least A1's term definitions (WS15). These restore correctness, honesty, and discoverability and bring the gateway/ministry path to the standard the annex demands.

**Deferred / further work (backlog references, not scheduled here):**

- **BL-plan008-admin-agent** — the Tier 2 administrative agent (Advanced; ships the coding-agent runbook; serves the deployer and governance audiences). Already tracked as plan-008 draft; the before-Manim sequencing and Appendix A Tier 2 cross-reference are gated by D6. Recommended before Manim so the fully-local Advanced path completes first.
- **BL-pilot-serving-guide** — the pilot serving guide (deployer track). Already deferred in CLAUDE.md; keep deferred-but-next (the priority after this remediation round).
- **Resolved by this plan (do NOT list as pending):** the Gemma 4 stack-memory measurement is no longer an open item — the example build measured it at ~9.3 GB (Ollama 8.4 GB + Open WebUI 934 MiB), confirming "about 9 GB"; the KB label update is scheduled as EX-memory-measured (WS9), so it is removed from the tracked-backlog list below.
- **Dropped after verification (record only, do not re-raise):** DEF-drop-mathtutor-freetext (Tier 1 classifies outputs not input provenance; the tutor is teacher-mediated with no learner-typed path; the annex lists complex maths as a burst task; the blocking safeguard already sits beside the example) and DEF-drop-teacher-hexagon (the reference page intentionally carries no hexagon embed per the user instruction of 2026-07-14 — do NOT re-embed `frugal-ai-hexagon-teacher-in-the-loop.svg` without user direction).
- **Deliberately unproposed:** DEF-unprop-dpi (glossary-only DPI coverage is proportionate until a DPI integration path exists; the annex marks DPI integration "where available") and DEF-unprop-annex-v2-metadata (the v2 metadata is itself a pending highlighted change awaiting COL review — do not bump).
- **Already-tracked backlog (DEF-tracked; do not duplicate as new work):** Dify + serving-engine runbooks, SGLang card, educator AI-literacy guide (needs an explicit user scope decision — see D1), the llms.txt/MCP endpoint check on the published domain, the interactive model-comparison tool (in development), the anchor-fragment audit check, the confidence-label audit check, the annex-v2 owner line (see D7), and the `/training/` and `/network/` dashboard attachment.

## Iterations

Ordered, independently committable — one commit per iteration; run `editorial_audit.py` (repo root **and** inside `docs/`) plus `git diff --check` each time. WS15's final iteration touches only one public line (A1 crosswalk).

1. **WS1 — Gateway envelope.** EX-gateway-audit-log first, then EX-gateway-install, EX-gateway-presidio, K1, K4, K7, K8. (Fold the WS5 `gateway-layer.md` anchor edit here or sequence WS5 after.)
2. **WS2 — Math-tutor SymPy guard.** EX-math-silent-true + EX-math-pip-network.
3. **WS3 — Stack-fits scoping + Dify reconciliation.** K2, then C1 (structural if D2 adopted, else textual fallback).
4. **WS4 — Annex §7/§8 table repair.** Source-verify first; repair only if the source is clean, else record for COL (feeds WS15).
5. **WS5 — Landing/README routing + time.** AUD-governance-appendixA (after WS1), AUD-itdeployer-chain (per D3), EX-quickstart-time (per D4), optional D5 Level label.
6. **WS6 — Coding-agent correctness and secrets.** EX-coding-key-plaintext, EX-coding-node-prereq, EX-coding-tavily-env.
7. **WS7 — Manim capstone.** EX-manim-squarearea, C2 (after WS1's manim/gateway edits).
8. **WS8 — Operations and pilot.** K5, K6, K14, K15 (adjacent to WS5's pilot/ops edits).
9. **WS9 — Chat-service + Ollama card + gemma card.** K13, EX-memory-measured, EX-gemma-tag-caution, EX-chat-comfortable, C4.
10. **WS10 — Curriculum-advisor rewrite + citations.** Six EX-curriculum items + K11.
11. **WS11 — Example-applications.** K9 + EX-matrix-prereq-chain.
12. **WS12 — Infrastructure and inference depth.** K10, K16.
13. **WS13 — Tier 1 procedural-gate note.** K12 across the three guides — last coordinated touch on each Governance-and-review section (after iterations 2, 7, 10).
14. **WS14 — Glossary + production checklist.** K17 (coordinate with WS1's glossary edit), K18.
15. **WS15 — Internal annex-v3 collection.** Scaffold (EX-annex-v3-artefact, incl. the D7 owner line), then A1 (+ its public crosswalk-row exception), then A2/A3/A5/A4/A6/A7/A10/A11/A12, then A8/A9 last. Fold in any K3 source-discrepancy record from iteration 4.
16. **Surface the decisions.** Present D1–D7 and the restated declines to the user; record the D6 amendments in the plan-008 draft; confirm the D7 owner line is added to both annex collections.

## Sources

- `internal/example-audit-2026-07-15.md` — end-to-end example build audit (three reader-blockers, audience-discoverability gaps, build-guide consistency slips, and the resolved ~9.3 GB stack-memory measurement; verified_mode preserved per finding).
- `internal/annex-grounded-review-2026-07-15.md` — KB checked against COL's reference architecture (K1–K18 KB improvements; A1–A12 agentic annex proposals; Part 4 dropped/unproposed/tracked).
