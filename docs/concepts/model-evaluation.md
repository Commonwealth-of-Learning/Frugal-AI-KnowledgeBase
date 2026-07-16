---
description: Guidance and tooling for evaluating, selecting, and benchmarking open-weight models — under development.
icon: gauge-high
---

# Model evaluation and benchmarking

This page will gather the knowledge base's guidance and tooling for evaluating, selecting, and benchmarking open-weight models: how to weigh a model against the memory band, hardware fit, context length, and language coverage a task needs, and how to keep those judgements measured rather than assumed.

It is under development. Until it fills in, the comparison lives in the [Inference layer](inference-layer.md): the [model comparison table](inference-layer.md#choose-a-model) and the three model cards are the current guidance, and the [reference architecture](../reference/sovereign-education-ai-reference-architecture.md) sets the selection criteria for a public deployment.

## Planned contents

- A benchmarking method that scores a model over memory band, hardware fit, and context length against the documented paths, with local measurement rather than source-listed figures.
- Evaluation against local-language and curriculum samples, extending the [shared model cautions](inference-layer.md#shared-model-cautions).
- The interactive open-weight model comparison tool (further work).
- Worked comparisons that keep the model cards and the comparison table in step as new models arrive.
