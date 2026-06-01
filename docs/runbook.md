# Runbook: NoiseProof Agent

## Current Status

Phase 22 adds an Evidence Ledger dashboard table: persisted evidence rows are now visible beside retrieval, gate, and report records in the plain operations dashboard.

Phase 22.5 adds a review-only cross-link decision: direct evidence -> gate -> report links are deferred until a single workflow parent exists.

Phase 23 adds a review-only workflow parent decision: future workflow-level provenance should use a separate `workflow_runs` table instead of reusing `agent_runs`.

Phase 24 added schema-only workflow parent storage before runtime writes existed.

Phase 25 adds metadata-only workflow parent persistence: `POST /workflow-runs` and `GET /workflow-runs` exist, but no orchestration path or child record writes use `workflow_run_id` yet.

Phase 26 adds workflow-run metadata visibility in the plain operations dashboard, labeled as metadata-only and not workflow execution.

Phase 27 reviews child `workflow_run_id` links and defers them until a workflow execution boundary exists.

Phase 28 adds a deterministic workflow execution preview: `POST /workflow-runs/execute-preview` creates a parent workflow row and runs retrieval -> evidence -> gate -> report preview steps without child `workflow_run_id` links.

Phase 29 adds nullable child `workflow_run_id` links for retrieval, evidence, gate, and report rows created by the deterministic workflow preview.

Phase 30 adds a workflow-run child inspection surface: `GET /workflow-runs/{id}` returns the parent workflow row, linked retrieval runs, linked Evidence Ledger records, linked Noise Gate records, linked Report records, and child summary counts.

Phase 30.5 reviews direct evidence -> gate -> report foreign-key links and defers them until downstream stages consume persisted upstream row ids.

Phase 31 adds workflow stage input manifests: deterministic workflow-created Noise Gate and Report records now show the persisted upstream ids they consumed, without claiming direct evidence -> gate -> report foreign-key lineage.

Phase 31.5 reviews direct cross-stage link schema and defers new FK/join-table storage in favor of a derived workflow lineage read model.

Phase 32 adds that derived workflow lineage read model: `GET /workflow-runs/{id}/lineage` reads existing workflow child records and `stage_input_manifest` values, resolves local stage inputs back to linked records where possible, and does not add new storage or direct FK/join-table lineage.

Phase 33 adds workflow lineage links to the plain operations dashboard: workflow rows now link to both `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/lineage`, with no dashboard polish or new lineage storage.

Phase 33.5 reviews missing manifest reference behavior for the derived lineage read model: `docs/review/workflow-lineage-missing-reference-review.md` keeps runtime behavior unchanged and selects a targeted missing-reference test as the next proof step.

Phase 34 adds that targeted missing-reference fixture: tests now prove `GET /workflow-runs/{id}/lineage` surfaces `missing_reference_count > 0`, missing Evidence Ledger ids, and missing Noise Gate ids without adding a malformed-manifest mutation endpoint or new lineage storage.

Phase 34.5 reviews the next lineage hardening boundary: non-list `input_evidence_ledger_entry_ids`, duplicate references, and cross-workflow references should be handled before adding schema. The review adds no runtime behavior.

Phase 35 hardens manifest-shape handling: non-list `input_evidence_ledger_entry_ids` values now produce an empty id list plus a structured warning instead of being treated as iterable evidence id lists.

Phase 35.5 reviews the workflow lineage warning taxonomy before changing the API shape: warning categories are named in `docs/review/workflow-lineage-warning-taxonomy-review.md`, while current warning strings remain human-readable.

Phase 36 adds structured warning taxonomy to the lineage response: `GET /workflow-runs/{id}/lineage` now returns `warning_codes` while preserving the existing human-readable `warnings`.

Phase 36.5 reviews warning-code documentation: `docs/review/workflow-lineage-warning-code-documentation-review.md` records that warning codes should be explained with their human-readable warnings before any dashboard or persistence expansion.

Phase 37 adds a runbook example for lineage warning codes: the lineage response shape now shows both human-readable `warnings` and machine-readable `warning_codes`, while noting that codes are response-level taxonomy only.

Phase 37.5 reviews dashboard surfacing for lineage warning codes: `docs/review/workflow-lineage-warning-code-dashboard-review.md` keeps `GET /ops/dashboard` unchanged in this review gate and defers rendering changes to a later bounded implementation gate.

Phase 38 surfaces the warning-code legend in `GET /ops/dashboard`: the dashboard now shows Lineage warning codes as response-level taxonomy only, not persisted dashboard analytics.

Phase 38.5 adds the dashboard warning-code smoke example below, without changing runtime behavior.

Phase 39 reviews workflow-version naming: `docs/review/workflow-version-naming-review.md` kept `phase36-structured-warning-taxonomy` as the reviewed runtime value until a dedicated update gate changed all affected examples together.

Phase 40 updates the runtime `workflow_version` to `phase40-lineage-warning-code-dashboard` across settings, schema defaults, tests, and examples without changing workflow semantics.

Phase 40.5 adds explicit expected workflow-version smoke checks for `/health` and `/ops/summary`. It documents the smallest reviewer-facing confirmation that the runtime marker changed, with no workflow semantics changed.

Phase 41 reviews workflow-version naming consistency and identifies stale executable schema defaults in `db/init/001_schema.sql` and `db/migrations/007_workflow_runs.sql`. It does not change schema defaults in the review gate.

Phase 42 updates fresh schema defaults and adds `db/migrations/010_workflow_version_defaults.sql` so omitted `workflow_version` values default to `phase40-lineage-warning-code-dashboard`. Historical migration 007 is not rewritten.

Phase 42.5 adds expected schema-default workflow-version smoke checks. They document how to inspect defaults only; they do not prove new workflow behavior.

Phase 43 verifies the local Docker DB schema defaults before and after applying migration 010. The existing volume was stale before the migration and current afterward; no volume deletion was performed.

Phase 44 reviews migration handling and selects a lightweight SQL migration runner as the next bounded implementation.

Phase 45 adds the lightweight SQL migration runner. It uses `schema_migrations` tracking over existing SQL files and is not a production migration platform.

Phase 46 verifies the lightweight SQL migration runner against the local Docker DB. The existing already-current database was baselined, and final status showed 9 applied / 0 pending migrations.

Phase 47 verifies the lightweight SQL migration runner apply path against an isolated fresh Docker DB. The runner saw 9 pending migrations, applied all 9, reached 9 applied / 0 pending, verified current workflow-version defaults, and removed the isolated test volume.

Phase 48 cleans up the migration runbook so the runner is the default path and manual SQL piping is a legacy/debug fallback.

Phase 49 verifies that a fresh migrated Docker DB can serve a minimal API path: `/health`, `/ops/summary`, `POST /documents`, and `GET /documents`.

Phase 50 refreshes application-facing evidence indexes so reviewers can find the newest local runtime proof artifacts without treating them as hosted deployment evidence.

Phase 51 verifies failure-case persistence on a fresh migrated Docker DB through `POST /failure-cases`, `GET /failure-cases`, and `/ops/summary` failure counts.

Phase 52 refreshes application-facing evidence indexes so the failure-case persistence smoke artifact is discoverable without claiming automatic failure detection.

Phase 53 verifies that a failure case can carry `agent_run_id` linkage to a persisted failed agent run on a fresh migrated Docker DB.

Phase 54 refreshes application-facing evidence indexes so the linked failure-case proof is discoverable without claiming automatic detection or complete workflow failure causality.

Phase 55 reviews workflow failure provenance and keeps `failure_cases` at operation-level linkage until a real workflow failure path exists.

Phase 56 verifies the workflow failure path with a test fixture: a downstream stage exception marks the workflow parent failed, while `failure_cases` remain unchanged and no `workflow_run_id` is added to failure cases.

Phase 58 reviews whether failure cases should link to workflow parents and keeps the schema unchanged until a real failure-case creation path exists.

Phase 59 refreshes application-facing docs with that failure-case workflow linkage boundary without changing schema, API behavior, or failure creation logic.

Phase 60 reviews failure-case creation paths and selects a manual failure-case draft before any automatic failure-case creation.

Phase 61 adds `POST /failure-cases/draft-preview`, a non-persisting helper that turns workflow failure evidence into a human-confirmed draft payload.

Phase 72 verifies the narrow workflow failure-to-draft smoke path: a failed `POST /workflow-runs/execute-preview` parent can feed `POST /failure-cases/draft-preview`, while `failure_cases` remain unchanged and no automatic failure-case creation is claimed.

Phase 80 reviews dashboard surfacing for manual failure-case workflow parent links and selects the Failure Cases table Workflow Parent column as the next bounded surface.

Phase 81 implements that bounded surface: `GET /ops/dashboard` now shows a Workflow Parent column in the Failure Cases table, and present `workflow_run_id` values link to `/workflow-runs/{id}`. This is a manual workflow parent link only, not automatic failure-case creation.

Expected failure-case draft preview smoke check:

```bash
curl -X POST http://localhost:8000/failure-cases/draft-preview \
  -H "Content-Type: application/json" \
  -d '{"question":"Which segment had enterprise demand growth?","workflow_status":"failed","error_message":"simulated evidence persistence failure","trace_json":{"stage":"workflow_execute_preview","error_type":"RuntimeError"}}'
```

Expected boundary:

```text
persistence_boundary: preview_only_not_persisted
human_confirmation_required: true
does not persist a failure case
```

Implemented:

- FastAPI app skeleton
- `GET /health`
- `GET /ops/summary`
- `POST /documents/profile`
- document metadata create/list endpoints
- agent run metadata create/list endpoints
- failure case create/list endpoints
- Failure-case workflow parent linkage dashboard surfacing v0
- `GET /ops/dashboard` Failure Cases table Workflow Parent column
- manual `workflow_run_id` values link to `/workflow-runs/{id}`
- messy market data fixtures
- Document Profiler v0
- parser adapter stubs for markdown, CSV, HTML/URL, PDF text-only fallback, and unknown source types
- `POST /documents/parse-preview`
- chunk strategy experiment v0 for fixed-window, heading-aware, and row-aware strategies
- `POST /documents/chunk-preview`
- lexical retrieval v0 over generated chunks
- `POST /retrieval-runs`
- `GET /retrieval-runs`
- Collection Plan Preview v0
- `POST /collection-plans/preview`
- Evidence Ledger Preview v0
- `POST /evidence-ledgers/preview`
- Noise Gate Preview v0
- `POST /noise-gates/preview`
- Claim-bounded Report Preview v0
- `POST /reports/preview`
- Persisted Report Preview Records v0
- `POST /reports`
- `GET /reports`
- generated, blocked, and needs-revision report counts from persisted Report records
- Record Linkage v0
- `workflow_trace_id` on persisted Evidence Ledger, Noise Gate, and Report records
- matching `workflow_trace_id` in `agent_runs.trace_json` for persisted evidence/gate/report endpoints
- Trace-id Lookup v0
- `GET /traces/{workflow_trace_id}`
- Persisted Record Filtering v0
- `GET /evidence-ledgers?workflow_trace_id=...`
- `GET /evidence-ledgers?status=...`
- `GET /noise-gates?workflow_trace_id=...`
- `GET /noise-gates?decision=...`
- `GET /reports?workflow_trace_id=...`
- `GET /reports?status=...`
- Dashboard Trace/Filter Links v0
- trace lookup and record filter links in `GET /ops/dashboard`
- Agent-run Linkage Review v0
- `docs/review/agent-run-linkage-review.md`
- Agent-run Lifecycle v0
- `run_with_trace()` parent run creation before operation execution
- completion/failure updates on the same `agent_runs` row
- Persisted Child Record Agent-run Linkage v0
- `agent_run_id` on persisted Evidence Ledger, Noise Gate, and Report records
- `db/migrations/006_child_agent_run_ids.sql`
- Dashboard Parent/Child Provenance Links v0
- parent run links on Noise Gate rows in `GET /ops/dashboard`
- parent run links on Report rows in `GET /ops/dashboard`
- Evidence Ledger Dashboard Table v0
- persisted Evidence Ledger rows in `GET /ops/dashboard`
- trace, parent run, and status filter links on Evidence Ledger dashboard rows
- Evidence-to-gate/report Local Cross-links Review v0
- `docs/review/evidence-to-gate-report-cross-links-review.md`
- direct evidence -> gate -> report links remain unimplemented until a single workflow parent exists
- Single Workflow Parent Review v0
- `docs/review/single-workflow-parent-review.md`
- `workflow_runs` schema exists; runtime persistence and workflow execution remain unimplemented until a dedicated runtime gate
- WorkflowRun Schema v0
- `workflow_runs` table in `db/init/001_schema.sql`
- `db/migrations/007_workflow_runs.sql`
- WorkflowRun Metadata Persistence v0
- `POST /workflow-runs`
- `GET /workflow-runs`
- WorkflowRun Dashboard Table v0
- `GET /ops/dashboard` shows workflow-run metadata rows
- WorkflowRun Child-link Review v0
- `docs/review/workflow-run-child-link-review.md`
- Deterministic Workflow Execution Preview v0
- `POST /workflow-runs/execute-preview`
- parent `workflow_runs` row creation and completion/failure updates
- deterministic retrieval -> evidence -> gate -> report preview sequence
- WorkflowRun Child-record Links v0
- `db/migrations/008_child_workflow_run_ids.sql`
- `workflow_run_id` on retrieval, Evidence Ledger, Noise Gate, and Report records created by the deterministic workflow preview
- child records still carry `workflow_trace_id` for correlation
- WorkflowRun Child Inspection Surface v0
- `GET /workflow-runs/{id}`
- workflow detail response with linked retrieval, Evidence Ledger, Noise Gate, and Report records
- child record summary counts by workflow parent
- Direct Evidence-to-gate/report Cross-link Review v0
- Workflow Stage Input Manifest v0
- `stage_input_manifest` on deterministic workflow Noise Gate records
- `stage_input_manifest` on deterministic workflow Report records
- Direct Cross-stage Link Schema Review v0
- `docs/review/direct-cross-stage-link-schema-review.md`
- direct evidence -> gate -> report foreign-key links and join tables remain unimplemented
- Workflow Lineage Read Model v0
- `GET /workflow-runs/{id}/lineage`
- derived read model over existing workflow child records and `stage_input_manifest`
- no migrations, columns, direct foreign keys, or join tables added
- Workflow Lineage Dashboard Links v0
- `GET /ops/dashboard` workflow rows expose detail and lineage links
- workflow lineage links point to `GET /workflow-runs/{id}/lineage`
- no dashboard polish, frontend framework, or new lineage storage added
- missing-reference behavior review exists in `docs/review/workflow-lineage-missing-reference-review.md`
- no malformed-manifest mutation endpoint, repair endpoint, migration, column, or join table added by the review gate
- missing-reference fixture exists in `apps/api/tests/test_routes.py`
- no migrations, columns, or join tables added by the missing-reference test gate
- boundary hardening review exists in `docs/review/workflow-lineage-boundary-hardening-review.md`
- no runtime behavior added by the boundary hardening review gate
- non-list `input_evidence_ledger_entry_ids` values are ignored as evidence ids and warned about
- cross-workflow references remain local missing references
- duplicate manifest references preserve order and count
- warning taxonomy review exists in `docs/review/workflow-lineage-warning-taxonomy-review.md`
- no structured warning code fields, migrations, columns, or join tables added by the taxonomy review gate
- `warning_codes` are exposed by `GET /workflow-runs/{id}/lineage`
- human-readable lineage `warnings` remain available
- no warning-code persistence, migrations, columns, or join tables added by the structured taxonomy gate
- warning-code documentation review exists in `docs/review/workflow-lineage-warning-code-documentation-review.md`
- no runtime behavior added by the warning-code documentation review gate
- runbook lineage response example includes `warnings` and `warning_codes`
- `warning_codes` remain response-level taxonomy only
- warning-code dashboard review exists in `docs/review/workflow-lineage-warning-code-dashboard-review.md`
- no dashboard rendering, migrations, columns, or join tables added by the dashboard review gate
- `GET /ops/dashboard` shows Lineage warning codes:
  - `derived_read_model_boundary`
  - `local_workflow_scope`
  - `missing_manifest_reference`
  - `invalid_manifest_shape`
- those codes are not persisted dashboard analytics
- `docs/review/direct-evidence-gate-report-cross-link-review.md`
- direct evidence -> gate -> report foreign-key links remain unimplemented
- Operations Dashboard v0
- `GET /ops/dashboard`
- Evaluation/Application Package v0
- `docs/evaluation/*`
- `docs/application/*`
- Auto Trace Recording v0
- preview endpoints create `agent_runs.trace_json` metadata
- Persisted Evidence Ledger Records v0
- `POST /evidence-ledgers`
- `GET /evidence-ledgers`
- unsupported and contradiction counts from persisted ledger entries
- Persisted Noise Gate Records v0
- `POST /noise-gates`
- `GET /noise-gates`
- blocked and needs-revision gate counts from persisted Noise Gate records
- PostgreSQL schema init SQL
- GitHub Actions API smoke CI

Not implemented:

- persisted file upload parsing
- robust PDF extraction
- persisted parse records
- persisted chunks
- autonomous workflow execution endpoints
- embeddings
- distributed tracing or hosted observability

## Local Database

From repo root:

```bash
cp .env.example .env
docker compose up -d db
```

The database init script is mounted from:

```text
db/init/001_schema.sql
```

It creates:

- `documents`
- `agent_runs`
- `failure_cases`
- `retrieval_runs`
- `evidence_ledger_entries`
- `noise_gate_records`
- `report_records`
- `workflow_runs`

It also enables:

- `pgcrypto`
- `vector`

If local port `5432` is already occupied by another Postgres process, keep the repo-local `.env` ignored and use:

```text
POSTGRES_PORT=55432
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
```

Default path: use the migration runner.

Fresh or reset local DB:

```powershell
cd apps/api
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
```

Existing already-migrated local DB without schema_migrations rows:

```powershell
cd apps/api
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner --baseline
uv run python -m app.migration_runner --status
```

Do not use `--baseline` on a fresh DB. Baseline records migration files as already applied without executing SQL; it is only for an existing local database that is already known to contain the migration effects.

Use the default command to apply pending files from `db/migrations/*.sql` in sorted filename order. The runner creates `schema_migrations` if needed and fails on SQL errors or checksum drift.

Manual fallback:

manual SQL piping is a legacy/debug fallback. Use it only when the runner itself is broken and you need to inspect whether a specific SQL file is valid against a local throwaway database.

```powershell
Get-Content db/migrations/002_evidence_ledger_entries.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
Get-Content db/migrations/003_noise_gate_records.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
Get-Content db/migrations/004_report_records.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
Get-Content db/migrations/005_workflow_trace_ids.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
Get-Content db/migrations/006_child_agent_run_ids.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
Get-Content db/migrations/007_workflow_runs.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
Get-Content db/migrations/008_child_workflow_run_ids.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
Get-Content db/migrations/009_stage_input_manifest.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
Get-Content db/migrations/010_workflow_version_defaults.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
```

General runner commands:

```powershell
cd apps/api
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner --baseline
uv run python -m app.migration_runner
```

Use `--status` to inspect pending SQL files without applying them.

Use `--baseline` only when an existing local database is already known to contain the migration effects but lacks `schema_migrations` records. Baseline records filenames, checksums, byte counts, and timestamps with no SQL execution.

The runner is a local inspectability tool, not a production migration platform. It does not replace database backups, environment promotion rules, hosted migration orchestration, or rollback planning.

Fresh DB apply-path verification from Phase 47:

```powershell
POSTGRES_PORT=55433 docker compose -p noiseproof-agent-fresh up -d db
cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55433/noiseproof"
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
docker compose -p noiseproof-agent-fresh exec -T db psql -U noiseproof -d noiseproof -c "SELECT table_name, column_default FROM information_schema.columns WHERE table_schema = 'public' AND table_name IN ('agent_runs', 'workflow_runs') AND column_name = 'workflow_version' ORDER BY table_name;"
docker compose -p noiseproof-agent-fresh exec -T db psql -U noiseproof -d noiseproof -c "SELECT filename FROM schema_migrations ORDER BY filename;"
POSTGRES_PORT=55433 docker compose -p noiseproof-agent-fresh down -v
```

Expected fresh DB runner evidence:

```text
Initial status: Applied migrations: 0 / Pending migrations: 9
Apply result: applied 002_evidence_ledger_entries.sql through 010_workflow_version_defaults.sql
Final status: Applied migrations: 9 / Pending migrations: 0
Schema defaults: phase40-lineage-warning-code-dashboard
Cleanup: isolated test volume removed
```

Fresh DB API smoke verification from Phase 49:

```powershell
POSTGRES_PORT=55435 docker compose -p noiseproof-agent-api-smoke up -d db
docker compose -p noiseproof-agent-api-smoke exec -T db pg_isready -U noiseproof -d noiseproof
cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55435/noiseproof"
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8018
```

Smoke calls:

```powershell
Invoke-RestMethod http://127.0.0.1:8018/health
Invoke-RestMethod http://127.0.0.1:8018/ops/summary
Invoke-RestMethod http://127.0.0.1:8018/documents -Method Post -ContentType "application/json" -Body '{"source_type":"markdown","source_uri":"sample://fresh-db-api-smoke.md","title":"Sample fresh DB smoke document","source_date":"2026-05-30","extraction_quality":"unknown","status":"registered"}'
Invoke-RestMethod http://127.0.0.1:8018/documents
Invoke-RestMethod http://127.0.0.1:8018/ops/summary
POSTGRES_PORT=55435 docker compose -p noiseproof-agent-api-smoke down -v
```

Expected fresh DB API evidence:

```text
GET /health: status_code 200, workflow_version phase40-lineage-warning-code-dashboard
GET /ops/summary before document create: status_code 200, document_count 0
POST /documents: status_code 201, title Sample fresh DB smoke document
GET /documents: status_code 200, title Sample fresh DB smoke document
GET /ops/summary after document create: status_code 200, document_count 1
Cleanup: isolated test volume removed
```

Failure-case persistence smoke verification from Phase 51:

```powershell
POSTGRES_PORT=55436 docker compose -p noiseproof-agent-failure-smoke up -d db
docker compose -p noiseproof-agent-failure-smoke exec -T db pg_isready -U noiseproof -d noiseproof
cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55436/noiseproof"
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8019
```

Smoke calls:

```powershell
Invoke-RestMethod http://127.0.0.1:8019/health
Invoke-RestMethod http://127.0.0.1:8019/ops/summary
Invoke-RestMethod http://127.0.0.1:8019/failure-cases -Method Post -ContentType "application/json" -Body '{"failure_type":"parser_timeout","description":"Parser preview exceeded local smoke timeout.","root_cause":"simulated parser timeout","fix_status":"open","next_action":"Record parser timeout and keep the source out of report generation until retried."}'
Invoke-RestMethod http://127.0.0.1:8019/failure-cases
Invoke-RestMethod http://127.0.0.1:8019/ops/summary
POSTGRES_PORT=55436 docker compose -p noiseproof-agent-failure-smoke down -v
```

Expected failure-case evidence:

```text
POST /failure-cases: status_code 201, failure_type parser_timeout
GET /failure-cases: status_code 200, root_cause simulated parser timeout
GET /ops/summary before create: failure_case_count 0
GET /ops/summary after create: failure_case_count 1
Cleanup: isolated test volume removed
```

Agent-run failure linkage smoke verification from Phase 53:

```powershell
POSTGRES_PORT=55437 docker compose -p noiseproof-agent-failure-link-smoke up -d db
docker compose -p noiseproof-agent-failure-link-smoke exec -T db pg_isready -U noiseproof -d noiseproof
cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55437/noiseproof"
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8020
```

Smoke calls:

```powershell
Invoke-RestMethod http://127.0.0.1:8020/health
Invoke-RestMethod http://127.0.0.1:8020/agent-runs -Method Post -ContentType "application/json" -Body '{"user_question":"Why did parser preview fail for the uploaded market note?","workflow_version":"phase40-lineage-warning-code-dashboard","status":"failed","error_message":"simulated parser timeout for smoke verification","trace_json":{"smoke":"agent-run-failure-linkage"}}'
Invoke-RestMethod http://127.0.0.1:8020/failure-cases -Method Post -ContentType "application/json" -Body '{"agent_run_id":"<created-agent-run-id>","failure_type":"linked_parser_timeout","description":"Failure case linked to the created agent run.","root_cause":"simulated parser timeout","fix_status":"open","next_action":"Retry parser preview with smaller input and preserve agent_run_id linkage."}'
Invoke-RestMethod http://127.0.0.1:8020/failure-cases
Invoke-RestMethod http://127.0.0.1:8020/agent-runs
Invoke-RestMethod http://127.0.0.1:8020/ops/summary
POSTGRES_PORT=55437 docker compose -p noiseproof-agent-failure-link-smoke down -v
```

Expected linked-failure evidence:

```text
POST /agent-runs: status_code 201, status failed
POST /failure-cases: status_code 201, failure_type linked_parser_timeout, agent_run_id present
GET /failure-cases: status_code 200, agent_run_id matches created run
GET /agent-runs: status_code 200, trace_json.smoke agent-run-failure-linkage
GET /ops/summary: agent_run_count 1, failure_case_count 1
Cleanup: isolated test volume removed
```

## API

From repo root:

```bash
cd apps/api
uv sync
uv run uvicorn app.main:app --reload
```

Expected local URL:

```text
http://localhost:8000
```

## Smoke Checks

```bash
curl http://localhost:8000/health
curl http://localhost:8000/ops/summary
curl http://localhost:8000/ops/dashboard
curl -X POST http://localhost:8000/workflow-runs `
  -H "Content-Type: application/json" `
  -d "{\"question\":\"Which sources disagree about memory demand?\",\"trace_json\":{\"phase\":\"metadata-only\"}}"
curl http://localhost:8000/workflow-runs
curl -X POST http://localhost:8000/workflow-runs/execute-preview `
  -H "Content-Type: application/json" `
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"strategy\":\"fixed-window\",\"sources\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"content\":\"Enterprise segment demand growth was 12 percent in 2026.\"}],\"draft_claims\":[\"Enterprise segment demand growth was supported by current retrieved evidence.\"]}"
curl http://localhost:8000/workflow-runs/<uuid>
curl http://localhost:8000/workflow-runs/<uuid>/lineage
```

Expected `/health` shape:

```json
{
  "status": "ok",
  "service": "noiseproof-agent-api",
  "workflow_version": "phase40-lineage-warning-code-dashboard"
}
```

Expected `/ops/summary` shape:

```json
{
  "status": "placeholder",
  "workflow_version": "phase40-lineage-warning-code-dashboard",
  "document_count": 0,
  "agent_run_count": 0,
  "failure_case_count": 0,
  "noise_gate_record_count": 0,
  "blocked_gate_count": 0,
  "revision_gate_count": 0,
  "report_record_count": 0,
  "generated_report_count": 0,
  "blocked_report_count": 0,
  "revision_report_count": 0,
  "unsupported_claim_count": 0,
  "contradiction_count": 0,
  "average_latency_ms": null,
  "notes": [
    "Retrieval runs recorded: 0. Evidence Ledger persisted entries now drive unsupported and contradiction counts.",
    "Embeddings, semantic retrieval, distributed tracing, and final report generation beyond deterministic previews are still not implemented."
  ]
}
```

Expected workflow-version smoke checks:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/ops/summary
```

Expected workflow-version fields:

```json
{
  "health": {
    "workflow_version": "phase40-lineage-warning-code-dashboard"
  },
  "ops_summary": {
    "workflow_version": "phase40-lineage-warning-code-dashboard"
  }
}
```

These checks confirm the runtime marker used by the smallest service surfaces. They do not mean workflow semantics changed; no workflow semantics changed in Phase 40 or Phase 40.5.

Expected schema-default workflow-version smoke checks:

```sql
SELECT table_name, column_default
FROM information_schema.columns
WHERE table_schema = 'public'
  AND column_name = 'workflow_version'
  AND table_name IN ('agent_runs', 'workflow_runs')
ORDER BY table_name;
```

Expected rows:

```text
agent_runs.workflow_version    DEFAULT 'phase40-lineage-warning-code-dashboard'
workflow_runs.workflow_version DEFAULT 'phase40-lineage-warning-code-dashboard'
```

This is a schema defaults only smoke check. It does not prove workflow execution behavior, child record lineage, retrieval quality, evidence quality, dashboard analytics, or distributed tracing.

Expected `/workflow-runs/{id}/lineage` response shape:

```json
{
  "workflow_run": {
    "id": "uuid",
    "question": "Which segment had enterprise demand growth?",
    "workflow_version": "phase40-lineage-warning-code-dashboard",
    "status": "completed"
  },
  "lineage_boundary": "derived_read_model_only",
  "evidence_ledger_entries": [],
  "noise_gate_lineage": [],
  "report_lineage": [],
  "summary": {
    "evidence_ledger_entry_count": 0,
    "noise_gate_record_count": 0,
    "report_record_count": 0,
    "gate_input_evidence_reference_count": 0,
    "report_input_evidence_reference_count": 0,
    "report_input_gate_reference_count": 0,
    "missing_reference_count": 0
  },
  "warnings": [
    "Workflow lineage read model is a derived read model over existing workflow child records and stage_input_manifest values.",
    "It adds no storage, foreign-key links, join tables, distributed tracing, LLM calls, or free-form final answer generation."
  ],
  "warning_codes": [
    "derived_read_model_boundary",
    "local_workflow_scope"
  ]
}
```

The `warning_codes` field is response-level taxonomy only. It is not persisted as a warning-code table, dashboard analytics surface, or strict relational lineage contract.

Expected `/ops/dashboard` warning-code legend:

```text
Lineage warning codes:
derived_read_model_boundary
local_workflow_scope
missing_manifest_reference
invalid_manifest_shape
```

The dashboard copy must keep saying these codes are response-level taxonomy only and not persisted dashboard analytics.

Profile fixture-like text:

```bash
curl -X POST http://localhost:8000/documents/profile \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"text\":\"# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.\"}"
```

Expected `/documents/profile` shape:

```json
{
  "source_type": "markdown",
  "character_count": 69,
  "line_count": 4,
  "approximate_token_count": 18,
  "has_tables": false,
  "has_urls": true,
  "has_dates": true,
  "has_numbers": true,
  "extraction_quality": "medium",
  "recommended_strategy": "heading-aware",
  "warnings": [
    "Very short text; profile may not represent a full document."
  ]
}
```

Preview parser output without saving it:

```bash
curl -X POST http://localhost:8000/documents/parse-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"content\":\"# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.\"}"
```

Expected `/documents/parse-preview` shape:

```json
{
  "source_type": "markdown",
  "parser": "markdown",
  "text": "# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.",
  "metadata": {
    "heading_count": 1,
    "link_count": 1,
    "bullet_count": 0
  },
  "warnings": [],
  "failure_case_candidate": null,
  "profile": {
    "source_type": "markdown",
    "character_count": 69,
    "line_count": 4,
    "approximate_token_count": 18,
    "has_tables": false,
    "has_urls": true,
    "has_dates": true,
    "has_numbers": true,
    "extraction_quality": "medium",
    "recommended_strategy": "heading-aware",
    "warnings": [
      "Very short text; profile may not represent a full document."
    ]
  }
}
```

PDF preview boundary:

```bash
curl -X POST http://localhost:8000/documents/parse-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"pdf\",\"content\":\"Extracted PDF text preview only.\"}"
```

The PDF parser is currently a text-only fallback. Robust PDF extraction is not claimed.

Preview chunk strategy comparison without saving chunks:

```bash
curl -X POST http://localhost:8000/documents/chunk-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"content\":\"# Market\nRevenue grew 12% in 2026.\n\n## Risks\nCosts rose 7%.\",\"max_characters\":80,\"overlap\":10}"
```

Expected `/documents/chunk-preview` shape:

```json
{
  "source_type": "markdown",
  "parser": "markdown",
  "profile": {},
  "parse_warnings": [],
  "failure_case_candidate": null,
  "strategies": [
    {
      "strategy": "fixed-window",
      "chunks": [
        {
          "strategy": "fixed-window",
          "chunk_index": 0,
          "text": "...",
          "character_count": 59,
          "approximate_token_count": 15,
          "metadata": {
            "start": 0,
            "end": 59
          }
        }
      ],
      "metrics": {
        "chunk_count": 1,
        "max_characters": 80,
        "overlap": 10
      },
      "warnings": []
    },
    {
      "strategy": "heading-aware",
      "chunks": [
        {
          "strategy": "heading-aware",
          "chunk_index": 0,
          "text": "...",
          "character_count": 34,
          "approximate_token_count": 9,
          "metadata": {
            "header_path": "Market",
            "heading_level": 1
          }
        }
      ],
      "metrics": {
        "chunk_count": 2,
        "boundary_count": 2
      },
      "warnings": []
    },
    {
      "strategy": "row-aware",
      "chunks": [
        {
          "strategy": "row-aware",
          "chunk_index": 0,
          "text": "...",
          "character_count": 8,
          "approximate_token_count": 2,
          "metadata": {
            "row_start": 1,
            "row_end": 1
          }
        }
      ],
      "metrics": {
        "chunk_count": 4,
        "boundary_count": 4
      },
      "warnings": [
        "Source type is not CSV; row-aware strategy used non-empty text lines as row boundaries."
      ]
    }
  ]
}
```

Run lexical retrieval v0 and record the run:

```bash
curl -X POST http://localhost:8000/retrieval-runs \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"strategy\":\"heading-aware\",\"sources\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"content\":\"# Demand\nEnterprise demand grew 12% in 2026.\"},{\"source_id\":\"doc-noise\",\"source_type\":\"markdown\",\"content\":\"# Weather\nRainfall was heavy in Seoul.\"}]}"
```

Expected `/retrieval-runs` response shape:

```json
{
  "id": "uuid",
  "question": "Which segment had enterprise demand growth?",
  "strategy": "heading-aware",
  "status": "completed",
  "latency_ms": 0,
  "result_count": 1,
  "hit_rate": 1.0,
  "citation_coverage": 1.0,
  "missing_evidence_count": 0,
  "metadata_json": {
    "source_count": 2,
    "top_k": 5,
    "max_characters": 500,
    "overlap": 0,
    "warning_count": 0
  },
  "created_at": "timestamp",
  "results": [
    {
      "source_id": "doc-demand",
      "source_type": "markdown",
      "chunk_strategy": "heading-aware",
      "chunk_index": 0,
      "text": "...",
      "score": 0.75,
      "matched_terms": ["demand", "enterprise", "growth"],
      "metadata": {}
    }
  ],
  "warnings": []
}
```

No-results retrieval is recorded with:

```json
{
  "status": "no_results",
  "result_count": 0,
  "missing_evidence_count": 1,
  "results": []
}
```

Create a Collection Plan Preview without saving or retrieving anything:

```bash
curl -X POST http://localhost:8000/collection-plans/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Did this company's AI narrative become materially stronger?\"}"
```

Expected `/collection-plans/preview` response shape:

```json
{
  "question": "Did this company's AI narrative become materially stronger?",
  "information_need": "Determine which role-diverse sources are needed before retrieval for: ...",
  "possible_claims": [
    "The available sources support a limited claim about: ...",
    "The available sources weaken or contradict a claim about: ...",
    "The current sources are insufficient to make a stronger claim about: ..."
  ],
  "required_roles": [
    "direct_support",
    "contradiction",
    "timeline_anchor",
    "missing_data_signal"
  ],
  "source_types_to_check": [
    "news",
    "financial_report",
    "company_statement",
    "analyst_note"
  ],
  "minimum_evidence_needed": "at least one direct support source; one contradiction or missing-data signal; one visible timeline anchor.",
  "known_risks": [
    "same-source repeated narrative may look like independent confirmation",
    "marketing narrative may outrun operational evidence"
  ],
  "stop_conditions": [
    "only same-source repeated narrative found",
    "no contradiction or missing-data signal found"
  ],
  "warnings": [
    "Collection Plan Preview does not judge truth or retrieve evidence.",
    "This plan only defines information roles needed before retrieval."
  ]
}
```

Buy/sell-style questions should include `user_intent_check` and a stop condition for buy/sell drift. This endpoint does not call an LLM, search external sources, expand retrieval, generate an Evidence Ledger, create a final report, build a dashboard, or persist records.

Create an Evidence Ledger Preview from retrieval candidates:

```bash
curl -X POST http://localhost:8000/evidence-ledgers/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"retrieval_results\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"chunk_strategy\":\"heading-aware\",\"chunk_index\":0,\"text\":\"Enterprise demand grew 12% in 2026.\",\"score\":0.75,\"matched_terms\":[\"demand\",\"enterprise\",\"growth\"],\"metadata\":{\"source_date\":\"2026-05-28\"}}]}"
```

Expected `/ops/dashboard` behavior:

```text
Returns text/html with Operations Dashboard v0, summary counts, recent agent runs, failure cases, and retrieval runs.
```

Expected failure-case workflow parent dashboard smoke check:

```text
Failure Cases
Workflow Parent
href="/workflow-runs/<workflow_run_id>">...
manual workflow parent link
not automatic failure-case creation
```

Expected `/evidence-ledgers/preview` response shape:

```json
{
  "question": "Which segment had enterprise demand growth?",
  "entries": [
    {
      "claim": "Which segment had enterprise demand growth",
      "source_id": "doc-demand",
      "source_type": "markdown",
      "source_date": "2026-05-28",
      "evidence_span": "Enterprise demand grew 12% in 2026.",
      "confidence": "medium",
      "limitation": "Supported by a lexical retrieval candidate; not yet validated by a Critic / Noise Gate.",
      "contradicting_source_ids": [],
      "status": "supported",
      "matched_terms": ["demand", "enterprise", "growth"],
      "role": "direct_support"
    }
  ],
  "summary": {
    "supported_count": 1,
    "weakly_supported_count": 0,
    "contradicted_count": 0,
    "unsupported_count": 0,
    "blocked_count": 0,
    "source_count": 1
  },
  "warnings": [
    "Evidence Ledger Preview does not judge final truth or generate a final report.",
    "Entries are derived from retrieval candidates and must still pass a future Critic / Noise Gate."
  ]
}
```

No-evidence and buy/sell-style questions produce `blocked` ledger entries. Contradiction language is surfaced as `contradicted`. The `/preview` endpoint does not call an LLM, search external sources, run a Critic / Noise Gate, create a final report, build a dashboard, or persist Evidence Ledger entries by itself.

Persist an Evidence Ledger v0 record set:

```bash
curl -X POST http://localhost:8000/evidence-ledgers \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Should I buy this company?\",\"retrieval_results\":[]}"
curl http://localhost:8000/evidence-ledgers
```

Expected persisted response shape:

```json
{
  "question": "Should I buy this company?",
  "entries": [
    {
      "id": "uuid",
      "question": "Should I buy this company?",
      "claim": "Should I buy this company",
      "status": "blocked",
      "role": "user_intent_check",
      "created_at": "timestamp"
    }
  ],
  "summary": {
    "blocked_count": 1
  },
  "stored_entry_count": 1
}
```

Evidence Ledger persistence is v0. It does not link entries to retrieval run ids, persist report records, call an LLM, or judge final truth. Noise Gate records are persisted separately by `POST /noise-gates`.

Preview whether current ledger entries can pass the Noise Gate:

```bash
curl -X POST http://localhost:8000/noise-gates/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
```

Expected `/noise-gates/preview` response shape:

```json
{
  "question": "Which segment had enterprise demand growth?",
  "decision": "pass",
  "final_response_allowed": true,
  "checks": [
    {
      "name": "every_strong_claim_has_evidence",
      "status": "pass",
      "message": "Every current ledger claim has source-linked evidence."
    }
  ],
  "blocked_claims": [],
  "downgraded_claims": [],
  "allowed_claims": ["Enterprise demand grew"],
  "required_revisions": [],
  "fallback_message": null,
  "warnings": [
    "Noise Gate Preview does not generate a report or call an LLM.",
    "It only checks whether current ledger evidence can pass into a future report stage."
  ]
}
```

Unsupported or blocked ledger entries return `decision: blocked`. Contradictions, missing source dates, missing limitations, high-confidence single-source claims, and overconfident draft language return `decision: needs_revision` unless trading-advice drift blocks the response. This endpoint does not call an LLM, persist gate records, create a final report, or build a dashboard.

Persist a Noise Gate v0 record:

```bash
curl -X POST http://localhost:8000/noise-gates \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Should I buy this company?\",\"evidence_entries\":[{\"claim\":\"Should I buy this company\",\"source_id\":null,\"source_type\":null,\"source_date\":null,\"evidence_span\":\"\",\"confidence\":\"none\",\"limitation\":\"Question drifts into buy/sell or financial-advice intent.\",\"contradicting_source_ids\":[],\"status\":\"blocked\",\"matched_terms\":[],\"role\":\"user_intent_check\"}],\"draft_claims\":[\"Should I buy this company?\"]}"
curl http://localhost:8000/noise-gates
```

Expected persisted response shape:

```json
{
  "id": "uuid",
  "question": "Should I buy this company?",
  "decision": "blocked",
  "final_response_allowed": false,
  "evidence_entry_count": 1,
  "draft_claim_count": 1,
  "created_at": "timestamp"
}
```

Current persistence is v0. It does not link gate records to an `agent_runs` id, persist report records, call an LLM, or judge final truth.

Preview a claim-bounded report after the Noise Gate:

```bash
curl -X POST http://localhost:8000/reports/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
```

Expected `/reports/preview` response shape:

```json
{
  "question": "Which segment had enterprise demand growth?",
  "status": "generated",
  "report": {
    "summary": "1 claim(s) can be stated with current evidence boundaries.",
    "claims": [
      {
        "claim": "Enterprise demand grew",
        "source_ids": ["doc-demand"],
        "evidence_spans": ["Enterprise demand grew 12% in 2026."],
        "confidence": "medium",
        "limitations": ["Supported by one retrieved source."],
        "contradictions": []
      }
    ],
    "limitations": ["Supported by one retrieved source."],
    "contradictions": [],
    "next_data_needed": [
      "Add an independent second source for claim: Enterprise demand grew",
      "Check for contradicting sources for claim: Enterprise demand grew"
    ]
  },
  "gate": {},
  "fallback_message": null,
  "required_revisions": [],
  "warnings": [
    "Report Preview is deterministic and does not use an LLM.",
    "It only formats claims that passed the Noise Gate; it does not create new claims."
  ]
}
```

If the Noise Gate returns `blocked` or `needs_revision`, `report` is `null` and the response includes `fallback_message` plus `required_revisions`. This endpoint does not call an LLM, persist report records, create a dashboard, or create claims outside the allowed gate output.

Persist a deterministic Report Preview v0 record:

```bash
curl -X POST http://localhost:8000/reports \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl http://localhost:8000/reports
```

Expected persisted response shape:

```json
{
  "id": "uuid",
  "question": "Which segment had enterprise demand growth?",
  "status": "generated",
  "workflow_trace_id": "uuid",
  "agent_run_id": "uuid",
  "gate_decision": "pass",
  "claim_count": 1,
  "evidence_entry_count": 1,
  "draft_claim_count": 1,
  "created_at": "timestamp"
}
```

Current report persistence is v0. It stores deterministic preview output only; it does not call an LLM or create a free-form final report.
Persisted evidence, gate, and report records include both `workflow_trace_id` and `agent_run_id`. The same `workflow_trace_id` is written to the matching `agent_runs.trace_json` entry for the persistence endpoint. This is local parent/child linkage, not full distributed tracing.
Use `GET /traces/{workflow_trace_id}` to inspect records and agent-run traces that share that id.
Use the persisted record list filters to narrow evidence, gate, and report records without adding search or ranking:

```bash
curl "http://localhost:8000/evidence-ledgers?workflow_trace_id=<uuid>"
curl "http://localhost:8000/evidence-ledgers?status=blocked"
curl "http://localhost:8000/noise-gates?workflow_trace_id=<uuid>"
curl "http://localhost:8000/noise-gates?decision=blocked"
curl "http://localhost:8000/reports?workflow_trace_id=<uuid>"
curl "http://localhost:8000/reports?status=generated"
curl "http://localhost:8000/traces/<uuid>"
```

Open the dashboard to use the same trace lookup and filter endpoints from a browser-readable surface:

```bash
curl http://localhost:8000/ops/dashboard
```

The dashboard links are navigation aids over existing records. Evidence Ledger, Noise Gate, and Report rows also expose parent run links through `GET /traces/{workflow_trace_id}`. They do not add ranking, search, LLM calls, distributed tracing, hosted observability, or UI polish.

### Local browser screenshot walkthrough

The local browser screenshot walkthrough records the current dashboard as a visual inspection artifact:

```text
docs/review/local-browser-screenshot-walkthrough.md
docs/review/media/local-browser-dashboard-walkthrough.png
```

To reproduce the same class of artifact, start the local database, apply migrations, run the API, create or reuse a deterministic workflow preview, and open:

```text
GET /ops/dashboard
GET /workflow-runs/{id}/lineage
```

The screenshot must remain a local visual proof surface only. It is not hosted deployment evidence, customer validation, external reviewer feedback, production observability, semantic retrieval evidence, or LLM evidence.

### External review request packet

Phase marker: external review request packet v0.

The external review request packet prepares the next feedback gate:

```text
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
.github/ISSUE_TEMPLATE/external-review-feedback.md
https://github.com/svy04/noiseproof-agent/issues/1
docs/review/external-feedback-intake-criteria.md
```

Use it when asking an outside reviewer to inspect the 5-minute proof path and leave bounded critique. This is request infrastructure only; it is not external reviewer feedback, customer validation, Braincrew acceptance, or hosted deployment evidence.

The next evidence gate remains:

```text
external reviewer feedback v0
```

Phase marker: external feedback intake criteria v0.

Only comments that satisfy `docs/review/external-feedback-intake-criteria.md` should be counted as external reviewer feedback. A self-authored comment, request for feedback, empty acknowledgement, generic praise, CI status, or bot-generated summary must not close the feedback gate.

Phase marker: external reviewer brief v0.

Use `docs/review/external-reviewer-brief.md` when the reviewer needs a 2-minute path. This is not external reviewer feedback and must not close the gate by itself.

Phase marker: external reviewer live proof route refresh v0.

Use `docs/review/external-reviewer-live-proof-route-refresh.md` when the reviewer needs the latest public portfolio proof route:

```text
https://svy04.github.io/proof-artifacts/noiseproof-live-route-verification-2026-06-01/
```

This route refresh helps external reviewers find the public proof surface, reviewer brief, and issue #1. It is not external reviewer feedback, not hosted deployment evidence for NoiseProof Agent, not customer validation, and not a product-complete claim.

Phase marker: external reviewer link map v0.

Use `docs/review/external-reviewer-link-map.md` when an outside reviewer needs direct links to issue #1, README, the proof path, the portfolio index, the screenshot walkthrough, and feedback criteria. This is link hygiene only. It is not external reviewer feedback, customer validation, Braincrew acceptance, or hosted deployment evidence.

Phase marker: external review root guide v0.

Use `CONTRIBUTING.md` when an outside reviewer starts from the repository root. `docs/review/external-review-root-guide.md` records why the root guide exists. It is review-entry infrastructure only and is not external reviewer feedback.

Phase marker: external review issue body encoding verification v0.

Use `docs/review/external-review-issue-body-encoding-verification.md` when verifying that the live public issue #1 body begins directly with `## Request` and first codepoint `35`. This is request-surface readability evidence only and is not external reviewer feedback.

Phase marker: external review issue body root-guide verification v0.

Use `docs/review/external-review-issue-body-root-guide-verification.md` when verifying that the live public issue #1 body includes the root review guide link. The verified `comment_count` is `1`, and the only current comment is owner-authored request/status context, so this does not close the external reviewer feedback gate.

Phase marker: external review issue body link-map verification v0.

Use `docs/review/external-review-issue-body-link-map-verification.md` when verifying that the live public issue #1 body includes the reviewer link map and direct README link. The verified `comment_count` is `1`, and the only current comment is owner-authored request/status context, so this does not close the external reviewer feedback gate.

Phase marker: external review issue template link-map refresh v0.

Use `docs/review/external-review-issue-template-link-map-refresh.md` when checking why `.github/ISSUE_TEMPLATE/external-review-feedback.md` includes direct reviewer links. This refresh helps future reviewers who open a new issue from the template, but it is not external reviewer feedback.

Phase marker: external review issue label verification v0.

Use `docs/review/external-review-issue-label-verification.md` when checking whether the live public issue #1 is labeled as an external review / feedback request. The verified labels are `external-review` and `feedback`; the verified `comment_count` remains `0`, so this does not close the external reviewer feedback gate.

Phase marker: external review owner request comment verification v0.

Use `docs/review/external-review-owner-request-comment-verification.md` when checking why the owner-authored issue #1 request/status comment does not count as feedback. The remote workflow screened the comment as `non_qualifying` with `self_authored_comment`; the downloaded artifacts kept `candidate_count: 0` and `draft_count: 0`.

Phase marker: external reviewer outreach packet v0.

Use `docs/review/external-reviewer-outreach-packet.md` when you need copy-paste outreach messages for an actual human reviewer. It has separate messages for an FDE / product engineer reviewer, a RAG / data engineer reviewer, and a founder / operator reviewer.

The outreach packet is request infrastructure only. It is not external reviewer feedback, customer validation, Braincrew acceptance, or hosted deployment evidence.

Phase marker: external feedback qualification preview v0.

Use `packages/review/external_feedback.py` when issue #1 has public comments and you need a local pre-screen before writing any proof artifact. The helper can flag obvious non-qualifying comments and possible candidates that still require manual acceptance.

The qualification preview does not close the gate. `candidate_found_manual_review_required` means a human still needs to compare the comment against `docs/review/external-feedback-intake-criteria.md` before recording external reviewer feedback.

Phase marker: external feedback screening cli v0.

Capture issue #1 comments and run the local CLI:

```powershell
$tmp = Join-Path $env:TEMP "noiseproof-issue-1-comments.json"
gh issue view 1 --repo svy04/noiseproof-agent --json comments | Set-Content -Path $tmp -Encoding utf8
python -m packages.review.external_feedback_cli --input $tmp --repository-owner svy04
```

The current smoke result for issue #1 is `pending` with `comment_count: 0`. This does not close the gate and is not external reviewer feedback.

Phase marker: external feedback screening workflow v0.

GitHub Actions workflow:

```text
.github/workflows/external-feedback-screen.yml
```

It runs on `workflow_dispatch`, `issue_comment` created/edited events, and push verification. It uploads `external-feedback-screen.json`.

The uploaded artifact is only a screen result. It is not accepted external reviewer feedback and does not close `external reviewer feedback v0`.

Phase marker: external feedback screening workflow verification v0.

Verified remote run:

```text
26724730074
```

Downloaded artifact:

```text
external-feedback-screen.json
```

The downloaded result was `pending` with `candidate_count: 0`. This proves the screening workflow uploaded an inspectable artifact, but it is not external reviewer feedback.

Phase marker: readme next-gate stale-claim refresh v0.

Use `docs/review/readme-next-gate-stale-claim-refresh.md` when checking why the README `What I Would Improve Next` section points to `external reviewer feedback v0`.

The refresh only removes a stale next-step claim from the repository front door. It is not external reviewer feedback, customer validation, Braincrew acceptance, hosted deployment evidence, or production readiness.

Phase marker: external feedback acceptance template v0.

Use `docs/review/external-feedback-acceptance-template.md` only after issue #1 receives a public outside comment that passes the screening workflow and satisfies `docs/review/external-feedback-intake-criteria.md`.

The template is empty proof infrastructure. It is not external reviewer feedback until a future qualifying public comment is manually accepted and recorded.

Phase marker: external feedback acceptance draft cli v0.

Use `python -m packages.review.external_feedback_acceptance_cli --input external-feedback-screen.json` only after the screening artifact contains candidate comments.

The CLI produces `manual_acceptance_required` drafts. It does not close the gate and is not external reviewer feedback.

Phase marker: external feedback acceptance draft workflow v0.

The GitHub Actions screening workflow uploads `external-feedback-acceptance-draft.json` next to `external-feedback-screen.json`.

The artifact is still a draft. It does not close the gate and is not external reviewer feedback.

Phase marker: external feedback acceptance draft workflow verification v0.

Verified remote run:

```text
26727047243
```

Downloaded artifacts:

```text
external-feedback-screen.json
external-feedback-acceptance-draft.json
```

The downloaded acceptance draft result was `pending` with `draft_count: 0`. This proves the workflow uploaded an inspectable draft artifact, but it is not external reviewer feedback.

Phase marker: owner-approved product continuation decision v0.

Use `docs/review/owner-approved-product-continuation-decision.md` when checking why product implementation is allowed to continue while `external reviewer feedback v0` remains pending.

This decision is not external reviewer feedback, customer validation, Braincrew acceptance, hosted deployment evidence, production readiness, or a product-complete claim. It unblocked `file upload preview v0` while the evidence gate stayed pending.

Inspect auto-created preview traces:

```bash
curl http://localhost:8000/agent-runs
```

Expected trace boundary:

```json
[
  {
    "workflow_version": "phase40-lineage-warning-code-dashboard",
    "status": "completed",
    "trace_json": {
      "endpoint": "POST /reports/preview",
      "phase": "phase40-lineage-warning-code-dashboard",
      "workflow_trace_id": "uuid",
      "report_status": "generated"
    }
  }
]
```

The trace is metadata for inspectability. It is not distributed tracing or hosted observability.

Phase marker: file upload preview v0.

Use `POST /documents/upload-preview` to inspect an uploaded file through parser preview and document profiling without creating a document record.

```bash
curl -X POST http://localhost:8000/documents/upload-preview \
  -F "source_type=markdown" \
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"
```

Expected boundary:

```json
{
  "persistence_boundary": "preview_only_not_persisted",
  "filename": "sample-note.md",
  "parser": "markdown",
  "warnings": [
    "Upload preview is preview-only and does not create documents or persist parse records.",
    "File upload preview does not claim robust PDF extraction."
  ]
}
```

The upload preview is preview-only. It does not create documents, parse records, chunks, retrieval runs, Evidence Ledger entries, Noise Gate records, reports, workflow runs, or failure cases.

Phase marker: uploaded file chunk preview v0.

Use `POST /documents/upload-chunk-preview` to inspect an uploaded file through parser preview, document profiling, and chunk strategy comparison without creating documents or chunks.

```bash
curl -X POST http://localhost:8000/documents/upload-chunk-preview \
  -F "source_type=csv" \
  -F "max_characters=500" \
  -F "overlap=0" \
  -F "file=@examples/messy-market-data/sample-market.csv;type=text/csv"
```

Expected boundary:

```json
{
  "persistence_boundary": "preview_only_not_persisted",
  "filename": "sample-market.csv",
  "parser": "csv",
  "strategies": [
    {"strategy": "fixed-window"},
    {"strategy": "row-aware"}
  ]
}
```

The uploaded file chunk preview is preview-only. It does not create documents, chunks, retrieval runs, Evidence Ledger entries, Noise Gate records, reports, workflow runs, or failure cases.

Phase marker: uploaded file retrieval preview v0.

Use `POST /documents/upload-retrieval-preview` to run lexical retrieval over an uploaded file without creating a retrieval run record.

```bash
curl -X POST http://localhost:8000/documents/upload-retrieval-preview \
  -F "question=Which source mentions enterprise demand growth?" \
  -F "source_type=markdown" \
  -F "strategy=fixed-window" \
  -F "top_k=3" \
  -F "max_characters=500" \
  -F "overlap=0" \
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"
```

Expected boundary:

```json
{
  "persistence_boundary": "preview_only_not_persisted",
  "filename": "sample-note.md",
  "status": "completed",
  "results": [
    {"source_id": "upload://sample-note.md"}
  ]
}
```

The uploaded file retrieval preview is preview-only. It does not create retrieval_runs, documents, chunks, Evidence Ledger entries, Noise Gate records, reports, workflow runs, or failure cases. Buy/sell questions are blocked at this preview boundary.

Phase marker: uploaded file Evidence Ledger preview v0.

Use `POST /documents/upload-evidence-preview` to run lexical retrieval over an uploaded file and convert the returned candidates into preview Evidence Ledger entries without creating retrieval run or Evidence Ledger records.

```bash
curl -X POST http://localhost:8000/documents/upload-evidence-preview \
  -F "question=Which source supports enterprise demand growth?" \
  -F "source_type=markdown" \
  -F "strategy=fixed-window" \
  -F "top_k=3" \
  -F "max_characters=500" \
  -F "overlap=0" \
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"
```

Expected boundary:

```json
{
  "persistence_boundary": "preview_only_not_persisted",
  "filename": "sample-note.md",
  "status": "completed",
  "retrieval": {
    "result_count": 1
  },
  "evidence": {
    "entries": [
      {"source_id": "upload://sample-note.md"}
    ]
  }
}
```

The uploaded file Evidence Ledger preview is preview-only. It does not create Evidence Ledger entries, retrieval_runs, documents, chunks, Noise Gate records, reports, workflow runs, or failure cases. It is not Noise Gate and not a final report. Buy/sell questions are blocked at this preview boundary.

Phase marker: uploaded file Noise Gate preview v0.

Use `POST /documents/upload-noise-gate-preview` to run lexical retrieval over an uploaded file, convert the returned candidates into preview Evidence Ledger entries, and check them with the deterministic Noise Gate without creating retrieval run, Evidence Ledger, or Noise Gate records.

```bash
curl -X POST http://localhost:8000/documents/upload-noise-gate-preview \
  -F "question=Which source supports enterprise demand growth?" \
  -F "source_type=markdown" \
  -F "strategy=fixed-window" \
  -F "top_k=3" \
  -F "max_characters=500" \
  -F "overlap=0" \
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"
```

Expected boundary:

```json
{
  "persistence_boundary": "preview_only_not_persisted",
  "filename": "sample-note.md",
  "status": "needs_revision",
  "gate": {
    "decision": "needs_revision",
    "final_response_allowed": false
  }
}
```

The uploaded file Noise Gate preview is preview-only. It does not create Noise Gate records, Evidence Ledger entries, retrieval_runs, documents, chunks, reports, workflow runs, or failure cases. It is not final report generation. Buy/sell questions are blocked at this preview boundary.

Phase marker: uploaded file report preview v0.

Use `POST /documents/upload-report-preview` to run lexical retrieval over an uploaded file, convert the returned candidates into preview Evidence Ledger entries, run the deterministic Noise Gate, and format a claim-bounded report preview only when the gate allows it.

```bash
curl -X POST http://localhost:8000/documents/upload-report-preview \
  -F "question=Which source supports enterprise demand growth?" \
  -F "source_type=markdown" \
  -F "strategy=fixed-window" \
  -F "top_k=3" \
  -F "max_characters=500" \
  -F "overlap=0" \
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"
```

Expected boundary:

```json
{
  "persistence_boundary": "preview_only_not_persisted",
  "filename": "sample-note.md",
  "status": "needs_revision",
  "report": {
    "status": "needs_revision",
    "report": null,
    "gate": {
      "decision": "needs_revision"
    }
  }
}
```

The uploaded file report preview is preview-only. It does not create report records, Noise Gate records, Evidence Ledger entries, retrieval_runs, documents, chunks, workflow runs, or failure cases. It is not LLM output. If the embedded Noise Gate returns `needs_revision` or `blocked`, the report body remains null. Buy/sell questions are blocked at this preview boundary.

Phase marker: uploaded file failure-case draft preview v0.

Use `POST /documents/upload-failure-case-draft-preview` to run the uploaded file report preview chain and turn the result into a human-confirmed failure-case draft payload without creating `failure_cases`.

```bash
curl -X POST http://localhost:8000/documents/upload-failure-case-draft-preview \
  -F "question=Which source supports enterprise demand growth?" \
  -F "source_type=markdown" \
  -F "strategy=fixed-window" \
  -F "top_k=3" \
  -F "max_characters=500" \
  -F "overlap=0" \
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"
```

Expected boundary:

```json
{
  "persistence_boundary": "preview_only_not_persisted",
  "status": "needs_revision",
  "draft_preview": {
    "persistence_boundary": "preview_only_not_persisted",
    "human_confirmation_required": true,
    "draft": {
      "fix_status": "draft"
    }
  }
}
```

The uploaded file failure-case draft preview is preview-only. It does not create failure_cases. It is not automatic failure detection and not root-cause automation. A human must confirm or edit the draft before submitting it through `POST /failure-cases`. Buy/sell questions remain blocked at this preview boundary.

Phase marker: uploaded file failure-case manual handoff smoke v0.

Manual handoff smoke path:

```bash
# 1. Create an uploaded-file failure-case draft.
curl -X POST http://localhost:8000/documents/upload-failure-case-draft-preview \
  -F "question=Should I sell this stock?" \
  -F "source_type=markdown" \
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"

# 2. Inspect the returned draft_preview.draft payload.
# 3. Manually submit the confirmed or edited draft payload.
curl -X POST http://localhost:8000/failure-cases \
  -H "Content-Type: application/json" \
  -d "{\"failure_type\":\"workflow_stage_error\",\"description\":\"Workflow question 'Should I sell this stock?' reached status blocked at uploaded_file_report_preview.\",\"root_cause\":\"UploadedReportBlocked: Reframe buy/sell or target-price intent into evidence-based market intelligence.\",\"fix_status\":\"draft\",\"next_action\":\"Review the failed workflow stage, confirm the failure type, then manually submit or edit the failure case.\"}"

curl http://localhost:8000/failure-cases
```

This smoke path is a manual handoff. It is not automatic failure-case creation, not automatic failure detection, and not root-cause automation.

Phase marker: uploaded file proof path index refresh v0.

Use `docs/review/uploaded-file-proof-path-index.md` when a reviewer needs the compact uploaded-file proof chain:

```text
file upload preview
-> uploaded file chunk preview
-> uploaded file retrieval preview
-> uploaded file Evidence Ledger preview
-> uploaded file Noise Gate preview
-> uploaded file report preview
-> uploaded file failure-case draft preview
-> uploaded file failure-case manual handoff smoke
```

The index is documentation only. It is not hosted deployment evidence, not external reviewer feedback, not customer validation, not automatic failure-case creation, and not runtime smoke evidence by itself.

Phase marker: uploaded file runtime smoke packet v0.

Use `docs/review/uploaded-file-runtime-smoke-packet.md` for the local HTTP proof packet over the uploaded-file chain.

Local smoke shape:

```powershell
docker compose up -d db
docker compose ps
cd apps/api
uv run python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8030

curl.exe -s http://127.0.0.1:8030/health

curl.exe -s -X POST http://127.0.0.1:8030/documents/upload-preview `
  -F "source_type=markdown" `
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"

curl.exe -s -X POST http://127.0.0.1:8030/documents/upload-chunk-preview `
  -F "source_type=markdown" `
  -F "max_characters=120" `
  -F "overlap=0" `
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"

curl.exe -s -X POST http://127.0.0.1:8030/documents/upload-retrieval-preview `
  -F "question=Which source supports enterprise demand growth?" `
  -F "source_type=markdown" `
  -F "strategy=fixed-window" `
  -F "top_k=3" `
  -F "max_characters=120" `
  -F "overlap=0" `
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"

curl.exe -s -X POST http://127.0.0.1:8030/documents/upload-evidence-preview `
  -F "question=Which source supports enterprise demand growth?" `
  -F "source_type=markdown" `
  -F "strategy=fixed-window" `
  -F "top_k=3" `
  -F "max_characters=120" `
  -F "overlap=0" `
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"

curl.exe -s -X POST http://127.0.0.1:8030/documents/upload-noise-gate-preview `
  -F "question=Which source supports enterprise demand growth?" `
  -F "source_type=markdown" `
  -F "strategy=fixed-window" `
  -F "top_k=3" `
  -F "max_characters=120" `
  -F "overlap=0" `
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"

curl.exe -s -X POST http://127.0.0.1:8030/documents/upload-report-preview `
  -F "question=Which source supports enterprise demand growth?" `
  -F "source_type=markdown" `
  -F "strategy=fixed-window" `
  -F "top_k=3" `
  -F "max_characters=120" `
  -F "overlap=0" `
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"

curl.exe -s -X POST http://127.0.0.1:8030/documents/upload-failure-case-draft-preview `
  -F "question=Which source supports enterprise demand growth?" `
  -F "source_type=markdown" `
  -F "strategy=fixed-window" `
  -F "top_k=3" `
  -F "max_characters=120" `
  -F "overlap=0" `
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"

# Manually submit the returned draft_preview.draft payload:
curl.exe -s -X POST http://127.0.0.1:8030/failure-cases `
  -H "Content-Type: application/json" `
  -d "<confirmed draft_preview.draft JSON>"

curl.exe -s http://127.0.0.1:8030/failure-cases
```

This packet is local runtime evidence only. It is not hosted deployment evidence, not external reviewer feedback, not customer validation, not automatic failure-case creation, and not production readiness.

Phase marker: persisted uploaded file intake review v0.

Use `docs/review/persisted-uploaded-file-intake-review.md` before adding any upload persistence behavior.

Current decision:

```text
preview-only remains the current runtime boundary
```

Do not persist raw uploaded bytes yet. Do not create file storage, document rows, chunks, retrieval runs, Evidence Ledger entries, Noise Gate records, reports, workflow runs, or failure cases from upload preview automatically.

Next bounded implementation candidate:

```text
uploaded file intake manifest preview v0
```

That candidate should expose the manifest shape a future persisted intake boundary would need while keeping `persistence_boundary = preview_only_not_persisted`.

Phase marker: uploaded file intake manifest preview v0.

Use `POST /documents/upload-intake-manifest-preview` to inspect the future upload intake manifest without persisting raw uploaded bytes.

```powershell
curl.exe -s -X POST http://127.0.0.1:8030/documents/upload-intake-manifest-preview `
  -F "source_type=markdown" `
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown"
```

Expected fields include `content_sha256`, `manifest.source_uri`, `manifest.profile`, `storage_decision = do_not_persist_raw_upload_yet`, `replayable = false`, and `persistence_boundary = preview_only_not_persisted`.

This endpoint is preview-only. It is not raw file storage, not retrieval persistence, not document row creation, and not production readiness.

Phase marker: uploaded file intake manifest runtime smoke v0.

Use `docs/review/uploaded-file-intake-manifest-runtime-smoke.md` for the local HTTP proof packet for the intake manifest endpoint.

Observed local smoke fields include:

```text
POST /documents/upload-intake-manifest-preview -> 200
content_sha256 -> 4e253da30538337b4fd8ceaaf24f1bdb6b1287a085b91d38c08b9b78eb4cd7a4
storage_decision -> do_not_persist_raw_upload_yet
replayable -> false
persistence_boundary -> preview_only_not_persisted
```

This smoke is not hosted deployment evidence, not external reviewer feedback, not raw file storage, and not retrieval persistence.

Phase marker: uploaded file intake manifest application refresh v0.

Use `docs/review/uploaded-file-intake-manifest-application-refresh.md` when updating application-facing claims about the upload intake manifest endpoint.

Allowed application claim:

```text
NoiseProof can expose a preview-only uploaded-file intake manifest with content hash, parser/profile summary, and explicit storage boundary before opening raw file persistence.
```

Forbidden application claim:

```text
This is not hosted deployment evidence, not raw file storage, not retrieval persistence, and not production readiness.
```

Phase marker: external reviewer upload-manifest request refresh v0.

Use `docs/review/external-reviewer-upload-manifest-request-refresh.md` when checking why the reviewer request path now points to uploaded-file intake manifest proof.

Reviewer-facing manifest proof:

```text
docs/review/uploaded-file-intake-manifest-preview.md
docs/review/uploaded-file-intake-manifest-runtime-smoke.md
docs/review/uploaded-file-intake-manifest-application-refresh.md
```

This request refresh is not external reviewer feedback, not raw file storage, not hosted deployment evidence, and not production readiness.

Phase marker: external reviewer upload-manifest issue-body refresh v0.

Use `docs/review/external-review-issue-body-upload-manifest-refresh.md` when checking the live issue #1 body update that points reviewers to uploaded-file intake manifest proof.

Live issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Expected issue-body marker:

```text
uploaded-file intake manifest proof
docs/review/uploaded-file-intake-manifest-runtime-smoke.md
not raw file storage
```

This is an owner-authored issue edit. It is not external reviewer feedback, not raw file storage, not hosted deployment evidence, and not production readiness.

Phase marker: persisted uploaded file intake schema review v0.

Use `docs/review/persisted-uploaded-file-intake-schema-review.md` before adding upload persistence schema.

Current decision:

```text
persist manifest metadata before raw uploaded bytes
```

Candidate table:

```text
uploaded_file_intake_manifests
```

This review is not a migration, not an endpoint, and not raw file storage. The next product gate is `uploaded file intake manifest persistence schema v0`.

Phase marker: uploaded file intake manifest persistence schema v0.

The manifest-only upload intake table is:

```text
uploaded_file_intake_manifests
```

Schema files:

```text
db/init/001_schema.sql
db/migrations/012_uploaded_file_intake_manifests.sql
```

Manifest metadata fields:

```text
content_sha256
filename
source_type
content_type
size_bytes
parser
profile_json
storage_decision
replayable
persistence_boundary
warnings_json
created_at
```

This schema stores manifest metadata only. It is not raw file storage and adds no endpoint. The next product gate is `uploaded file intake manifest persistence repository review v0`.

Phase marker: uploaded file intake manifest persistence repository review v0.

Repository review artifact:

```text
docs/review/uploaded-file-intake-manifest-persistence-repository-review.md
```

Proposed repository surface:

```text
create_manifest(manifest)
list_recent_manifests(limit)
```

This review keeps repository scope to manifest metadata in `uploaded_file_intake_manifests`. It adds no endpoint, no repository code, and no raw uploaded bytes. The next product gate is `uploaded file intake manifest persistence repository v0`.

Phase marker: uploaded file intake manifest persistence repository v0.

Implemented repository surface:

```text
UploadedFileIntakeManifestCreate
create_uploaded_file_intake_manifest(payload)
list_uploaded_file_intake_manifests(limit)
```

This is repository code only. It adds no endpoint, stores no raw uploaded bytes, and is not automatic persistence from upload preview. The next product gate is `uploaded file intake manifest persistence endpoint review v0`.

Phase marker: uploaded file intake manifest persistence endpoint review v0.

Proposed endpoint surface:

```text
POST /documents/upload-intake-manifests
GET /documents/upload-intake-manifests
```

This review routes the future POST through `create_uploaded_file_intake_manifest` and the future GET through `list_uploaded_file_intake_manifests`. It adds no endpoint code, no raw uploaded bytes, and is not document creation. The next product gate is `uploaded file intake manifest persistence endpoint v0`.

Phase marker: uploaded file intake manifest persistence endpoint v0.

Endpoint smoke commands:

```bash
curl -F "source_type=markdown" -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown" http://localhost:8000/documents/upload-intake-manifests
curl http://localhost:8000/documents/upload-intake-manifests
```

Expected boundary:

```text
persistence_boundary = manifest_only_no_raw_file_storage
storage_decision = do_not_persist_raw_upload_yet
replayable = false
```

This endpoint stores no raw uploaded bytes, is not document creation, and is not parser output persistence. The next product gate is `uploaded file intake manifest persistence runtime smoke v0`.

## Metadata Examples

Create a document metadata record:

```bash
curl -X POST http://localhost:8000/documents \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"pdf\",\"source_uri\":\"sample://market-report-001.pdf\",\"title\":\"Sample market report\",\"source_date\":\"2026-05-28\",\"extraction_quality\":\"unknown\",\"status\":\"registered\"}"
```

Create an agent run metadata record:

```bash
curl -X POST http://localhost:8000/agent-runs \
  -H "Content-Type: application/json" \
  -d "{\"user_question\":\"Which sources conflict on demand growth?\"}"
```

Create a failure case metadata record:

```bash
curl -X POST http://localhost:8000/failure-cases \
  -H "Content-Type: application/json" \
  -d "{\"failure_type\":\"unsupported_claim\",\"description\":\"Draft stated demand growth without source evidence.\",\"next_action\":\"Require source id before report generation.\"}"
```

## Verification Without Docker

If Docker is unavailable, run the API compile and smoke tests:

```bash
cd apps/api
uv sync
uv run python -m compileall app ../../packages/ingestion ../../packages/review
uv run pytest -q
```

These tests use an in-memory repository override. They do not prove PostgreSQL runtime connectivity.

## Evaluation And Application Package

Review these Phase 10-14 artifacts before making application claims:

```text
docs/evaluation/eval-plan.md
docs/evaluation/retrieval-eval-report.md
docs/evaluation/failure-cases.md
docs/application/braincrew-role-map.md
docs/application/cover-message.md
docs/application/portfolio-index.md
docs/review/application-ready-review.md
docs/review/direct-evidence-gate-report-cross-link-review.md
```

## Boundary

Do not claim persisted chunks, embeddings, DB persistence for collection plans, direct evidence -> gate -> report cross-links, distributed tracing, hosted observability, or free-form answer generation exists until those stages are implemented and verified with examples. `workflow_runs` can be created, listed, viewed on the dashboard, created by a deterministic execution-preview endpoint, and inspected through `GET /workflow-runs/{id}`. That preview runs retrieval -> evidence -> gate -> report deterministically, Phase 29 attaches those child records to nullable `workflow_run_id` fields while still carrying `workflow_trace_id`, and Phase 30 exposes those child records from the parent workflow detail response. Phase 31 records `stage_input_manifest` on deterministic workflow-created Noise Gate and Report rows so persisted upstream ids are visible, Phase 31.5 keeps direct evidence -> gate -> report foreign-key links and join tables deferred, and Phase 32 exposes `GET /workflow-runs/{id}/lineage` as a derived read model over existing records rather than new lineage storage. The current dashboard is a plain operations view over existing metadata, not a polished product UI. Direct `agent_run_id` child-record linkage exists for persisted Evidence Ledger, Noise Gate, and Report records, but it remains local service provenance rather than distributed tracing.
