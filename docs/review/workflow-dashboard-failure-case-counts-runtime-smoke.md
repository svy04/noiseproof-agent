# Workflow Dashboard Failure-case Counts Runtime Smoke

Status: implemented.

Phase marker: workflow dashboard failure-case counts runtime smoke v0.

## Purpose

Verify the workflow dashboard failure-case counts read model against local Docker PostgreSQL plus live FastAPI HTTP.

This smoke proves the dashboard cue added in `docs/review/workflow-dashboard-failure-case-counts.md` works outside the in-memory test repository.

## Runtime Setup

Database:

```powershell
$env:POSTGRES_PORT='55434'
docker compose -p noiseproof-phase514 config
docker compose -p noiseproof-phase514 up -d db
docker compose -p noiseproof-phase514 ps
```

Observed database status:

```text
database status: healthy
published port: 55434 -> 5432
project: noiseproof-phase514
```

The runtime database contained the expected workflow and failure-case tables:

```text
public | workflow_runs | table | noiseproof
public | failure_cases | table | noiseproof
```

API:

```powershell
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55434/noiseproof'
uv run uvicorn app.main:app --host 127.0.0.1 --port 8100
```

## HTTP Flow

The smoke used live HTTP requests against `http://127.0.0.1:8100`.

```text
GET /health -> 200
POST /workflow-runs -> 201
POST /workflow-runs -> 201
POST /failure-cases/workflow-runs/{workflow_run_id} -> 201
GET /ops/dashboard -> 200
```

Observed values:

```json
{
  "health_status": "ok",
  "linked_workflow_status_code": 201,
  "unlinked_workflow_status_code": 201,
  "failure_case_handoff_status_code": 201,
  "dashboard_status_code": 200,
  "workflow_run_id": "2b8586f5-f445-4457-b5c9-3c0dd7105671",
  "unlinked_workflow_run_id": "40c0be51-476a-4b37-84c8-0f6063f289e8",
  "linked_failure_case_id": "bc91f74e-a959-4f50-962d-fe25b17b5096",
  "handoff_boundary": "caller_triggered_workflow_failure_case_persistence",
  "dashboard_contains_linked_failure_cases_header": true,
  "dashboard_contains_read_only_boundary": true,
  "dashboard_contains_linked_failure_case_filter": true,
  "dashboard_omits_unlinked_failure_case_filter": true,
  "dashboard_contains_review_queue_linked_count": true
}
```

Marker summary:

```text
dashboard_contains_linked_failure_cases_header: true
dashboard_contains_read_only_boundary: true
dashboard_contains_linked_failure_case_filter: true
dashboard_omits_unlinked_failure_case_filter: true
dashboard_contains_review_queue_linked_count: true
```

The linked workflow count appeared as:

```text
href="/failure-cases?workflow_run_id=2b8586f5-f445-4457-b5c9-3c0dd7105671">1</a>
```

The unlinked workflow did not emit a failure-case filter link.

## Cleanup

The API server was stopped, then the Phase 514 compose project was removed:

```powershell
docker compose -p noiseproof-phase514 down -v
```

Observed cleanup:

```text
Container noiseproof-agent-db Removed
Volume noiseproof-phase514_noiseproof_pgdata Removed
Network noiseproof-phase514_default Removed
port_8100_clear=true
```

## Boundaries

This is local Docker PostgreSQL plus live FastAPI HTTP proof only.

It is not automatic failure detection.

It is not background automation.

It is not complete workflow failure causality.

It is not root-cause automation.

It is not a retry or repair system.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.

The dashboard count proves only that existing persisted failure-case records with `workflow_run_id` are visible from the local operations dashboard.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
