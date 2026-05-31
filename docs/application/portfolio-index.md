# Portfolio Index

Status: Phase 10 application artifact.

This page maps the repository into a reviewer-readable path.

Fast path: `docs/review/external-reader-proof-path.md` is the 5-minute path for external readers. It starts with `README.md`, then points to this portfolio index, the failure-case workflow parent proof index, the application-ready review, and the Braincrew role map.

Boundary: this fast path is not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

Public portfolio surface: `docs/review/portfolio-site-proof-artifact-route-verification.md` records that the live portfolio proof artifact points back to this repo without converting that route into NoiseProof hosted deployment evidence.

Demo surface: `docs/review/demo-transcript-capture.md` records a self-authored route walkthrough for collection planning, deterministic workflow preview, lineage, and dashboard inspection. It is not external reviewer feedback or hosted deployment evidence.

Visual local proof surface: `docs/review/local-browser-screenshot-walkthrough.md` records a local browser screenshot of `GET /ops/dashboard` with workflow-run lineage links. It is not external reviewer feedback, not hosted deployment evidence, not customer validation, and not production observability.

External review request surface: `docs/review/external-review-request.md` prepares a structured request for outside critique and points reviewers to `.github/ISSUE_TEMPLATE/external-review-feedback.md`. It is not external reviewer feedback itself.

Proof-marker archive: `docs/review/readme-proof-marker-archive.md` preserves legacy README proof markers after README scanability cleanup. It is source-level provenance, not product runtime evidence, not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

## Start Here

1. `README.md`
2. `docs/review/external-reader-proof-path.md`
3. `docs/product-brief.md`
4. `docs/architecture.md`
5. `docs/runbook.md`
6. `docs/application/braincrew-role-map.md`

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
| Failure-case draft preview | `POST /failure-cases/draft-preview` | implemented v0 |
| Failure-case draft preview smoke verification | `docs/review/failure-case-draft-preview-smoke-verification.md` | verified test fixture |
| Failure-case draft manual handoff smoke verification | `docs/review/failure-case-draft-manual-handoff-smoke-verification.md` | verified test fixture |
| Failure-case draft fresh DB handoff smoke verification | `docs/review/failure-case-draft-fresh-db-handoff-smoke-verification.md` | verified local |
| Workflow failure-to-draft smoke verification | `docs/review/workflow-failure-to-draft-smoke-verification.md` | verified test fixture |
| Failure-case workflow parent linkage fresh DB verification | `docs/review/failure-case-workflow-parent-linkage-fresh-db-verification.md` | verified local |
| Failure-case workflow parent linkage application refresh | `docs/application/portfolio-index.md`, `docs/application/braincrew-role-map.md`, `docs/review/application-ready-review.md` | implemented v0 |
| Failure-case workflow parent linkage dashboard surfacing | `GET /ops/dashboard` Failure Cases table Workflow Parent column | implemented v0 |
| Failure-case workflow parent linkage fresh DB dashboard smoke verification | `docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-verification.md` | verified local |
| Failure-case workflow parent linkage proof index | `docs/review/failure-case-workflow-parent-linkage-proof-index.md` | implemented v0 |
| Failure-case workflow parent linkage stale-claim cleanup | `docs/review/failure-case-workflow-parent-linkage-stale-claim-cleanup.md` | implemented v0 |
| External-reader proof path | `docs/review/external-reader-proof-path.md` | implemented v0 |
| Portfolio site proof artifact route verification | `docs/review/portfolio-site-proof-artifact-route-verification.md` | verified live portfolio route |
| Demo transcript capture | `docs/review/demo-transcript-capture.md` | self-authored route walkthrough |
| Local browser screenshot walkthrough | `docs/review/local-browser-screenshot-walkthrough.md` | self-authored local visual walkthrough |
| External review request packet | `docs/review/external-review-request.md` | request packet only; feedback not yet received |
| README proof-marker archive | `docs/review/readme-proof-marker-archive.md` | source-level provenance only; not product runtime evidence |
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
| `docs/review/failure-case-draft-preview-smoke-verification.md` | route-level smoke for non-persisting failure-case draft preview |
| `docs/review/failure-case-draft-manual-handoff-smoke-verification.md` | route-level smoke for manually handing a draft payload to failure-case persistence |
| `docs/review/failure-case-draft-fresh-db-handoff-smoke-verification.md` | fresh migrated Docker DB proof for manually handing a draft payload to failure-case persistence |
| `docs/review/workflow-failure-to-draft-smoke-verification.md` | route-level smoke for failed workflow parent evidence feeding non-persisting draft preview |
| `docs/review/failure-case-workflow-parent-linkage-fresh-db-verification.md` | fresh migrated Docker DB proof for manual failure-case workflow parent linkage |
| `docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-verification.md` | local fresh migrated Docker DB dashboard evidence for manual failure-case Workflow Parent links; includes `dashboard_contains_workflow_link: true` |
| `docs/review/failure-case-workflow-parent-linkage-proof-index.md` | reviewer reader path for schema boundary -> manual persistence -> fresh DB persistence -> dashboard surfacing -> fresh DB dashboard proof |
| `docs/review/portfolio-site-proof-artifact-route-verification.md` | live portfolio route proof that the public NoiseProof proof surface references the current repo proof path and boundaries |
| `docs/review/demo-transcript-capture.md` | self-authored route transcript for collection planning, deterministic workflow preview, lineage, and dashboard inspection |
| `docs/review/local-browser-screenshot-walkthrough.md` | local browser screenshot walkthrough for the operations dashboard and workflow-run lineage link |
| `docs/review/external-review-request.md` | structured request packet for external critique; not external reviewer feedback |
| `docs/review/failure-case-workflow-parent-linkage-stale-claim-cleanup.md` | current-facing cleanup for stale manual-linkage deferred wording |
| `docs/review/readme-proof-marker-archive.md` | source-level provenance for legacy README proof markers; not product runtime evidence |

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

Short current claim:

NoiseProof Agent is a small, inspectable portfolio service for evidence-first market-intelligence workflows. It shows local service boundaries for profiling, parser/chunk/retrieval previews, persisted evidence/gate/report records, workflow-parent lineage, failure-case persistence, and manual failure-case workflow-parent provenance before any free-form final answer is claimed.

Detailed proof history remains in `docs/review/external-reader-proof-path.md`, `docs/review/failure-case-workflow-parent-linkage-proof-index.md`, `docs/review/application-ready-review.md`, `docs/review/readme-proof-marker-archive.md`, and `docs/GOAL.md`.

Allowed claim: local, inspectable portfolio evidence exists for the current bounded workflow surfaces.

Forbidden claim: this is not hosted deployment evidence, not automatic failure-case creation, not complete workflow failure causality, not production RAG quality, and not a product-complete declaration.
