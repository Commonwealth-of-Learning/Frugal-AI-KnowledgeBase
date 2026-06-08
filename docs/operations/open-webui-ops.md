---
description: Operate, update, back up, and troubleshoot the local AI chat service.
icon: wrench
---

# Local AI chat service operations

This runbook covers routine operation for the local AI chat service built with Open WebUI, Ollama, and the local model profile.

This is a single-machine runbook. It is not a production operations plan.

## Deployment profiles

| Profile | Hardware | Open WebUI image | Ollama location | Status |
| --- | --- | --- | --- | --- |
| Host Ollama | [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) | `ghcr.io/open-webui/open-webui:main` | Host machine at `http://host.docker.internal:11434` | Current first path |
| Integrated Ollama | [NVIDIA DGX Spark](../components/hardware/nvidia-dgx-spark.md) | `ghcr.io/open-webui/open-webui:ollama` | Inside the Open WebUI container | Candidate development and pilot path |

## Start, stop, and restart

| Task | Command |
| --- | --- |
| Start Open WebUI | `docker start open-webui` |
| Stop Open WebUI | `docker stop open-webui` |
| Restart Open WebUI | `docker restart open-webui` |
| Check running containers | `docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"` |

Start Ollama if it is not already running:

```bash
ollama serve
```

On macOS, Ollama may already run as a background app.

## Health checks

| Check | Command | Expected result |
| --- | --- | --- |
| Ollama API responds | `curl http://localhost:11434/api/tags` | JSON response with model data. |
| Model is available | `ollama list` | `qwen3.5` or `qwen3.5-dev` appears. |
| Model is loaded | `ollama ps` | Running model appears after first use. |
| Open WebUI container is running | `docker ps --filter name=open-webui` | Container status is `Up`. |
| Web interface responds | `curl -s -o /dev/null -w '%{http_code}' http://localhost:3000` | `200` or a redirect response. |
| Host Ollama connection is configured | Admin Settings > Connections > Ollama | URL is `http://host.docker.internal:11434`. |

## Update Open WebUI

Back up the `open-webui` volume before an update. Shared or pilot deployments should pin an Open WebUI version and keep a stable `WEBUI_SECRET_KEY`; the `:main` tag is suitable only for local development where manual updates are acceptable.

Pull the latest image:

```bash
docker pull ghcr.io/open-webui/open-webui:main
```

Stop the current container:

```bash
docker stop open-webui
```

Remove the stopped container. The named `open-webui` volume keeps the data:

```bash
docker rm open-webui
```

Recreate the container:

```bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

Confirm it is running:

```bash
docker ps --filter name=open-webui
```

## Back up chat data

Create a backup from the Docker volume. This captures chats, users, settings, uploads, and generated content stored in Open WebUI:

```bash
docker run --rm -v open-webui:/data -v $(pwd):/backup alpine tar czf /backup/openwebui-$(date +%Y%m%d).tar.gz /data
```

Keep backups somewhere appropriate for the data policy. If users enter sensitive information, treat the backup as sensitive too.

## Restore chat data

Stop the container:

```bash
docker stop open-webui
```

Restore the volume from a known backup. This replaces the current Open WebUI volume contents:

```bash
docker run --rm -v open-webui:/data -v $(pwd):/backup alpine sh -c "rm -rf /data/* && tar xzf /backup/openwebui-YYYYMMDD.tar.gz -C /"
```

Start the container:

```bash
docker start open-webui
```

## Tools and functions (orchestration)

Tools and functions add the [Orchestration layer](../concepts/orchestration-layer.md) to the local AI chat service, as used by the [Teacher assistant](../getting-started/teacher-assistant.md). Manage them in Workspace, then Tools, and enable them per model in Workspace, then Models.

A tool is Python that runs inside the Open WebUI process. Import or run only tools the institution has written or reviewed, and treat tool code as code to review rather than configuration. Keep tools dependency-free where possible, because saving a tool with requirements pauses the interface while packages install.

The data-volume backup already captures tool definitions and settings, so back up before changing tools. For teacher-in-the-loop use, review assistant outputs and tool usage periodically. Stronger audit logging and control over external requests belong to the gateway layer, in a later increment.

## Gateway (LiteLLM)

The [AI gateway](../getting-started/ai-gateway.md) runs as a local process on the host and serves an OpenAI-compatible endpoint on port 4000. Open WebUI connects to it at `http://host.docker.internal:4000/v1`.

- Start and stop: run the gateway with its configuration file, and stop the process to take it offline.
- Keys: keep the gateway master key and any approved-provider keys in the host environment, not in a configuration file under version control.
- Redaction services: the Presidio analyser and anonymiser run as local containers; confirm both are running before relying on redaction.
- Audit log: review the gateway log for requests, routes, and masked entities as part of teacher-in-the-loop review.
- Cloud burst: keep external routing off unless a task needs it, and confirm the redaction guardrail applies to every model before enabling it.

## DGX Spark candidate pattern

The DGX Spark pattern uses the Open WebUI image with integrated Ollama, GPU access, and two persistent volumes: one for Open WebUI data and one for Ollama models. Use this as a development or pilot starting point after DGX Spark access, Docker permissions, and monitoring are ready.

Pull the integrated image:

```bash
docker pull ghcr.io/open-webui/open-webui:ollama
```

Start the integrated container:

```bash
docker run -d -p 8080:8080 --gpus=all \
  -v open-webui:/app/backend/data \
  -v open-webui-ollama:/root/.ollama \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:ollama
```

Open [http://localhost:8080](http://localhost:8080) for manual setup. For NVIDIA Sync, expose the service through a custom port such as `12000` and monitor GPU and memory use through the DGX Dashboard before pilot use.

## Cleanup and rollback

Stop and remove the Open WebUI container:

```bash
docker rm -f open-webui
```

Remove an unused development image only after confirming it is no longer needed. Use the same pattern for the integrated `:ollama` image if the DGX Spark candidate setup is being removed:

```bash
docker rmi ghcr.io/open-webui/open-webui:main
```

## Troubleshooting

| Problem | Likely cause | Fix |
| --- | --- | --- |
| Browser cannot open `localhost:3000` | Container is stopped or port changed. | Run `docker ps --filter name=open-webui` and restart the container. |
| Open WebUI cannot see models | Ollama is stopped or the connection URL is wrong. | Start Ollama and check the Open WebUI connection points to `http://host.docker.internal:11434`. |
| Model responses are slow | Memory pressure or too-large context. | Close memory-heavy apps and use the `qwen3.5-dev` 8K profile. |
| Docker says the container name exists | Old container remains after a failed recreate. | Run `docker rm open-webui`, then create it again. |
| Port 3000 is already in use | Another app is using the port. | Run Open WebUI with another host port, such as `-p 3001:8080`. |
| DGX Spark container cannot see the GPU | GPU flag or container runtime is missing. | Recreate the integrated container with `--gpus=all` after Docker GPU access is confirmed. |
| Model list loads slowly | An unreachable Ollama endpoint is configured. | Remove stale endpoints or lower the model-list timeout in the deployment environment. |

## When to move beyond this runbook

Create a stronger operations plan before using this as a shared service. A pilot should define account ownership, backups, update windows, acceptable data, support contacts, and review rules for education use.
