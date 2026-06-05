# Workflow Direct Stage Links Runtime Smoke

Status: implemented.

Phase marker: workflow direct stage links runtime smoke v0.

## Purpose

Record local Docker PostgreSQL plus live FastAPI HTTP evidence that workflow direct stage links are created and exposed through the lineage endpoint.

This smoke verifies both:

- `db/migrations/023_workflow_stage_links.sql` applies on the local Docker database
- `POST /workflow-runs/execute-preview` creates direct stage links visible from `GET /workflow-runs/{id}/lineage`

## Environment

```text
Docker PostgreSQL
db_health=healthy
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
FastAPI: http://127.0.0.1:8010
```

## Migration Evidence

```text
Applied migrations: 21
Pending migrations: 1
pending 023_workflow_stage_links.sql
Applied migrations: 21
Pending migrations: 1
applied 023_workflow_stage_links.sql
Applied migrations: 22
Pending migrations: 0
```

## HTTP Smoke

Request sequence:

```text
POST /workflow-runs/execute-preview
GET /workflow-runs/{id}/lineage
```

Observed response summary:

```json
{
  "workflow_run_id":  "ddc3c6b3-b895-478f-862d-0120632bcc82",
  "workflow_status":  "completed",
  "lineage_boundary":  "derived_read_model_with_direct_workflow_stage_links",
  "direct_stage_link_count":  3,
  "link_types":  "evidence_to_report,evidence_to_noise_gate,noise_gate_to_report",
  "warning_codes":  "derived_read_model_boundary,local_workflow_scope,direct_stage_link_table",
  "persistence_boundaries":  "workflow_created_records_only_not_standalone_payload_lineage"
}
```

## Boundary

This is local Docker PostgreSQL plus live FastAPI HTTP evidence only.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not distributed tracing.

It is not hosted observability.

It is not autonomous workflow execution.

It is not product-complete.

Standalone gate/report endpoints remain payload-only unless they create explicit stage links.

## Verification Commands

```powershell
docker compose up -d db
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55432/noiseproof'
uv run --project apps/api python -m app.migration_runner --status
uv run --project apps/api python -m app.migration_runner
uv run --project apps/api python -m app.migration_runner --status
cd apps/api
uv run uvicorn app.main:app --host 127.0.0.1 --port 8010
```

Then call:

```text
POST http://127.0.0.1:8010/workflow-runs/execute-preview
GET http://127.0.0.1:8010/workflow-runs/{id}/lineage
```
