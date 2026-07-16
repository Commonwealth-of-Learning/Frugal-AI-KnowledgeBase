---
description: Use the coding agent to storyboard, generate, and render Manim animations that illustrate a mathematics concept, under review.
icon: film
---

# Manim animator

This guide uses the [coding agent](coding-agent.md) to generate and render [Manim](https://www.manim.community/) animations that illustrate a mathematics concept — the animated companion to the [math tutor](math-tutor.md). It is the most advanced build in the knowledge base: an agent that writes code and runs a renderer, using a stronger model through the gateway for the hard code generation.

{% hint style="warning" %}
Level: advanced. Expected time: about 60 minutes, plus the Manim install. This is a development path. The agent writes files and runs a renderer, so it works under review and scoped permissions. Generating correct animation code is demanding, and a small local model will often fail, which is why this build uses a stronger model through controlled cloud burst.
{% endhint %}

## Why this is the hard case

A math tutor explains; an animator shows. Producing a correct Manim scene means writing real Python against a specific API and rendering it — the work a coding agent is built for, and the work where a small local model is weakest. This build is honest about that: it pairs the [coding agent](coding-agent.md) with a stronger model reached through the [gateway](ai-gateway.md), and keeps a person in the loop.

The workflow adapts the pattern documented in [Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim)'s [HERMES workflow](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/HERMES_LEARNS_MANIM.md) (MIT licence): the agent works as a tool-using collaborator in a repository, loading a written skill, staging the work from storyboard to scene code, rendering, and inspecting the rendered result against explicit quality gates rather than trusting that a file exists. Math-To-Manim's own pipelines run on hosted proprietary models; the pattern is model-independent, and this guide applies it with open components — OpenCode, with models governed through the gateway. Its fuller pipeline stages typed artifacts from intent to storyboard to scene code to render manifest, a structure a team can grow into.

## Fit and limits

- **Good for** — Generating and rendering short Manim animations for a mathematics concept, reviewed before use.
- **Not for** — Unattended generation, learner-facing release without review, or reliable output from a small local model.
- **Governance** — Tier 1 (high-risk, learner-facing): a teacher reviews the animation before learner use. Two surfaces: the agent's local actions (write and render) and its model calls through the gateway.
- **Caution** — Manim's render stack (LaTeX, ffmpeg) is heavy, and animation code often needs human correction.

## Prerequisites

- The [coding agent](coding-agent.md) is set up, with OpenCode pointed at the gateway.
- The [gateway](ai-gateway.md) has a controlled cloud-burst model configured for the code generation — an approved external provider and key the institution supplies, since the gateway's cloud-burst step is a template. This is the one build in the series that does not run fully locally.
- Manim and its system dependencies are installed; see the Manim documentation.

## Component map

| Layer | This build uses |
| --- | --- |
| Application | OpenCode coding agent, producing a Manim scene |
| Gateway | [LiteLLM](../components/gateways/litellm.md), routing to a stronger model by controlled cloud burst |
| Inference | A stronger coding model for generation; a local model for routine edits |
| Infrastructure | [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) |

## 1. Install Manim

Install Manim and its system dependencies for the platform; see the [Manim installation guide](https://docs.manim.community/en/stable/installation.html). For example, with pip in a virtual environment so the install does not touch the system Python:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install manim
```

Check it:

```bash
manim --version
```

## 2. Select a capable model

Generating Manim code reliably needs a stronger model than the first local path. In OpenCode, select the gateway's cloud-burst model for this work, so the hard generation is governed by the gateway through redaction, an approved destination, and audit logging, while routine edits can stay on the local model. Keep code-generation prompts free of personal data.

## 3. Teach the agent Manim in AGENTS.md

The [coding agent](coding-agent.md) guide introduced `AGENTS.md` as the project's instructions to the agent. For animation work, extend it into a small Manim [skill](../reference/glossary.md): the facts and procedure the agent should follow instead of guessing them. Keep it short, and review it like any other file.

```markdown
# Manim notes for the agent

- One scene class per file; name the class after the concept.
- Propose a plain-language storyboard and wait for approval before writing code.
- Render at low quality first: manim -ql <file> <SceneClass>.
- After rendering, report what the animation shows, step by step, for review.
- Text must stay readable, and elements must not overlap or leave the frame.
```

A written skill compounds: each correction a reviewer makes can be folded back into the notes, so the next animation starts from what the team already learned.

## 4. Storyboard, then build

Launch OpenCode in the project directory and start in the Plan agent. Ask for a short animation of a concept, for example animating the area under the curve of x squared from 0 to 2. The skill above has the agent propose a storyboard first: the scenes, the on-screen text, and what moves, in plain language. The storyboard is the cheapest review point in the workflow — a teacher can correct a wrong emphasis or a misleading visual before any code exists. Approve the storyboard, then switch to the Build agent to write the scene; with `edit` and `bash` set to ask, each write and render waits for approval.

## 5. Render and inspect

Let the agent render the scene at low quality first:

```bash
manim -ql scene.py AreaUnderCurve
```

Open the rendered file and inspect it against explicit gates, adapted from the HERMES workflow's review checklist:

- the animation shows the concept correctly, in the storyboard's order;
- on-screen text is readable at the size learners will watch;
- elements do not overlap, drift, or leave the frame;
- the pacing leaves time to follow each step.

Correct or re-prompt on the specific defect, and fold recurring corrections back into the Manim notes. A teacher reviews the animation before any use with learners.

## Verify

| Check | Expected result |
| --- | --- |
| Storyboard comes first | The agent proposes a plain-language storyboard and waits for approval before writing code. |
| Model is capable | The agent produces a Manim scene that imports and runs. |
| Render works | `manim -ql` produces a video file without errors. |
| Actions are gated | Writing the scene and running the render wait for approval. |
| Reviewed | The animation passes the inspection gates and is treated as a draft for teacher review. |

## Governance and review

This build sits in Tier 1 (high-risk, learner-facing) of the risk-tiered teacher-in-the-loop in the [sovereign education-AI reference architecture](../reference/sovereign-education-ai-reference-architecture.md): because the animation reaches learners, a teacher approves it before release. It also carries the Application-layer governance surfaces, described in the [Application layer](../concepts/application-layer.md): the agent's local actions are gated by Plan mode, scoped permissions, and human approval; its model calls are governed by the gateway, including the controlled cloud burst used for generation; and no network-reaching tools are added beyond the renderer it runs locally. In this development path the Tier 1 approval gate is procedural: the teacher operates the single-user interface and learners have no direct access. The reference architecture expects a technically enforced approval gate for learner-facing deployment, which is further work before any learner-facing pilot.

The staged workflow adds an early review point: the storyboard is approved before code is written, so teacher judgement enters at the cheapest stage. The `AGENTS.md` skill the agent follows is itself a reviewed file, and corrections folded back into it keep review effort from repeating.

## Troubleshooting

| Problem | Check | Fix |
| --- | --- | --- |
| The render fails on text or LaTeX | System dependencies | Install the LaTeX and ffmpeg dependencies Manim needs; see the Manim documentation. |
| The generated scene does not run | Model strength | Use the stronger cloud-burst model for generation; small local models often produce broken scenes. |
| The agent renders without asking | Permissions | Set `bash` to ask in OpenCode, or work in the Plan agent first. |
| Text overlaps or is unreadable | Inspection gates | Re-prompt naming the specific defect; low-quality renders make defects cheap to find and fix. |

## Next step

This completes the through-line: a local [chat service](offline-chat-service.md), a [math tutor](math-tutor.md) that computes exactly, the [gateway](ai-gateway.md) that governs any cloud burst, and an agent that animates the result. Use [Local AI chat service operations](../operations/open-webui-ops.md) to operate the stack.
