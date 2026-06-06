---
description: Operate, update, back up, and troubleshoot the local AI chat service.
icon: wrench
---

# Local AI chat service operations

This runbook covers routine operation for the local AI chat service built with Open WebUI, Ollama, and the local model profile.

This is a single-machine runbook. It is not a production operations plan.

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

## Update Open WebUI

Pull the latest image:

```bash
docker pull ghcr.io/open-webui/open-webui:main
```

Recreate the container while keeping the named data volume:

```bash
docker stop open-webui
docker rm open-webui

docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

## Back up chat data

Create a backup directory:

```bash
mkdir -p ~/open-webui-backups
```

Copy the local database from the container:

```bash
docker cp open-webui:/app/backend/data/webui.db ~/open-webui-backups/webui-$(date +%Y%m%d).db
```

Keep backups somewhere appropriate for the data policy. If users enter sensitive information, treat the backup as sensitive too.

## Restore chat data

Stop the container:

```bash
docker stop open-webui
```

Copy a backup into the container:

```bash
docker cp ~/open-webui-backups/webui-YYYYMMDD.db open-webui:/app/backend/data/webui.db
```

Start the container:

```bash
docker start open-webui
```

## Troubleshooting

| Problem | Likely cause | Fix |
| --- | --- | --- |
| Browser cannot open `localhost:3000` | Container is stopped or port changed. | Run `docker ps --filter name=open-webui` and restart the container. |
| Open WebUI cannot see models | Ollama is stopped or the connection URL is wrong. | Start Ollama and check the Open WebUI connection points to `http://host.docker.internal:11434`. |
| Model responses are slow | Memory pressure or too-large context. | Close memory-heavy apps and use the `qwen3.5-dev` 8K profile. |
| Docker says the container name exists | Old container remains after a failed recreate. | Run `docker rm open-webui`, then create it again. |
| Port 3000 is already in use | Another app is using the port. | Run Open WebUI with another host port, such as `-p 3001:8080`. |

## When to move beyond this runbook

Create a stronger operations plan before using this as a shared service. A pilot should define account ownership, backups, update windows, acceptable data, support contacts, and review rules for education use.
