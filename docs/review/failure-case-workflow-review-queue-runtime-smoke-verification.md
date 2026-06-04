# Failure-case Workflow Review Queue Runtime Smoke Verification

Status: verified local smoke.

Phase marker: failure-case workflow review queue runtime smoke verification v0.

Label: Failure-case workflow review queue runtime smoke verification.

This artifact records local fresh migrated Docker DB evidence for the failure-case workflow review queue read model.

## Scope

This smoke verifies only the combined local path:

```text
fresh migrated Docker DB
  -> migration runner
  -> FastAPI process
  -> POST /workflow-runs
  -> POST /failure-cases with workflow_run_id
  -> GET /failure-cases/workflow-review-queue
```

## Environment

```text
date: 2026-06-04
compose_project: noiseproof_phase358
postgres_port: 55458
api_port: 8058
database_url: postgresql://noiseproof:noiseproof@localhost:55458/noiseproof
db_container: noiseproof-phase358-db
api_process_pid: 68880
docker_server_version: 29.4.3
docker_compose_version: v5.1.3
```

The default `noiseproof-agent-db` container was already running, so this smoke used a temporary compose override outside the repo to give the Phase 358 DB a separate container name and port. The observed DB startup command was:

```powershell
docker compose -p noiseproof_phase358 -f docker-compose.yml -f $env:TEMP\noiseproof-phase358-compose.override.yml up -d db
```

## Migration evidence

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

## Runtime smoke evidence

The FastAPI process was started against the fresh migrated database on `127.0.0.1:8058`.

Observed calls:

```text
GET /health
POST /workflow-runs
POST /workflow-runs
POST /workflow-runs
POST /failure-cases
GET /failure-cases/workflow-review-queue
GET /failure-cases
```

Observed response summary:

```json
{
  "health_status": "ok",
  "workflow_version": "phase40-lineage-warning-code-dashboard",
  "pending_workflow_id": "c6130750-57f9-4e17-af31-24fb85ba4c93",
  "linked_workflow_id": "b4402b71-d048-46e3-a798-d52f04e0c448",
  "completed_workflow_id": "3d8c98d9-c9be-422a-8bfe-6ab4c92b60cb",
  "linked_failure_case_id": "babd6443-da4a-441a-bb85-41ee7760ddeb",
  "queue_boundary": "failed_workflow_review_queue_read_model_only",
  "persistence_boundary": "read_model_only_no_automatic_failure_case_creation",
  "pending_review_count": 1,
  "linked_failure_case_count": 1,
  "item_count": 2,
  "completed_workflow_excluded": true,
  "pending_review_status": "needs_failure_case_review",
  "linked_review_status": "failure_case_linked",
  "pending_stage": "workflow_execute_preview",
  "linked_stage": "report_preview",
  "pending_draft_preview_path": "/failure-cases/draft-preview",
  "linked_failure_case_ids": [
    "babd6443-da4a-441a-bb85-41ee7760ddeb"
  ],
  "failure_case_count": 1,
  "failure_cases_still_manual": true,
  "warnings": [
    "This read model does not create failure_cases.",
    "A human confirmation boundary remains required before persistence.",
    "This is not automatic failure detection or root-cause automation."
  ]
}
```

Runtime assertions:

```text
pending_review_count: 1
linked_failure_case_count: 1
needs_failure_case_review
failure_case_linked
completed_workflow_excluded: true
read_model_only_no_automatic_failure_case_creation
does not create failure_cases
failure_cases_still_manual: true
```

## Cleanup evidence

The API process was stopped and the Docker Compose project was removed with its volume.

```text
stopping_api_pid=68880
Container noiseproof-phase358-db Removed
Volume noiseproof_phase358_noiseproof_phase358_pgdata Removed
Network noiseproof_phase358_default Removed
```

Post-cleanup checks returned no listener on port `8058` and no `noiseproof-phase358-db` container.

## Boundary

This is local fresh migrated Docker DB evidence only.

This is not hosted deployment evidence.
This is not external reviewer feedback.
This is not automatic failure-case creation.
This is not automatic failure detection.
This is not root-cause automation.
This is not complete workflow failure causality.
This is not production incident management readiness.

The verified claim is limited to this:

```text
Given a fresh local PostgreSQL database with migrations applied, GET /failure-cases/workflow-review-queue can show one failed workflow that still needs human failure-case review, one failed workflow that already has a linked manual failure case, and no completed workflow in the review queue, without creating new failure_cases.
```
