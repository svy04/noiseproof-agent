# Workflow Failed Stage Event Runtime Smoke

Phase marker: workflow failed stage event runtime smoke v0.

This smoke records local Docker PostgreSQL plus live FastAPI HTTP evidence that a
workflow preview failure can leave an inspectable failed stage event before the
request returns a 500.

## Runtime Setup

Observed runtime:

```text
Docker PostgreSQL -> noiseproof-agent-db
db_port -> 55432
api_port -> 8046
db_health=healthy
Applied migrations: 23
Pending migrations: 0
```

Smoke mechanism:

```text
smoke-only CHECK constraint -> smoke_fail_evidence_stage
target table -> evidence_ledger_entries
constraint removed after smoke
```

The CHECK constraint intentionally forced the Evidence Ledger insert to fail
after retrieval completed. This was a local runtime smoke only.

## HTTP Evidence

Observed calls:

```text
GET /health -> 200
POST /workflow-runs/execute-preview -> 500
GET /workflow-runs/{id} -> 200
GET /workflow-runs/{id}/proof-bundle -> 200
GET /failure-cases -> 200
```

Observed workflow:

```text
workflow_run_id -> d8c9769b-22e9-476c-919f-a9cd7d2db287
workflow_status -> failed
retrieval -> completed
evidence_ledger -> failed
failure_case_count_delta -> 0
```

Observed stage-event summary:

```json
{
  "workflow_stage_event_count": 2,
  "stage_status": "failed",
  "failed_stage_name": "evidence_ledger",
  "failed_stage_boundary": "local_workflow_stage_failure_event_no_retry_no_auto_failure_case",
  "failure_case_count_delta": 0
}
```

The failed stage event stored `error_type -> CheckViolation` and an error
message containing the `smoke_fail_evidence_stage` constraint name inside the
stage output summary and workflow error message.

## Boundary

This proves only:

```text
local workflow stage failure event inspection
failed Evidence Ledger stage surfaced through workflow detail
failed Evidence Ledger stage surfaced through proof bundle read model
failure cases are not created automatically by this failure path
```

This does not prove:

```text
not automatic failure-case creation
not retry behavior
not root-cause automation
not complete workflow failure causality
not distributed tracing
not hosted observability
not external reviewer feedback
not hosted deployment evidence
not product-complete
```
