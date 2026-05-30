# Runtime migration runner verification

Status: accepted

## Scope

Docker runtime verification performed for the lightweight SQL migration runner.

This verifies that the runner can inspect an existing local database, baseline an already-current volume, and then report no pending SQL migrations. It does not verify hosted migration orchestration, rollback behavior, backups, production deployment, API behavior, or workflow execution semantics.

## Environment

- Date: 2026-05-30
- Compose service: `db`
- Container: `noiseproof-agent-db`
- Port mapping from local `.env`: `55432 -> 5432`
- Database: `noiseproof`
- Runner command path: `cd apps/api; uv run python -m app.migration_runner`

## Initial runner status before baseline

```text
Applied migrations: 0
Pending migrations: 9
pending 002_evidence_ledger_entries.sql
pending 003_noise_gate_records.sql
pending 004_report_records.sql
pending 005_workflow_trace_ids.sql
pending 006_child_agent_run_ids.sql
pending 007_workflow_runs.sql
pending 008_child_workflow_run_ids.sql
pending 009_stage_input_manifest.sql
pending 010_workflow_version_defaults.sql
```

Interpretation:

The local database already contained these migration effects from prior manual commands, but it had no `schema_migrations` tracking records yet.

## Runner baseline result

```text
Applied migrations: 0
Pending migrations: 9
baselined 002_evidence_ledger_entries.sql
baselined 003_noise_gate_records.sql
baselined 004_report_records.sql
baselined 005_workflow_trace_ids.sql
baselined 006_child_agent_run_ids.sql
baselined 007_workflow_runs.sql
baselined 008_child_workflow_run_ids.sql
baselined 009_stage_input_manifest.sql
baselined 010_workflow_version_defaults.sql
```

## Final runner status after baseline

```text
Applied migrations: 9
Pending migrations: 0
```

## Boundary

This verification used baseline mode because the local DB was already current but lacked migration tracking. Baseline mode must not be used as a substitute for applying migrations to a database that is not already known to contain those migration effects.

The runner is still a local inspectability tool, not a production migration platform.
