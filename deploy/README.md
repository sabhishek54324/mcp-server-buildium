# Deploying this server over HTTP

The upstream project runs over stdio. These files run the same server as a network service behind a
token gate. **Nothing secret belongs in this folder or in this repository.**

| File | What it does |
| --- | --- |
| `Dockerfile` | Builds the server image from this repository |
| `run_http.py` | Serves the server over HTTP (the project's own entry point uses stdio) |
| `Caddyfile.gate` | Lets through only requests that carry the gate token |
| `docker-compose.prod.yml` | Runs the server and the gate |

## Settings (two files on the host, outside the repository)

`BUILDIUM_ENV_FILE` (default `/etc/buildium-mcp/buildium.env`):

```text
BUILDIUM_CLIENT_ID=...
BUILDIUM_CLIENT_SECRET=...
```

Use a **read-only** Buildium API key (the server has write tools), and the sandbox key first.
`BUILDIUM_BASE_URL` defaults to the sandbox, `https://apisandbox.buildium.com`. Set it to
`https://api.buildium.com` for live data. Optional: `BUILDIUM_CATEGORIES=leases,rentals,tasks` to enable
only some tool categories.

`GATE_ENV_FILE` (default `/etc/buildium-mcp/gate.env`):

```text
MCP_GATE_TOKEN=<at least 24 characters, for example from: openssl rand -hex 24>
```

## Run

```bash
docker compose -f deploy/docker-compose.prod.yml up -d --build
```

The gate listens on `${MCP_BIND:-172.17.0.1}:8767`. Without the token it answers `401`.

## Update

```bash
git pull && docker compose -f deploy/docker-compose.prod.yml up -d --build
```
