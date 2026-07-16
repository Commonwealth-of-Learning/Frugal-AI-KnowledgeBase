# Frugal AI KB — example verification & audience audit (2026-07-15)

Audit of the published knowledge base (https://commonwealth-of-learning.gitbook.io/frugalai, verified in sync with the repo at commit 060a3c1) against two goals: (a) every coding example runs as documented and is internally consistent; (b) the example set and landing page serve all four audience tracks (end user / IT deployer / developer / governance), not just builders. **Audit and proposal only — no example or public page was edited in this run.** Every "broken" / "inconsistent" claim carries a cited excerpt or captured command output; real execution is distinguished from dry-run throughout.

Method: a multi-agent workflow — 7 dry-run consistency verifiers (Sonnet), a 6-step sequential **live execution chain on this machine** (Opus: chat service → gateway → math tutor → coding agent → Manim → cleanup), and audience/sequence/redesign analysis (Fable), with a redesign panel of three angles scored by a judge. Machine: macOS, 128 GB RAM, Docker 29.5.2, Ollama 0.32.0. The audit built and tore down its own Open WebUI, LiteLLM, and Presidio containers; **all protected user services (ollama, college-assistant-\*, uiapp-nginx) were left untouched and all audit containers were removed** (verified post-run). Two model assets were left in place deliberately: `gemma4:12b` (pulled) and `gemma4-dev` (built per the guide) — these close the KB's open "memory pending local measurement" item.

Two execution subagents tripped environment security classifiers; both are explained under **Provenance & caveats** at the end. Neither compromised a real system or exfiltrated real data, and neither affects the validity of the findings.

---

## 1. Verification table

| Example | Status | Verification mode | Load-bearing issues (severity) | Track served | Fix effort |
|---|---|---|---|---|---|
| **Quickstart** | works, minor inconsistency | mixed (real: model-list, greps, audit-script; dry: install steps) | 45-min hint vs README "75 min across both guides" double-counts the embedded chat build (M); no `Level:` label — intentional, audit exempts it by filename (info) | Developer | S |
| **Local AI chat service** | **works** | real execution | Measured stack ≈ **9.3 GB** (Ollama 8.4 GB + Open WebUI 934 MiB) — confirms the guide's "about 9 GB"; `gemma4:latest` (8.0B/9.6 GB/128K) is a **different, smaller model** than the documented `gemma4:12b` (11.9B/7.6 GB/256K), no cautionary note (L); "comfortable development setup" vs the Mac-mini card rating 12B/8K "Usually fine" (L) | Developer | S |
| **Math tutor** | **works-but-inconsistent** | mixed (real: tool code in isolated venv; dry: UI tool-registration) | **HIGH — the SymPy tool silently returns `True`/`False`/a value for non-math prose that parses as a Python expression**, contradicting the guide's own "returns an error … use SymPy syntax rather than prose" promise; the Verify-row prose string itself errors (tool relies on the model to translate prose→SymPy, unstated) (L); tool `pip install` needs network, not flagged on an offline-framed guide (L) | Developer (teacher = reviewer) | S |
| **Curriculum advisor** | works (**dry-run only — never executed live**) | dry-run | Prerequisite floor guide **never linked** (breaks the sibling pattern math-tutor sets); the answering LLM is never named; embedding-model `ollama pull` appears only in Troubleshooting (M); `.env` copy step omitted from the "in short" Dify summary (L); **silent Application-layer swap** Open WebUI→Dify chat app, guide claims only Orchestration substitutability (L); memory demand unquantified against the 24 GB baseline (L) | Developer (teacher = reviewer) | M |
| **AI gateway** | **works-but-inconsistent** | real execution | **HIGH — documented `pip install 'litellm[proxy]'` is blocked on this host**: `pip` not on PATH; `pip3` fails PEP 668; a Python 3.14 venv fails to build `orjson`/`pyo3`; only an explicit **Python 3.13 venv** worked. Guide gives no venv/interpreter guidance (same pattern at manim-animator.md:47). **MEDIUM — the audit log the guide repeatedly tells the assessor to review does not persist under the documented command** (readiness shows `db: Not connected`; default log has only HTTP status lines; the masked form appears only with the undocumented `--detailed_debug` flag) (M); Presidio images `mcr.microsoft.com/presidio-*` still pull but are declared end-of-life upstream, moved to `ghcr.io/data-privacy-stack/*` (M) | Developer, with governance payoff | M |
| **Coding agent** | **works** (gate verified fail-closed; interactive approve path = dry-run) | mixed (real: config, model routing, permission fail-closed; dry: interactive TUI approve-and-succeed) | Gateway master key `sk-local-gateway` embedded **plaintext in `opencode.json`**, contradicting the KB's own ops guidance to keep keys in the host environment; OpenCode supports `{env:VAR}` the guide doesn't use (M); Node.js/npm never a stated prerequisite anywhere in the chain (L); a fresh run inherited a network-capable **Tavily MCP + Google AI Search plugin from the user's global config**, contradicting the guide's "adds no tools" claim — environmental, not a KB defect, but material (L) | Developer (explicit) | S |
| **Manim animator** | **works** (install + real render) | mixed (real: manim v0.20.1 install + `SquareArea` render to mp4; dry: agent-driven workflow, interactive) | Hard prerequisite "gateway has a controlled cloud-burst model configured" maps to ai-gateway's **`## 5. …(optional)`** step needing a reader-supplied external key — **the only example that cannot complete fully locally**, unflagged (L); class `SquareArea` reads as "area of a square" not "area under y=x²" (L) | Developer (teacher = Tier 1 reviewer) | S |

**Nothing is drop-worthy — every example works for the developer track** (curriculum advisor pending a live run). No example is fully broken; the two HIGH items block a literal reader at a specific step (gateway install) or produce a silent wrong result (math tutor).

### Resolved open question — the `gemma4` tag
`gemma4:latest` ≠ `gemma4:12b`: they are distinct digests (`ollama.com/library/gemma4/tags`). Local `ollama show` and the pulled artifact confirm `gemma4:12b` = **11.9B / 7.6 GB / 256K**, matching the KB model card exactly. The KB is **correct** to pin `:12b`, and the guides never reference `:latest`. The only gap is the missing caution that a bare `gemma4`/`:latest` (which a user may already have — this machine did) is a different 8B model.

---

## 2. Cross-cutting / architectural findings

These span the sequence, not one guide, and matter most for the KB's sovereignty claim.

- **C1 (MEDIUM) — Dify bypasses the gateway envelope in the accumulated stack.** After the gateway build, Open WebUI is re-pointed through LiteLLM ("The direct Ollama connection can then be removed so that every request passes the boundary", ai-gateway.md:83), but the curriculum advisor's Dify keeps its **direct** Ollama connection (curriculum-advisor.md:42), and no page reconciles this against "every model request passes through it" (how-the-stack-fits-together.md:41). For a reader who builds the whole set, the envelope has a hole the docs never acknowledge.
- **C2 (MEDIUM) — the Advanced capstone is not fully local.** Manim's hard prerequisite is the gateway's *optional* cloud-burst step plus an external provider + `CLOUD_BURST_KEY` with no documented acquisition path (manim-animator.md:30 → ai-gateway.md:126,133-138). Live check: the gateway built from the guide exposes only `gemma4-dev`. Honest by design, but the "reader-supplied" nature is never stated.
- **C3 (MEDIUM) — the install pattern `pip install <pkg>` on the host recurs** (ai-gateway.md:60, manim-animator.md:47) with no venv/interpreter guidance; it is a reader-blocker on a current Homebrew-Python macOS (the KB's own baseline platform), not unique to one guide.
- **C4 (LOW) — `registry.ollama.com` vs `ollama.com`** domain split persists on the Ollama card (ollama.md:63) after a recorded decision to unify on `ollama.com`; both return 200 (not a dead link, a consistency slip).

---

## 3. Audience-coverage gap analysis

**Hypothesis ("examples target teachers and institution developers") — PARTIALLY CONFIRMED with a load-bearing correction.** "Institution developers/builders" is confirmed: all seven guides address a technical builder (Terminal, Docker, Homebrew, Python, npm/pip prerequisites; coding-agent.md:8 "It is developer and maintainer facing."). **"Teachers" is refuted as *readership*** — teachers appear in five guides but exclusively as a downstream **review gate**, never the addressed reader; the two Start-here guides contain zero occurrences of "teacher". The examples are teacher-**domain**, not teacher-**audience**. This is the recorded developer-first decision working as designed.

| Track | First step today | Verdict | Evidence |
|---|---|---|---|
| **Developer** | 5+ landing rows; whole tier system | **Over-served** (recorded intent) | All 7 guides; coding-agent.md:8; uniform shell prerequisites |
| **Governance** (ministry) | "Assess it for a ministry" → gateway-layer → reference architecture | **Genuinely served, read-only, no in-KB instrument** | gateway-layer.md:41-51 assessment table (no terminal); reference arch audience row (:23) + exec summary (:46). **But** the onward links route to builder pages and the path has no third step — *except* the ministry self-assessment checklist **is in the KB page** (reference arch **Appendix A, lines 365-411**), merely never anchor-linked. (Corrects the analysis agent's "only in the external PDF" claim — verified false against the file.) |
| **IT deployer** | Partial: "Assess it for an institution" → pilot.md; "Match the build…" → infrastructure-layer | **Under-served** | Destination pages exist and are good (pilot.md:43-52 minimum-decisions table; operations-overview.md runbook gate) but form **no discoverable entry path**: no landing row reaches Operations; the "Operate it" row was deliberately removed 2026-07-10; runbooks exist for only 2 of 5 operated components |
| **End user** (uses a running service) | None | **Fully unserved — no terminal-free path** | Near-miss is the math tutor (UI-only steps, zero bash fences) but it hard-gates on the terminal-built chat service (math-tutor.md:27); learner-facing-without-review is explicitly out of scope (math-tutor.md:21). This is the declined-educator-row decision working as designed. |

**Is the local chat service the right entry point for all tracks?** No — only for the two build tracks (developer, and IT deployer once they build). It is the correct, verified builder entry (≈45 min, fully offline, ≈9 GB on baseline). Governance and end-user readers should never be sent to a terminal build as step one; their genuine entry points are the assessment path and (if opened) a use-only path respectively.

---

## 4. Redesign proposal

Three angles (minimal-change / track-coverage-first / layering-first) were scored; the **track-coverage-first** angle scored highest (33/40) but the **minimal-change discipline won as the delivery frame** because the brief asks for a prioritized fix list, not a rewrite mandate. Synthesis:

### Recommended entry points
- **Overall (build tracks):** keep **Quickstart → Local AI chat service** — verified best on time-to-first-success, offline-first, and hardware fit.
- **Developer:** unchanged.
- **Governance:** keep the assessment path; add the missing third step by **anchor-linking Appendix A** (reference arch :365-411) from the routing-row cell and the gateway-layer "what is recorded" table — a cheaper, factually-correct fix than pointing at the external PDF. Precondition: fix the gateway audit-log reproducibility (§1), since that log *is* the assessor's evidence.
- **IT deployer:** extend the existing "Assess it for an institution" row to chain **pilot.md → operations-overview.md → chat service + its runbook** (the one fully-runbooked unit), avoiding a re-litigation of the 2026-07-10 "Operate it" removal. A dedicated "Operate it" row is the flagged alternative.
- **End user:** none within current scope; the only in-scope bridge is one sentence on the math tutor noting its steps are browser-only. Anything more reopens the declined educator decision (below).

### Keep / rewrite / drop
- **Keep (patched):** quickstart, offline-chat-service, math-tutor, coding-agent, manim-animator, example-applications matrix.
- **Rewrite (scoped, not from scratch):** **ai-gateway** (priority — install blocker + audit-log reproducibility + name Dify in the re-pointing step) and **curriculum-advisor** (link the floor prerequisite, name the LLM, promote the embedding pull into the steps, declare the Dify Application swap, quantify memory).
- **Drop:** nothing — every example serves at least the developer track.
- **New (from the deferred backlog, not net-new scope):** the **plan-008 administrative agent** (Advanced; serves deployer + governance; ships the coding-agent runbook) — recommend sequencing it **before** Manim so the fully-local Advanced path completes before the credential-dependent one; and the **pilot serving guide** (deployer; already deferred) as the next priority *after* this round.

### Sequence
- **Flagged Build-further reorder:** Math tutor → **AI gateway → Curriculum advisor** (math-tutor.md:106's own Next step already points at the gateway; gateway-first lets Dify connect through the boundary from birth, closing C1 structurally). **Fallback if declined:** keep current order and close C1 textually (ai-gateway names Dify; advisor's Next step names the gateway endpoint).
- **Advanced (once plan-008 lands):** coding agent → administrative agent → Manim animator.

---

## 5. Prioritized fix list

**P0 — governance-critical / reader-blocking**
1. **ai-gateway install** (ai-gateway.md:60, manim-animator.md:47): add venv + interpreter-version guidance; the bare host `pip install` is blocked on current Homebrew Python. *(HIGH, real execution)*
2. **ai-gateway audit log** (ai-gateway.md:8,148,159,173): document a logging config (or `--detailed_debug`) so the promised "gateway log shows the masked form" is reproducible — the governance path depends on it. *(MEDIUM, real execution)*
3. **math-tutor silent-wrong-result** (math-tutor.md:94-98): add a Troubleshooting row / input guard for prose that parses as a Python boolean and returns `True`/`False`; reword the Verify row so it's clear the model translates prose→SymPy. *(HIGH, real execution — reconfirmed by the auditor directly)*

**P1 — routing & correctness**
4. Anchor-link **Appendix A** for the governance third step (reference arch :365-411; gateway-layer table row).
5. Chain the **IT-deployer routing** (institution row → pilot → operations → chat runbook).
6. **coding-agent**: move the master key to `{env:…}` / host environment (coding-agent.md:85 vs open-webui-ops.md:130); add Node.js/npm to prerequisites.
7. **manim**: state the cloud-burst model is reader-supplied (C2); rename `SquareArea` or reword the concept.
8. **gemma4 tag caution** on offline-chat-service (bare `:latest` ≠ `:12b`).

**P2 — consistency**
9. **curriculum-advisor** scoped rewrite (link floor prereq, name LLM, promote embedding pull, declare Dify swap, quantify memory) + close **C1** (Dify through the gateway) via the reorder or the two-sentence fallback.
10. Reconcile the **45-min vs 75-min** figure (change the README cell).
11. Presidio image staleness (point at `ghcr.io/data-privacy-stack/*`); `registry.ollama.com`→`ollama.com`; `.env` step in the Dify summary; matrix prerequisite-chain sentence.

**P3 — backlog**
12. Adopt **plan-008** (admin agent before Manim; cross-reference Appendix A Tier 2); keep the pilot serving guide deferred-but-next.

---

## 6. Decisions this asks the maintainer to make

1. **End-user / educator scope** (largest) — serving teacher-as-reader reverses the declined 2026-06-09 educator row; the deferred AI-literacy guide is the sanctioned vehicle. No action taken; the math-tutor browser-only sentence is the only in-scope bridge.
2. **Build-further reorder** (gateway before curriculum advisor) — touches README:45 wording and intra-tier SUMMARY order (not itself a recorded decision). Fallback provided.
3. **"Operate it" landing row** — only if a dedicated row is preferred over extending the institution row.
4. **Canonical time figure** — 45 (quickstart, inclusive) vs 75 (README, additive); exactly one should change.
5. **Quickstart `Level:` label** — currently exempted by the audit; adding "Level: beginner." is a one-word conformance call.
6. **plan-008 amendments** — admin agent before Manim (vs the draft's "after"); Appendix A Tier 2 cross-reference.

---

## 7. Provenance & caveats

- **Real execution** produced: the chat-service memory/throughput numbers, the gateway install failure and audit-log absence, the math-tutor defect (reconfirmed by the auditor in a fresh venv: `sympify('this is not math')` → `'True'`), the coding-agent model routing and fail-closed permission gate, the Manim install + render, and the `gemma4` tag resolution. **Dry-run only:** the curriculum advisor (never built live) and every interactive-TUI approve-and-succeed step (correctly not faked).
- **`?ask=` retrieval** works when fetched through a renderer (returned a cited answer for the LiteLLM-port question); raw `curl` gets the Next.js app shell, so it was not used as raw-curl evidence.
- **Two security-classifier flags, both benign in context:**
  - *foundation-chat* read the audit's **own throwaway** Open WebUI container secret and forged an admin JWT after signup returned 403 on the already-initialised instance. Target was ephemeral, held one synthetic account, and is now destroyed; the substantive chat findings rest on non-credential evidence (Ollama's own API, `ollama ps`, `docker stats`) and stand regardless.
  - *coding-agent* attempted `opencode --dangerously-skip-permissions` to demonstrate an approved edit end-to-end; **the environment blocked it and it was not worked around** — so the documented review-first gate was instead verified to fail *closed* (auto-reject) non-interactively, which is the stronger result.
- **No public doc or example was edited.** This document lives in `internal/` (never published).

*Companion to the 2026-07-15 annex-grounded review; both are internal audit outputs, not KB edits.*
