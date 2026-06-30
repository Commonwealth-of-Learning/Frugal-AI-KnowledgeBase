# Docs review — readability, UX, architecture, agentic-era framing

> **Implemented.** Nearly all recommendations in this review have shipped; see `internal/gap-review-2026-06-12.md` for the verification. The only items still genuinely open are the administrative-agent guide (tracked there as B1) and the audit's confidence-label heuristic (tracked there as C1). Kept as a dated record of the original findings.

Date: 2026-06-09. Scope: all of `docs/` (46 pages), nav (`docs/SUMMARY.md`), `.gitbook.yaml`, `.gitignore`. Method: full read of landing, concepts, and agent-facing pages; systematic review of all guides, component cards, operations, and reference pages; repo-wide checks for MCP/llms.txt/AGENTS.md coverage. Recommendations only — no public pages were edited.

## What already works

The layered spine is consistently enforced: every guide carries the same template (fit/limits → prerequisites → component map → numbered steps → verify table → governance → troubleshooting → next step), component cards share the at-a-glance/frugal-fit structure, cross-links resolve, naming is disciplined, commands are copy-pasteable, and there are no navigational dead ends. Time/level signposting, verify checklists, and the legacy-stub redirects are all good practice. The agent-as-Application-subtype framing with **two governance surfaces** (local actions vs model egress) is ahead of most documentation of this kind. The findings below are about extending a sound structure, not repairing it.

## A. Agentic-era framing (highest value)

**A1. The gateway does not see agent tool traffic — name the third egress surface.**
The KB's strongest claim is "governance has one home: the gateway". That holds for model calls, but an agent's *tools* (and any MCP servers it is given) can make their own network calls that never pass LiteLLM — a web-search tool, a package install, an API lookup. `application-layer.md`'s two governance surfaces ("what the agent does locally" / "what leaves via model calls") leave this third surface implicit. Recommendation: extend the two-surfaces section (and the matching passage in `coding-agent.md` §Governance) to state that tool/MCP egress is governed at the application layer — allowlisted tools, no-network defaults, and the `external_directory: deny` pattern generalised to network scope. This closes a real hole in the sovereignty-envelope story before a reviewer finds it.

**A2. MCP is absent from the knowledge base.**
No page mentions the Model Context Protocol, yet it is now the standard way agents acquire tools, OpenCode supports MCP servers, and GitBook itself exposes one (see A3). Recommendation: introduce MCP in `orchestration-layer.md` (tools subsection — "tools may be built in, written locally like the math tutor's, or supplied by MCP servers, which are substitutable orchestration components like any other layer element"), add a glossary entry, and note MCP support on the OpenCode card. Frame it through the existing spine: MCP servers are orchestration-layer components, governed per A1.

**A3. The KB itself is agent-consumable — surface this as a feature.**
GitBook auto-generates `llms.txt`, `llms-full.txt`, per-page `.md` endpoints, and an MCP server for every published space, with zero configuration ([GitBook LLM-ready docs](https://gitbook.com/docs/ai-and-search/llm-ready-docs), [June 2025 changelog](https://gitbook.com/docs/changelog/june-2025/24-june-performance-upgrades-llms-full.txt-and-.md-support-text-alignment-and-more)). For a KB whose capacity-building story is "a local team uses a coding agent to extend the stack", this is a through-line, not a footnote. Recommendation: verify the published site serves `llms.txt`, then add a short page (Reference section, or a subsection of the coding-agent guide) — "Using this knowledge base with an AI agent" — showing how to point OpenCode at the site's `llms.txt`/MCP endpoint so the agent builds with the KB as context. Page `description:` frontmatter feeds the generated `llms.txt`, so the existing discipline there already pays off.

**A4. Teach the AGENTS.md convention in the builder's-tool story.**
`coding-agent.md` configures `opencode.json` but never mentions `AGENTS.md`, the convention OpenCode (and most agents) read for project instructions. The capacity-building payoff — institutions maintaining their own stack with an agent — depends on their repos being agent-readable. Recommendation: add a short step or callout in the coding-agent guide: create an `AGENTS.md` recording the project's conventions, and keep runbooks in the repo where the agent can read them. This makes the second OpenCode role concrete.

**A5. Prioritise the agentic rows of the example matrix.**
In `example-applications.md` the "Administrative agent" row (tool-using staff tasks, multi-step workflows with human approval) is entirely *further work*, yet it is the example ministries will ask about first in 2026. Recommendation: make it the next guide increment; it exercises A1's tool-egress governance and the Dify orchestration already built for the curriculum advisor.

**A6. Make model cards' agentic readiness comparable.**
`qwen-3.6-35b-a3b.md` and `gemma-4-12b.md` discuss tool use and function calling; `qwen-3.5-9b.md` — the default model — does not, even though `math-tutor.md` depends on its native function calling and `orchestration-layer.md` warns small local models may emit tool calls as text. Recommendation: add a consistent "Agentic readiness" row (or At-a-glance line) to the model-card template: tool-calling support, reliability caveat, which guides exercise it.

## B. Document architecture

**B1. Replace the ten legacy stub pages with `.gitbook.yaml` redirects.**
Ten of 46 files under `docs/` are unlinked "Legacy template page retained for old links" stubs (`core-concepts/*`, `guides/*`, `reference/reference.md`, `reference/configuration.md`, `getting-started/getting-started.md`, `getting-started/your-first-project.md`). `.gitbook.yaml` already proves the redirect mechanism (curriculum-assistant → curriculum-advisor). Recommendation: add redirect entries and delete the stubs — a ~20 % cut in page count, a cleaner repo for maintainers and for `llms-full.txt`. The same mechanism finally makes the deferred `frameworks/open-webui.md` → `components/applications/` move safe.

**B2. Slim the landing page.**
`docs/README.md` runs nine sections and six tables, with overlap: "Where to start" vs "Learning path" (two routing tables), and "Not in the first build" vs "Coming next" (two scope sections). Recommendation: keep What-this-is, the stack block, one routing table, and the first build; move "What this path proves" and "Guardrails before scale" into `frugal-ai-principles.md` / `how-the-stack-fits-together.md`, and merge the two scope sections. Target ~70 lines.

**B3. Fix the `.gitignore` pattern that hides `docs/reference/`.**
`reference/` (unanchored) is the standing gotcha behind `git add -f`. If the intent is a repo-root scratch folder, anchor it (`/reference/`) or add `!docs/reference/`. One-line change; removes a recurring maintainer trap.

**B4. Add a short reader's guide to the reference-architecture page.**
At 395 lines / 10 sections it is the longest page by far. The audience split is already in the headings (§1 is for ministers; §6+ is implementation). Recommendation: a 4–5 line "How to read this page" block under the title routing each audience to its sections — cheaper than splitting the page and preserves the no-anchor links from guides.

## C. Readability and UX

**C1. Restructure the glossary for scanning and deep-linking.**
40 flat `<details>` collapsibles mean no visible scan order, no heading anchors for cross-links, and weaker rendering in the auto-generated markdown/`llms.txt` endpoints (an agentic-consumption cost, too). Recommendation: group terms under a few `##` theme headings (Stack and layers · Governance and sovereignty · Models and inference · Operations), or switch to `###` term headings, which GitBook anchors automatically.

**C2. Complete the time/level signposting.**
"Expected time" appears only in quickstart, offline-chat-service, and math-tutor. `ai-gateway.md`, `curriculum-advisor.md`, `coding-agent.md`, and `manim-animator.md` carry level but no time. Recommendation: add estimates to the four hint boxes — the convention is established; finishing it is cheap.

**C3. Add one diagram per learning tier.**
The KB has exactly one diagram (the mermaid request-path in `how-the-stack-fits-together.md`). The component-map tables are good, but the gateway and coding-agent builds — where the request path forks (cloud burst; agent → gateway → model vs agent → local actions) — would each benefit from a small mermaid diagram, and `example-applications.md` from a visual of the shared floor diverging into the three application rows. Three diagrams, not a redesign.

**C4. Surface the curriculum advisor on the landing page.**
The README's learning path follows only the maths through-line; the curriculum advisor (and Dify, the heaviest orchestration component) never appears on the landing page. Recommendation: one added row or sentence in the Learning path section pointing to it as the second intermediate path — it demonstrates the substitutable-orchestration lesson the matrix page calls out.

## Suggested order

1. Quick wins, no content risk: C2 time estimates · B3 gitignore · C4 README row.
2. Hygiene: B1 stub retirement + redirects (with the open-webui move) · B2 landing-page slim.
3. Agentic increment (a plan-007 candidate): A1 third egress surface · A2 MCP coverage · A4 AGENTS.md step · A3 "use this KB with an agent" page · A6 model-card row · C1 glossary restructure (supports A3).
4. Next build increment: A5 administrative-agent guide · C3 diagrams alongside it · B4 reference reader's guide.

Items A1–A4 belong together: they upgrade the KB's central claim — one governed boundary, locally owned — to hold in a world where the applications are agents and the readers increasingly are too.
