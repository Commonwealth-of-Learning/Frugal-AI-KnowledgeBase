---
description: Build a tool-using teacher assistant on the local AI chat service, with teacher review.
icon: chalkboard-user
---

# Teacher assistant

This guide adds a small tool-using assistant to the local AI chat service, to help a teacher draft materials such as lesson plans and rubrics. It is the first [Orchestration layer](../concepts/orchestration-layer.md) slice: the same hardware, runtime, and model as the chat service, with one local tool added and a teacher reviewing every output.

{% hint style="info" %}
This is a development path. The assistant drafts material for a teacher to review; it does not produce learner-facing content automatically.
{% endhint %}

## Fit and limits

| Question | Answer |
| --- | --- |
| Good for | Drafting lesson plans, rubrics, and other teacher-only material, with a tool the model can call for a task it is unreliable at. |
| Not for | Learner-facing output without review, tools with real side effects, or autonomous multi-step actions. |
| Governance | Operates at the teacher-only tier: a teacher reviews and edits every output before any learner use. |
| Caution | Local tool calling is less reliable than a hosted service. The model may occasionally describe a tool call instead of making it. |

## Prerequisites

- The [Local AI chat service](offline-chat-service.md) is built and running, with Ollama, Qwen3.5-9B, and Open WebUI.
- Qwen3.5-9B is used here because it supports tool calling. A more tool-reliable model can be substituted after local testing.

## Component map

| Layer | This slice uses |
| --- | --- |
| Application | [Open WebUI](../components/frameworks/open-webui.md) |
| Orchestration | Open WebUI tools and functions |
| Inference | [Ollama](../components/runtimes/ollama.md) with [Qwen3.5-9B](../components/models/qwen-3.5-9b.md) |
| Infrastructure | [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) |

The gateway stays local-only: the assistant sends nothing outside the machine.

## 1. Add a tool

In Open WebUI, open Workspace, then Tools, then add a new tool. A tool is a small Python class whose methods the model can call. Each method needs type hints and a docstring, which Open WebUI turns into the description the model sees.

The example below adds one read-only tool that returns the date range for a school term week, a calculation small models often get wrong:

```python
"""
title: Term week dates
description: Returns the start and end date for a school term week.
version: 0.1.0
licence: MIT
"""

from datetime import date, timedelta


class Tools:
    def term_week_dates(self, term_start: str, week: int) -> str:
        """
        Return the Monday-to-Friday date range for a school term week.
        :param term_start: The first Monday of term, as YYYY-MM-DD.
        :param week: The term week number, starting at 1.
        """
        start = date.fromisoformat(term_start) + timedelta(weeks=week - 1)
        end = start + timedelta(days=4)
        return f"Week {week}: {start.isoformat()} to {end.isoformat()}"
```

Save the tool. Import or run only tool code the institution has written or reviewed, because a tool runs as code on the host.

## 2. Enable the tool for the model

Open Workspace, then Models, then edit the model used by the chat service. In the Tools section, enable the new tool and save. Enabling a tool gives the model the option to call it; it does not force a call.

If tools are not called reliably, set Function Calling to Native in the model's advanced parameters.

## 3. Use and review

Start a chat with the model, select the tool with the plus icon next to the message box, and ask a question that needs it, such as drafting a plan for a given term week. A teacher then reviews and edits the draft before any use with learners.

## Verify

| Check | Expected result |
| --- | --- |
| Tool is listed | The new tool appears in Workspace, then Tools. |
| Tool is enabled | The tool is selectable in chat through the plus icon. |
| Tool executes | A question that needs the tool returns a computed result, not a description of a tool call. |
| Review step | Output is treated as a draft for teacher review before any learner use. |

## Governance and review

This assistant operates at the teacher-only tier described in the [sovereign education-AI reference architecture](../reference/sovereign-education-ai-reference-architecture.md):

- a teacher reviews and edits every output before any learner sees it;
- the first tools are read-only and have no side effects;
- the gateway stays local-only, so no prompt or output leaves the machine;
- assistant use and outputs are reviewed periodically as part of operations.

Tools with real side effects, automatic learner-facing output, and external routing are out of scope for this slice. They belong to later increments with stronger controls.

## Troubleshooting

| Problem | Check | Fix |
| --- | --- | --- |
| The model describes a tool call instead of running it | Model advanced parameters | Set Function Calling to Native, and confirm the tool is enabled for the model. |
| The tool is not offered in chat | Workspace, then Models | Enable the tool for the model and save, or select it with the plus icon. |
| The tool errors on a date | Input format | Use an ISO date such as 2026-09-07 for the term start. |
| Saving the tool installs packages | Tool requirements | Keep tools dependency-free where possible; package installs pause the interface. |

## Next step

Use [Local AI chat service operations](../operations/open-webui-ops.md) to manage tools, back up the data volume, and review assistant use.
