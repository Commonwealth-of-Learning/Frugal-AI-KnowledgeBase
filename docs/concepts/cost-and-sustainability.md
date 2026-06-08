---
description: Why Frugal AI is about predictable cost and sustainability, with an illustrative total-cost comparison and the energy case for local models.
icon: leaf
---

# Cost and sustainability

Frugal AI is not cheap AI. Cost matters, but as one part of sovereignty: predictable spending, no per-seat dependency, and lower energy use over time.

## An illustrative cost comparison

The figures below are illustrative, not a benchmark or a quote. They show how to compare a local service with a cloud subscription. Substitute local prices and real usage before drawing any conclusion.

Assume, for illustration only:

- a one-time local hardware cost of about US$1,000, used over three years, which is about US$28 per month;
- modest electricity for a desktop-class machine;
- a cloud assistant at about US$20 per user per month.

For 20 staff, the cloud subscription is about US$400 per month, or about US$14,400 over three years. The local machine is about US$28 per month plus electricity, shared across all users, and that figure stays roughly flat as more people use the same machine, while subscription cost rises with every seat.

This is a planning sketch, not a benchmark. Real figures depend on hardware, electricity, the model, usage, and the capability each option provides. A local model and a frontier cloud model are not equal in capability, which is why the [gateway](gateway-layer.md) allows controlled cloud burst for the few tasks that need it.

## The energy case

Local small models draw far less power per request than frontier models in large data centres, and a desktop-class machine runs on ordinary power. For institutions in low-connectivity or constrained-grid settings, lower and more predictable energy use is part of sustainability, alongside less electronic waste from reusing modest hardware over several years. These are qualitative points; measure local energy use before making efficiency claims.

## How this connects

Predictable cost and sustainability are why the knowledge base starts at the frugal floor in [The Frugal AI stack](how-the-stack-fits-together.md) and adds layers and cloud burst only when a task needs them. The reference architecture's monitoring section tracks cost predictability and the share of inference processed locally.

## Related pages

- [The Frugal AI stack](how-the-stack-fits-together.md)
- [Frugal AI principles](frugal-ai-principles.md)
- [Gateway layer](gateway-layer.md)
