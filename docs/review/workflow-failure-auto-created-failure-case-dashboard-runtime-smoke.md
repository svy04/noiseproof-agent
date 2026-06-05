# Workflow Failure Auto-created Failure-case Dashboard Runtime Smoke

Status: implemented.

Phase marker: workflow failure auto-created failure-case dashboard runtime smoke v0.

## Purpose

Verify that a local v0 auto-created workflow failure case is visible from the operations dashboard read model.

This extends the workflow failure auto-created failure-case runtime proof by checking the operator-facing dashboard surface after the failed workflow creates a linked failure case.

## Runtime Setup

Observed runtime:

```text
Docker PostgreSQL -> noiseproof-agent-db
db_port -> 55432
api_port -> 8104
db_health=healthy
Applied migrations: 23
Pending migrations: 0
```

API:

```powershell
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55432/noiseproof'
uv run uvicorn app.main:app --host 127.0.0.1 --port 8104
```

Smoke mechanism:

```text
smoke-only CHECK constraint -> smoke_fail_auto_dashboard
target table -> evidence_ledger_entries
constraint removed after smoke
```

The CHECK constraint intentionally forced the Evidence Ledger insert to fail after retrieval completed. This was a local runtime smoke only.

## HTTP Evidence

Observed calls:

```text
GET /health -> 200
POST /workflow-runs/execute-preview -> 500
GET /workflow-runs/{id} -> 200
GET /workflow-runs/{id}/proof-bundle -> 200
GET /failure-cases?workflow_run_id={id} -> 200
GET /failure-cases -> 200
GET /ops/dashboard -> 200
```

Observed values:

```json
{
  "health_status": "ok",
  "execute_status_code": 500,
  "workflow_run_id": "f4511706-b1fe-448e-8cd2-99ad9250dadd",
  "workflow_status": "failed",
  "workflow_error_type": "CheckViolation",
  "failed_stage": "evidence_ledger",
  "auto_failure_case_id": "e2814e46-de30-4b07-be16-397c6c557d55",
  "failure_case_id": "e2814e46-de30-4b07-be16-397c6c557d55",
  "failure_case_persistence_boundary": "auto_created_from_workflow_failure_local_v0",
  "detail_failure_case_count": 1,
  "bundle_detail_failure_case_count": 1,
  "filtered_failure_case_count": 1,
  "failure_case_count_before": 7,
  "failure_case_count_after": 8,
  "failure_case_count_delta": 1,
  "failure_type": "workflow_stage_error",
  "fix_status": "open",
  "dashboard_status_code": 200,
  "dashboard_contains_linked_failure_cases_header": true,
  "dashboard_contains_read_only_boundary": true,
  "dashboard_contains_auto_created_failure_case_filter": true,
  "dashboard_contains_auto_created_failure_case_id": true,
  "dashboard_contains_workflow_parent_link": true,
  "dashboard_contains_review_queue_linked_count": true,
  "failed_stage_boundary": "local_workflow_stage_failure_event_auto_failure_case_local_v0",
  "stage_event_count": 2
}
```

Marker summary:

```text
failure_case_count_delta -> 1
auto_failure_case_id -> e2814e46-de30-4b07-be16-397c6c557d55
auto_created_from_workflow_failure_local_v0
local_workflow_stage_failure_event_auto_failure_case_local_v0
dashboard_contains_linked_failure_cases_header -> true
dashboard_contains_read_only_boundary -> true
dashboard_contains_auto_created_failure_case_filter -> true
dashboard_contains_auto_created_failure_case_id -> true
dashboard_contains_workflow_parent_link -> true
dashboard_contains_review_queue_linked_count -> true
```

The dashboard contained the auto-created failure-case workflow filter:

```text
/failure-cases?workflow_run_id=f4511706-b1fe-448e-8cd2-99ad9250dadd
```

The dashboard also contained the auto-created failure case id in the review queue linked failure-case cell:

```text
e2814e46-de30-4b07-be16-397c6c557d55
```

## Cleanup

The smoke-only CHECK constraint was removed:

```text
ALTER TABLE evidence_ledger_entries DROP CONSTRAINT IF EXISTS smoke_fail_auto_dashboard;
```

The local API process was stopped:

```text
port_8104_clear=true
```

The existing shared local Docker database was left running because it was already active before this smoke.

## Boundaries

This is local Docker PostgreSQL plus live FastAPI HTTP proof only.

It proves only that an already auto-created local v0 workflow failure case is visible from the existing operations dashboard read model.

It is not retry behavior.

It is not root-cause automation.

It is not complete workflow failure causality.

It is not production background worker behavior.

It is not distributed tracing.

It is not hosted observability.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, request-surface refresh for this dashboard proof if it should be routed to reviewers, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
