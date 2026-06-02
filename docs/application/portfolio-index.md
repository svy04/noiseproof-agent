# Portfolio Index

Status: Phase 10 application artifact.

This page maps the repository into a reviewer-readable path.

Fast path: `docs/review/external-reader-proof-path.md` is the 5-minute path for external readers. It starts with `README.md`, then points to this portfolio index, the failure-case workflow parent proof index, the application-ready review, and the Braincrew role map.

Boundary: this fast path is not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

Public portfolio surface: `docs/review/portfolio-site-proof-artifact-route-verification.md` records that the live portfolio proof artifact points back to this repo without converting that route into NoiseProof hosted deployment evidence.

Latest public proof route refresh: `docs/review/external-reviewer-live-proof-route-refresh.md` points reviewers to `https://svy04.github.io/proof-artifacts/noiseproof-live-route-verification-2026-06-01/`. It is not external reviewer feedback and not NoiseProof hosted deployment evidence.

Demo surface: `docs/review/demo-transcript-capture.md` records a self-authored route walkthrough for collection planning, deterministic workflow preview, lineage, and dashboard inspection. It is not external reviewer feedback or hosted deployment evidence.

Visual local proof surface: `docs/review/local-browser-screenshot-walkthrough.md` records a local browser screenshot of `GET /ops/dashboard` with workflow-run lineage links. It is not external reviewer feedback, not hosted deployment evidence, not customer validation, and not production observability.

External review request surface: `docs/review/external-review-request.md` prepares a structured request for outside critique and points reviewers to `.github/ISSUE_TEMPLATE/external-review-feedback.md` and `https://github.com/svy04/noiseproof-agent/issues/1`. It is not external reviewer feedback itself.

External feedback intake surface: `docs/review/external-feedback-intake-criteria.md` defines which public comments can qualify as external reviewer feedback. It is not feedback itself.

External reviewer brief: `docs/review/external-reviewer-brief.md` gives a 2-minute path for reviewers before they comment on issue #1. It is not external reviewer feedback itself.

External reviewer link map: `docs/review/external-reviewer-link-map.md` gives direct GitHub and public route links for reviewers who should not need to navigate the repository tree manually. It is not external reviewer feedback itself.

External review root guide: `CONTRIBUTING.md` is a root-level GitHub entry guide for external reviewers. `docs/review/external-review-root-guide.md` records why it exists. It is not external reviewer feedback itself.

External review issue body encoding verification: `docs/review/external-review-issue-body-encoding-verification.md` records that issue #1 starts directly with `## Request` and first codepoint `35`. It is not external reviewer feedback itself.

External review issue body root-guide verification: `docs/review/external-review-issue-body-root-guide-verification.md` records that issue #1 currently contains a direct root review guide link. It is not external reviewer feedback itself.

External review issue body link-map verification: `docs/review/external-review-issue-body-link-map-verification.md` records that issue #1 currently contains direct reviewer links and has `comment_count: 1` with only owner-authored request/status context. It is not external reviewer feedback itself.

External review issue template link-map refresh: `docs/review/external-review-issue-template-link-map-refresh.md` records that `.github/ISSUE_TEMPLATE/external-review-feedback.md` now contains direct reviewer links. It is not external reviewer feedback itself.

External review issue label verification: `docs/review/external-review-issue-label-verification.md` records that issue #1 is open and labeled `external-review` and `feedback`, while `comment_count` remains `0`. It is not external reviewer feedback itself.

External review owner request comment verification: `docs/review/external-review-owner-request-comment-verification.md` records that a public owner-authored request/status comment was screened as `non_qualifying` with `self_authored_comment`, leaving `candidate_count: 0` and `draft_count: 0`. It is not external reviewer feedback itself.

External reviewer outreach packet: `docs/review/external-reviewer-outreach-packet.md` gives copy-paste messages for asking FDE/product engineer, RAG/data engineer, and founder/operator reviewers to inspect issue #1. It is not external reviewer feedback itself.

External reviewer upload-manifest request refresh: `docs/review/external-reviewer-upload-manifest-request-refresh.md` points the reviewer request path to the uploaded-file intake manifest proof. It is not external reviewer feedback itself, not raw file storage, and not hosted deployment evidence.

External review issue body upload-manifest refresh: `docs/review/external-review-issue-body-upload-manifest-refresh.md` records the owner-authored issue #1 body update that points reviewers to the uploaded-file intake manifest proof. It is not external reviewer feedback itself, not raw file storage, and not hosted deployment evidence.

External reviewer upload-manifest persistence request refresh: `docs/review/external-reviewer-upload-manifest-persistence-request-refresh.md` points the reviewer request path to the uploaded-file intake manifest persistence proof. It is not external reviewer feedback itself, not raw file storage, and not hosted deployment evidence.

External review issue body upload-manifest persistence refresh: `docs/review/external-review-issue-body-upload-manifest-persistence-refresh.md` records the owner-authored issue #1 body update that points reviewers to the uploaded-file intake manifest persistence proof. It is not external reviewer feedback itself, not raw file storage, and not hosted deployment evidence.

Persisted uploaded file intake schema review: `docs/review/persisted-uploaded-file-intake-schema-review.md` selects manifest metadata before raw uploaded bytes. It is review-only and adds no migration or endpoint.

Uploaded file intake manifest persistence schema: `uploaded_file_intake_manifests` now exists in `db/init/001_schema.sql` and `db/migrations/012_uploaded_file_intake_manifests.sql`. It stores manifest metadata only, not raw uploaded bytes.

Uploaded file intake manifest persistence repository review: `docs/review/uploaded-file-intake-manifest-persistence-repository-review.md` defines the small repository boundary before code: `create_manifest` and `list_recent_manifests`, metadata only, no raw uploaded bytes, no endpoint.

Uploaded file intake manifest persistence repository: `docs/review/uploaded-file-intake-manifest-persistence-repository.md` records the first repository code for `UploadedFileIntakeManifestCreate`, `create_uploaded_file_intake_manifest`, and `list_uploaded_file_intake_manifests`. It is not automatic persistence from upload preview and adds no endpoint.

Uploaded file intake manifest persistence endpoint review: `docs/review/uploaded-file-intake-manifest-persistence-endpoint-review.md` defines `POST /documents/upload-intake-manifests` and `GET /documents/upload-intake-manifests` as the future API boundary, with no raw uploaded bytes and no document creation.

Uploaded file intake manifest persistence endpoint: `docs/review/uploaded-file-intake-manifest-persistence-endpoint.md` records the POST/GET API for manifest metadata only. It stores no raw uploaded bytes, is not document creation, and is not parser output persistence.

Uploaded file intake manifest persistence runtime smoke: `docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md` records local Docker DB plus FastAPI POST/GET evidence for persisting manifest metadata. It is local runtime evidence only, not hosted deployment or external reviewer feedback.

Uploaded file intake manifest persistence application refresh: `docs/review/uploaded-file-intake-manifest-persistence-application-refresh.md` surfaces the persistence runtime smoke in the portfolio, Braincrew role map, application-ready review, README, and runbook. It is not hosted deployment evidence, not external reviewer feedback, not Braincrew acceptance, and not raw file storage.

Uploaded file parsed document persistence: `docs/review/uploaded-file-parsed-document-persistence.md` records `POST /documents/upload-parsed-documents`, which persists uploaded-file document metadata and parser/profile output with `document_metadata_and_profile_only_no_raw_file_storage`. It stores no raw uploaded bytes and no parsed text, and it is not robust PDF extraction.

Uploaded file parsed document persistence runtime smoke: `docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP evidence for `POST /documents/upload-parsed-documents` and `GET /documents`. It is local runtime evidence only, not hosted deployment or external reviewer feedback.

Uploaded file parsed document persistence application refresh: `docs/review/uploaded-file-parsed-document-persistence-application-refresh.md` surfaces the parsed document persistence runtime smoke in the portfolio, Braincrew role map, application-ready review, README, and runbook. It is not hosted deployment evidence, not external reviewer feedback, not Braincrew acceptance, not robust PDF extraction, and not raw file storage.

External reviewer parsed-document persistence request refresh: `docs/review/external-reviewer-parsed-document-persistence-request-refresh.md` points the reviewer request path to the uploaded-file parsed document persistence proof. It is not external reviewer feedback itself, not raw file storage, and not hosted deployment evidence.

External review issue body parsed document persistence refresh: `docs/review/external-review-issue-body-parsed-document-persistence-refresh.md` records the owner-authored issue #1 body update that points reviewers to the uploaded-file parsed document persistence proof. It is not external reviewer feedback itself, not raw file storage, and not hosted deployment evidence.

Uploaded file chunk persistence review: `docs/review/uploaded-file-chunk-persistence-review.md` selects `document_chunks` as the next schema boundary while keeping raw file storage, full parsed text persistence, embeddings, and retrieval persistence out of scope.

Uploaded file chunk persistence schema: `docs/review/uploaded-file-chunk-persistence-schema.md` records `document_chunks` in `db/init/001_schema.sql` and `db/migrations/013_document_chunks.sql`. It is schema-only and adds no endpoint, repository code, chunk rows, embeddings, or retrieval persistence.

Uploaded file chunk persistence repository review: `docs/review/uploaded-file-chunk-persistence-repository-review.md` selects `DocumentChunkCreate`, `create_document_chunk`, and `list_document_chunks` as the next repository boundary without adding code, endpoints, embeddings, or chunk rows.

Uploaded file chunk persistence repository: `docs/review/uploaded-file-chunk-persistence-repository.md` records `DocumentChunkCreate`, `create_document_chunk`, and `list_document_chunks` code over `document_chunks`. It adds no endpoint, upload-preview automation, embeddings, or retrieval persistence.

Uploaded file chunk persistence endpoint review: `docs/review/uploaded-file-chunk-persistence-endpoint-review.md` selects `POST /documents/{document_id}/chunks` and `GET /documents/{document_id}/chunks` as the next explicit document-scoped endpoint boundary. It adds no endpoint code, upload-preview automation, embeddings, or retrieval persistence.

Uploaded file chunk persistence endpoint: `docs/review/uploaded-file-chunk-persistence-endpoint.md` records `POST /documents/{document_id}/chunks` and `GET /documents/{document_id}/chunks` over `DocumentChunkRequest`/`DocumentChunkOut`. It adds no upload-preview automation, embeddings, or retrieval persistence.

Uploaded file chunk persistence runtime smoke: `docs/review/uploaded-file-chunk-persistence-runtime-smoke.md` records local Docker DB plus API smoke evidence for `POST /documents/{document_id}/chunks` and `GET /documents/{document_id}/chunks`. It confirms upload chunk preview stayed `preview_only_not_persisted` and adds no embeddings or retrieval persistence.

Uploaded file chunk persistence application refresh: `docs/review/uploaded-file-chunk-persistence-application-refresh.md` surfaces the chunk persistence runtime smoke in the portfolio, Braincrew role map, application-ready review, README, and runbook. It is not hosted deployment evidence, not external reviewer feedback, not Braincrew acceptance, not automatic upload-preview-to-chunk persistence, and not retrieval persistence.

External reviewer chunk persistence request refresh: `docs/review/external-reviewer-chunk-persistence-request-refresh.md` points the reviewer request path to the uploaded-file chunk persistence proof. It is not external reviewer feedback itself, not automatic upload-preview-to-chunk persistence, and not hosted deployment evidence.

External review issue body chunk persistence refresh: `docs/review/external-review-issue-body-chunk-persistence-refresh.md` records the owner-authored issue #1 body update that points reviewers to the uploaded-file chunk persistence proof. It is not external reviewer feedback itself, not automatic upload-preview-to-chunk persistence, and not hosted deployment evidence.

External feedback current-state chunk issue verification: `docs/review/external-feedback-current-state-chunk-issue-verification.md` records the current issue #1 screen after the chunk persistence issue-body refresh. It observes `comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and `self_authored_comment`; it does not close external reviewer feedback v0.

Uploaded file chunk persistence handoff review: `docs/review/uploaded-file-chunk-persistence-handoff-review.md` selects an explicit future `POST /documents/upload-chunks` endpoint as the next product gate. It is review-only, keeps the existing upload chunk preview preview-only, uses existing documents and document_chunks tables, and adds no endpoint, schema, raw uploaded byte storage, embeddings, or retrieval persistence.

Uploaded file chunk persistence handoff endpoint: `docs/review/uploaded-file-chunk-persistence-handoff-endpoint.md` records `POST /documents/upload-chunks` route-level behavior. It creates a document row and document_chunks rows through an explicit handoff endpoint while keeping upload chunk preview preview-only, storing no raw uploaded bytes, storing no full parsed text, and adding no embeddings or retrieval persistence.

Uploaded file chunk persistence handoff runtime smoke: `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP evidence for `POST /documents/upload-chunks`. It observed a document row and four chunk rows for the created document while keeping `explicit_upload_to_chunks_no_raw_file_storage` and `chunk_text_only_no_raw_file_storage` boundaries.

Uploaded file chunk persistence handoff application refresh: `docs/review/uploaded-file-chunk-persistence-handoff-application-refresh.md` surfaces the handoff runtime smoke in the portfolio, Braincrew role map, application-ready review, README, and runbook. It is not hosted deployment evidence, not external reviewer feedback, not Braincrew acceptance, not raw uploaded byte storage, and not retrieval persistence.

Uploaded file retrieval persistence review: `docs/review/uploaded-file-retrieval-persistence-review.md` selects a future `POST /documents/{document_id}/retrieval-runs` endpoint over existing `document_chunks` and `retrieval_runs`. It is review-only and adds no schema, endpoint code, embeddings, semantic retrieval, Evidence Ledger generation, or financial advice behavior.

Uploaded file retrieval persistence endpoint: `docs/review/uploaded-file-retrieval-persistence-endpoint.md` records `POST /documents/{document_id}/retrieval-runs` route-level behavior. It reads existing `document_chunks`, persists one row in the existing `retrieval_runs` table, and stores `metadata_json.candidate_chunk_ids` while staying lexical only with no embeddings, semantic retrieval, Evidence Ledger generation, or financial advice behavior.

Uploaded file retrieval persistence runtime smoke: `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP evidence for `POST /documents/{document_id}/retrieval-runs`. It observed `retrieval_result_count -> 2`, `metadata_source_table -> document_chunks`, and matching `candidate_chunk_ids` in `GET /retrieval-runs`; it is not hosted deployment evidence or external reviewer feedback.

Uploaded file retrieval persistence application refresh: `docs/review/uploaded-file-retrieval-persistence-application-refresh.md` surfaces the retrieval runtime smoke in the portfolio, Braincrew role map, application-ready review, README, and runbook. It is not hosted deployment evidence, not external reviewer feedback, not Braincrew acceptance, not Evidence Ledger generation, and not semantic retrieval.

External reviewer retrieval persistence request refresh: `docs/review/external-reviewer-retrieval-persistence-request-refresh.md` points reviewer-facing request surfaces to the uploaded-file retrieval persistence proof. It is request infrastructure only and does not close external reviewer feedback.

External reviewer chunk handoff request refresh: `docs/review/external-reviewer-chunk-handoff-request-refresh.md` points reviewer-facing request surfaces to the uploaded-file chunk handoff proof. It is request infrastructure only and does not close external reviewer feedback.

External reviewer chunk handoff issue-body refresh: `docs/review/external-review-issue-body-chunk-handoff-refresh.md` records the owner-authored issue #1 body update that points reviewers to the uploaded-file chunk handoff proof. It is not external reviewer feedback.

External feedback current-state chunk handoff issue verification: `docs/review/external-feedback-current-state-chunk-handoff-issue-verification.md` records the current issue #1 screen after the chunk handoff issue-body refresh. It observes `comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and `self_authored_comment`; it does not close external reviewer feedback v0.

External feedback qualification preview: `docs/review/external-feedback-qualification-preview.md` documents the local screening helper in `packages/review/external_feedback.py`. It can identify possible candidates for manual review, but it is not external reviewer feedback itself.

External feedback screening CLI: `docs/review/external-feedback-screening-cli.md` documents `python -m packages.review.external_feedback_cli` for real `gh issue view --json comments` payloads. It is not external reviewer feedback itself.

External feedback screening workflow: `docs/review/external-feedback-screening-workflow.md` documents `.github/workflows/external-feedback-screen.yml`, which runs the CLI from GitHub Actions and uploads `external-feedback-screen.json`. It is not external reviewer feedback itself.

External feedback screening workflow verification: `docs/review/external-feedback-screening-workflow-verification.md` records remote run `26724730074` and the downloaded `external-feedback-screen.json` artifact. It is not external reviewer feedback itself.

README next-gate stale-claim refresh: `docs/review/readme-next-gate-stale-claim-refresh.md` updates the README next-step section so it points to `external reviewer feedback v0` instead of an older workflow-lineage gate. It is not external reviewer feedback itself.

External feedback acceptance template: `docs/review/external-feedback-acceptance-template.md` defines how to record a future qualifying public review comment after manual acceptance. It is not external reviewer feedback itself.

External feedback acceptance draft CLI: `docs/review/external-feedback-acceptance-draft-cli.md` documents `python -m packages.review.external_feedback_acceptance_cli`, which turns candidate screening artifacts into draft manual acceptance records. It is not external reviewer feedback itself.

External feedback acceptance draft workflow: `.github/workflows/external-feedback-screen.yml` now uploads `external-feedback-acceptance-draft.json` next to the screening artifact. The external feedback acceptance draft workflow is not external reviewer feedback itself.

External feedback acceptance draft workflow verification: `docs/review/external-feedback-acceptance-draft-workflow-verification.md` records remote run `26727047243` and the downloaded screening plus acceptance-draft artifacts. It is not external reviewer feedback itself.

Owner-approved product continuation decision: `docs/review/owner-approved-product-continuation-decision.md` records owner approval to resume product implementation while `external reviewer feedback v0` remains pending. It is not external reviewer feedback, not customer validation, and not Braincrew acceptance.

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
| External feedback intake criteria | `docs/review/external-feedback-intake-criteria.md` | qualification criteria only; feedback still pending |
| External reviewer brief | `docs/review/external-reviewer-brief.md` | 2-minute reviewer path only; feedback still pending |
| External reviewer live proof route refresh | `docs/review/external-reviewer-live-proof-route-refresh.md` | latest public portfolio proof route; feedback still pending |
| External reviewer outreach packet | `docs/review/external-reviewer-outreach-packet.md` | copy-paste outreach messages only; feedback still pending |
| External feedback qualification preview | `docs/review/external-feedback-qualification-preview.md` | local comment screen only; feedback still pending |
| External feedback screening CLI | `docs/review/external-feedback-screening-cli.md` | CLI over real issue-comment JSON; feedback still pending |
| External feedback screening workflow | `docs/review/external-feedback-screening-workflow.md` | Actions wrapper over screening CLI; feedback still pending |
| External feedback screening workflow verification | `docs/review/external-feedback-screening-workflow-verification.md` | remote pending artifact verification; feedback still pending |
| Owner-approved product continuation decision | `docs/review/owner-approved-product-continuation-decision.md` | owner-approved continuation; external reviewer feedback still pending |
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
| `docs/review/external-feedback-intake-criteria.md` | qualification criteria for accepting future external reviewer feedback |
| `docs/review/external-reviewer-brief.md` | 2-minute path for reviewers before leaving feedback |
| `docs/review/external-reviewer-live-proof-route-refresh.md` | latest public proof route for reviewer orientation; not external reviewer feedback |
| `docs/review/external-reviewer-link-map.md` | direct reviewer links for issue #1, README, proof path, portfolio index, and feedback criteria; not external reviewer feedback |
| `CONTRIBUTING.md` / `docs/review/external-review-root-guide.md` | root-level GitHub review guide; not external reviewer feedback |
| `docs/review/external-review-issue-body-encoding-verification.md` | live issue #1 body starts with request heading and first codepoint 35; not external reviewer feedback |
| `docs/review/external-review-issue-body-root-guide-verification.md` | live issue #1 body verification for direct root review guide link; comment count is 1 with owner-authored request/status context |
| `docs/review/external-review-issue-body-link-map-verification.md` | live issue #1 body verification for direct reviewer links; comment count is 1 with owner-authored request/status context |
| `docs/review/external-review-issue-template-link-map-refresh.md` | issue template direct-link refresh for future external review issues; not external reviewer feedback |
| `docs/review/external-review-issue-label-verification.md` | live issue #1 label verification for `external-review` and `feedback`; comment count remains 0 |
| `docs/review/external-review-owner-request-comment-verification.md` | live owner-authored issue comment rejection proof; `self_authored_comment`, candidate count 0, draft count 0 |
| `docs/review/external-reviewer-outreach-packet.md` | copy-paste outreach packet for actual human reviewers; not external reviewer feedback |
| `docs/review/external-feedback-qualification-preview.md` | local screening helper for public issue comments; not external reviewer feedback |
| `docs/review/external-feedback-screening-cli.md` | command-line path for screening real issue-comment JSON; not external reviewer feedback |
| `docs/review/external-feedback-screening-workflow.md` | GitHub Actions wrapper over the screening CLI; not external reviewer feedback |
| `docs/review/external-feedback-screening-workflow-verification.md` | downloaded remote screening artifact; pending and not external reviewer feedback |
| `docs/review/readme-next-gate-stale-claim-refresh.md` | README next-step now points to external reviewer feedback v0; not external reviewer feedback |
| `docs/review/external-feedback-acceptance-template.md` | template for recording future accepted public review comments; not external reviewer feedback |
| `docs/review/external-feedback-acceptance-draft-cli.md` | CLI for converting candidate screen artifacts into manual acceptance drafts; not external reviewer feedback |
| `docs/review/external-feedback-acceptance-draft-workflow-verification.md` | downloaded remote acceptance-draft artifact; pending and not external reviewer feedback |
| `docs/review/owner-approved-product-continuation-decision.md` | owner-approved continuation decision; external reviewer feedback remains pending |
| `docs/review/file-upload-preview.md` | preview-only upload boundary for parser/profile inspection; not retrieval |
| `docs/review/uploaded-file-chunk-preview.md` | preview-only upload-to-chunk boundary; not retrieval |
| `docs/review/uploaded-file-retrieval-preview.md` | preview-only upload-to-retrieval boundary; lexical retrieval only |
| `docs/review/uploaded-file-evidence-preview.md` | preview-only uploaded file Evidence Ledger preview; not Noise Gate or final report |
| `docs/review/uploaded-file-noise-gate-preview.md` | preview-only uploaded file Noise Gate preview; not final report |
| `docs/review/uploaded-file-report-preview.md` | preview-only uploaded file report preview; not LLM output or persisted report |
| `docs/review/uploaded-file-failure-case-draft-preview.md` | preview-only uploaded file failure-case draft; human confirmation still required |
| `docs/review/uploaded-file-failure-case-manual-handoff-smoke.md` | upload failure-case draft manually persisted through existing failure-case endpoint; not automatic creation |
| `docs/review/uploaded-file-proof-path-index.md` | compact uploaded-file proof path from upload preview through manual failure-case handoff |
| `docs/review/uploaded-file-runtime-smoke-packet.md` | local Docker DB plus FastAPI HTTP smoke over uploaded-file proof path through manual failure-case handoff; not hosted deployment evidence |
| `docs/review/persisted-uploaded-file-intake-review.md` | review-only decision to keep uploads preview-only before adding persisted file intake storage or schema |
| `docs/review/uploaded-file-intake-manifest-preview.md` | preview-only upload intake manifest endpoint with content hash and explicit no-raw-storage decision |
| `docs/review/uploaded-file-intake-manifest-runtime-smoke.md` | local FastAPI HTTP smoke for the intake manifest endpoint; not hosted deployment evidence or raw file storage |
| `docs/review/uploaded-file-intake-manifest-application-refresh.md` | application-facing refresh for upload intake manifest runtime smoke; not hosted deployment evidence or raw file storage |
| `docs/review/external-reviewer-upload-manifest-request-refresh.md` | request-path refresh that points external reviewers to uploaded-file intake manifest proof; not external reviewer feedback |
| `docs/review/external-review-issue-body-upload-manifest-refresh.md` | owner-authored issue #1 body update pointing to uploaded-file intake manifest proof; not external reviewer feedback |
| `docs/review/external-reviewer-upload-manifest-persistence-request-refresh.md` | request-path refresh that points external reviewers to uploaded-file intake manifest persistence proof; not external reviewer feedback |
| `docs/review/external-review-issue-body-upload-manifest-persistence-refresh.md` | owner-authored issue #1 body update pointing to uploaded-file intake manifest persistence proof; not external reviewer feedback |
| `docs/review/persisted-uploaded-file-intake-schema-review.md` | review-only decision to persist manifest metadata before raw uploaded bytes |
| `docs/review/uploaded-file-intake-manifest-persistence-schema.md` | schema-only manifest metadata table; no raw uploaded bytes |
| `docs/review/uploaded-file-intake-manifest-persistence-repository-review.md` | review-only repository boundary for manifest metadata persistence; no endpoint |
| `docs/review/uploaded-file-intake-manifest-persistence-repository.md` | repository code for manifest metadata create/list; no endpoint |
| `docs/review/uploaded-file-intake-manifest-persistence-endpoint-review.md` | review-only API boundary for manifest metadata persistence; no endpoint code |
| `docs/review/uploaded-file-intake-manifest-persistence-endpoint.md` | POST/GET manifest metadata persistence endpoint; no raw uploaded bytes |
| `docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md` | local Docker DB plus FastAPI POST/GET manifest persistence smoke; not hosted evidence |
| `docs/review/uploaded-file-intake-manifest-persistence-application-refresh.md` | application-facing refresh for manifest persistence runtime smoke; not hosted evidence |
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

NoiseProof Agent is a small, inspectable portfolio service for evidence-first market-intelligence workflows. It shows local service boundaries for profiling, parser/chunk/retrieval previews, upload intake manifest runtime smoke with content hash and no-raw-storage decision, persisted evidence/gate/report records, workflow-parent lineage, failure-case persistence, and manual failure-case workflow-parent provenance before any free-form final answer is claimed.

Detailed proof history remains in `docs/review/external-reader-proof-path.md`, `docs/review/failure-case-workflow-parent-linkage-proof-index.md`, `docs/review/application-ready-review.md`, `docs/review/external-reviewer-live-proof-route-refresh.md`, `docs/review/readme-proof-marker-archive.md`, and `docs/GOAL.md`.

Allowed claim: local, inspectable portfolio evidence exists for the current bounded workflow surfaces.

Forbidden claim: this is not hosted deployment evidence, not raw file storage, not automatic failure-case creation, not complete workflow failure causality, not production RAG quality, and not a product-complete declaration.
