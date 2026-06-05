# Workflow Failure Auto Failure-case Creation Runtime Smoke

Status: implemented.

Phase marker: workflow failure auto failure-case creation runtime smoke v0.

## Purpose

Verify the local v0 workflow failure auto failure-case creation path against Docker PostgreSQL plus live FastAPI HTTP.

This smoke proves the route-level behavior from `docs/review/workflow-failure-auto-failure-case-creation.md` works outside the in-memory test repository.

## Runtime Setup

Observed runtime:

```text
Docker PostgreSQL -> noiseproof-agent-db
db_port -> 55432
api_port -> 8103
db_health=healthy
Applied migrations: 23
Pending migrations: 0
```

API:

```powershell
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55432/noiseproof'
uv run uvicorn app.main:app --host 127.0.0.1 --port 8103
```

Smoke mechanism:

```text
smoke-only CHECK constraint -> smoke_fail_auto_failure_case
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
```

Observed workflow:

```text
workflow_run_id -> a81bd16b-9291-4049-94a2-f4d0bbbf0b2f
workflow_status -> failed
workflow_error_type -> CheckViolation
failed_stage -> evidence_ledger
retrieval -> completed
evidence_ledger -> failed
stage_event_count -> 2
```

Observed failure-case linkage:

```text
auto_failure_case_id -> 399aa3be-fa49-44b6-bfbb-d87700be0b1a
failure_case_id -> 399aa3be-fa49-44b6-bfbb-d87700be0b1a
failure_case_persistence_boundary -> auto_created_from_workflow_failure_local_v0
detail_failure_case_count -> 1
bundle_detail_failure_case_count -> 1
filtered_failure_case_count -> 1
failure_case_count_before -> 5
failure_case_count_after -> 6
failure_case_count_delta -> 1
```

Observed failed stage boundary:

```text
failed_stage_boundary -> local_workflow_stage_failure_event_auto_failure_case_local_v0
failure_type -> workflow_stage_error
fix_status -> open
root_cause -> CheckViolation: new row for relation "evidence_ledger_entries" violates check constraint "smoke_fail_auto_failure_case"
```

The proof bundle surfaced the linked failure case through:

```text
detail.summary.failure_case_count -> 1
detail.failure_cases[0].id -> 399aa3be-fa49-44b6-bfbb-d87700be0b1a
proof_surfaces -> /failure-cases?workflow_run_id=a81bd16b-9291-4049-94a2-f4d0bbbf0b2f
```

## Smoke Correction

The first DB lookup used the stale column name `user_question`. Runtime schema inspection showed the current column is `question`.

The smoke proceeded by reading the created workflow through the live `GET /workflow-runs` and `GET /workflow-runs/{id}` APIs, and the smoke-only constraint was removed.

## Boundary

This proves only:

```text
local Docker PostgreSQL plus live FastAPI HTTP behavior
failed Evidence Ledger stage creates one linked local v0 failure case
workflow trace records auto_failure_case_id
workflow trace records auto_created_from_workflow_failure_local_v0
workflow detail and proof bundle surface the linked failure case
```

This does not prove:

```text
not retry behavior
not root-cause automation
not complete workflow failure causality
not production background worker behavior
not distributed tracing
not hosted observability
not external reviewer feedback
not hosted deployment evidence
not product-complete
```

## Cleanup

The smoke-only CHECK constraint was removed:

```text
constraint removed after smoke
```

The local API process was stopped:

```text
port_8103_clear=true
```

The existing shared local Docker database was left running because it was already active before this smoke.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
