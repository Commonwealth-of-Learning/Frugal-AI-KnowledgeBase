---
title: Frugal AI Docs Improvement Plan
type: feat
status: active
date: 2026-06-08
origin: internal/handoff-2026-06-08.md
review-source: Editorial and technical review of the published docs/ slice, June 2026
---

# Frugal AI Docs Improvement Plan

> **Related:** the strategic spine is now `2026-06-08-002-feat-frugal-ai-layered-repositioning-plan.md`. This plan remains the content-quality backlog whose items fold into that plan's increments.

## Overview

The published Frugal AI knowledge base (`docs/`) is strong, disciplined work. Its source-confidence labelling, its honesty about "what this path does not prove yet", and its refusal to dress a development path up as production are the right instincts and must be preserved. This plan does not propose a rewrite. It records a prioritised set of corrections and enrichments arising from a full review of the linked public slice against the live COL Frugal page and primary model sources.

Work is ordered from highest-stakes to cosmetic: model-card fact-checking first (re-verified against the upstream `config.json` on 2026-06-08; see U1), then equity, alignment, and economic-evidence gaps, then an information-architecture split, then governance habits modelled by the hands-on path, then smaller substantive points.

> **Verification note (2026-06-08):** A review had flagged the Qwen3.5-9B architecture and the Gemma 4 `<turn|>` token as likely errors. Re-checking the primary sources showed both card claims are correct (see U1). The headline "factual correction" did not survive verification; only a minor parameter-label reconciliation remains. This is recorded so a future maintainer does not re-open settled facts.

---

## Problem Frame

The knowledge base is really two documents in one binding: a single-machine developer recipe (Mac mini -> Ollama -> Open WebUI, with a runbook) welded to a ministry-facing reference architecture (layered model, sovereignty envelope, risk-tiered teacher-in-the-loop, pilot blueprint). The work is accurate and careful, but a few issues reduce its credibility and its fit with COL's identity:

- the three model cards are the highest-integrity surface, since reviewers copy them verbatim; on re-verification they are accurate, with only a 35B/36B parameter-label note outstanding;
- multilingual capability, one of the strongest equity arguments for small open models and central to COL's mission, is almost entirely absent;
- on-brand COL assets from the live page (Aptus heritage, the alliance/Compact framing) are thin or missing;
- "Frugal AI is not cheap AI" is asserted but never demonstrated with a cost model;
- the two audiences share one navigation with no signposting, and two glossaries define the same terms differently;
- the one runnable path quietly models a few habits (all-interface bind, no offline proof) that contradict the document's own thesis.

The reviewed surface is the slice linked from `docs/SUMMARY.md`. Unlinked legacy pages under `docs/core-concepts/`, `docs/guides/`, and parts of `docs/reference/` are out of scope here and tracked separately in the handoff.

---

## Requirements Trace

- R1. Correct the Qwen3.5-9B architecture and MoE description after confirming against the upstream `config.json`.
- R2. Reconcile the Gemma 4 end-of-turn token and the Qwen3.6 35B/36B parameter naming.
- R3. Reassure the builder that the Ollama registry build of Qwen3.5 handles text and image, so the documented path is not mistaken for broken.
- R4. Surface language coverage on every model card and add a language/accessibility line to the principles.
- R5. Name low-resource-language quality as a risk in the annex quality-gap material.
- R6. Anchor the principles in COL's Aptus heritage and strengthen the alliance/Compact framing in the annex executive summary.
- R7. Align external citations to the canonical titles listed on the COL Frugal page; verify or drop unconfirmed resources.
- R8. Add an explicitly illustrative total-cost-of-ownership comparison and develop the energy/sustainability argument.
- R9. Signpost reader paths between the builder recipe and the ministry annex.
- R10. Consolidate to one canonical glossary and one headline Frugal AI definition; factor shared model-card caveats into one referenced block.
- R11. In the hands-on path, bind Open WebUI to localhost, add an offline-verification step, and add a backup-residency note.
- R12. Enrich the teacher-in-the-loop framing and link the operational tiers to the JL4D TiL strategy.
- R13. Demote NVIDIA DGX Spark to one option in the pilot defaults and state which model tier each machine targets.
- R14. Preserve existing strengths: source-confidence labelling, development/pilot/production boundaries, British spelling, no direct second person, and the naming registry.

**Actors:** A1 local AI builder; A2 ministry or institutional evaluator; A3 docs maintainer; A4 LLM/MCP reader.

---

## Scope Boundaries

- Do not rewrite pages that are already accurate and on-brand; make targeted edits.
- Do not introduce unverified benchmark or performance numbers; keep source-confidence discipline.
- Do not add new component, runtime, or model pages unless a corrected fact requires it.
- Do not promote unlinked legacy pages into the public path as part of this work.
- Do not change GitBook styling beyond Markdown and existing block patterns.
- Keep all naming aligned with `internal/naming-registry.md`.

---

## Context & Research

### Files reviewed (linked public slice)

- `docs/README.md`, `docs/SUMMARY.md`
- `docs/getting-started/quickstart.md`, `docs/getting-started/offline-chat-service.md`
- `docs/concepts/frugal-ai-principles.md`, `docs/concepts/how-the-stack-fits-together.md`
- `docs/components/models/qwen-3.5-9b.md`, `docs/components/models/qwen-3.6-35b-a3b.md`, `docs/components/models/gemma-4-12b.md`
- `docs/components/environments/pilot.md`, `docs/components/hardware/nvidia-dgx-spark.md`
- `docs/operations/open-webui-ops.md`
- `docs/reference/glossary.md`, `docs/reference/sovereign-education-ai-reference-architecture.md`

### External references

- COL Frugal page (`https://www.col.org/frugal`): leads with "inclusive, equitable", roots the work in Aptus, frames Frugal AI as "durable institutional infrastructure rather than an externally sourced service", and lists canonical resources including the Gaborone to New Delhi Compact, the Technical Annex, the TVET piece, and the JL4D TiL-AI article.
- Primary model sources: Hugging Face model cards and `config.json`, the Ollama library, and Unsloth model guides for Qwen3.5-9B, Qwen3.6-35B-A3B, and Gemma 4 12B.

### Confirmed observations

- Two glossaries exist: `docs/reference/glossary.md` (28 `<details>` entries) and Section 10 of the annex (8 table rows). Both define Frugal AI, Teacher-in-the-Loop, RAG, the airlock, cloud burst, edge device, and store-and-forward, with differently worded definitions. The annex even calls it "Privacy airlock" while the glossary heads the entry "Airlock".
- Neither Frugal AI definition echoes the COL page's "durable institutional infrastructure" framing.
- The build guide and the runbook both run `docker run -d -p 3000:8080 ...`, which binds to all interfaces.
- The guide's Verify table proves chat and multi-turn but never proves offline operation, the headline resilience benefit.
- `docs/components/environments/pilot.md` hardcodes NVIDIA DGX Spark as the headline pilot hardware default.

---

## Key Technical Decisions

- Treat the three model cards as the highest-integrity surface: an IIT Jodhpur or ministry reviewer will copy them verbatim, so a single architecture error is more damaging than any prose weakness.
- Verify the Qwen3.5-9B architecture against `config.json` before editing, then carry the verified fact into the card. Do not edit from inference alone.
- Make the canonical Frugal AI definition match the COL page wording so the knowledge base and the source speak with one voice.
- Keep all new cost and energy material explicitly labelled illustrative-not-benchmark, consistent with the document's own source-confidence rule.
- Split audiences by signposting and an explicit entry point rather than by physically separating the repository, to avoid breaking existing links and the audit's required summary entries.

---

## Implementation Units

Priority key: P0 must land first; P1 high value; P2 smaller substantive; P3 cosmetic.

- [x] U1. **P0 - Verify and reconcile the model-card facts** (verified 2026-06-08)

**Goal:** Confirm the three model cards against primary sources before any edit, then apply only the changes the sources support.

**Requirements:** R1, R2, R3, R14.

**Files:**
- Modify: `docs/components/models/qwen-3.6-35b-a3b.md` (only)
- No change: `docs/components/models/qwen-3.5-9b.md`, `docs/components/models/gemma-4-12b.md`

**Verification findings (primary sources):**
- **Qwen3.5-9B is correct as written.** `Qwen/Qwen3.5-9B/config.json` shows `model_type: qwen3_5`, `architectures: ["Qwen3_5ForConditionalGeneration"]`, a dense FFN (`intermediate_size: 12288` with no `num_experts` / `num_experts_per_tok` / `moe_intermediate_size`), a hybrid `layer_types` pattern of `linear_attention` (Gated DeltaNet) and `full_attention` with `attn_output_gate: true`, and an embedded `vision_config` (depth-27 vision tower). This confirms the card's "dense hybrid Gated DeltaNet and Gated Attention model with a vision encoder" and its "Dense checkpoint ... FFN layers rather than routed-expert fields" note. The suspected MoE/encoder-free correction was wrong; do not apply it. The contrast is proven by the sibling config below.
- **Gemma 4 `<turn|>` is correct as written.** Gemma 4 changed its turn structure from Gemma 3's `<end_of_turn>`; `<turn|>` (token id 106) is the real end-of-turn token, corroborated by the Unsloth Gemma-4 tokenizer bug report. Do not "fix" it to `<end_of_turn>`.
- **Qwen3.6-35B-A3B confirmed MoE.** `Qwen/Qwen3.6-35B-A3B/config.json` shows `model_type: qwen3_5_moe`, `num_experts: 256`, `num_experts_per_tok: 8`, `shared_expert_intermediate_size: 512`, `num_hidden_layers: 40`, `hidden_size: 2048` — all matching the card. The card's headline name is "35B" (total, A3B = ~3B active) while the Source confidence table records an Ollama label of "36B".

**Applied change:** add a one-line reconciliation to the Qwen3.6 card so the 35B-versus-36B naming is explained rather than left to the reader. No other model-card edits are warranted.

**Optional follow-up (not a correction):** the Qwen3.5-9B vision projector caveat (card line 64) could be paired with one reassuring line that the Ollama registry build `qwen3.5:9b` handles text and image, so a builder does not mistake the documented path for broken. Tracked as an enhancement, not a P0 fix.

**Held correct (do not change):** all three Apache 2.0 licences; the `qwen3.5:9b` tag and 6.6 GB size; the Gemma 4 dense/encoder-free description; the Qwen3.5-9B dense/vision-encoder description.

---

- [ ] U2. **P1 - Surface multilingualism as an equity feature**

**Goal:** Make language coverage a first-class, on-brand attribute instead of an omission.

**Requirements:** R4, R5.

**Files:**
- Modify: `docs/components/models/qwen-3.5-9b.md`, `docs/components/models/qwen-3.6-35b-a3b.md`, `docs/components/models/gemma-4-12b.md`
- Modify: `docs/concepts/frugal-ai-principles.md`
- Modify: `docs/reference/sovereign-education-ai-reference-architecture.md` (Section 6 quality-gap row, line 213)

**Approach:**
- The Qwen cards never mention language coverage; the Gemma card mentions it only under "Good for" (line 27). Add a language-coverage line to each model card's At a glance and Source confidence, source-listed (for example Qwen3.6 across many languages, Gemma 4 across 140+), labelled to the upstream source.
- Add a short "language and accessibility" principle to `frugal-ai-principles.md`, tying multilingual reach to COL's inclusive/equitable framing and its GEDSI work (GIRLS Inspire, Empowering Women and Girls).
- In the annex quality-gap material, name low-resource-language quality explicitly as a managed risk, not only "open-ended tasks".

**Verification:** every model card states language coverage with a source label; principles name language and accessibility; annex quality-gap row references low-resource languages.

---

- [ ] U3. **P1 - Strengthen alignment with the COL framing**

**Goal:** Borrow two on-brand assets from the live COL page and correct citations.

**Requirements:** R6, R7.

**Files:**
- Modify: `docs/concepts/frugal-ai-principles.md`
- Modify: `docs/reference/sovereign-education-ai-reference-architecture.md` (Executive Summary, Section 1)
- Audit: any page citing COL resources

**Approach:**
- Cite Aptus in the principles as the heritage anchor for offline-first and edge material ("open-source hardware enabling learning without grid electricity or Internet"), signalling institutional continuity rather than a from-scratch AI initiative.
- Add a short paragraph to the annex executive summary connecting the technical architecture to the Compact commitment and the "shared value / growing alliance" framing toward the Commonwealth Digital Skills Alliance and endorsement at the India AI Impact Summit 2026, which is what a minister responds to.
- Align citations to canonical titles from the COL page: the TiL work is the JL4D article "Teacher in the Loop AI (TiL-AI): A Strategy for Empowering Educators in Developing Countries through OER Adaptation". Verify that any resource titled like "Frugal AI: A Blueprint for Digital Sovereignty in Commonwealth Education" actually exists among the listed resources; if it cannot be confirmed, drop it.

**Verification:** Aptus cited in principles; Compact/alliance paragraph present in the annex summary; all COL citations match canonical titles or are removed.

---

- [ ] U4. **P1 - Demonstrate "frugal" as an economic claim**

**Goal:** Convert an asserted cost benefit into a demonstrated, clearly-caveated one, and develop the latent sustainability argument.

**Requirements:** R8.

**Files:**
- Modify: `docs/concepts/frugal-ai-principles.md` or a new concept page
- Cross-reference: annex Section 8 "Cost predictability" indicator (line 250)
- Modify: `docs/reference/glossary.md` (Frugal AI energy line, line 62)

**Approach:**
- Add an illustrative total-cost-of-ownership comparison (for example a Mac mini amortised over three years versus N cloud seats at a stated monthly rate), with every assumption stated and an explicit "illustrative, not a benchmark" label consistent with the document's source-confidence discipline. This complements the annex's existing cost-predictability indicator, which currently has no model behind it.
- Develop the energy/sustainability argument that currently appears only as "lower energy use" in the glossary, as a natural COL differentiator. Keep claims qualitative unless a source is cited.

**Verification:** a labelled illustrative TCO comparison exists; sustainability is developed beyond a single glossary phrase; nothing reads as a measured benchmark.

---

- [ ] U5. **P1 - Resolve the two-documents-in-one-binding seam**

**Goal:** Help each audience find its path, and remove the glossary and boilerplate drift hazards.

**Requirements:** R9, R10.

**Files:**
- Modify: `docs/README.md` (Choose a path table, lines 22-27), `docs/SUMMARY.md`
- Modify: `docs/reference/sovereign-education-ai-reference-architecture.md` (Section 10 glossary, lines 303-316)
- Modify: `docs/reference/glossary.md`
- Modify: the three model cards ("Not suitable for" blocks)

**Approach:**
- Signpost reader paths far more aggressively at the top: either strengthen the README "Choose a path" routing for builders versus ministries, or promote the annex to an explicit "For ministries and officials" entry point with its own lead-in, rather than appearing as one reference page near the end.
- Consolidate to one canonical glossary. Keep `docs/reference/glossary.md` as the single source, reduce the annex Section 10 to a short list that links into it, and reconcile the "Airlock" / "Privacy airlock" heading. Adopt one headline Frugal AI definition that echoes the COL page's "durable institutional infrastructure rather than an externally sourced service" and use it in both the glossary and the principles.
- The three "Not suitable for" lists are near-identical boilerplate (production without testing, sensitive data without governance, autonomous agentic actions). Factor the shared caveats into one referenced block and keep only model-specific cautions inline.

**Verification:** one canonical glossary with a single Frugal AI definition matching COL wording; consistent airlock naming; shared caveats referenced once; a clear ministry entry point.

---

- [ ] U6. **P1 - Make the hands-on path model the governance it preaches**

**Goal:** Stop the runnable path modelling habits the document warns against.

**Requirements:** R11.

**Files:**
- Modify: `docs/getting-started/offline-chat-service.md` (Step 4 `docker run`, lines 87-95; Verify table, lines 121-128)
- Modify: `docs/operations/open-webui-ops.md` (recreate command, lines 72-79; backup note, line 95)

**Approach:**
- Bind Open WebUI to localhost in the development path (`-p 127.0.0.1:3000:8080`) and state that exposing beyond localhost is a pilot decision requiring authentication and TLS. Small change, large signalling value for a document about data control.
- Add one offline-verification step to the guide's Verify table: disconnect networking and confirm chat still works, so the central offline-first claim is demonstrated, not just asserted. This is squarely in the spirit of "build something real first".
- Add a one-line backup-residency note to the runbook backup section (do not push the volume to a personal cloud drive; keep backups in-jurisdiction), reinforcing the existing "treat the backup as sensitive" line.

**Verification:** dev bind is localhost with a stated pilot caveat; an offline check appears in the Verify table; backup residency is addressed.

---

- [ ] U7. **P2 - Smaller substantive points**

**Goal:** Tighten coherence between the annex and COL's richer TiL stance, and fix the off-brand pilot hardware default.

**Requirements:** R12, R13.

**Files:**
- Modify: `docs/reference/sovereign-education-ai-reference-architecture.md` (Section 5 risk-tiered TiL, lines 180-192)
- Modify: `docs/components/environments/pilot.md` (Defaults table, lines 32-39; At a glance, line 16)
- Modify: `docs/components/models/qwen-3.6-35b-a3b.md` (local-fit framing)

**Approach:**
- The annex frames Teacher-in-the-Loop purely as risk-tiered approval gating, so it reads as a compliance checkbox. Add one sentence linking the operational tiers to the JL4D TiL strategy and the teacher-as-contextual-adjudicator framing (the AI-certified versus teacher-certified distinction, the Segal et al. 2017 lineage), so TiL reads as a pedagogical stance.
- The pilot defaults table hardcodes NVIDIA DGX Spark as the headline hardware, which sits awkwardly against "reduce lock-in" and "match the model to the machine" for SIDS/LMIC ministries facing cost, export, and availability constraints. Make "a measured equivalent" the consistent default and demote Spark to "one option", matching the phrasing already used elsewhere.
- State explicitly that the 35B candidate targets the DGX Spark tier, not the 24 GB Mac mini, instead of leaving the reader to infer it from the memory tables.

**Verification:** TiL links to the pedagogical strategy; pilot default leads with a measured equivalent; model-to-machine tiering is stated, not implied.

---

- [ ] U8. **Verification pass**

**Goal:** Confirm the edits are accurate, on-brand, and audit-clean.

**Requirements:** R1-R14.

**Approach:**
- Re-confirm each changed model fact against its primary source before merge.
- Run `python3 internal/tools/editorial_audit.py` and again from inside `docs/`.
- Run `git diff --check` for whitespace.
- Focused wording scan for second person and discouraged terms across changed pages.
- Confirm `docs/SUMMARY.md` still lists all required entries and no new links break.

---

## Risks & Dependencies

| Risk | Mitigation |
|------|------------|
| Editing model architecture from inference rather than source | U1 requires `config.json` confirmation before any edit. |
| New cost or energy claims read as benchmarks | Label all such material illustrative-not-benchmark; keep qualitative unless sourced. |
| Glossary consolidation breaks an in-page anchor link | Keep `glossary.md` as the canonical file and have the annex link to it; check anchors after edit. |
| Localhost bind confuses a reader on a second device | State the pilot exposure path explicitly alongside the change. |
| Citation correction removes a real resource | Verify existence on the COL page before dropping; prefer correction over deletion. |
| Audit regressions from new prose | Run the editorial audit and wording scan in U8 before completion. |

---

## Documentation / Operational Notes

- This is a documentation change; no application runtime or deployment configuration changes.
- Stage any `docs/reference/` edits with `git add -f` because `.gitignore` hides `docs/reference/` (see handoff "Git And Ignore Gotchas").
- Preserve the existing strengths called out in R14 throughout; this plan refines, it does not redesign.

---

## Sources & References

- Handoff: `internal/handoff-2026-06-08.md`
- Naming: `internal/naming-registry.md`
- COL Frugal page: `https://www.col.org/frugal`
- Technical Annex (authoritative source): `https://www.col.org/wp-content/uploads/2026/02/Technical-Annex-for-Sovereign-Education.pdf`
- Primary model sources: Hugging Face model cards and `config.json`, the Ollama library, and Unsloth model guides for Qwen3.5-9B, Qwen3.6-35B-A3B, and Gemma 4 12B.
