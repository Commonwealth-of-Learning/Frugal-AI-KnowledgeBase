---
description: Build a private local AI chat service with Ollama, Qwen3.5-9B, and Open WebUI.
icon: comments
---

# Local AI chat service

This guide builds a private local AI chat service with Ollama, Qwen3.5-9B, and Open WebUI. It is a development path for learning how the first Frugal AI stack works before pilot or production decisions are made.

{% hint style="info" %}
Expected time: about 30 minutes if Docker and Ollama are already installed.
{% endhint %}

## Component map

| Component | Page | Role |
| --- | --- | --- |
| Hardware | [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) | Defines the memory budget for the path. |
| Environment | [Development environment](../components/environments/development.md) | Sets expectations for a single-user local setup. |
| Runtime | [Ollama](../components/runtimes/ollama.md) | Runs the model and provides the local API. |
| Model | [Qwen3.5-9B](../components/models/qwen-3.5-9b.md) | Provides the chat capability. |
| Framework | [Open WebUI](../components/frameworks/open-webui.md) | Provides the browser chat interface. |
| Operations | [Local AI chat service operations](../operations/open-webui-ops.md) | Keeps the service healthy after setup. |

## Prerequisites

- Docker Desktop is installed and running.
- Ollama is installed.
- 20 GB of free disk space is available.
- A terminal and browser are available on the same machine.

## 1. Start Ollama

Start the Ollama service:

```bash
ollama serve
```

On macOS, Ollama may already be running as a menu bar app. If the command says the address is already in use, leave the existing service running and continue.

Check the local API:

```bash
curl http://localhost:11434/api/tags
```

## 2. Pull the model

Pull the 9B model:

```bash
ollama pull qwen3.5:9b
```

Ollama currently lists `qwen3.5:9b` at about 6.6 GB with a 256K context window. This guide uses a smaller 8K context for a comfortable development setup on a 24 GB Mac.

## 3. Create a development model profile

Create a local model profile with a smaller context window.

Create `/tmp/Modelfile-qwen3.5-dev` with this content:

```text
FROM qwen3.5:9b
PARAMETER num_ctx 8192
```

Create the profile:

```bash
ollama create qwen3.5-dev -f /tmp/Modelfile-qwen3.5-dev
```

Test it:

```bash
ollama run qwen3.5-dev "Explain Frugal AI in two short sentences."
```

## 4. Start Open WebUI

Run Open WebUI in Docker:

```bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

Open [http://localhost:3000](http://localhost:3000).

On first launch, create the local admin account. This account is for the local Open WebUI instance.

## 5. Select the model

In Open WebUI:

1. Open the model selector.
2. Choose `qwen3.5-dev`.
3. Send a short test message.

If the model does not appear, check that Ollama is running:

```bash
ollama ps
```

Open WebUI should connect to Ollama at `http://host.docker.internal:11434` when running in Docker Desktop.

## Verify

| Check | Expected result |
| --- | --- |
| Open WebUI loads | `http://localhost:3000` opens in the browser. |
| Model appears | `qwen3.5-dev` is available in the model selector. |
| Chat works | A short prompt returns a response. |
| Multi-turn chat works | The model can answer a follow-up in the same conversation. |
| Memory remains comfortable | Expected total stack use is about 8 GB, depending on Docker and context use. |

{% hint style="warning" %}
The memory and speed values in this guide are expected development values, not a formal benchmark. Check the machine with `ollama ps` and Activity Monitor.
{% endhint %}

## Troubleshooting

| Problem | Check | Fix |
| --- | --- | --- |
| Open WebUI cannot connect to Ollama | `curl http://localhost:11434/api/tags` | Start or restart Ollama, then restart Open WebUI. |
| No model appears | `ollama list` | Confirm `qwen3.5-dev` exists. Re-run the model profile step if needed. |
| Responses are slow | Activity Monitor memory pressure | Close memory-heavy apps or reduce context size. |
| Port 3000 is in use | `lsof -i :3000` | Run Open WebUI on another host port, such as `-p 3001:8080`. |
| Container exits | `docker logs open-webui` | Check Docker Desktop is running and recreate the container if needed. |

## Stop and restart

Stop the browser interface:

```bash
docker stop open-webui
```

Start it again:

```bash
docker start open-webui
```

Restart it after a configuration change:

```bash
docker restart open-webui
```

To unload the model from memory:

```bash
ollama stop qwen3.5-dev
```

## Next step

Use [Local AI chat service operations](../operations/open-webui-ops.md) for updates, backup, restore, and routine health checks.
