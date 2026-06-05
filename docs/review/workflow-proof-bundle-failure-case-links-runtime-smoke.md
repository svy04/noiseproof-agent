# Workflow Proof Bundle Failure-case Links Runtime Smoke

Status: implemented.

Phase marker: workflow proof bundle failure-case links runtime smoke v0.

## Purpose

Verify the workflow proof bundle failure-case links read model against local Docker PostgreSQL plus live FastAPI HTTP.

This smoke proves the read model added in `docs/review/workflow-proof-bundle-failure-case-links.md` works outside the in-memory test repository.

## Runtime Setup

Database:

```powershell
# command shape: docker compose up -d db
$env:POSTGRES_PORT='55432'
docker compose -p noiseproof-phase509 up -d db
```

Observed database status:

```text
database status: healthy
Applied migrations: 21
Pending migrations: 0
```

API:

```powershell
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55432/noiseproof'
uv run uvicorn app.main:app --host 127.0.0.1 --port 8099
```

## HTTP Flow

The smoke used live HTTP requests against `http://127.0.0.1:8099`.

```text
GET /health -> 200
POST /workflow-runs -> 201
POST /failure-cases/workflow-runs/{workflow_run_id} -> 201
POST /failure-cases -> 201
GET /workflow-runs/{workflow_run_id} -> 200
GET /workflow-runs/{workflow_run_id}/proof-bundle -> 200
GET /failure-cases?workflow_run_id={workflow_run_id} -> 200
```

Observed values:

```json
{
  "health_status": "ok",
  "workflow_status_code": 201,
  "failure_case_handoff_status_code": 201,
  "unrelated_failure_status_code": 201,
  "detail_status_code": 200,
  "proof_bundle_status_code": 200,
  "filtered_failure_cases_status_code": 200,
  "workflow_run_id": "4b5895ca-933b-4cce-abf3-c798a06d6bb1",
  "linked_failure_case_id": "54bd2538-4b60-4864-beea-cc31a45b5178",
  "unrelated_failure_case_id": "2e60984c-ec08-4c6c-b8cd-8a10db138fb3",
  "detail_failure_case_count": 1,
  "bundle_failure_case_count": 1,
  "filtered_failure_case_count": 1,
  "filtered_first_failure_case_id": "54bd2538-4b60-4864-beea-cc31a45b5178",
  "unrelated_filtered_out": true,
  "proof_surface_has_failure_case_filter": true,
  "bundle_warning_has_failure_case_link": true,
  "bundle_boundary": "read_model_only_existing_records_no_new_storage"
}
```

Marker summary:

```text
detail_failure_case_count: 1
bundle_failure_case_count: 1
filtered_failure_case_count: 1
unrelated_filtered_out: true
proof_surface_has_failure_case_filter: true
```

The proof bundle warning included:

```text
failure_cases are linked by workflow_run_id
```

## Cleanup

The API server was stopped, then the Phase 509 compose project was removed:

```powershell
docker compose -p noiseproof-phase509 down -v
```

Observed cleanup:

```text
Container noiseproof-agent-db Removed
Volume noiseproof-phase509_noiseproof_pgdata Removed
Network noiseproof-phase509_default Removed
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

The linked failure case proves only that an existing persisted failure-case record explicitly references the workflow parent by `workflow_run_id`, and that the workflow detail/proof bundle read models surface that reference.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
