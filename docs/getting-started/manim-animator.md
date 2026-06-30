---
description: Use the coding agent to generate and render Manim animations that illustrate a mathematics concept, under review.
icon: film
---

# Manim animator

This guide uses the [coding agent](coding-agent.md) to generate and render [Manim](https://www.manim.community/) animations that illustrate a mathematics concept — the animated companion to the [math tutor](math-tutor.md). It is the most advanced build in the knowledge base: an agent that writes code and runs a renderer, using a stronger model through the gateway for the hard code generation.

{% hint style="warning" %}
Level: advanced. Expected time: about 45 minutes, plus the Manim install. This is a development path. The agent writes files and runs a renderer, so it works under review and scoped permissions. Generating correct animation code is demanding, and a small local model will often fail, which is why this build uses a stronger model through controlled cloud burst.
{% endhint %}

## Why this is the hard case

A math tutor explains; an animator shows. Producing a correct Manim scene means writing real Python against a specific API and rendering it — the work a coding agent is built for, and the work where a small local model is weakest. This build is honest about that: it pairs the [coding agent](coding-agent.md) with a stronger model reached through the [gateway](ai-gateway.md), and keeps a person in the loop.

## Fit and limits

- **Good for** — Generating and rendering short Manim animations for a mathematics concept, reviewed before use.
- **Not for** — Unattended generation, learner-facing release without review, or reliable output from a small local model.
- **Governance** — Tier 1 (high-risk, learner-facing): a teacher reviews the animation before learner use. Two surfaces: the agent's local actions (write and render) and its model calls through the gateway.
- **Caution** — Manim's render stack (LaTeX, ffmpeg) is heavy, and animation code often needs human correction.

## Prerequisites

- The [coding agent](coding-agent.md) is set up, with OpenCode pointed at the gateway.
- The [gateway](ai-gateway.md) has a controlled cloud-burst model configured, for the code generation.
- Manim and its system dependencies are installed; see the Manim documentation.

## Component map

| Layer | This build uses |
| --- | --- |
| Application | OpenCode coding agent, producing a Manim scene |
| Gateway | [LiteLLM](../components/gateways/litellm.md), routing to a stronger model by controlled cloud burst |
| Inference | A stronger coding model for generation; a local model for routine edits |
| Infrastructure | [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) |

## 1. Install Manim

Install Manim and its system dependencies for the platform; see the [Manim installation guide](https://docs.manim.community/en/stable/installation.html). For example, with pip:

```bash
pip install manim
```

Check it:

```bash
manim --version
```

## 2. Select a capable model

Generating Manim code reliably needs a stronger model than the first local path. In OpenCode, select the gateway's cloud-burst model for this work, so the hard generation is governed by the gateway through redaction, an approved destination, and audit logging, while routine edits can stay on the local model. Keep code-generation prompts free of personal data.

## 3. Generate a scene in review-first mode

Launch OpenCode in a project directory and start in the Plan agent. Ask for a short animation of a concept, for example animating the area under the curve of x squared from 0 to 2. Review the proposed scene, then switch to the Build agent to write the file; with `edit` and `bash` set to ask, each write and render waits for approval.

## 4. Render and review

Let the agent render the scene at low quality first:

```bash
manim -ql scene.py SquareArea
```

Open the rendered file, check the animation against the concept, and correct or re-prompt as needed. A teacher reviews the animation before any use with learners.

## Verify

| Check | Expected result |
| --- | --- |
| Model is capable | The agent produces a Manim scene that imports and runs. |
| Render works | `manim -ql` produces a video file without errors. |
| Actions are gated | Writing the scene and running the render wait for approval. |
| Reviewed | The animation is treated as a draft for teacher review. |

## Governance and review

This build sits in Tier 1 (high-risk, learner-facing) of the risk-tiered teacher-in-the-loop in the [sovereign education-AI reference architecture](../reference/sovereign-education-ai-reference-architecture.md): because the animation reaches learners, a teacher approves it before release. It also carries the Application-layer governance surfaces, described in the [Application layer](../concepts/application-layer.md): the agent's local actions are gated by Plan mode, scoped permissions, and human approval; its model calls are governed by the gateway, including the controlled cloud burst used for generation; and no network-reaching tools are added beyond the renderer it runs locally.

## Troubleshooting

| Problem | Check | Fix |
| --- | --- | --- |
| The render fails on text or LaTeX | System dependencies | Install the LaTeX and ffmpeg dependencies Manim needs; see the Manim documentation. |
| The generated scene does not run | Model strength | Use the stronger cloud-burst model for generation; small local models often produce broken scenes. |
| The agent renders without asking | Permissions | Set `bash` to ask in OpenCode, or work in the Plan agent first. |

## Next step

This completes the through-line: a local [chat service](offline-chat-service.md), a [math tutor](math-tutor.md) that computes exactly, the [gateway](ai-gateway.md) that governs any cloud burst, and an agent that animates the result. Use [Local AI chat service operations](../operations/open-webui-ops.md) to operate the stack.
