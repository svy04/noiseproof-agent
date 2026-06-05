# Workflow Proof Bundle Runtime Smoke

Status: Accepted

Phase marker: workflow proof bundle runtime smoke v0

## Purpose

Verify `GET /workflow-runs/{id}/proof-bundle` against local Docker PostgreSQL plus live FastAPI HTTP, after the route-level read model already passed in-memory tests.

This smoke checks that the endpoint can collect existing workflow detail, derived lineage, and trace lookup surfaces from a real PostgreSQL-backed run without creating new storage or overclaiming distributed tracing.

## Environment

```text
Docker version: 29.4.3
Docker Compose version: v5.1.3
database container: noiseproof-agent-db
database status: healthy
database port: 55432 -> 5432
DATABASE_URL: postgresql://noiseproof:noiseproof@127.0.0.1:55432/noiseproof
FastAPI URL: http://127.0.0.1:8058
```

Migration runner status:

```text
Applied migrations: 21
Pending migrations: 0
```

## Commands

```powershell
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@127.0.0.1:55432/noiseproof'
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8058
```

Then, using `curl.exe`:

```text
GET  /health
POST /workflow-runs/execute-preview
GET  /workflow-runs/{workflow_run_id}/proof-bundle
POST /workflow-runs
GET  /workflow-runs/{metadata_only_workflow_run_id}/proof-bundle
```

## Observed Result

```text
health_status_code: 200
health_status: ok
workflow_version: phase40-lineage-warning-code-dashboard
execute_preview_status_code: 201
workflow_run_id: b357de11-b221-4788-8029-d50038c2c37b
workflow_trace_id: e2026ab6-2bf2-470c-959b-0cfb09e77482
proof_bundle_status_code: 200
bundle_boundary: read_model_only_existing_records_no_new_storage
proof_surface_count: 3
proof_surface_trace_path_present: true
detail_retrieval_run_count: 1
detail_evidence_ledger_entry_count: 1
detail_noise_gate_record_count: 1
detail_report_record_count: 1
lineage_boundary: derived_read_model_only
lineage_missing_reference_count: 0
lineage_warning_codes:
  - derived_read_model_boundary
  - local_workflow_scope
trace_agent_run_count: 0
trace_evidence_ledger_entry_count: 1
trace_noise_gate_record_count: 1
trace_report_record_count: 1
warning_mentions_distributed_tracing: true
metadata_only_create_status_code: 201
metadata_only_workflow_run_id: f85af812-93cc-4a8b-bf9e-56754d4a8af3
metadata_only_proof_bundle_status_code: 200
metadata_only_workflow_trace_id_is_null: true
metadata_only_trace_is_null: true
metadata_only_proof_surface_count: 2
metadata_only_warning_mentions_no_trace: true
```

## Interpretation

The live route can bundle three existing proof surfaces for a deterministic workflow preview:

```text
/workflow-runs/{id}
/workflow-runs/{id}/lineage
/traces/{workflow_trace_id}
```

For a metadata-only workflow row without `trace_json.workflow_trace_id`, the same endpoint returns `workflow_trace_id: null`, `trace: null`, two proof surfaces, and a warning that trace lookup is omitted. That keeps metadata-only workflows from pretending to have trace-level proof.

The observed `trace_agent_run_count: 0` is expected for deterministic workflow execution preview. The workflow-created child records carry `workflow_trace_id`, but that path does not create an `agent_runs` row.

## Boundaries

This smoke is local Docker PostgreSQL plus live FastAPI HTTP evidence only.

It is:

- not distributed tracing
- not hosted observability
- not a new lineage storage model
- direct Evidence Ledger -> Noise Gate -> Report stage links are now represented by Phase 530 workflow-created link tables; this older smoke remains bounded to proof-bundle runtime behavior
- not semantic retrieval quality evidence
- not embedding generation
- not LLM output
- not external reviewer feedback
- not hosted deployment evidence
- not customer validation
- not Braincrew acceptance
- not product-complete

The proof bundle makes existing records easier to inspect. It does not make the underlying proof stronger than the existing workflow detail, lineage, and trace lookup records.
