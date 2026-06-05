# Ops Dashboard Anchor GET Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: ops dashboard anchor GET runtime smoke v0.

## Purpose

Record local Docker PostgreSQL plus live FastAPI HTTP evidence that clickable `GET /ops/dashboard` anchors marked with `data-method="GET"` resolve as inspection routes in a fresh database runtime.

## Runtime Setup

Commands:

```text
$env:POSTGRES_PORT='55435'
docker compose -p noiseproof-phase522 config
docker compose -p noiseproof-phase522 up -d db
docker inspect -f '{{.State.Health.Status}}' noiseproof-agent-db
```

Observed:

```text
docker compose rendered only the db service for this run
published DB port: 55435
db health: healthy
```

API command:

```text
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55435/noiseproof'
uv run uvicorn app.main:app --host 127.0.0.1 --port 8101
```

Smoke client:

```text
Python stdlib urllib.request against http://127.0.0.1:8101
```

PowerShell `Invoke-WebRequest` hit a local HTML handling `NullReferenceException` during the first dashboard fetch, so that partial attempt is not used as success evidence.

## Runtime Evidence

Observed result:

```text
all_extracted_dashboard_get_anchors_returned_200: true
post_only_draft_preview_was_not_clickable: true
```

```json
{
  "phase_marker": "ops dashboard anchor GET runtime smoke v0",
  "database_url": "postgresql://noiseproof:noiseproof@localhost:55435/noiseproof",
  "api_base_url": "http://127.0.0.1:8101",
  "health_status_code": 200,
  "health_status": "ok",
  "workflow_status_code": 201,
  "workflow_run_id": "40b0ff6c-4d51-4581-b4c1-ee18ac77b48f",
  "failure_status_code": 201,
  "failure_case_id": "2abdd43e-2c30-46a9-aa20-684936a78155",
  "dashboard_status_code": 200,
  "extracted_anchor_count": 38,
  "unique_anchor_count": 25,
  "all_extracted_dashboard_get_anchors_returned_200": true,
  "post_only_draft_preview_was_not_clickable": true
}
```

Representative resolved hrefs:

```text
/workflow-runs/40b0ff6c-4d51-4581-b4c1-ee18ac77b48f -> 200
/workflow-runs/40b0ff6c-4d51-4581-b4c1-ee18ac77b48f/lineage -> 200
/workflow-runs/40b0ff6c-4d51-4581-b4c1-ee18ac77b48f/proof-bundle -> 200
/failure-cases?workflow_run_id=40b0ff6c-4d51-4581-b4c1-ee18ac77b48f -> 200
/traces/5a0d550f-f751-4944-8fde-0475dcd257e1 -> 200
/evidence-ledgers?status=unsupported -> 200
/noise-gates?decision=blocked -> 200
/reports?status=generated -> 200
```

The server log showed `GET /ops/dashboard` and each extracted inspection route returning `200 OK`.

## Cleanup

Commands:

```text
docker compose -p noiseproof-phase522 down -v
```

Observed:

```text
noiseproof-agent-db stopped and removed
noiseproof-phase522_noiseproof_pgdata removed
noiseproof-phase522_default network removed
```

## Boundary

This is local Docker PostgreSQL plus live FastAPI HTTP evidence only.

It is not hosted deployment evidence.

It is not browser automation evidence.

It is not external reviewer feedback.

It is not a route behavior change.

It is not background automation.

It is not automatic failure-case creation.

It is not complete workflow failure causality.

It is not LLM-backed repair.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
