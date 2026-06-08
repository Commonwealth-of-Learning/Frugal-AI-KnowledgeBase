---
description: The application layer — what people use, with agents as a subtype that needs two kinds of governance.
icon: shapes
---

# Application layer

This page describes the Application layer of [The Frugal AI stack](how-the-stack-fits-together.md). The application layer is what a person actually uses, built on the layers below it and governed at the gateway.

## What applications are

Applications turn the lower layers into something a person uses for a task: a chat service, a search interface, a math tutor, or a coding agent. An application uses only the layers it needs. The [local AI chat service](../getting-started/offline-chat-service.md) uses inference alone; the [math tutor](../getting-started/math-tutor.md) adds orchestration; a coding agent adds more autonomy still.

## Agents are a subtype

An agent is an application that can take steps on its own: it plans, calls tools, edits files, or runs commands, rather than only answering. Agents are the most capable application type and the most demanding to govern, because their actions have real effects. Chat services and assistants are applications; an agent is an application that acts. A coding agent has a second role: a local team uses it to build and maintain the rest of the stack — writing tools, configurations, and components — which is how the institution grows its own capacity.

## Two governance surfaces

An agent has to be controlled in two different places, and they are easy to confuse.

- What the agent does locally: editing files, running commands. These are real side effects, governed by the application's own controls — a review step before changes, a scoped working directory, and human approval.
- What leaves the institution: the model calls the application makes. These are governed at the gateway — redaction, approved destinations, and audit logging, with any cloud burst inside the envelope.

The gateway governs egress; the application governs its own actions. A safe agent needs both.

## Frugal practice

Start with the least autonomous application that does the job. Use a review-first mode, scope the agent to a working directory, and require approval for actions with side effects. Route model calls through the gateway so governance stays in one place.

## First agent: the coding agent

The [coding agent](../getting-started/coding-agent.md) guide runs OpenCode, an open-source coding agent, on the local stack. It shows both governance surfaces in practice: the agent's actions are gated by review and permissions, and its model calls go through the gateway.

## Related pages

- [The Frugal AI stack](how-the-stack-fits-together.md)
- [Coding agent](../getting-started/coding-agent.md)
- [Application: OpenCode](../components/applications/opencode.md)
- [Gateway layer](gateway-layer.md)
