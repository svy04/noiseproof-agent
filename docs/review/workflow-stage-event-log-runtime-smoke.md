# Workflow Stage Event Log Runtime Smoke

Status: implemented.

Phase marker: workflow stage event log runtime smoke v0.

## Purpose

Record local Docker PostgreSQL plus live FastAPI HTTP evidence that deterministic workflow stage event rows are created and exposed through workflow detail and proof-bundle read models.

This smoke verifies:

- `db/migrations/024_workflow_stage_events.sql` is applied on the local Docker database
- `POST /workflow-runs/execute-preview` records local stage events for retrieval, Evidence Ledger, Noise Gate, and Report
- `GET /workflow-runs/{id}` exposes `stage_events` and `summary.workflow_stage_event_count`
- `GET /workflow-runs/{id}/proof-bundle` exposes the same stage event count through its detail read model

## Environment

```text
Docker PostgreSQL
db_health=healthy
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
FastAPI: http://127.0.0.1:8011
```

## Migration Evidence

```text
Applied migrations: 23
Pending migrations: 0
applied 024_workflow_stage_events.sql
```

## HTTP Smoke

Request sequence:

```text
POST /workflow-runs/execute-preview
GET /workflow-runs/{id}
GET /workflow-runs/{id}/proof-bundle
```

Observed response summary:

```json
{
  "workflow_run_id":  "a9f3c486-43be-4b66-9cc9-7a0c2240b21c",
  "workflow_status":  "completed",
  "detail_stage_event_count":  4,
  "bundle_stage_event_count":  4,
  "stage_names":  "retrieval,evidence_ledger,noise_gate,report",
  "stage_orders":  "1,2,3,4",
  "stage_statuses":  "completed",
  "event_boundary":  "local_workflow_stage_event_log_not_distributed_tracing"
}
```

## Boundary

This is local Docker PostgreSQL plus live FastAPI HTTP evidence only.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not distributed tracing.

It is not OpenTelemetry.

It is not hosted observability.

It is not autonomous workflow execution.

It is not product-complete.

## Verification Commands

```powershell
docker compose up -d db
docker compose ps
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55432/noiseproof'
uv run --project apps/api python -m app.migration_runner --status
docker exec noiseproof-agent-db psql -U noiseproof -d noiseproof -tAc "select 'applied ' || filename from schema_migrations where filename = '024_workflow_stage_events.sql';"
cd apps/api
uv run uvicorn app.main:app --host 127.0.0.1 --port 8011
```

Then call:

```text
POST http://127.0.0.1:8011/workflow-runs/execute-preview
GET http://127.0.0.1:8011/workflow-runs/{id}
GET http://127.0.0.1:8011/workflow-runs/{id}/proof-bundle
```
