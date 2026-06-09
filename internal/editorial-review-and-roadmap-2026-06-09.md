# Editorial machinery review and iterative roadmap

Date: 2026-06-09. Companion to `internal/docs-review-2026-06-09.md` (public-docs findings, cited below as A1–C4). Scope here: `internal/editorial-guide.md`, `internal/editor-workflow.md`, `internal/naming-registry.md`, `internal/templates/` (11 files), `internal/tools/editorial_audit.py`, plus a fresh fetch of [col.org/frugal](https://www.col.org/frugal) for tone grounding. The roadmap follows the agreed sequencing: trim and clean first, ground tone in COL sources, then landing page and a minimum demonstration set, agentic framing gradually, sample applications last.

## 1. Editorial machinery findings

### Editorial guide

Strong document: the voice definition, preferred-terms table, writing rules, and style examples are precise and consistently reflected in the live docs. Three issues.

**Source inputs are stale against the live COL page.** The guide's Source Inputs list the Blueprint article as a key source; the current col.org/frugal Key Resources list no longer features it. Resources now listed that the guide omits: *Beyond the Classroom: Frugal AI in TVET*, the *Teacher in the Loop AI (TiL-AI)* JL4D article, and the Gaborone Statement. This single refresh also resolves two plan-001 leftovers ("verify or drop the Blueprint resource"; "align the teacher-in-the-loop JL4D citation" — the canonical citation is now linked from the COL page itself).

**Page patterns are defined in three places.** Guide structure lives in the editorial guide (§Page Patterns), again in the workflow (§8 Review Page Structure), and again in `templates/`. The closing rule "when a template and the editorial guide disagree, follow the editorial guide and update the template" admits the drift without preventing it. Recommendation: make the editorial guide the single owner of patterns; reduce the workflow's §8 to "check the page against its pattern in the editorial guide"; reduce templates per §Templates below.

**No agentic vocabulary.** The preferred-terms table, writing rules, and audience model predate the agentic findings (A1–A4 in the docs review). When agentic framing lands (Iteration 4), the guide needs: preferred terms for agent/tool/MCP language (e.g. prefer "the agent's tool calls" over "the AI does it autonomously"; "scoped permissions" over "safe by default"), a rule naming the three egress surfaces, and a note that page `description:` frontmatter feeds the auto-generated `llms.txt`, so descriptions are written for agent retrieval as well as the sidebar.

### Editor workflow

The 12-step process is sound and the operations-check and naming-gate steps are good institutional discipline. Two issues.

**Stale embedded review.** §Template Review Findings (template risks list) and the later §Template Set ("the templates now reflect this workflow") contradict each other, and a point-in-time review is living inside a process document. Recommendation: delete both sections; replace with one line pointing to the exemplar-pages table (which is the genuinely useful part) and to whatever template set survives Iteration 1.

**No tone-resync step.** Step 3 orders source material but nothing prompts re-checking COL sources as they evolve (the Blueprint drift above is the proof). Recommendation: add a small step or per-increment checklist line — "confirm the editorial guide's Source Inputs still match col.org/frugal Key Resources" — so grounding decays gracefully instead of silently.

### Templates

Findings from a full template-vs-live-page comparison:

- **Practice is ahead of the templates.** Live guides consistently add sections the guide template never prompts: *Governance and review* (math-tutor, curriculum-advisor, ai-gateway, coding-agent), *Localise it*, and the level/time hint box. Runbooks add transition gates ("when to move beyond") absent from the runbook template. The `_Layer:_` tag every component card carries appears in no template.
- **Coverage gaps.** No template exists for the page types added since: gateway card, agent card, orchestration-platform card, or the reference adaptation. The audit's template check therefore cannot cover them either.
- **Quality is uneven.** model-card, guide, hardware-profile, and framework-card templates embed real guidance ("keep only…", "label planning values as estimates"); layer-overview, concept-page, landing-page, and stack templates are bare heading skeletons.
- Confidence labelling (measured / source-listed / expected / estimated) is enforced only in the hardware template though the workflow requires it everywhere.

Recommendation — consistent with the workflow's own "use the current docs as the stronger examples": **invert the relationship.** Designate one live exemplar per page type (the workflow already lists them), keep each template as a thin file: the heading pattern from the editorial guide, a link to the exemplar, and only the guidance lines that aren't obvious from the exemplar (confidence labels, layer tag, hint-box format). Retire the four skeleton templates outright; their pattern lists in the editorial guide do the same job. Create new templates only when a new page type actually recurs (the agent card, in Iteration 4). This ends the triple maintenance.

### Audit tool

`editorial_audit.py` (650 lines) covers frontmatter, site names, summary structure and required entries, first-screen abbreviations, at-a-glance format, placeholders, templates, plans, and port allocations. The final-pass checklist still does several things manually that the script could absorb, in rough order of value:

1. **Internal link validation** — the checklist says "links point to existing files" but no check appears to resolve relative links; this is the most common silent breakage in a restructure-heavy repo, and Iteration 1 (deletions and moves) is exactly when it pays for itself. Build this first.
2. Second-person scan (the workflow already prescribes the `rg` pattern — fold it in, with an allowlist for safety-warning exceptions).
3. `_Layer:_` tag presence on component cards.
4. Level/time hint presence on guides (would have caught the four missing "Expected time" estimates, C2).
5. Confidence-label presence near memory/performance figures (heuristic; warn-only).

Keep the tool warn-only and fast; it is an editor's instrument, not CI.

### Naming registry

No issues found; it is short, current, and the audit enforces it. One addition when Iteration 4 lands: register the agentic role label set (whether `MCP server:` becomes a role or stays inside Orchestration) before any page uses it, in keeping with the naming gate.

## 2. Tone grounding from col.org/frugal (fetched today)

The live page's register confirms the editorial guide's reading: institutional, multilateral, values-driven, calm. Load-bearing vocabulary to keep aligned with: *inclusive, equitable and governed responsibly*; *multilateral and values driven*; *open education as a public good*; *capacity-building*; *durable institutional infrastructure rather than an externally sourced service*; *operate within national constraints… build local capability over time*; *teacher-led, localised, and frugal models*; *digital public goods over proprietary dependency*; *empowering educators and institutions, not replacing them*; *guardrails and data sovereignty*. The KB's core-message section already mirrors this almost verbatim — the grounding task is maintenance, not rewrite.

Two content signals beyond tone: the page centres the **Gaborone to New Delhi Compact** (endorsement at the India AI Impact Summit 2026) and the **alliance** framing (Commonwealth Digital Skills Alliance, SIDS and LMIC focus). The plan-001 leftover "add the Compact/alliance paragraph to the annex executive summary" is therefore timely and belongs in Iteration 2, and the landing page's COL section should name the Compact's Summit moment while it is current.

## 3. Iterative roadmap

Each iteration is sized like the existing increments (a plan in `internal/plans/`), ends with the editorial audit and a weekly-review check, and leaves the KB publishable.

**Iteration 1 — Trim and clean (plan-007 candidate).**
Build the link checker (audit item 1) first, then: retire the ten legacy stubs via `.gitbook.yaml` redirects and move `frameworks/open-webui.md` to `components/applications/` (docs review B1); fix the `.gitignore` `reference/` anchor (B3); delete the workflow's stale template-review sections; thin the template set to exemplar-pointers and retire the four skeletons; fold the second-person scan into the audit. Outcome: smaller repo, single source of truth for patterns, tooling that protects the next iterations.

**Iteration 2 — Ground the editorial layer in COL sources.**
Refresh the editorial guide's Source Inputs against the live Key Resources (drop/annotate Blueprint; add TVET, TiL-AI, Gaborone Statement); add the tone-resync line to the workflow; clear the three plan-001 leftovers (JL4D citation, Blueprint decision, Compact/alliance paragraph); re-read the landing page and `frugal-ai-principles.md` against §2's vocabulary and adjust only where they diverge. Outcome: every public claim of COL framing traces to a current source.

**Iteration 3 — Landing page and the minimum demonstration set.**
Slim `docs/README.md` per the landing pattern (B2: one routing table, merged scope sections, curriculum-advisor row added per C4). Then polish a deliberately small exemplar set to demonstrate readability and usage end to end: **Quickstart + Local AI chat service** (guides), **Qwen3.5-9B** (model card), **Ollama** (runtime card) — these become the canonical exemplars the thinned templates point to. Complete the time/level hints on the four guides missing them (C2); restructure the glossary under theme headings (C1); add the audit checks for hints and layer tags as those conventions are confirmed. Outcome: a reader (or reviewer) can judge the whole KB's quality from the landing page plus four pages.

**Iteration 4 — Agentic framing, gradually.**
In dependency order: name the third egress surface (tool/MCP traffic bypasses the gateway) in `application-layer.md` and the coding-agent guide (A1); introduce MCP in `orchestration-layer.md`, the glossary, and the OpenCode card (A2); add the AGENTS.md step to the coding-agent guide (A4); add the "Using this knowledge base with an AI agent" page after verifying the published site's `llms.txt`/MCP endpoint (A3); add the agentic-readiness row to model cards (A6). Alongside: agentic preferred terms and the llms.txt-description rule in the editorial guide; register any new role label; create the agent-card template now that the type recurs. Outcome: the sovereignty-envelope claim holds for agents, and the KB practises the agent-readability it teaches.

**Iteration 5 — Sample applications and overall pass.**
Re-examine the worked applications (math tutor, curriculum advisor, AI gateway, coding agent, Manim animator) against the refreshed style and agentic framing in one editorial sweep; add the per-tier diagrams (C3); add the reference page's reader's-guide block (B4); then the administrative-agent guide (A5) as the next build increment — it is the matrix's most ministry-relevant empty row and exercises Iteration 4's governance. Outcome: the example matrix is current, visual, and extends into the agentic use cases stakeholders will ask about.

## 4. Why this order works

The sequence front-loads reversible, low-risk subtraction while the link checker makes restructuring safe; grounds tone before any page is rewritten so rewrites happen once; proves the style on a four-page exemplar set before propagating it; and introduces agentic content only after the editorial machinery (terms, templates, audit checks, naming) can support it — so the agentic pages arrive consistent rather than retrofitted. Sample applications come last because every earlier iteration changes the standard they are judged against.
