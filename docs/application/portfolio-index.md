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

External feedback current-state architecture issue verification: `docs/review/external-feedback-current-state-architecture-issue-verification.md` records the current issue #1 screen after the architecture current-state issue-body refresh. It observes `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and `self_authored_comment`; it does not close external reviewer feedback v0.

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

Uploaded PDF text extraction: `docs/review/uploaded-pdf-text-extraction.md` records that `POST /documents/upload-preview` can extract digital PDF text with PyMuPDF from uploaded PDF bytes while keeping `preview_only_not_persisted`; it is not robust PDF extraction, OCR, table extraction, raw file storage, hosted deployment evidence, or external reviewer feedback.

Uploaded PDF downstream handoff: `docs/review/uploaded-pdf-downstream-handoff.md` records that `POST /documents/upload-chunk-preview`, `POST /documents/upload-chunks`, and `POST /documents/upload-retrieval-preview` reuse PyMuPDF digital text extraction for uploaded PDF bytes before chunking or lexical retrieval; it is not robust PDF extraction, OCR, table extraction, raw file storage, hosted deployment evidence, or external reviewer feedback.

Uploaded PDF downstream handoff runtime smoke: `docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP evidence for uploaded digital PDF bytes flowing through upload preview, upload chunk preview, explicit upload-to-chunks persistence, listed chunk lookup, and upload retrieval preview. It is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, or raw file storage.

Uploaded PDF downstream handoff application refresh: `docs/review/uploaded-pdf-downstream-handoff-application-refresh.md` surfaces the uploaded PDF downstream handoff runtime smoke in the reader-facing application docs. It is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, or raw file storage.

External reviewer PDF downstream handoff request refresh: `docs/review/external-reviewer-pdf-downstream-handoff-request-refresh.md` points reviewer-facing request surfaces to the uploaded PDF downstream handoff runtime smoke. It is request infrastructure only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, or raw file storage.

External reviewer PDF downstream handoff issue-body refresh: `docs/review/external-review-issue-body-pdf-downstream-handoff-refresh.md` records the owner-authored issue #1 body update that points reviewers to the uploaded PDF downstream handoff proof. It is not external reviewer feedback itself, not hosted deployment evidence, not robust PDF extraction, OCR, table extraction, or raw file storage.

External feedback current-state PDF downstream handoff issue verification: `docs/review/external-feedback-current-state-pdf-downstream-handoff-issue-verification.md` records the current issue #1 screen after the PDF downstream handoff issue-body refresh. It keeps external reviewer feedback pending because the only comment is self-authored and candidate_count remains 0.

Uploaded PDF retrieval-run provenance: `docs/review/uploaded-pdf-retrieval-run-provenance.md` records route-level proof that PDF-derived upload chunk rows keep `parser: pdf-pymupdf`, `digital_pdf_text_extraction: true`, and `robust_pdf_extraction: false` into persisted document retrieval-run candidate provenance. It is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

Uploaded PDF retrieval-run provenance runtime smoke: `docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP evidence for uploaded digital PDF bytes flowing through upload-to-chunks persistence into persisted document retrieval-run candidate provenance. It is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

Uploaded PDF retrieval-run-linked Evidence Ledger provenance: `docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance.md` records route-level/schema proof that retrieval-run-linked Evidence Ledger entries persist uploaded PDF candidate chunk provenance in `metadata_json`, including `parser: pdf-pymupdf`, `digital_pdf_text_extraction: true`, and `robust_pdf_extraction: false`. It is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Noise Gate behavior, or report generation.

External reviewer PDF retrieval-run provenance request refresh: `docs/review/external-reviewer-pdf-retrieval-run-provenance-request-refresh.md` points reviewer-facing request surfaces to the uploaded PDF retrieval-run provenance runtime proof. It is request infrastructure only, not a live public issue body edit, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

External reviewer PDF retrieval-run provenance issue-body refresh: `docs/review/external-review-issue-body-pdf-retrieval-run-provenance-refresh.md` records the owner-authored issue #1 body update that points reviewers to the uploaded PDF retrieval-run provenance runtime proof. It is not external reviewer feedback itself, not hosted deployment evidence, not robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

External feedback current-state PDF retrieval-run provenance issue verification: `docs/review/external-feedback-current-state-pdf-retrieval-run-provenance-issue-verification.md` records the current issue #1 screen after the PDF retrieval-run provenance issue-body refresh. It keeps external reviewer feedback pending because the only comment is self-authored and candidate_count remains 0.

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

External review issue body retrieval persistence refresh: `docs/review/external-review-issue-body-retrieval-persistence-refresh.md` records the owner-authored issue #1 body update that points reviewers to the uploaded-file retrieval persistence proof. It is not external reviewer feedback, not Evidence Ledger generation, and not hosted deployment evidence.

External feedback current-state retrieval persistence issue verification: `docs/review/external-feedback-current-state-retrieval-persistence-issue-verification.md` records the current issue #1 screen after the retrieval persistence issue-body refresh. It observes `comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and `self_authored_comment`; it does not close external reviewer feedback v0.

Retrieval-run-linked Evidence Ledger endpoint: `docs/review/retrieval-run-linked-evidence-ledger-endpoint.md` records `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, migration `014_evidence_ledger_retrieval_run_id.sql`, and deterministic Evidence Ledger persistence linked to `retrieval_run_id`. It is not semantic retrieval, not embeddings, not LLM judgment, not hosted deployment evidence, and not external reviewer feedback.

Retrieval-run-linked Evidence Ledger runtime smoke: `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md` records local Docker DB migration status (`13 applied / 0 pending`) plus live FastAPI HTTP calls through `GET /health`, document/chunk/retrieval persistence, `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, and `GET /evidence-ledgers`. It is local runtime evidence only, not hosted deployment evidence or external reviewer feedback.

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
| `docs/review/retrieval-run-linked-evidence-ledger-endpoint.md` | persisted retrieval run to Evidence Ledger handoff endpoint; no LLM or embeddings |
| `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md` | local Docker DB plus FastAPI smoke for retrieval-run-linked Evidence Ledger rows |
| `docs/review/retrieval-run-linked-noise-gate-endpoint.md` | persisted retrieval run plus linked Evidence Ledger rows to Noise Gate handoff endpoint; no report generation |
| `docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md` | local Docker DB plus FastAPI smoke for pre-ledger 409 and post-ledger Noise Gate persistence |
| `docs/review/retrieval-run-linked-report-endpoint.md` | persisted retrieval run plus linked Evidence Ledger and Noise Gate rows to Report handoff endpoint; no LLM |
| `docs/review/retrieval-run-linked-report-runtime-smoke.md` | local Docker DB plus FastAPI smoke for pre-gate 409 and post-gate Report persistence |
| `docs/review/external-reviewer-report-handoff-request-refresh.md` | reviewer-facing request-path refresh for retrieval-run-linked Report proof; not external reviewer feedback |
| `docs/review/external-review-issue-body-report-handoff-refresh.md` | owner-authored issue #1 body update for retrieval-run-linked Report proof; not external reviewer feedback |
| `docs/review/external-feedback-current-state-report-handoff-issue-verification.md` | live issue #1 current-state screen after report handoff refresh; feedback gate remains pending |
| `docs/review/application-ready-report-handoff-checklist-refresh.md` | application-ready checklist rows for linked Noise Gate and Report persistence; documentation-only |
| `docs/review/retrieval-run-linked-proof-surface-regression-coverage.md` | regression coverage index that keeps linked Evidence Ledger, Noise Gate, and Report endpoint/smoke docs together |
| `docs/review/semantic-retrieval-readiness-review.md` | source-first review for future semantic retrieval; selects embedding schema review before implementation |
| `docs/review/embedding-schema-review.md` | review-only schema decision for future `chunk_embeddings`; no migration, vector column, embeddings, or semantic retrieval |
| `docs/review/embedding-schema-migration.md` | schema-only `chunk_embeddings` migration and fresh-db schema update; no embedding generation or semantic retrieval |
| `docs/review/embedding-schema-runtime-verification.md` | local Docker PostgreSQL/pgvector verification that migration `015_chunk_embeddings.sql` applies and `embedding` uses vector |
| `docs/review/embedding-repository-review.md` | review-only repository boundary for future `ChunkEmbeddingCreate`, `create_chunk_embedding`, and `list_chunk_embeddings` |
| `docs/review/embedding-repository.md` | metadata/persistence-only repository code for caller-provided chunk embeddings; no endpoint or embedding generation |
| `docs/review/embedding-endpoint-review.md` | review-only chunk-scoped API boundary for future caller-provided chunk embeddings; no endpoint code |
| `docs/review/embedding-endpoint.md` | route-level caller-provided chunk embedding persistence; no embedding generation or semantic retrieval |
| `docs/review/embedding-endpoint-runtime-smoke.md` | local Docker DB plus live FastAPI HTTP proof for caller-provided chunk embedding POST/GET and generated-claim rejection |
| `docs/review/embedding-endpoint-application-refresh.md` | application-facing refresh for caller-provided chunk embedding runtime proof; no generation or semantic retrieval claim |
| `docs/review/semantic-retrieval-implementation-review.md` | review-only decision for caller-provided query-vector semantic retrieval preview; no generation, persistence, or vector index claim |
| `docs/review/semantic-retrieval-preview-endpoint.md` | preview-only semantic retrieval endpoint over existing chunks and embeddings; no retrieval run persistence or generation claim |
| `docs/review/semantic-retrieval-preview-runtime-smoke.md` | local Docker DB plus live FastAPI smoke for semantic retrieval preview; no persistence or quality claim |
| `docs/review/semantic-retrieval-persistence-review.md` | review-only decision to persist semantic candidates through a new `POST /documents/{document_id}/semantic-retrieval-runs` endpoint and the existing `retrieval_runs` table; no endpoint code or Evidence Ledger generation |
| `docs/review/semantic-retrieval-persistence-endpoint.md` | endpoint code for persisting caller-provided-vector semantic candidates into `retrieval_runs`; no runtime smoke, embedding generation, or Evidence Ledger generation |
| `docs/review/semantic-retrieval-persistence-runtime-smoke.md` | local Docker DB plus live FastAPI HTTP proof for persisted semantic retrieval runs; no embedding generation, Evidence Ledger generation, or vector search quality claim |
| `docs/review/semantic-retrieval-persistence-application-refresh.md` | application-facing refresh for caller-provided semantic retrieval persistence runtime proof; no embedding generation or vector search quality evidence |
| `docs/review/semantic-retrieval-quality-review.md` | review-only quality-evaluation plan for semantic retrieval; selects fixture before quality claims |
| `examples/semantic-retrieval-quality/README.md` | tiny labeled fixture for semantic retrieval quality evaluation; 4 queries, 6 chunks, 8 qrels, no embedding generation |
| `packages/ingestion/retrieval/quality_metrics.py` | toy fixture evaluator for Hit@k, Recall@k, MRR@k, nDCG@k, missing embedding rate, disagreement, and role coverage; not vector search quality evidence |
| `docs/evaluation/semantic-retrieval-quality-report.md` | toy fixture metric report with visible misses and semantic/lexical disagreement; not vector search quality evidence |
| `docs/review/semantic-retrieval-quality-report-application-refresh.md` | application-facing refresh for the toy metric report; not vector search quality evidence or a benchmark result |
| `docs/review/semantic-retrieval-quality-report-reviewer-request-refresh.md` | reviewer-facing request-path refresh for the toy metric report; not external reviewer feedback |
| `docs/review/semantic-retrieval-quality-report-issue-body-refresh.md` | owner-authored issue #1 body update for the toy metric report; not external reviewer feedback |
| `docs/review/external-feedback-current-state-semantic-quality-report-issue-verification.md` | current live issue #1 screen after semantic quality report issue-body refresh; feedback gate remains pending |
| `docs/review/semantic-retrieval-quality-report-proof-surface-regression-coverage.md` | regression coverage index for the semantic quality report proof chain; toy metrics only, not vector search quality evidence |
| `docs/review/semantic-retrieval-quality-report-proof-surface-final-scan.md` | application-facing stale quality claim scan for the semantic quality report; no positive quality claim found |
| `docs/review/semantic-retrieval-quality-report-regeneration-command.md` | command path for byte-for-byte regeneration of the toy semantic retrieval quality report from explicit fixture inputs |
| `docs/review/semantic-retrieval-quality-report-regeneration-failure-boundary.md` | structured failure boundary for malformed ranking fixtures in the report regeneration command |
| `docs/review/semantic-retrieval-quality-report-check-mode.md` | check-only staleness detection for committed toy semantic retrieval quality report regeneration |
| `docs/review/semantic-retrieval-quality-report-ci-check.md` | CI staleness protection for committed toy semantic retrieval quality report regeneration |
| `docs/review/semantic-retrieval-quality-report-ci-remote-verification.md` | remote GitHub Actions evidence that the toy report staleness CI step ran successfully |
| `docs/review/semantic-retrieval-quality-report-ci-remote-issue-body-refresh.md` | owner-authored issue #1 refresh pointing reviewers to the semantic quality CI remote verification proof |
| `docs/review/uploaded-raw-file-storage.md` | raw upload quarantine metadata plus PostgreSQL BYTEA storage; no download endpoint, malware scanning, robust PDF extraction, hosted deployment evidence, or external reviewer feedback |
| `docs/review/uploaded-raw-file-storage-runtime-smoke.md` | local Docker PostgreSQL plus live FastAPI HTTP evidence for raw upload quarantine storage; not hosted deployment evidence, external reviewer feedback, malware scanning, or a download endpoint |
| `docs/review/uploaded-raw-file-storage-application-refresh.md` | application-facing refresh for raw upload quarantine runtime proof; not hosted deployment evidence, external reviewer feedback, malware scanning, or a download endpoint |
| `docs/review/external-reviewer-raw-file-storage-request-refresh.md` | reviewer-facing request-path refresh for the uploaded raw file storage proof; not external reviewer feedback, hosted deployment evidence, malware scanning, or a download endpoint |
| `docs/review/external-review-issue-body-raw-file-storage-refresh.md` | owner-authored issue #1 body update pointing reviewers to the uploaded raw file storage proof; not external reviewer feedback, hosted deployment evidence, malware scanning, or a download endpoint |
| `docs/review/external-feedback-current-state-raw-file-storage-issue-verification.md` | current-state screen after raw file storage issue-body refresh; candidate_count 0 and only self-authored comment, so external feedback remains pending |
| `docs/review/uploaded-raw-file-storage-safety-review.md` | source-first safety review for raw upload quarantine; selects scan result schema review before download or malware scanning |
| `docs/review/uploaded-raw-file-scan-result-schema-review.md` | review-only decision for future `raw_file_scan_results` linked to `uploaded_raw_files(id)`; no migration, scanner, or download endpoint |
| `docs/review/uploaded-raw-file-scan-result-schema.md` | schema-only `raw_file_scan_results` table linked to `uploaded_raw_files(id)` for future scan attempts; no scanner, ClamAV, download endpoint, or runtime evidence |
| `docs/review/uploaded-raw-file-scan-result-repository-review.md` | review-only repository boundary for caller-provided raw file scan result rows; no repository code, endpoint, scanner execution, or download endpoint |
| `docs/review/uploaded-raw-file-scan-result-repository.md` | repository-only caller-provided raw file scan result persistence; no endpoint, scanner execution, ClamAV integration, download endpoint, or runtime evidence |
| `docs/review/uploaded-raw-file-scan-result-endpoint-review.md` | review-only selection of parent-scoped metadata-only scan result routes; no endpoint code, scanner execution, ClamAV integration, download endpoint, or runtime evidence |
| `docs/review/uploaded-raw-file-scan-result-endpoint.md` | metadata-only parent-scoped scan result POST/GET endpoints; no scanner execution, ClamAV integration, download endpoint, or runtime evidence |
| `docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md` | local Docker DB plus live FastAPI HTTP proof for metadata-only scan result POST/GET and path/body mismatch 400; not scanner execution, ClamAV integration, download endpoint, or hosted evidence |
| `docs/review/external-reviewer-scan-result-endpoint-request-refresh.md` | reviewer-facing request-path refresh for the uploaded raw file scan result endpoint proof; not external reviewer feedback, hosted deployment evidence, malware scanning, or a download endpoint |
| `docs/review/external-review-issue-body-scan-result-endpoint-refresh.md` | owner-authored issue #1 body update pointing reviewers to the uploaded raw file scan result endpoint proof; not external reviewer feedback, hosted deployment evidence, malware scanning, or a download endpoint |
| `docs/review/external-feedback-current-state-scan-result-endpoint-issue-verification.md` | current-state issue #1 screen after the scan-result endpoint issue-body refresh; candidate_count 0 and only self-authored comment, so external feedback remains pending |
| `docs/review/uploaded-raw-file-scanner-adapter-review.md` | review-only selection of the generic scanner adapter boundary before ClamAV, scanner execution, file signature validation, or download behavior |
| `docs/review/uploaded-raw-file-scanner-adapter.md` | generic scanner adapter types and failure mapping for unavailable scanners/timeouts; no ClamAV integration, scanner process execution, file signature validation, or download behavior |
| `docs/review/uploaded-raw-file-clamav-adapter-review.md` | review-only selection of conservative `ClamAvScannerAdapter` subprocess boundaries before ClamAV execution, daemon sockets, or download behavior |
| `docs/review/uploaded-raw-file-clamav-adapter.md` | conservative `ClamAvScannerAdapter` code with deterministic failure/clean/infected mapping; no ClamAV installation, runtime verification, endpoint, or download behavior |
| `docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md` | deterministic command smoke for `ClamAvScannerAdapter` mappings through fake runners; no real ClamAV execution, signature database verification, endpoint behavior, or malware scanning evidence |
| `docs/review/external-reviewer-clamav-adapter-runtime-smoke-request-refresh.md` | reviewer-facing request-path refresh for the ClamAV adapter runtime smoke proof; not external reviewer feedback, hosted deployment evidence, real ClamAV execution, signature database evidence, or malware scanning |
| `docs/review/external-review-issue-body-clamav-adapter-runtime-smoke-refresh.md` | owner-authored issue #1 body update pointing reviewers to the ClamAV adapter runtime smoke proof; not external reviewer feedback, hosted deployment evidence, real ClamAV execution, signature database evidence, or malware scanning |
| `docs/review/external-feedback-current-state-clamav-adapter-runtime-smoke-issue-verification.md` | current-state issue #1 screen after the ClamAV adapter runtime smoke issue-body refresh; candidate_count 0 and only self-authored comment, so external feedback remains pending |
| `docs/review/uploaded-raw-file-scan-execution-review.md` | source-first review for a future explicit raw upload scan execution endpoint; separates scanner execution from caller-provided scan metadata and adds no endpoint code or malware scanning evidence |
| `docs/review/uploaded-raw-file-scan-execution-endpoint.md` | explicit raw upload scan execution endpoint; default scanner-unavailable maps to scan_error, metadata only, no real ClamAV execution, malware scanning evidence, hosted proof, or download endpoint |
| `docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md` | local Docker PostgreSQL plus live FastAPI HTTP proof for the explicit raw upload scan endpoint with default scanner-unavailable / scan_error; not real ClamAV execution, malware scanning evidence, hosted proof, or external feedback |
| `docs/review/external-reviewer-scan-execution-endpoint-request-refresh.md` | reviewer-facing request-path refresh for the scan execution endpoint runtime proof; not external reviewer feedback, hosted deployment evidence, real ClamAV execution, or malware scanning |
| `docs/review/external-review-issue-body-scan-execution-endpoint-refresh.md` | owner-authored issue #1 body update pointing reviewers to the scan execution endpoint runtime proof; not external reviewer feedback, hosted deployment evidence, real ClamAV execution, or malware scanning |
| `docs/review/external-feedback-current-state-scan-execution-endpoint-issue-verification.md` | current-state issue #1 screen after the scan execution endpoint issue-body refresh; candidate_count 0 and only self-authored comment, so external feedback remains pending |
| `docs/review/uploaded-raw-file-clamav-runtime-verification-review.md` | source-first review selecting a future Dockerized ClamAV + EICAR runtime smoke; review-only, not runtime evidence, malware scanning evidence, or API endpoint verification with real ClamAV |
| `docs/review/uploaded-raw-file-dockerized-clamav-eicar-runtime-smoke.md` | local Dockerized ClamAV EICAR proof; EICAR detected as Eicar-Test-Signature with image digest and signature DB version recorded, not production malware scanning evidence or API endpoint verification |
| `docs/review/clamav-api-integration-boundary-review.md` | review-only decision not to wire Docker CLI execution into the API endpoint; selects ClamAV service boundary review before real endpoint integration |
| `docs/review/clamav-service-boundary-review.md` | review-only decision to design a dedicated ClamAV service boundary before compose/API code; no clamd exposure, endpoint integration, or malware scanning evidence |
| `docs/review/clamav-compose-service-review.md` | review-only decision to design a future internal-only `clamav` Docker Compose service before compose/API code; no compose code, clamd runtime verification, endpoint integration, or malware scanning evidence |
| `docs/review/clamav-compose-service-implementation.md` | optional internal-only `clamav` Docker Compose service behind the `scanner` profile; no host port publishing, clamd runtime verification, endpoint integration, or malware scanning evidence |
| `docs/review/clamav-compose-service-config-verification.md` | config-only proof that `docker compose --profile scanner config` renders optional `clamav` with scanner profile, expose 3310, no clamd host port publishing, and no runtime/malware claim |
| `docs/review/clamav-compose-service-runtime-smoke.md` | local Docker Compose ClamAV service runtime proof: healthy container, `PONG` from clamd, signature DB observed, no host port bindings; no API endpoint integration or malware scanning evidence |
| `docs/review/clamav-compose-eicar-runtime-smoke.md` | local Docker Compose ClamAV EICAR proof: container-internal EICAR detected as `Eicar-Test-Signature`, temporary file deleted, payload absent from repo; no API endpoint integration or production malware scanning evidence |
| `docs/review/clamav-service-scanner-adapter-review.md` | review-only decision to add a future `ClamdScannerAdapter` using clamd `INSTREAM` over the internal Docker network; no adapter code or API endpoint integration |
| `docs/review/clamav-service-scanner-adapter.md` | `ClamdScannerAdapter` code and fake-socket unit coverage for clamd `INSTREAM`; no API endpoint integration, default scanner switch, or real endpoint proof |
| `docs/review/clamav-api-service-network-boundary-review.md` | review-only decision that API-to-clamd integration must run inside the Compose network rather than publishing unauthenticated clamd TCP to the host |
| `docs/review/clamav-api-compose-service-review.md` | review-only decision to add a future profiled `api` Compose service on the same network as `clamav`; scanner opt-in explicit, clamd host ports unpublished |
| `docs/review/clamav-api-compose-service-implementation.md` | `apps/api/Dockerfile` plus profiled `api` Compose service using `db` and future `clamav` service names; scanner default remains unavailable, no endpoint runtime proof |
| `docs/review/clamav-api-compose-service-config-verification.md` | config-only proof that profiled `api` renders with `DATABASE_URL` to `db`, `CLAMD_HOST=clamav`, scanner unavailable default, and no ClamAV host port publishing |
| `docs/review/clamav-api-compose-service-runtime-smoke.md` | local Docker Compose API runtime proof: profiled `api` starts and `GET /health` returns 200 while scanner remains unavailable; not scan endpoint proof |
| `docs/review/clamav-api-endpoint-scanner-opt-in-review.md` | review-only decision to add a future explicit `NOISEPROOF_SCANNER=clamd` path for the raw-file scan endpoint while leaving the default scanner unavailable |
| `docs/review/clamav-api-endpoint-scanner-opt-in-implementation.md` | explicit scanner selection code proof: `NOISEPROOF_SCANNER=clamd` maps to `ClamdScannerAdapter` while default remains unavailable; not endpoint runtime proof |
| `docs/review/clamav-api-endpoint-scanner-opt-in-runtime-smoke.md` | local Docker Compose clean-file endpoint proof: raw upload scan uses `clamav-clamd` and returns `scan_verdict=clean`; not malware detection proof |
| `docs/review/clamav-api-endpoint-malicious-detection-runtime-review.md` | review-only safety gate for future EICAR-through-API proof; clean-file endpoint proof exists, malicious detection remains pending |
| `docs/review/clamav-api-endpoint-malicious-detection-runtime-blocked.md` | blocked malicious-detection runtime attempt; EICAR-through-API proof remains pending and no payload was committed |
| `docs/review/clamav-api-endpoint-malicious-detection-test-harness-review.md` | review-only plan for a future opt-in malicious/test-signature harness using owner-provided runtime-only input; payload remains uncommitted and detection proof remains pending |
| `docs/review/clamav-api-endpoint-malicious-detection-test-harness.md` | disabled-by-default opt-in command harness for future malicious/test-signature endpoint proof; fake-client coverage only, not malware detection proof |
| `docs/review/clamav-api-endpoint-malicious-detection-harness-default-smoke.md` | default no-op command smoke for the malicious/test-signature harness: not_configured, no API calls, no payload committed, no detection claim |
| `docs/review/clamav-api-endpoint-malicious-detection-stdin-input-review.md` | review-only decision to add a stdin-only owner input path before retrying malicious/test-signature endpoint proof; no payload supplied or committed |
| `docs/review/clamav-api-endpoint-malicious-detection-stdin-input-harness.md` | stdin input option for the opt-in malicious/test-signature harness; fake-client coverage only, no payload supplied, no detection proof |
| `docs/review/clamav-api-endpoint-malicious-detection-stdin-default-smoke.md` | safe no-op stdin command smoke: not_configured, no API calls, no payload committed, owner-provided runtime smoke still pending |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-preflight.md` | runtime preflight for future owner-provided malicious/test-signature smoke: API up, clamd reachable, no payload supplied, no scan request made |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-input-guard.md` | fail-fast guard for missing owner input: require-owner-input returns exit 4 without API calls, preventing no-op smoke overclaim |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-packet.md` | no-payload packet for the future owner-provided malicious/test-signature runtime smoke: stdin command template, exact success criteria, no API call |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-validator.md` | metadata-only validator for a future owner-provided runtime smoke report; no payload, no API call, no scan endpoint call, and not production malware scanning evidence |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-validator-leak-field-hardening.md` | validator hardening that rejects payload-bearing JSON fields and reports field paths only; not endpoint runtime proof |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-report-contract.md` | no-payload accepted/rejected metadata contract for the future owner-provided runtime smoke report validator |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-report-schema.md` | JSON Schema-shaped accepted report surface for future owner-provided runtime smoke reports; validator remains authoritative |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-validator-strict-shape-alignment.md` | validator now rejects unknown report fields to match the schema's `additionalProperties: false` boundary |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-cross-shell-packet.md` | no-payload POSIX and PowerShell command templates for future owner-provided runtime smoke; not endpoint runtime proof |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-report-path-guard.md` | validator rejects owner-runtime smoke report paths inside the repo so future reports stay outside repository storage |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-output-path-guard.md` | actual owner-runtime smoke harness rejects repo-internal output paths before API calls |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-validator-handoff-report.md` | actual owner-runtime smoke harness can emit the strict validator-accepted metadata shape outside the repo; not endpoint runtime proof |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-command-template-handoff-alignment.md` | no-payload packet command template now points future owner runtime smokes to the strict validator handoff report path |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-post-run-validation-command.md` | no-payload packet now includes the post-run validator command for owner runtime smoke metadata reports |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-post-run-validation-cross-shell-commands.md` | no-payload packet now includes POSIX and PowerShell post-run validator commands for owner runtime smoke metadata reports |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-post-run-validation-success-criteria.md` | no-payload packet now states validator success criteria for future owner runtime smoke metadata reports |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-empty-marker-guard.md` | quote-only stdin markers now fail as missing owner input instead of reaching the scan endpoint |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-signature-file-input.md` | safer outside-repo signature-file input path for future owner runtime smoke attempts |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-signature-file-read-guard.md` | missing or unreadable signature-file paths now return structured no-payload read-failure reports |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-current-readiness-recheck.md` | current local Docker/API/clamd readiness recheck before owner runtime input; no scan request and no malicious-detection proof |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-input-discovery.md` | no-payload command for discovering whether owner runtime input is configured; no payload inspection and no scan request |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-input-discovery-ci-check.md` | GitHub Actions no-payload missing-input discovery check before the normal API test suite |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-input-discovery-ci-remote-verification.md` | remote GitHub Actions proof that the no-payload missing-input discovery step ran successfully |
| `docs/review/external-review-issue-body-owner-runtime-input-discovery-refresh.md` | owner-authored issue #1 body update pointing reviewers to the owner-runtime input discovery CI remote verification proof; not external reviewer feedback or endpoint malicious-detection runtime proof |
| `docs/review/external-review-issue-body-bom-cleanup.md` | owner-authored issue #1 body cleanup restoring `first_codepoint: 35` after a leading BOM appeared; not external reviewer feedback or endpoint malicious-detection runtime proof |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-input-source-contract-alignment.md` | owner-runtime input discovery/validator contract alignment: discoverable sources include environment, but validator-accepted sources remain file/stdin; not endpoint malicious-detection runtime proof |
| `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-input-source-contract-ci-check.md` | CI guard that checks the no-payload discovery output preserves discoverable vs accepted source separation; not endpoint malicious-detection runtime proof |
| `docs/review/external-review-issue-body-owner-runtime-input-source-contract-refresh.md` | owner-authored issue #1 body update pointing reviewers to the owner-runtime input-source contract CI proof; not external reviewer feedback or endpoint malicious-detection runtime proof |
| `docs/review/external-feedback-current-state-owner-runtime-input-source-contract-issue-verification.md` | current live issue #1 screen after the owner-runtime input-source contract issue-body refresh; candidate_count 0 and only self-authored comment, so external feedback remains pending |
| `docs/review/ci-node24-actions-runtime-opt-in.md` | workflow runtime compatibility opt-in after remote Node.js 20 action deprecation warning; not product runtime evidence |
| `docs/review/ci-node24-actions-runtime-remote-verification.md` | remote CI and External Feedback Screen success after Node.js 24 opt-in; annotation still present as forced-runtime notice |
| `docs/review/architecture-current-state-refresh.md` | current-state architecture refresh separating implemented upload/chunk/retrieval/evidence handoff surfaces from still-unproven robust PDF extraction, embedding generation, hosted deployment, external feedback, and endpoint malicious-detection proof |
| `docs/review/external-reviewer-architecture-current-state-request-refresh.md` | reviewer request surface refresh linking external-review request docs and issue template to the architecture current-state refresh; request infrastructure only, not external feedback |
| `docs/review/external-review-issue-body-architecture-current-state-refresh.md` | owner-authored issue #1 body update pointing reviewers to the architecture current-state refresh; not external reviewer feedback, hosted deployment evidence, or endpoint malicious-detection proof |
| `docs/review/failure-case-workflow-parent-linkage-stale-claim-cleanup.md` | current-facing cleanup for stale manual-linkage deferred wording |
| `docs/review/readme-proof-marker-archive.md` | source-level provenance for legacy README proof markers; not product runtime evidence |

## What Not To Claim

- production RAG quality
- robust PDF extraction
- semantic retrieval quality evidence
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

NoiseProof Agent is a small, inspectable portfolio service for evidence-first market-intelligence workflows. It shows local service boundaries for profiling, parser/chunk/retrieval previews, upload intake manifest runtime smoke with content hash, raw upload quarantine metadata with PostgreSQL BYTEA storage, persisted evidence/gate/report records, retrieval-run-linked Evidence Ledger, Noise Gate, and Report handoffs, workflow-parent lineage, failure-case persistence, and manual failure-case workflow-parent provenance before any free-form final answer is claimed.

Detailed proof history remains in `docs/review/external-reader-proof-path.md`, `docs/review/failure-case-workflow-parent-linkage-proof-index.md`, `docs/review/application-ready-review.md`, `docs/review/external-reviewer-live-proof-route-refresh.md`, `docs/review/readme-proof-marker-archive.md`, and `docs/GOAL.md`.

Allowed claim: local, inspectable portfolio evidence exists for the current bounded workflow surfaces.

Forbidden claim: this is not hosted deployment evidence, not a raw-file download/scanning system, not automatic failure-case creation, not complete workflow failure causality, not production RAG quality, and not a product-complete declaration.
