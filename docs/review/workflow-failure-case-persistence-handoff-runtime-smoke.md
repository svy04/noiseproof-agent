# Workflow Failure-case Persistence Handoff Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: workflow failure-case persistence handoff runtime smoke v0.

Label: Workflow failure-case persistence handoff runtime smoke.

This artifact records local Docker PostgreSQL plus live FastAPI HTTP evidence for the caller-triggered workflow failure-case persistence handoff.

## Commands

```powershell
$env:POSTGRES_PORT='55432'
docker compose config
docker compose up -d db
docker compose ps db

cd apps/api
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55432/noiseproof'
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8044
```

HTTP smoke:

```text
GET /health
POST /workflow-runs
POST /failure-cases/workflow-runs/{workflow_run_id}
GET /failure-cases
GET /failure-cases/workflow-review-queue
POST /failure-cases/workflow-runs/{completed_workflow_run_id}
POST /failure-cases/workflow-runs/{already_linked_workflow_run_id}
```

## Observed

```text
docker compose config -> exit 0
docker compose up -d db -> db running
docker compose ps db -> healthy
Applied migrations: 21
Pending migrations: 0
GET /health -> 200
POST /workflow-runs -> 201
POST /failure-cases/workflow-runs/{workflow_run_id} -> 201
GET /failure-cases -> 200
GET /failure-cases/workflow-review-queue -> 200
workflow_status -> failed
workflow_id -> 5c6013c4-08b7-4f4e-97a8-f4dc8d9799cb
persistence_status -> open
persistence_boundary -> caller_triggered_workflow_failure_case_persistence
persisted_workflow_run_id -> 5c6013c4-08b7-4f4e-97a8-f4dc8d9799cb
persisted_failure_type -> workflow_stage_error
persisted_stage -> runtime_smoke_stage
queue_pending_review_count -> 0
queue_linked_failure_case_count -> 1
queue_status_for_workflow -> failure_case_linked
listed_contains_failure_case -> true
completed_workflow_status_code -> 409
completed_workflow_detail -> workflow status is not reviewable for failure-case persistence
first_failed_handoff_status -> open
duplicate_status_code -> 409
duplicate_detail -> failure case already exists for workflow_run_id
```

## Allowed Claim

NoiseProof has local Docker PostgreSQL plus live FastAPI HTTP evidence that a failed workflow parent can be converted into one linked persisted failure case through `POST /failure-cases/workflow-runs/{workflow_run_id}`, and that the workflow review queue then reports `failure_case_linked`.

## Boundary / Non-claims

This is local runtime evidence only.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not background automation.

This is not automatic root-cause classification.

This is not complete workflow failure causality.

This is not LLM-backed repair.

This is not product-complete.

## Next Gate

The next bounded gate can either:

```text
1. add reviewer-facing request refresh for this runtime smoke,
2. verify current external feedback state if outside feedback exists,
3. or continue with another source-first product gap from docs/GOAL.md.
```
