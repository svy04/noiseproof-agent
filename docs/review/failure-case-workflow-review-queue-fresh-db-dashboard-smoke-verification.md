# Failure-case Workflow Review Queue Fresh DB Dashboard Smoke Verification

Status: verified local smoke.

Phase marker: failure-case workflow review queue fresh-db dashboard smoke verification v0.

Label: Failure-case workflow review queue fresh DB dashboard smoke verification.

This artifact records local fresh migrated Docker DB dashboard evidence for the failure-case workflow review queue section in `GET /ops/dashboard`.

## Scope

This smoke verifies only the combined local path:

```text
fresh migrated Docker DB
  -> migration runner
  -> FastAPI process
  -> POST /workflow-runs
  -> POST /failure-cases with workflow_run_id
  -> GET /failure-cases/workflow-review-queue
  -> GET /ops/dashboard
  -> HTML contains the Failure-case Workflow Review Queue section
```

## Environment

```text
date: 2026-06-04
compose_project: noiseproof_phase361
postgres_port: 55461
api_port: 8061
database_url: postgresql://noiseproof:noiseproof@localhost:55461/noiseproof
db_container: noiseproof-phase361-db
api_process_pid: 49036
docker_server_version: 29.4.3
docker_compose_version: v5.1.3
```

This smoke used a temporary DB-only Compose file outside the repo so it could verify a fresh database without reusing the default `noiseproof-agent-db` container or the default `55432` port.

## Migration Evidence

The database was created from a fresh Docker volume, then the migration runner was executed against that database.

Initial status:

```text
Applied migrations: 0
Pending migrations: 17
pending 002_evidence_ledger_entries.sql
pending 003_noise_gate_records.sql
pending 004_report_records.sql
pending 005_workflow_trace_ids.sql
pending 006_child_agent_run_ids.sql
pending 007_workflow_runs.sql
pending 008_child_workflow_run_ids.sql
pending 009_stage_input_manifest.sql
pending 010_workflow_version_defaults.sql
pending 011_failure_case_workflow_run_id.sql
pending 012_uploaded_file_intake_manifests.sql
pending 013_document_chunks.sql
pending 014_evidence_ledger_retrieval_run_id.sql
pending 015_chunk_embeddings.sql
pending 016_uploaded_raw_files.sql
pending 017_raw_file_scan_results.sql
pending 018_evidence_ledger_metadata_json.sql
```

Migration command:

```powershell
uv run python -m app.migration_runner
```

Applied output:

```text
applied 002_evidence_ledger_entries.sql
applied 003_noise_gate_records.sql
applied 004_report_records.sql
applied 005_workflow_trace_ids.sql
applied 006_child_agent_run_ids.sql
applied 007_workflow_runs.sql
applied 008_child_workflow_run_ids.sql
applied 009_stage_input_manifest.sql
applied 010_workflow_version_defaults.sql
applied 011_failure_case_workflow_run_id.sql
applied 012_uploaded_file_intake_manifests.sql
applied 013_document_chunks.sql
applied 014_evidence_ledger_retrieval_run_id.sql
applied 015_chunk_embeddings.sql
applied 016_uploaded_raw_files.sql
applied 017_raw_file_scan_results.sql
applied 018_evidence_ledger_metadata_json.sql
```

Final status:

```text
Applied migrations: 17
Pending migrations: 0
```

## Runtime Smoke Evidence

The FastAPI process was started against the fresh migrated database on `127.0.0.1:8061`.

Observed calls:

```text
GET /health
POST /workflow-runs
POST /workflow-runs
POST /workflow-runs
POST /failure-cases
GET /failure-cases/workflow-review-queue
GET /ops/dashboard
GET /failure-cases
```

Observed response summary:

```json
{
  "health_status": "ok",
  "pending_workflow_id": "25217f07-1cd7-4b75-90ea-085b68b0c1e5",
  "linked_workflow_id": "4a8ea42f-7756-43b4-98cc-7cf618546e6b",
  "completed_workflow_id": "228f9c78-8608-44bd-953e-185cb6609f29",
  "linked_failure_case_id": "b354ef4b-5b6b-4aff-b037-0e5083527924",
  "queue_pending_review_count": 1,
  "queue_linked_failure_case_count": 1,
  "queue_item_count": 2,
  "failure_case_count": 1,
  "dashboard_contains_review_queue": true,
  "dashboard_contains_pending_count": true,
  "dashboard_contains_linked_count": true,
  "dashboard_contains_pending_status": true,
  "dashboard_contains_linked_status": true,
  "dashboard_contains_pending_workflow_link": true,
  "dashboard_contains_linked_workflow_link": true,
  "dashboard_contains_linked_failure_case_id": true,
  "dashboard_contains_draft_preview": true,
  "dashboard_contains_no_auto_creation_boundary": true,
  "dashboard_did_not_create_failure_cases": true,
  "completed_workflow_excluded_from_queue": true,
  "persistence_boundary": "read_model_only_no_automatic_failure_case_creation"
}
```

Runtime assertions:

```text
pending_review_count: 1
linked_failure_case_count: 1
dashboard_contains_review_queue: true
dashboard_contains_pending_status: true
dashboard_contains_linked_status: true
dashboard_contains_draft_preview: true
dashboard_did_not_create_failure_cases: true
completed_workflow_excluded_from_queue: true
read_model_only_no_automatic_failure_case_creation
does not create failure_cases
```

The `GET /ops/dashboard` HTML contained:

- `Failure-case Workflow Review Queue`
- `pending_review_count`
- `linked_failure_case_count`
- `needs_failure_case_review`
- `failure_case_linked`
- `/workflow-runs/25217f07-1cd7-4b75-90ea-085b68b0c1e5`
- `/workflow-runs/4a8ea42f-7756-43b4-98cc-7cf618546e6b`
- `b354ef4b-5b6b-4aff-b037-0e5083527924`
- `/failure-cases/draft-preview`
- `does not create failure_cases`

## Cleanup Evidence

The API process was stopped and the Docker Compose project was removed with its volume.

```text
stopping_api_pid=49036
Container noiseproof-phase361-db Removed
Volume noiseproof_phase361_noiseproof_phase361_pgdata Removed
Network noiseproof_phase361_default Removed
```

## Boundary

This is local fresh migrated Docker DB dashboard evidence only.

This is not hosted deployment evidence.
This is not external reviewer feedback.
This is not automatic failure-case creation.
This is not automatic failure detection.
This is not root-cause automation.
This is not complete workflow failure causality.
This is not production incident management readiness.

The verified claim is limited to this:

```text
Given a fresh local PostgreSQL database with migrations applied, GET /ops/dashboard
can show the Failure-case Workflow Review Queue section with one failed workflow
that still needs human failure-case review, one failed workflow that already has
a linked manual failure case, and no completed workflow in the queue, without
creating new failure_cases.
```
