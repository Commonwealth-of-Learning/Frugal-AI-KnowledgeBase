# Annex v2 draft — proposed changes (highlighted in yellow)

_Owner: TBC — assign a COL focal point to receive these proposals for review (plan-009 decision D7; gap-review-2026-06-12 C3). The same owner covers the agentic annex-v3 collection when it is created (plan-009 WS15)._

Extracted from the COL annex working draft (`Annex_Full_Draft.docx`). Unhighlighted draft text is unchanged from v1; everything below was highlighted yellow as a proposed v2 change. `〖+ … +〗` marks the highlighted span in its surrounding context. These changes are **not** applied to the knowledge base page; they are collected here for COL review.


```
[table under: ]
| 〖+This is a working revision (v2 draft) of the v1 (February 2026) Annex, prepared for COL review. Every change from v1 is shown as highlighted. Unhighlighted text is unchanged from v1. All substantive additions are consolidated into new Appendices B–H, which deliver the task-model-fit framework, the monitoring & evaluation measurement sheet, the privacy airlock test plan, the dated open-source options scan, the section review map, the change log, and the freshness register. New factual claims carry dated, verifiable sources. Guardrails honoured: no expansion into high-stakes automated decisions (certification, progression, grading); cloud burst remains the exception, not the default; teacher approval for learner-facing content is unchanged or strengthened; child-safety and data-protection language is preserved or reinforced.+〗 |
```

```
[table under: ]
| Purpose | Reference architecture and options menu for sovereign, Frugal AI in education; countries may adopt, adapt, or set aside as appropriate |
| Intended audience | Senior officials, EMIS and ICT units, curriculum authorities, teacher education institutions, public universities, regulators |
| Status | 〖+For discussion and adaptation  - working revision under COL intern review+〗 |
| Version / date | 〖+v1 \| February 2026  →  v2 draft \| June 2026 (redlined for COL review)+〗 |
| Scope note | A practical baseline for teacher-support and system enablement. High-stakes automated decision-making (e.g., student progression, certification) is out of scope for this baseline. |
| Document conventions | This annex presents options, and also defines a Minimum Government Baseline of safeguards for any public deployment that (i) processes education data or (ii) produces content intended for learners. Components beyond the baseline are presented as optional modules. |
```

## Contents
- **New:** Appendix B: Change Log (v1 → v2)
- **New:** Appendix C: Annex Review Map (Sections 3, 4, 5, 8, 9)
- **New:** Appendix D: Task–Model Fit Framework and Test Template
- **New:** Appendix E: Monitoring & Evaluation Measurement Sheet
- **New:** Appendix F: Privacy Airlock Test Plan
- **New:** Appendix G: Open-Source Options Scan (dated, vendor-neutral)
- **New:** Appendix H: Freshness Register

## 1. Executive Summary for Ministers and Officials › What about the quality gap?
- **Inline insertion:** Quality is managed through task specialisation and hybrid options. Locally hosted models are optimised for core education workflows on national infrastructure — predictable latency, predictable costs, offline continuity, and data residency, while remaining grounded in ministry-approved knowledge bases. Where additional capability is required for specific high-complexity tasks, this architecture supports controlled cloud burst within a defined sovereignty envelope (data minimisation, jurisdictional controls, audit logging, and offline fallback). The appropriate split between local and cloud processing should be established empirically through pilots, reflecting language, curriculum, and connectivity constraints〖+ — see the Task–Model Fit Framework (Appendix D) for the method used to decide and validate that split.+〗

## 3. Reference Architecture (Layered Model)
- **New:** Layer cross-references (new). Layer E (Privacy Airlock) is operationalised by the Privacy Airlock Test Plan in Appendix F. Layer F (Model Layer) selection is governed by the Task–Model Fit Framework (Appendix D) and the dated Open-Source Options Scan (Appendix G); no model is selected on capability ranking alone. Layer H (Operations) evaluation pipelines emit the indicators defined in the Monitoring & Evaluation Measurement Sheet (Appendix E).

## 4. Hosting Topologies and Hybrid Options › 4.2 The Hybrid Model: Addressing the Quality Gap
- **New:** The decision about which tasks run locally, offline, or via controlled cloud burst is not made by judgement alone. It is made — and re-validated in every pilot — using the Task–Model Fit Framework in Appendix D, which records for each task the allowed and prohibited data, the model under test, the acceptable-quality bar, latency/memory/cost limits, and the offline fallback. The lists below are illustrative planning assumptions only and must be confirmed against that framework in-country.
- **Inline insertion:** Cloud burst requires additional governance controls: data minimisation before transmission, approved cloud providers (sovereign cloud or trusted partners), audit logging of cloud interactions, and fallback to local processing when connectivity fails. Risk tiering and approval gates apply regardless of whether processing is local or cloud-based. 〖+Cloud burst remains the exception, invoked only when a task fails the local acceptable-quality bar in Appendix D; it is never the default path.+〗

## 4. Hosting Topologies and Hybrid Options › 4.3 Open-Source Options (Illustrative)
- **New:** This area moves quickly. A dated, vendor-neutral scan of current small-language-model families, serving runtimes, RAG components, safety tooling and observability — with licence, hardware requirement, offline suitability, language support, risks and a review-by date for each — is provided in Appendix G (current as of June 2026). It names examples only and never describes any tool as “best.” For Global South deployment the decisive test is whether a model performs in the relevant local languages and on the target curriculum; every entry carries the instruction: “Test in pilots before final choice.”

## 5. Governance Guardrails: Risk-Tiered Teacher-in-the-Loop › 5.3 Data Protection and Privacy Airlock
- **New:** How this is tested. The privacy airlock is not assumed to work; it is verified. Appendix F (Privacy Airlock Test Plan) sets out, using synthetic data only, how to detect personal identifiers (direct and contextual), how to redact or mask them, how to treat quasi-identifiers, how to aggregate small cohorts safely (minimum cell-size suppression), how to measure redaction recall/precision, and the default retention and secure-deletion periods for prompts, outputs and logs. Real learner data is never used for testing. None of these controls is relaxed for any tier.

## 6. Implementation Challenges and Mitigations › 6.2 Quality Gap
- **Inline insertion:** Mitigations: Adopt hybrid topology with cloud burst for complex tasks. Match model capability to task requirements—many educational tasks do not require frontier intelligence〖+ (apply the Task–Model Fit Framework, Appendix D)+〗. Invest in model fine-tuning for local languages and curricula. Participate in initiatives to improve open-source educational models (see Frugal AI Challenge concept below).

## 6. Implementation Challenges and Mitigations › 6.3 Pilot-to-Scale Chasm
- **Inline insertion:** Mitigations: Implement risk-tiered approval to reduce the volume requiring teacher review. Design cascade training models where trained teachers train others. Integrate AI literacy into existing teacher professional development rather than creating parallel programmes〖+ — aligning, where useful, to the UNESCO AI Competency Framework for Teachers (2024); see Section 7+〗. Simplify the teacher interface to minimise training burden. Plan for scale from pilot design stage.

## 6. Implementation Challenges and Mitigations › 6.4 The Frugal AI Challenge Concept
- **New:** Grounding the challenge (new). To make the challenge measurable rather than aspirational, the following reference assumptions are provided. They define what entrants must report and what evaluators must measure; they are not performance claims. Figures are current as of June 2026 and must be revalidated (see Appendix H).

```
[table under: 6. Implementation Challenges and Mitigations › 6.4 The Frugal AI Challenge Concept]
| Parameter | Reference assumption (report actuals; validate in pilot) |
| 〖+Device type+〗 | 〖+Single-board edge device, e.g. Raspberry Pi 5 (or “Aptus Pi”/equivalent); no internet during evaluation+〗 |
| 〖+RAM+〗 | 〖+8 GB minimum; 16 GB recommended headroom for model + RAG index + OS+〗 |
| 〖+Storage+〗 | 〖+≈ 64 GB content storage (curriculum content + knowledge-base index + model weights); report the exact allocation used+〗 |
| 〖+Model size / family+〗 | 〖+Open-weights small language model, ~1B–4B parameters (e.g. Llama 3.2 1B/3B, Gemma 3 1B/4B, Qwen2.5 family) — examples only, not endorsements+〗 |
| 〖+Quantisation level+〗 | 〖+4-bit (e.g., Q4_K_M / GGUF or equivalent); report the exact scheme and resulting on-device footprint in MB/GB+〗 |
| 〖+Expected response time+〗 | 〖+Report median and 95th-percentile time-to-first-token and tokens/sec. On a Pi 5, 1B–3B models commonly run ~4–10 tokens/sec (hardware-dependent)+〗 |
| 〖+Offline installation size+〗 | 〖+Total on-device footprint (weights + index + runtime) to fit target storage; report exact MB/GB+〗 |
| 〖+Mathematics topics to test+〗 | 〖+A defined curriculum slice (e.g. grades 6–8 arithmetic, fractions, ratios, basic algebra, word problems) in the target language(s)+〗 |
| 〖+Quality checks+〗 | 〖+Accuracy on a held-out curriculum item bank; correct working shown; safe handling of out-of-scope queries; citation to approved sources where RAG is used+〗 |
| 〖+Failure cases to report+〗 | 〖+Hallucinated steps; wrong final answer with confident tone; language/script errors; refusal failures on sensitive content; latency beyond threshold; crash/OOM under load+〗 |
```
- **New:** The aim is not to claim success but to make explicit what must be measured. Evaluation criteria and metric definitions are consistent with Appendix D (Task–Model Fit) and Appendix E (Monitoring & Evaluation). Any learner-facing tutoring output remains Tier 1 (teacher approval before release).

## 7. Policy Alignment
- **New:** Additional instruments for ministry consideration (new; added only where they help a ministry reason about governance, teacher capacity, student safety, data protection or DPI). Each carries a dated source; see Appendix H for review dates.

```
[table under: 7. Policy Alignment]
| Instrument (dated) | Why it helps a ministry | Reflected here as |
| 〖+UNESCO AI Competency Framework for Teachers (Sept 2024)+〗 | 〖+Defines teacher AI competencies across an Acquire–Deepen–Create progression; supports cascade training design+〗 | 〖+Teacher capacity building (Sections 6.3, 9); AI-literacy integration+〗 |
| 〖+UNESCO AI Competency Framework for Students (Sept 2024)+〗 | 〖+Positions students as responsible co-creators, not passive users; informs safe, age-appropriate use+〗 | 〖+Safety-by-design; learner-facing Tier 1 controls+〗 |
| 〖+African Union Continental AI Strategy (July 2024) and Continental Data Policy Framework (2022)+〗 | 〖+Africa-centric, development-focused governance; data-protection emphasis relevant to many LMICs/SIDS partners+〗 | 〖+Sovereign operation; sovereignty envelope; data-protection baseline+〗 |
```

## 8. Monitoring and Evaluation (Suggested 12-Month Indicators)
- **New:** From indicators to measurements (new). Each indicator above is given a precise operational definition — formula, data source, sampling rule, unit, and target window — in the Monitoring & Evaluation Measurement Sheet (Appendix E). That sheet specifies exactly how to compute median and 95th-percentile latency, offline availability, cloud burst frequency, Tier 1 approval/edit rate, Tier 2 audit pass rate, and teacher usage per month, so two countries measure the same thing the same way.
- **Inline insertion:** Telemetry should be privacy-preserving by design: collect the minimum necessary; aggregate at district/national level; apply suppression rules for small cohorts; restrict access to authorised teams; and prohibit collection of learner free text for monitoring unless explicitly authorised and protected. 〖+Appendix E includes an explicit “do-not-collect” list (no learner free text, no raw prompts/outputs containing PII, no individual-teacher performance ranking, no device or location identifiers beyond district level) to prevent monitoring from becoming surveillance.+〗

## 9. Pilot Blueprint Template
- **New:** Companion artefacts (new). To complete a pilot design using this template, attach: the Task–Model Fit records for each in-scope task (Appendix D); the Privacy Airlock test results on synthetic data (Appendix F); the Monitoring & Evaluation Measurement Sheet with baseline and month-6/12 targets entered (Appendix E); and the relevant rows of the Open-Source Options Scan with review-by dates (Appendix G). These turn the blueprint from a checklist into evidence a ministry can audit.

## 10. Glossary of Key Terms
- **New:** Quantisation: A compression technique that lowers the numeric precision of model weights (e.g., from 16-bit to 4-bit) to reduce memory and storage, enabling larger models to run on edge devices, usually with a small, measurable quality trade-off.
- **New:** Task–Model Fit: A structured method for deciding whether a given education task should run locally, offline, or via controlled cloud burst, based on data sensitivity, acceptable quality, latency/memory/cost limits, and offline fallback (see Appendix D).
- **New:** Quantisation-Aware Training (QAT): Training or fine-tuning that anticipates low-precision deployment, so the quantised model preserves quality close to the full-precision version.

## Appendix A: Self-Assessment Checklist for Ministries (Optional) › Monitoring and Evaluation
- **New:** Added self-check items (new): Task–Model Fit records exist for each in-scope task (Appendix D); the privacy airlock has been tested on synthetic data with documented redaction recall (Appendix F); M&E indicators have operational definitions and entered baselines (Appendix E); selected open-source tools/models carry recorded review-by dates (Appendices G and H).

## Appendix B: Change Log (v1 → v2)
- **New:** This log records every substantive change in this revision and the reason for it. No high-stakes automated-decision scope was added; cloud burst remains non-default; teacher approval and child-safety/data-protection language were preserved or strengthened.

```
[table under: Appendix B: Change Log (v1 → v2)]
| S.N. | Location | Change | Why |
| 〖+1+〗 | 〖+Title / front matter+〗 | 〖+Added “How to read this revision” banner; version updated to v2 draft (June 2026); reading conventions and guardrail statement.+〗 | 〖+Make the redline self-explanatory to COL reviewers.+〗 |
| 〖+2+〗 | 〖+§1, §4.2, §6.2+〗 | 〖+Cross-referenced the new Task–Model Fit Framework (Appendix D) where the local/cloud split is discussed.+〗 | 〖+Task 2; makes the “validate in pilots” instruction operational.+〗 |
| 〖+3+〗 | 〖+§3 (Layered Model)+〗 | 〖+Added a layer cross-reference note tying Layers E, F and H to Appendices F, D/G and E.+〗 | 〖+Task 1; connects architecture layers to test/measurement methods.+〗 |
| 〖+4+〗 | 〖+§4.2+〗 | 〖+Clarified that cloud burst is the exception, invoked only on local-quality failure; never default.+〗 | 〖+Guardrail: do not make cloud burst the default.+〗 |
| 〖+5+〗 | 〖+§4.3 (Open-Source Options)+〗 | 〖+Pointed to dated, vendor-neutral Open-Source Options Scan (Appendix G); added language-first test and “Test in pilots before final choice.”+〗 | 〖+Task 5.+〗 |
| 〖+6+〗 | 〖+§5.3 (Privacy Airlock)+〗 | 〖+Added a “How this is tested” paragraph referencing the Privacy Airlock Test Plan (Appendix F); reaffirmed synthetic-data-only testing and no tier relaxation.+〗 | 〖+Task 4; guardrail on data protection.+〗 |
| 〖+7+〗 | 〖+§6.3, §7+〗 | 〖+Linked teacher-capacity guidance to UNESCO AI Competency Framework for Teachers (2024).+〗 | 〖+Task 6; dated source.+〗 |
| 〖+8+〗 | 〖+§6.4 (Frugal AI Challenge)+〗 | 〖+Added grounded reference-assumptions table (device, RAM, storage, model size, quantisation, response time, footprint, topics, quality checks, failure cases).+〗 | 〖+Task 7.+〗 |
| 〖+9+〗 | 〖+§7 (Policy Alignment)+〗 | 〖+Added dated instruments: UNESCO AI Competency Frameworks for Teachers and Students (Sept 2024); African Union Continental AI Strategy (July 2024) + Continental Data Policy Framework (2022).+〗 | 〖+Task 6; only governance-relevant additions, each dated.+〗 |
| 〖+10+〗 | 〖+§8 (M&E)+〗 | 〖+Added “From indicators to measurements” note and explicit do-not-collect list; pointed to Measurement Sheet (Appendix E).+〗 | 〖+Task 3; privacy-preserving telemetry.+〗 |
| 〖+11+〗 | 〖+§9 (Pilot Blueprint)+〗 | 〖+Added “Companion artefacts” paragraph listing the appendices that complete a pilot design.+〗 | 〖+Tasks 1–5; turns checklist into auditable evidence.+〗 |
| 〖+12+〗 | 〖+§10 (Glossary)+〗 | 〖+Added Quantisation, Quantisation-Aware Training, and Task–Model Fit entries.+〗 | 〖+Task 5 (glossary refresh).+〗 |
| 〖+13+〗 | 〖+Appendix A+〗 | 〖+Added self-check items for the new appendices.+〗 | 〖+Keeps the optional checklist consistent with the revision.+〗 |
| 〖+14+〗 | 〖+Appendices B–H+〗 | 〖+New deliverables: change log, review map, task-model-fit framework/template, M&E measurement sheet, privacy airlock test plan, open-source scan, freshness register.+〗 | 〖+All seven required deliverables.+〗 |
```

## Appendix C: Annex Review Map (Sections 3, 4, 5, 8, 9)
- **New:** A section-by-section map (Task 1): what each focus section currently says, what should be made clearer, and what evidence or test demonstrates it. Italic rows are the priority focus sections named in the brief.

```
[table under: Appendix C: Annex Review Map (Sections 3, 4, 5, 8, 9)]
| Section | What it says now | What to update / clarify | Evidence / test needed |
| 〖+3. Architecture layers+〗 | 〖+Eight layers A–H with objectives and minimum components.+〗 | 〖+Tie each layer to a test/measurement method; clarify that Model Layer selection is governed by task-model fit, not capability ranking.+〗 | 〖+Layer-to-appendix cross-references (added); per-layer acceptance criteria recorded in pilot design.+〗 |
| 〖+4.1 Topologies+〗 | 〖+Four topologies A–D with fit and considerations.+〗 | 〖+Make explicit that hybrid (D) is for capability balancing, with fallback obligations.+〗 | 〖+Documented topology choice + one-page data-flow diagram (§9).+〗 |
| 〖+4.2 Hybrid / local-vs-cloud+〗 | 〖+Lists tasks for local vs cloud burst as planning assumptions.+〗 | 〖+Replace judgement with a repeatable decision method; reaffirm cloud burst is non-default.+〗 | 〖+Task–Model Fit records per task (Appendix D); cloud burst frequency metric (Appendix E).+〗 |
| 〖+4.3 Open-source options+〗 | 〖+Generic categories of open-source components.+〗 | 〖+Provide dated, vendor-neutral examples with licence, hardware, offline, language, risks, review date; language-first test.+〗 | 〖+Open-Source Options Scan (Appendix G); pilot language evaluation.+〗 |
| 〖+5.3 Privacy airlock+〗 | 〖+States airlock controls (minimisation, redaction, quasi-identifiers, retention, audit).+〗 | 〖+Add a concrete test method on synthetic data and measurable redaction targets.+〗 | 〖+Privacy Airlock Test Plan with recall/precision results (Appendix F).+〗 |
| 〖+8. Monitoring & evaluation+〗 | 〖+Indicator domains with measurement examples and reporting cadence.+〗 | 〖+Convert indicators into precise operational definitions; add do-not-collect list.+〗 | 〖+M&E Measurement Sheet with formulas and baselines (Appendix E).+〗 |
| 〖+9. Pilot blueprint+〗 | 〖+Template of pilot design elements.+〗 | 〖+Attach companion evidence artefacts to each element.+〗 | 〖+Completed Appendices D, E, F, G for the specific pilot.+〗 |
```

## Appendix D: Task–Model Fit Framework and Test Template
- **New:** Purpose. A repeatable method for deciding whether an education task should run locally, offline, or via controlled cloud burst — and for proving that decision in a pilot. The question is never “which model is most powerful?” but “which model, tool or topology is safe, affordable, useful and governable for this specific task?”

```
[table under: Appendix D: Task–Model Fit Framework and Test Template › D.1 What to record for each task]
| Field | Definition |
| 〖+Task+〗 | 〖+The concrete education task (e.g., generate a 10-item grade-7 fractions quiz in the national language).+〗 |
| 〖+Placement+〗 | 〖+Local / offline-only / controlled cloud burst. Default to local; cloud burst only if the local option fails the quality bar.+〗 |
| 〖+Data allowed+〗 | 〖+The minimum data the task needs (e.g., curriculum text, approved OER).+〗 |
| 〖+Data NOT allowed+〗 | 〖+Data prohibited from the prompt/path (e.g., learner names, IDs, free text, small-school quasi-identifiers).+〗 |
| 〖+Model/tool under test+〗 | 〖+Named candidate(s) with version and quantisation; examples only, never “best.”+〗 |
| 〖+Acceptable quality+〗 | 〖+The minimum bar the output must meet to be used as-is or with light editing, e.g., curriculum accuracy, correct working shown, safe refusal on out-of-scope/sensitive queries, defined per task type, not generically .+〗 |
| 〖+Latency limit+〗 | 〖+Acceptable median and 95th-percentile response time for the use context.+〗 |
| 〖+Memory/compute limit+〗 | 〖+The maximum RAM/VRAM, storage and compute the task may consume on the target device class — a hard ceiling the local candidate must fit within before cloud burst is even considered.+〗 |
| 〖+Cost limit+〗 | 〖+Acceptable cost per 1,000 tasks (local amortised compute, or cloud burst price).+〗 |
| 〖+Fallback if internet fails+〗 | 〖+What happens offline (e.g., serve local model; queue store-and-forward; degrade gracefully). Mandatory for any cloud-burst task.+〗 |
| 〖+Tier+〗 | 〖+Risk tier (§5.1). Any learner-facing output is Tier 1 regardless of placement.+〗 |
| 〖+Result / decision+〗 | 〖+Pass/fail against the bar; chosen placement; review-by date.+〗 |
```

```
[table under: Appendix D: Task–Model Fit Framework and Test Template › D.2 Worked examples (illustrative; validate in pilots)]
| Task | Placement | Data not allowed | Acceptable quality | Latency / memory | Fallback |
| 〖+Document formatting+〗 | 〖+Local (Tier 3)+〗 | 〖+Any learner PII+〗 | 〖+Formatting correct; no content change+〗 | 〖+< 2 s; minimal (CPU-only, no model load beyond formatting rules)+〗 | 〖+N/A (local only)+〗 |
| 〖+Quiz generation+〗 | 〖+Local (Tier 1 on release)+〗 | 〖+Learner names/IDs+〗 | 〖+Curriculum-aligned items; correct answer key; no learner PII in prompt or output+〗 | 〖+p95 < 10 s; fits a 1–3B model at 4-bit on the edge device+〗 | 〖+Local; queue if busy+〗 |
| 〖+Lesson planning+〗 | 〖+Local (Tier 2)+〗 | 〖+Learner free text+〗 | 〖+Aligned to syllabus; teacher-editable+〗 | 〖+p95 < 15 s; 1–4B model at 4-bit+〗 | 〖+Local+〗 |
| 〖+Translation / localisation+〗 | 〖+Local (Tier 1/2)+〗 | 〖+Identifiers+〗 | 〖+Human-acceptable in target language; terminology correct+〗 | 〖+p95 < 10 s per paragraph; multilingual-capable SLM, 1–4B at 4-bit+〗 | 〖+Local; flag low-confidence+〗 |
| 〖+Retrieval from approved docs+〗 | 〖+Local (Tier 1/2)+〗 | 〖+Out-of-corpus data+〗 | 〖+Correct passage + citation; no fabrication+〗 | 〖+p95 < 5 s; embedding + vector index sized to the in-country knowledge base+〗 | 〖+Local index; report miss+〗 |
| 〖+Maths problem-solving (hard)+〗 | 〖+Local first; cloud burst only on fail+〗 | 〖+Learner PII; quasi-identifiers+〗 | 〖+Correct answer + valid working; safe refusals+〗 | 〖+p95 < 25 s+〗 | 〖+Local model; if cloud down, local + teacher review+〗 |
```

## Appendix D: Task–Model Fit Framework and Test Template › D.2 Worked examples (illustrative; validate in pilots)
- **New:** Decision rule: run locally if the local candidate meets the acceptable-quality bar within the latency, memory and cost limits; escalate to controlled cloud burst only for the specific task that fails locally, and only with the sovereignty-envelope controls of §4.4. Re-test at each review-by date and whenever the model, curriculum or language scope changes.

## Appendix E: Monitoring & Evaluation Measurement Sheet
- **New:** Operational definitions so every country measures the same indicator the same way. Targets are placeholders for ministries to set at baseline; they are not COL benchmarks.

```
[table under: Appendix E: Monitoring & Evaluation Measurement Sheet]
| Metric | Definition / formula | Data source | Unit / cadence | Example target |
| 〖+Median latency+〗 | 〖+50th percentile of end-to-end response time per task type, over all requests in the period.+〗 | 〖+Application/gateway logs (timestamps).+〗 | 〖+Seconds; monthly+〗 | 〖+Set at baseline+〗 |
| 〖+95th-percentile latency+〗 | 〖+p95 of end-to-end response time per task type (tail latency users actually feel).+〗 | 〖+Application/gateway logs.+〗 | 〖+Seconds; monthly+〗 | 〖+Set at baseline+〗 |
| 〖+Offline availability+〗 | 〖+(Time core services answer locally with no internet ÷ scheduled offline-service time) × 100, from offline service tests.+〗 | 〖+Scheduled offline probe results.+〗 | 〖+%; monthly+〗 | 〖+≥ 95% of scheduled offline-service time (set locally at baseline)+〗 |
| 〖+Cloud burst frequency+〗 | 〖+(Requests routed to cloud burst ÷ total requests) × 100. Should stay low; spikes trigger review.+〗 | 〖+Gateway routing logs.+〗 | 〖+%; monthly+〗 | 〖+e.g. < 5% (set locally)+〗 |
| 〖+Tier 1 approval/edit rate+〗 | 〖+Of Tier 1 drafts, % approved before release and % edited before approval (proxy for draft quality).+〗 | 〖+Workflow approval logs.+〗 | 〖+%; monthly+〗 | 〖+Track trend+〗 |
| 〖+Tier 2 audit pass rate+〗 | 〖+% of sampled Tier 2 outputs meeting quality & safety criteria, on a defined sampling fraction.+〗 | 〖+QA sample audits.+〗 | 〖+%; monthly+〗 | 〖+≥ 90% (set locally at baseline; track trend monthly)+〗 |
| 〖+Teacher usage / month+〗 | 〖+Median number of substantive workflow sessions (generate + review/edit + save/export) per active teacher per calendar month, aggregated at district level.+〗 | 〖+Aggregated usage logs.+〗 | 〖+Count + median; monthly+〗 | 〖+Track uptake+〗 |
| 〖+Language coverage+〗 | 〖+% of core learning resources available in each target local language.+〗 | 〖+Knowledge-base inventory.+〗 | 〖+%; quarterly+〗 | 〖+Set per language+〗 |
| 〖+Training completion+〗 | 〖+% of targeted teachers completing the Tier 1 workflow training.+〗 | 〖+Training records.+〗 | 〖+%; quarterly+〗 | 〖+100% of the targeted cohort trained before go-live; ≥ 90% sustained at month 6+〗 |
```
- **New:** Do NOT collect (privacy-preserving telemetry): learner free text; raw prompts/outputs containing PII; individual-teacher performance rankings; device or geolocation identifiers below district level; any data enabling re-identification in small cohorts. Aggregate at district/national level, apply small-cohort suppression, and restrict log access to authorised teams. Learner free text may be collected only where explicitly authorised and protected.

## Appendix F: Privacy Airlock Test Plan
- **New:** Purpose. Verify, before and during a pilot, that personal data is reduced, redacted or controlled before it reaches any AI model. All testing uses synthetic data only — never real learner data.

## Appendix F: Privacy Airlock Test Plan › F.1 Detecting personal identifiers
- **New:** Direct identifiers: names, student/staff IDs, national IDs, phone, email, address, dates of birth, biometric references. Use pattern rules (regex for IDs/phones/emails) plus a named-entity recogniser tuned to local name forms and scripts.
- **New:** Contextual identifiers: free-text fields that may embed names or events; flag and route for redaction or exclusion.

## Appendix F: Privacy Airlock Test Plan › F.2 Removing or masking identifiers
- **New:** Redaction (remove), masking (replace with [REDACTED]/placeholder token), or pseudonymisation (consistent surrogate) depending on whether the field is needed downstream. Default to removal where the task does not need the field.

## Appendix F: Privacy Airlock Test Plan › F.3 Handling quasi-identifiers
- **New:** Treat combinations such as school + grade + rare attribute as re-identifying in small schools and islands. Generalise (e.g., age band not date of birth), suppress rare values, or drop the field before processing.

## Appendix F: Privacy Airlock Test Plan › F.4 Aggregating small groups safely
- **New:** Apply a minimum cell-size rule (e.g., suppress any reported group with fewer than k members; set k locally, commonly k = 5–10) and suppress complementary cells so totals cannot be back-calculated.

```
[table under: Appendix F: Privacy Airlock Test Plan › F.5 Testing whether redaction works]
| Test | Method (synthetic data) |
| 〖+Recall (miss rate)+〗 | 〖+Run a labelled synthetic corpus with known identifiers; recall = correctly detected identifiers ÷ all identifiers actually present in the synthetic test bank (e.g., records S-01–S-05); miss rate = 1 − recall; set a target ceiling, e.g. < 2% missed direct identifiers.+〗 |
| 〖+Precision (over-redaction)+〗 | 〖+precision = correct redactions ÷ all redactions; track to avoid destroying useful curriculum text.+〗 |
| 〖+Quasi-identifier test+〗 | 〖+Seed rare combinations; confirm generalisation/suppression triggers before model processing.+〗 |
| 〖+Leakage / end-to-end+〗 | 〖+Confirm no identifier reaches the model input or cloud-burst payload; inspect logged prompts (themselves redacted).+〗 |
| 〖+Adversarial+〗 | 〖+Obfuscated identifiers (spacing, homoglyphs, alternate scripts) to probe detector robustness.+〗 |
```

## Appendix F: Privacy Airlock Test Plan › F.6 Retention of prompts, outputs and logs
- **New:** Set documented default retention (e.g., prompts/outputs retained only as long as operationally necessary, then securely deleted; audit logs retained for a defined oversight period). Apply secure deletion, restrict access, and provide redress workflows. Record the chosen periods in the pilot design and the Freshness Register (Appendix H).
- **New:** Guardrail: none of these controls is relaxed for any risk tier, and no real learner data is used in testing.

## Appendix G: Open-Source Options Scan (dated, vendor-neutral)
- **New:** Current as of June 2026. Examples only — nothing here is described as “best,” and inclusion is not a COL endorsement. For Global South deployment the decisive test is local-language and curriculum performance. Every row carries the instruction: “Test in pilots before final choice.” Review-by dates are in Appendix H.

```
[table under: Appendix G: Open-Source Options Scan (dated, vendor-neutral) › G.1 Small language model families (open-weights)]
| Family / sizes | Licence (verify) | Hardware / offline | Language support | Risks / limits | Notes (dated) |
| 〖+Llama 3.2 (1B, 3B)+〗 | 〖+Llama Community Licence (use restrictions; check)+〗 | 〖+Edge-feasible at 4-bit (≈ 0.7–2 GB); runs on a Raspberry Pi 5 or similar SBC offline+〗 | 〖+Primarily English-centred; test local languages+〗 | 〖+Weaker on hard reasoning; licence not OSI-approved+〗 | 〖+Meta, Sept 2024; edge-oriented+〗 |
| 〖+Gemma 3 (270M, 1B, 4B, 12B, 27B)+〗 | 〖+Gemma Terms (check use terms)+〗 | 〖+270M–4B sizes edge-feasible at 4-bit (≈ 0.2–3 GB); 12B/27B need more capable hardware and are not edge-suitable offline+〗 | 〖+140+ languages claimed; verify quality per language+〗 | 〖+Use-term restrictions; verify per-language quality+〗 | 〖+Google, Mar 2025 (1B/4B/12B/27B); the 270M variant followed in Aug 2025; QAT checkpoints+〗 |
| 〖+Qwen 2.5 (0.5B–7B+)+〗 | 〖+Apache-2.0 for several sizes (verify per size)+〗 | 〖+Small sizes edge-capable at 4-bit; offline+〗 | 〖+Strong multilingual; up to 128K context+〗 | 〖+Check per-size licence; provenance due diligence+〗 | 〖+Alibaba; multilingual strength+〗 |
| 〖+Phi-4 family+〗 | 〖+MIT (verify variant)+〗 | 〖+Small but reasoning-focused; 4-bit edge feasible+〗 | 〖+English-leaning; test local languages+〗 | 〖+Smaller multilingual coverage+〗 | 〖+Microsoft; strong maths/reasoning for size+〗 |
| 〖+Mistral 7B (and small variants)+〗 | 〖+Apache-2.0 (base)+〗 | 〖+7B needs more memory; small variants edge-feasible+〗 | 〖+Multilingual varies; test+〗 | 〖+7B heavier for low-end edge+〗 | 〖+Good fine-tuning base+〗 |
```

```
[table under: Appendix G: Open-Source Options Scan (dated, vendor-neutral) › G.2 Inference serving / runtimes]
| Tool | Licence | Profile / offline suitability | Best-fit context |
| 〖+llama.cpp+〗 | 〖+MIT+〗 | 〖+Pure C/C++, minimal deps, GGUF quantisation; runs on laptops, Raspberry Pi, phones, CPU-only servers. Strongest pure-edge/offline option.+〗 | 〖+Edge / CPU-only / offline+〗 |
| 〖+Ollama+〗 | 〖+MIT+〗 | 〖+One-command setup, model library, OpenAI-compatible API; wraps llama.cpp. Easiest local/dev deployment; offline-capable.+〗 | 〖+Local dev, single-node pilots+〗 |
| 〖+vLLM+〗 | 〖+Apache-2.0+〗 | 〖+PagedAttention + continuous batching; very high concurrent throughput; needs GPU/server. Not an edge tool.+〗 | 〖+Central hub / GPU production+〗 |
| 〖+ExecuTorch+〗 | 〖+BSD-style (verify)+〗 | 〖+Meta’s on-device runtime for mobile/embedded edge deployment; for app-embedded inference.+〗 | 〖+Phone / embedded edge+〗 |
```

```
[table under: Appendix G: Open-Source Options Scan (dated, vendor-neutral) › G.3 RAG, safety and observability (categories with examples)]
| Category | Examples (verify licence; test in pilot) | Offline |
| 〖+Vector search / RAG store+〗 | 〖+In-country self-hostable vector databases and embedding models (e.g., open vector stores; sentence-embedding models). Choose self-hostable, no external API.+〗 | 〖+Yes, if self-hosted+〗 |
| 〖+Document ingestion / orchestration+〗 | 〖+Open ingestion + retrieval orchestration libraries; keep all indexing in-country.+〗 | 〖+Yes+〗 |
| 〖+Safety / moderation+〗 | 〖+Open policy-filter and content-classification models for prohibited content and child safeguarding; pair with human review for learner-facing content.+〗 | 〖+Yes+〗 |
| 〖+Observability+〗 | 〖+Open metrics/logging and dashboard stacks for latency, availability, error rates; feed the M&E sheet (Appendix E).+〗 | 〖+Yes+〗 |
```

## Appendix G: Open-Source Options Scan (dated, vendor-neutral) › G.3 RAG, safety and observability (categories with examples)
- **New:** Selection still follows national procurement rules, licence checks, security due diligence and evaluation against local language and curriculum requirements. Licence labels above are indicative and must be reconfirmed at the version actually deployed.

## Appendix H: Freshness Register
- **New:** Time-sensitive claims in this revision and when they should be re-checked. The model/tool landscape moves fastest and is reviewed most often.

```
[table under: Appendix H: Freshness Register]
| Item | As of | Review by | Owner / source |
| 〖+SLM families & sizes (Appendix G.1, §6.4)+〗 | 〖+Jun 2026+〗 | 〖+Dec 2026+〗 | 〖+Technical lead; vendor model cards+〗 |
| 〖+Serving runtimes (Appendix G.2)+〗 | 〖+Jun 2026+〗 | 〖+Dec 2026+〗 | 〖+Technical lead; project docs+〗 |
| 〖+Edge device throughput (§6.4 tokens/sec, RAM)+〗 | 〖+Jun 2026+〗 | 〖+Dec 2026+〗 | 〖+Technical lead; pilot benchmarks+〗 |
| 〖+Licence labels (Appendix G)+〗 | 〖+Jun 2026+〗 | 〖+Sep 2026+〗 | 〖+Procurement/legal; official licences+〗 |
| 〖+UNESCO AI Competency Frameworks (§7)+〗 | 〖+2024+〗 | 〖+Jun 2027+〗 | 〖+Policy lead; UNESCO+〗 |
| 〖+African Union Continental AI Strategy (§7)+〗 | 〖+Jul 2024+〗 | 〖+Jun 2027+〗 | 〖+Policy lead; AU+〗 |
| 〖+Retention/redaction thresholds (Appendix F)+〗 | 〖+Jun 2026+〗 | 〖+Per pilot+〗 | 〖+Data protection officer; national law+〗 |
| 〖+M&E example targets (Appendix E)+〗 | 〖+Jun 2026+〗 | 〖+Month 6 / 12+〗 | 〖+M&E lead; pilot baselines+〗 |
```

## Appendix H: Freshness Register › Sources for new factual claims (dated)
- **New:** • UNESCO AI Competency Framework for Students (2024) — accessed June 2026.
- **New:** • African Union, Continental AI Strategy (July 2024) — accessed June 2026.
- **New:** • Google Developers Blog — Gemma 3 270M (2025) / Gemma releases — accessed June 2026.
- **New:** • Ollama model library (sizes, families) — accessed June 2026.
- **New:** • Red Hat — vLLM or llama.cpp: choosing an inference engine (2025) — accessed June 2026.
- **New:** • Stratosphere Lab — LLMs on Raspberry Pi 5 (2025) — accessed June 2026.
- **New:** Licences and exact model behaviour must be reconfirmed at the version deployed; treat all model/tool entries as illustrative and validate in pilots.