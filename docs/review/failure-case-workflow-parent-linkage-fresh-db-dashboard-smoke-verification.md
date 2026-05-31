# Failure-case Workflow Parent Linkage Fresh DB Dashboard Smoke Verification

Status: verified local smoke.

Phase marker: failure-case workflow parent linkage fresh-db dashboard smoke verification v0.

Label: Failure-case workflow parent linkage fresh DB dashboard smoke verification.

This artifact records local fresh migrated Docker DB dashboard evidence for the manual failure-case workflow parent link.

## Scope

This smoke verifies only the combined local path:

```text
fresh migrated Docker DB
  -> migration runner
  -> FastAPI process
  -> POST /workflow-runs
  -> POST /failure-cases with workflow_run_id
  -> GET /ops/dashboard
  -> HTML contains the manual Workflow Parent link
```

## Environment

```text
compose_project: noiseproof_phase84
postgres_port: 55445
api_port: 8025
database_url: postgresql://noiseproof:noiseproof@localhost:55445/noiseproof
docker_container: noiseproof-agent-db
```

## Migration evidence

The database was created from a fresh Docker volume, then the migration runner was executed against that database.

```text
Applied migrations: 0
Pending migrations: 10
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
```

Follow-up status check:

```text
Applied migrations: 10
Pending migrations: 0
```

## Runtime smoke evidence

The FastAPI process was started against the fresh migrated database. The smoke created a workflow parent and then created a manual failure case with that workflow parent id.

```json
{
  "workflow_id": "5eaeab08-406a-4696-af97-ea74fc2e31f3",
  "failure_case_id": "cb674d42-a448-4c65-bb3e-686233fcb2f6",
  "failure_case_workflow_run_id": "5eaeab08-406a-4696-af97-ea74fc2e31f3",
  "status_code": 200,
  "dashboard_contains_failure_cases": true,
  "dashboard_contains_workflow_parent": true,
  "dashboard_contains_workflow_link": true,
  "dashboard_contains_manual_boundary": true,
  "dashboard_contains_not_automatic_creation": true
}
```

Dashboard assertions:

```text
dashboard_contains_failure_cases: true
dashboard_contains_workflow_parent: true
dashboard_contains_workflow_link: true
dashboard_contains_manual_boundary: true
dashboard_contains_not_automatic_creation: true
```

The `GET /ops/dashboard` HTML contained:

- `Failure Cases`
- `Workflow Parent`
- `/workflow-runs/5eaeab08-406a-4696-af97-ea74fc2e31f3`
- `manual workflow parent link`
- `not automatic failure-case creation`

## Cleanup evidence

The API process was stopped and the Docker Compose project was removed with its volume.

```text
stopped_api_pid=49080
Container noiseproof-agent-db Removed
Volume noiseproof_phase84_noiseproof_pgdata Removed
Network noiseproof_phase84_default Removed
```

## Boundary

This is local fresh migrated Docker DB dashboard evidence only.

This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not automatic failure detection.
This is not complete workflow failure causality.
This is not production migration orchestration.
This is not incident management readiness.

The verified claim is limited to this:

```text
Given a fresh local PostgreSQL database with migrations applied, a manually persisted
failure_cases.workflow_run_id can appear as a Workflow Parent link in GET /ops/dashboard.
```
