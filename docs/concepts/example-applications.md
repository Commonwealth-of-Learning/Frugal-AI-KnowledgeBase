---
description: How the same Frugal AI layers support different education applications, from a math tutor to a curriculum knowledge assistant.
icon: table-cells
---

# Example applications

The layered stack is general: the same frugal floor supports many education applications, with different layers added above it. This page is a menu of worked and planned examples. Each grows from beginner to advanced as the layers are added, and new rows are filled in only when their guides exist.

## The matrix

Every example starts from the same beginner floor — the [local AI chat service](../getting-started/offline-chat-service.md) — and diverges above it.

| Application | Beginner (shared floor) | Intermediate | Advanced |
| --- | --- | --- | --- |
| Math tutor | Local chat | [Math tutor](../getting-started/math-tutor.md): a tool computes exactly | [Manim animator](../getting-started/manim-animator.md): an agent animates the result |
| Curriculum knowledge assistant | Local chat | [Curriculum knowledge assistant](../getting-started/curriculum-assistant.md): RAG over approved documents on Dify | Dify multi-step workflows at pilot scale *(further work)* |
| Administrative helpdesk | Local chat | A tool-using assistant for routine staff tasks *(further work)* | Agent workflows with human approval *(further work)* |

The math-tutor row is built end to end, and the curriculum knowledge assistant's intermediate cell is now built (RAG on Dify); its advanced cell and the helpdesk row remain planned. Cells stay marked *further work* until their guides exist.

## What the matrix shows

Two lessons. First, the **Orchestration layer is substitutable**: the math tutor uses a simple Open WebUI tool, while the curriculum assistant will use Dify, a heavier workflow platform with built-in retrieval. Different substrates, the same layer, each chosen to fit the task. Second, **flexibility is frugal**: every example reuses the lower layers, so a new application is mostly new work at the top, not a new stack.

## Localise every example

A Frugal AI application becomes locally owned when it is adapted to its context: aligned to the national curriculum's topics and sequence, written with local names, places, and examples, and used in the local language, which the models support across many. The [math tutor](../getting-started/math-tutor.md) shows this in practice. Localisation applies to every row of the matrix; see the language principle in [Frugal AI principles](frugal-ai-principles.md).

## Related pages

- [The Frugal AI stack](how-the-stack-fits-together.md)
- [Math tutor](../getting-started/math-tutor.md)
- [Frugal AI principles](frugal-ai-principles.md)
