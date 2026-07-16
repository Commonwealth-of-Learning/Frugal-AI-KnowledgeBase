# Landing-page gap analysis and audience-flow recommendation — 2026-07-15

A review of `docs/README.md` against the concerns raised: weak agent coverage; skills and tool use; the agent loop/harness not explained or cited; the "governance has two homes" framing being clumsy; how the stack expands gracefully as models/frameworks/tools evolve; pilot/production not covered; and the target audience flow. Method: five parallel analysts (content coverage, governance framing, extensibility, environments, audience flow) → synthesis → an adversarial verification pass. The verifier's corrections are folded in below (it caught three overstated "gaps" that are already partly present, and one internal inconsistency). **Assessment only — no page was edited.**

## Decisions resolved (2026-07-15) and implemented

The user chose **audience-flow Option A** (four tracks, refine not cut) and the **place-led governance heading** ("Where governance lives: the gateway and the loop"). Implemented on the landing and supporting pages: the place-led governance reword with the **harness** named and linked (A1) and the "loop as well as the data" sentence dropped (B3); an environments-ladder paragraph linking development → pilot → production (D1/D2); the From-COL signpost distinguishing the in-KB reference architecture from COL's strategy/policy/news out-links (audience flow); a "How a component is swapped" section on the stack page plus a landing linking clause (C1/C2); the "Scope and next work" living-reference reframe (C3); and the cross-page "one home" scoping on `gateway-layer.md` and `litellm.md` (B2). Not changed: no skills block or Application-layer expansion on the landing (A3/A2, depth stays on concept pages); no educator/teacher routing row (declined 2026-06-09 reaffirmed). The Appendix A deep-link (P1 item 3) was left as the existing named mention rather than a guessed heading anchor, since the editorial audit does not validate URL fragments.

## Overview

The landing is well-developed and structurally sound; nothing needs restructuring. The real issues are **framing** (the governance section runs two counting systems — "two homes" vs "three surfaces" — in adjacent lines), **concept-coverage** (the harness is paraphrased but never named or linked; substitutability is asserted but the swap *mechanism* is never shown), **discoverability** (two of three environment pages are unreachable from the landing), and one open **positioning** decision (the target audience). Every fix is reassembly of claims already true elsewhere in the KB; none needs new doctrine.

---

## 1. Target audience flow (the lead decision)

The proposed model — *developers = focus; ministry/stakeholders = out to COL + the reference architecture; teachers/students = consumers* — is **directionally right and consistent with the recorded developer-first decision, but should be adopted as a refinement, not a literal cut.** Two corrections:

- **The reference architecture and its Appendix A ministry self-assessment checklist are IN the KB, not on COL's site.** So "direct the ministry out to COL" must be scoped to **strategy, policy, and news** (which the From-COL section already hands out, `README.md:81`). The **technical governance/assessment** path — the gateway assessment table (`gateway-layer.md:40-53`), "what the gateway does not govern" (`:36-38`), and the Appendix A checklist — is a genuine in-KB asset and must stay reachable. Cutting the ministry row would strand the reader whose instrument lives in-KB.
- **The 3-audience model silently omits the institution / IT-deployer track**, which the prior audience audit found distinct and under-served (`example-audit-2026-07-15.md`). It should stay a thin track, not fold into "developer."
- **Refinement to the "consumer" label:** the KB models the teacher as a **Tier 1 reviewer** inside developer-built products (`example-applications.md:30`, `orchestration-layer.md:48`), which is stronger and more accurate than "consumer" — a reviewer, not merely an end user. Still out of scope as a *direct KB reader*, so the declined educator row stands.

**Recommended flow (four tracks):**

| Audience | Treatment | Landing entry | Rationale |
|---|---|---|---|
| **Developer / IT operator building the stack** | Serve deeply (primary) | Six builder rows + the tier system | Matches developer-first (`README.md:2`); over-service here is accepted intent |
| **Ministry / policy** | Thin read-only entry **+ split hand-off** (keep the row) | "Assess it for a ministry" → gateway layer + **in-KB** reference architecture + Appendix A; strategy/policy/news → **out** via From-COL | The governance instrument is in-KB; only strategy/policy/news go to COL |
| **Institution / IT deployer** | Thin entry + hand-off (keep as a distinct track) | "Assess it for an institution" → pilot → operations → chat runbook | A genuine track the 3-audience model omits; pages are strong but were under-discovered |
| **Teacher / student** | Out of scope as a direct reader; present only as the in-product Tier 1 review gate | None | Reaffirms the declined 2026-06-09 educator row; the deferred AI-literacy guide is the sanctioned future vehicle |

**Landing implications:** keep all six developer rows; keep the ministry row but make the split hand-off explicit and **deep-link** the Appendix A mention it already carries (`README.md:41`); keep+extend the institution row to reach the chat-service runbook and production readiness; add a one-line signpost in From-COL distinguishing the out-destination (COL: strategy/policy/news) from the in-KB reference architecture (technical governance). Do **not** add an educator/teacher row.

**Options to choose between:** **A (recommended)** four tracks, refine-not-cut; **B** the literal 3-audience model (risks stranding the ministry reader and hiding the IT-deployer track); **C** developer-only (drop both assessment rows for a single "for ministries and institutions → COL + reference architecture" signpost; cleanest table but removes the only in-KB governance/IT paths and reopens the 2026-07-10 routing decisions).

---

## 2. Gap analysis

### A. Agent / skills / tools / loop coverage

- **A1 (medium) — "harness" is paraphrased but never named or linked (the stated complaint, confirmed).** `README.md:34` describes "the loop that runs an agent — assembling its context, calling its tools, keeping its memory" but never uses "harness" or links its definition. Canonical homes exist and are unlinked: `orchestration-layer.md:37-39` ("the loop is the agent's harness…") and `glossary.md:24` ("Agent loop (harness)"). **Fix:** name and cite once in the existing sentence (link the harness to the orchestration-layer section or the glossary entry — confirm the anchor resolves under the audit link checker first). Keep the depth (Pi, delegation capacity, memory governance) on orchestration-layer. Effort S.
- **A2 (low) — agent is glossed only in the governance section, after first appearing unglossed in the stack line** (`README.md:21`). Ordering polish only; one clear definition exists. Do not give the Application layer more landing real estate. Effort S.
- **A3 (low, do NOT fix on the landing) — "Skill" (written skills) and the component-card convention are absent from the landing.** The concept lives on application-layer, orchestration-layer ("Tools by governance profile"), coding-agent, and manim. This depth is **correctly deferred** off the landing; surfacing it belongs on the concept pages, not README. No landing change recommended.

### B. Governance framing (the "clumsy" section)

- **B1 (high) — the section counts "two homes" in the heading but "three surfaces" in the body four lines later, with no reconciling sentence.** `README.md:30` ("two homes: the gateway and the loop") vs `README.md:34` ("three governance surfaces: local actions, model egress, and tool egress"). Read together, the counts look like a contradiction — this is the clumsiness. **Fix:** reconcile the two counts in one opening (options in §3). Effort S.
- **B2 (medium) — cross-page "one home" vs "two homes" overloads the word "home."** `gateway-layer.md:57` ("governance needs one home rather than many") and `litellm.md:22` ("governance has one home") use "home" to mean *config consolidation for model egress*; `README.md:30` uses "home" to mean *gateway + loop*. **Fix:** scope the two "one home" phrasings to model egress. (Correction from the verifier: `how-the-stack-fits-together.md:43` is **already** scoped — "For model requests, governance has one architectural home" — so only `gateway-layer.md:57` and `litellm.md:22` need tightening. This touches wording the recent two-homes retitle deliberately left unchanged — a tightening, not a reversal; confirm first.) Effort S.
- **B3 (low) — the section's closing sentence adds a fourth vocabulary:** `README.md:34` "sovereignty therefore covers the loop as well as the data" ("data" is never defined). Replace or drop once the opening is reconciled. Effort S.

**Verifier caution (important):** the concept pages deliberately keep "second home" for the loop (`how-the-stack-fits-together.md:43`, `orchestration-layer.md:39`). So whatever landing wording is chosen must stay **reconcilable with "home"** — a heading that drops "home" entirely would create a new landing-vs-concept vocabulary split, the exact problem B1 is trying to remove. The recommended fix therefore **keeps "home" and maps it to the three surfaces**, rather than replacing it with "enforcement points."

### C. Extensibility / graceful evolution (the models/frameworks/tools question)

- **C1 (high) — substitutability is asserted but the swap mechanism is never shown where a developer lands.** `README.md:18` ("layers are substitutable and optional"), `README.md:71` ("any part of the stack, including the model, can be replaced"), `how-the-stack-fits-together.md:10` ("swap a runtime, change models… without replacing the whole system") — none says **how**. The real answer (every runtime/gateway exposes an OpenAI-compatible endpoint, so a swap is an endpoint change behind the gateway, not a rebuild) is buried in per-component rows (`inference-layer.md:8,27`; `gateway-layer.md:69`). This is the actual evolution question. **Fix:** add a **"How the stack grows"** treatment to `how-the-stack-fits-together.md` — **unified with the existing "What each layer adds as the system grows" section (`:67`), not a duplicate section** (verifier correction) — naming the stable-interface seam with the vLLM/LM-Studio cards as worked examples, then one linking clause on `README.md:18`. Effort M.
- **C2 (medium) — the growth story is vertical (adding layers), not horizontal (swapping a component).** `how-the-stack-fits-together.md:67-76` answers "what do I add," not "how do I replace Ollama with vLLM or Gemma with a newer model." **Fix:** in the same growth section, add a horizontal-axis paragraph using existing evidence (model-card replaceability rows, the OpenAI-compatible endpoint), keeping the "further work" idiom for named swap candidates (e.g. Qwen3.6-35B-A3B). Effort M.
- **C3 (low) — "Scope and next work" frames extensibility as out-of-scope limits, not a living-reference property.** `README.md:88-90` reads as caveats; the discipline (new paths admitted only when their supporting pages exist) is genuinely an extensibility property. **Fix:** reframe one sentence to name the growth discipline positively, keeping the "further work" idiom. Effort S.

*The internal naming registry stays internal; any public how-to-swap guidance references the visible component cards, not the registry.*

### D. Environments (pilot / production)

- **D1 (medium) — two of three environment pages are unreachable from the landing; production appears only as an out-of-scope negative.** `README.md:42` is the only `environments/` link (pilot, via the institution row); `development.md` and `production.md` are never linked; production surfaces only at `README.md:90`. All three pages exist and are well-built. The "pilot and production not covered" complaint is accurate **as discoverability**, not content. **Fix:** link all three by extending the institution row (correction: pilot → operations **already** links at `README.md:42`; the genuinely missing links are the chat-service runbook, `development.md`, and `production.md`). Effort S.
- **D2 (medium) — the development→pilot→production ladder is stated only defensively** (`README.md:13,90`), never as orientation. **Fix:** one orienting sentence after the first-build section naming the ladder, linking all three pages, stating pilot serving and production operations are further work. Effort S.
- **D3 (low) — the deployment-environment axis is absent as a first-class concept** (the landing surfaces only the layer axis). If D2's sentence is too thin, a compact 3–4 line "From development toward shared use" mini-section after the first build — brief, build-oriented, not a stakeholder flow. Effort M.

---

## 3. Governance framing — concrete replacement (recommended)

Reconcile the count while **keeping "home"** so the landing and concept pages speak one vocabulary:

> **Heading:** `## Governance: two homes covering three surfaces`
> **Opening:** "A Frugal AI build has three surfaces where control can leak — model egress, local actions, and tool egress — held at two homes: the gateway and the agent loop. Every model request that could leave the institution passes through the gateway, the sovereignty envelope; agents add the second home, the loop they run in, because their local actions and their tools' network calls never touch the gateway."

Then: name and link the [harness] in the agent paragraph (A1); replace the "loop as well as the data" closing sentence (B3); scope the two cross-page "one home" phrasings to model egress (B2). This resolves the exact contradiction the user feels while preserving the settled three-surfaces convention and the "second home" language already live on the concept pages.

(Alternatives if a different register is preferred: **place-led** — "## Where governance lives: the gateway and the loop", opening that states three surfaces held at those two places; **boundary metaphor** — "## Governance sits at the boundary — and, for agents, at the loop". Both must keep "home"/"loop" reconcilable with the concept pages.)

---

## 4. Prioritised completion list

**P0 — resolves the stated complaints**
1. Reconcile the governance section (new heading + opening; §3). *Decision-gated on register choice only.* S.
2. Name and cite "harness" in the loop sentence (A1). *Decision-free.* S.

**P1 — audience-flow implementation (gated on the audience decision)**
3. Ministry row: make the split hand-off explicit and deep-link the existing Appendix A mention (`README.md:41`). S.
4. Extend the institution row to reach the chat-service runbook + `development.md`/`production.md` (D1), closing the IT-deployer and environments gaps together, without re-adding "Operate it." S.
5. Environments-ladder sentence after the first build (D2), coordinated with item 4 to avoid duplication. S.
6. From-COL signpost distinguishing the out-destination (strategy/policy/news) from the in-KB reference architecture. S.
7. Fix the governance closing sentence (B3, comes with item 1). S.

**P2 — extensibility and cross-page coherence**
8. "How the stack grows" content on `how-the-stack-fits-together.md`, unified with the existing growth section (C1, C2), + one landing linking clause. M.
9. Scope the cross-page "one home" phrasings on `gateway-layer.md:57` and `litellm.md:22` (B2). *Confirm first.* S.
10. Reframe "Scope and next work" as a living-reference property, keeping the "further work" idiom (C3). S.

**Not recommended:** a skills block on the landing (A3, depth belongs on concept pages); more landing space for the Application layer (A2); any educator/teacher routing row (reverses the declined 2026-06-09 decision).

---

## 5. Decisions for the user

1. **Audience-flow model** (lead) — Option A (four tracks, recommended) / B (literal 3-audience) / C (developer-only signpost).
2. **Governance-section register** — "two homes covering three surfaces" (recommended) / place-led / boundary-metaphor.
3. **Cross-page "one home" scoping** (B2) — tighten `gateway-layer.md:57` + `litellm.md:22` to model egress (touches wording the retitle left unchanged; tightening, not reversal).
4. **IT-deployer row shape** — extend the institution row (recommended) vs a dedicated build-progression row.
5. **Educator/end-user scope** (latent) — reaffirm declined (recommended) vs open it as a separate scoped plan.

*Companion to `internal/example-audit-2026-07-15.md` (audience audit) and `internal/plans/2026-07-15-009-feat-audit-remediation-plan.md`. Assessment only; no landing edits made.*
