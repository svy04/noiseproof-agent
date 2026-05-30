# Portfolio Index

Status: Phase 10 application artifact.

This page maps the repository into a reviewer-readable path.

## Start Here

1. `README.md`
2. `docs/product-brief.md`
3. `docs/architecture.md`
4. `docs/runbook.md`
5. `docs/application/braincrew-role-map.md`

## Implementation Artifacts

| Area | Artifact | Status |
|---|---|---|
| API service | `apps/api/app/main.py` | implemented |
| Metadata persistence | `apps/api/app/db.py` and `db/init/001_schema.sql` | implemented |
| Profiler | `packages/ingestion/profiler.py` | implemented |
| Parser boundaries | `packages/ingestion/parsers/*` | implemented |
| Chunking | `packages/ingestion/chunking/experiment.py` | implemented |
| Retrieval | `packages/ingestion/retrieval/lexical.py` | implemented |
| Collection plan | `packages/ingestion/collection/planner.py` | implemented |
| Evidence Ledger preview | `packages/ingestion/evidence/ledger.py` | implemented |
| Evidence Ledger persistence | `POST /evidence-ledgers`, `GET /evidence-ledgers` | implemented v0 |
| Noise Gate preview | `packages/ingestion/noise_gate/gate.py` | implemented |
| Noise Gate persistence | `POST /noise-gates`, `GET /noise-gates` | implemented v0 |
| Report preview | `packages/ingestion/reports/report.py` | implemented |
| Report preview persistence | `POST /reports`, `GET /reports` | implemented v0 |
| Record linkage | `workflow_trace_id` on persisted evidence/gate/report records and agent-run traces | implemented v0 |
| Trace lookup | `GET /traces/{workflow_trace_id}` | implemented v0 |
| Persisted record filters | `workflow_trace_id` / status filters on evidence, gate, and report lists | implemented v0 |
| Dashboard trace/filter links | browser-readable trace lookup and persisted record filter links | implemented v0 |
| Agent-run linkage review | `docs/review/agent-run-linkage-review.md` | reviewed |
| Agent-run lifecycle | parent `agent_runs` row is created before traced operations and updated after completion/failure | implemented v0 |
| Persisted child record agent-run linkage | `agent_run_id` on Evidence Ledger, Noise Gate, and Report records | implemented v0 |
| Dashboard parent/child provenance links | parent run links on persisted Noise Gate and Report dashboard rows | implemented v0 |
| Evidence Ledger dashboard table | persisted Evidence Ledger rows with trace, parent run, and status links | implemented v0 |
| Evidence-to-gate/report cross-links review | `docs/review/evidence-to-gate-report-cross-links-review.md` | reviewed |
| Single workflow parent review | `docs/review/single-workflow-parent-review.md` | reviewed |
| WorkflowRun schema | `workflow_runs` table in `db/init/001_schema.sql` and migration `007_workflow_runs.sql` | implemented v0 |
| WorkflowRun metadata persistence | `POST /workflow-runs`, `GET /workflow-runs` | implemented v0 |
| WorkflowRun dashboard visibility | `GET /ops/dashboard` workflow-run metadata table | implemented v0 |
| WorkflowRun child-link review | `docs/review/workflow-run-child-link-review.md` | reviewed |
| Deterministic workflow execution preview | `POST /workflow-runs/execute-preview` | implemented v0 |
| WorkflowRun child-record links | nullable `workflow_run_id` on retrieval, evidence, gate, and report records | implemented v0 |
| WorkflowRun child inspection | `GET /workflow-runs/{id}` | implemented v0 |
| Direct evidence-to-gate/report cross-link review | `docs/review/direct-evidence-gate-report-cross-link-review.md` | reviewed |
| Workflow stage input manifest | `stage_input_manifest` on workflow-created Noise Gate and Report records | implemented v0 |
| Direct cross-stage link schema review | `docs/review/direct-cross-stage-link-schema-review.md` | reviewed |
| Workflow lineage read model | `GET /workflow-runs/{id}/lineage` | implemented v0 |
| Workflow lineage dashboard links | `GET /ops/dashboard` workflow row detail/lineage links | implemented v0 |
| Workflow lineage missing-reference review | `docs/review/workflow-lineage-missing-reference-review.md` | reviewed |
| Workflow lineage missing-reference test | `apps/api/tests/test_routes.py` broken manifest fixture | implemented v0 |
| Workflow lineage boundary hardening review | `docs/review/workflow-lineage-boundary-hardening-review.md` | reviewed |
| Workflow lineage manifest-shape hardening | `GET /workflow-runs/{id}/lineage` manifest id extraction | implemented v0 |
| Workflow lineage warning taxonomy review | `docs/review/workflow-lineage-warning-taxonomy-review.md` | reviewed |
| Structured warning taxonomy | `GET /workflow-runs/{id}/lineage` `warning_codes` | implemented v0 |
| Workflow lineage warning code documentation review | `docs/review/workflow-lineage-warning-code-documentation-review.md` | reviewed |
| Workflow lineage warning code runbook example | `docs/runbook.md` lineage response shape | implemented v0 |
| Workflow lineage warning code dashboard review | `docs/review/workflow-lineage-warning-code-dashboard-review.md` | reviewed |
| Workflow lineage warning code dashboard surfacing | `GET /ops/dashboard` warning-code legend | implemented v0 |
| Workflow lineage warning code dashboard smoke example | `docs/runbook.md` dashboard legend example | implemented v0 |
| Workflow version naming review | `docs/review/workflow-version-naming-review.md` | reviewed |
| Workflow version naming update | `phase40-lineage-warning-code-dashboard` | implemented v0 |
| Lightweight SQL migration runner | `python -m app.migration_runner` | implemented v0 |
| Migration runner fresh DB verification | `docs/review/migration-runner-fresh-db-verification.md` | verified local |
| Fresh DB API smoke verification | `docs/review/fresh-db-api-smoke-verification.md` | verified local |
| Failure-case persistence smoke verification | `docs/review/failure-case-persistence-smoke-verification.md` | verified local |
| Agent-run failure linkage smoke verification | `docs/review/agent-run-failure-linkage-smoke-verification.md` | verified local |
| Workflow failure linkage smoke verification | `docs/review/workflow-failure-linkage-smoke-verification.md` | verified test fixture |
| Failure-case workflow linkage review | `docs/review/failure-case-workflow-linkage-review.md` | reviewed |
| Operations dashboard | `GET /ops/dashboard` | implemented |
| Auto trace recording | `apps/api/app/services/run_trace.py` | implemented for preview endpoint metadata |

## Verification Artifacts

| Artifact | Purpose |
|---|---|
| `apps/api/tests/test_routes.py` | API and workflow boundary tests |
| `apps/api/tests/test_docs.py` | Phase 10 documentation artifact tests |
| `.github/workflows/ci.yml` | CI smoke and tests |
| `docs/evaluation/eval-plan.md` | evaluation plan |
| `docs/evaluation/retrieval-eval-report.md` | current retrieval boundary report |
| `docs/evaluation/failure-cases.md` | failure case ledger |
| `docs/review/migration-runner-fresh-db-verification.md` | runner apply-path evidence on isolated fresh Docker DB |
| `docs/review/fresh-db-api-smoke-verification.md` | API smoke evidence on isolated fresh migrated Docker DB |
| `docs/review/failure-case-persistence-smoke-verification.md` | failure-ledger persistence evidence on isolated fresh migrated Docker DB |
| `docs/review/agent-run-failure-linkage-smoke-verification.md` | linked failure-case evidence through `agent_run_id` on isolated fresh migrated Docker DB |
| `docs/review/workflow-failure-linkage-smoke-verification.md` | failed workflow parent evidence through route-level test fixture |
| `docs/review/failure-case-workflow-linkage-review.md` | review boundary for deferring `workflow_run_id` on failure cases |

## What Not To Claim

- production RAG quality
- robust PDF extraction
- semantic retrieval
- distributed tracing
- external customer validation
- financial prediction quality
- trading advice
- Product Engineer-level production ownership
- hosted deployment evidence
- automatic failure detection
- complete workflow failure causality

## Current Best Claim

NoiseProof Agent is a small, inspectable data-agent portfolio project that shows how unsupported claims can be persisted, gated, blocked, stored as report-shaped preview records, linked to a deterministic workflow parent, inspected from that parent, and kept bounded before any free-form final answer exists. Workflow-created gate and report records now carry local `stage_input_manifest` values that show persisted upstream ids consumed by deterministic preview stages, `GET /workflow-runs/{id}/lineage` derives a readable lineage view from those existing records, and the operations dashboard links workflow rows to both detail and lineage views. Missing-reference behavior has been reviewed and covered by a targeted broken-manifest fixture, manifest-shape handling now rejects non-list evidence id values with a warning, warning categories have been reviewed, the lineage response now exposes `warning_codes` while preserving human-readable warnings, warning-code documentation has been reviewed, the runbook now shows the lineage response shape, dashboard surfacing has been reviewed before rendering change, and the dashboard now shows a bounded warning-code legend. The migration runner has local fresh-DB apply-path evidence, the API has a local fresh migrated Docker DB smoke check for health, ops summary, and document metadata persistence, failure-case persistence has local smoke evidence, and a manually created failure case can carry `agent_run_id` linkage to a failed agent run. A route-level test fixture also shows a failed deterministic workflow parent can be inspected after a downstream stage exception. Direct evidence -> gate -> report foreign-key and join-table lineage remains intentionally unclaimed, automatic failure detection is not claimed, complete workflow failure causality is not claimed, workflow failure linkage smoke is not fresh Docker DB evidence, and the local Docker smoke checks are not hosted deployment evidence.

Failure cases are not linked to workflow parents yet. The current failure-case workflow linkage review keeps `workflow_run_id` on failure cases deferred until the system has a real failure-case creation path from failed workflow parents.
