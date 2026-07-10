---
description: Build a math tutor that gives exact answers by calling a computation tool, under teacher review.
icon: square-root-variable
---

# Math tutor

This guide turns the local AI chat service into a math tutor that gives exact answers by calling a computation tool, instead of relying on the model's own arithmetic. It is the first [Orchestration layer](../concepts/orchestration-layer.md) build: the same hardware, runtime, and model as the chat service, with one local tool added and a teacher reviewing the output. It is also the knowledge base's working answer to the annex's Frugal AI Challenge framing — a maths tutor that computes locally and offline (see the [reference architecture](../reference/sovereign-education-ai-reference-architecture.md)).

{% hint style="info" %}
Level: intermediate. Expected time: about 20 minutes once the [Local AI chat service](offline-chat-service.md) is running. This is a development path; a teacher reviews explanations before they reach learners.
{% endhint %}

## Why a tool

Small local models are unreliable at arithmetic and algebra; they often produce confident but wrong numbers. The orchestration layer fixes this by letting the model call a tool for the calculation and explain the result it gets back. That is the point of the layer: the model reasons and explains, while the tool computes exactly.

## Fit and limits

- **Good for** — Exact arithmetic, algebra, and calculus in a tutoring chat, with the model explaining each step.
- **Not for** — Learner-facing use without review, or trusting the model's own mental arithmetic.
- **Governance** — Tier 1 (learner-facing): a teacher approves explanations before any learner use.
- **Caution** — The tool fixes the calculation, not the teaching; a correct result can still be explained poorly.

## Prerequisites

- The [Local AI chat service](offline-chat-service.md) is built and running, with Ollama, Gemma 4 12B, and Open WebUI.

## Component map

| Layer | This build uses |
| --- | --- |
| Application | [Open WebUI](../components/applications/open-webui.md) |
| Orchestration | An Open WebUI tool that computes with SymPy |
| Inference | [Ollama](../components/runtimes/ollama.md) with [Gemma 4 12B](../components/models/gemma-4-12b.md) |
| Infrastructure | [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) |

The gateway stays local-only: nothing leaves the machine.

## 1. Add the computation tool

In Open WebUI, open Workspace, then Tools, then add a new tool. The example computes exactly with SymPy; the `requirements` line installs SymPy when the tool is saved.

```python
"""
title: Exact mathematics
description: Evaluate, simplify, and solve mathematical expressions exactly with SymPy.
version: 0.1.0
licence: MIT
requirements: sympy
"""

import sympy


class Tools:
    def compute(self, expression: str) -> str:
        """
        Evaluate, simplify, or solve a mathematical expression exactly.
        :param expression: A SymPy expression, for example "integrate(x**2, x)" or "solve(x**2 - 4, x)".
        """
        try:
            return str(sympy.sympify(expression))
        except Exception as error:
            return f"Could not evaluate the expression: {error}"
```

Save the tool. Import or run only tool code the institution has written or reviewed, because a tool runs as code on the host.

## 2. Enable the tool for the model

Open Workspace, then Models, then edit the model used by the chat service. In the Tools section, enable the computation tool and save. If tools are not called reliably, set Function Calling to Native in the model's advanced parameters.

## 3. Tutor and review

Start a chat, select the tool with the plus icon, and ask a question that needs exact mathematics, such as solving an equation or integrating a function. The model calls the tool for the calculation and explains the result. A teacher reviews the explanation before any use with learners.

## Verify

| Check | Expected result |
| --- | --- |
| Tool is enabled | The computation tool is selectable in chat through the plus icon. |
| Tool computes | A question such as "solve x squared minus 4 equals 0" returns the exact result from the tool, not a guess. |
| Explanation is reviewed | Output is treated as a draft for teacher review before any learner use. |

## Governance and review

This build sits in Tier 1 (high-risk, learner-facing) of the risk-tiered teacher-in-the-loop in the [sovereign education-AI reference architecture](../reference/sovereign-education-ai-reference-architecture.md): because explanations reach learners, a teacher approves each one before release. The tool is read-only with no side effects, and the gateway stays local-only. Tools with side effects, automatic learner-facing output, and external routing are out of scope here.

Approval assumes [AI literacy](../reference/glossary.md): the reviewing teacher knows the model can guess arithmetic and fabricate steps, and checks the explanation against the tool's exact result before release.

## Troubleshooting

| Problem | Check | Fix |
| --- | --- | --- |
| The model answers without the tool | Tool is enabled | Enable the tool for the model, or select it with the plus icon, and set Function Calling to Native. |
| Saving the tool is slow | Requirements install | The `requirements: sympy` line installs SymPy on save, which pauses the interface briefly. |
| The tool returns an error | Expression format | Use SymPy syntax, for example `solve(x**2 - 4, x)`, rather than prose. |

## Localise it

A math tutor is most useful when it fits its context. Align the examples to the national curriculum's topics and sequence, write word problems with local names, places, and currency, and prompt in the local language — the model supports many. Adapting the examples locally is part of the Frugal AI approach.

## Next step

For genuinely hard problems, route the tutor through the [AI gateway](ai-gateway.md) and burst to a stronger model, redacted first. For animated explanations, a coding agent can generate and render them; see the [Manim animator](manim-animator.md). Use [Local AI chat service operations](../operations/open-webui-ops.md) to manage tools and review use.
