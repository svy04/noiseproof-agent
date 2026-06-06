# External Reviewer Shortlist

Status: implemented.

Phase marker: external reviewer shortlist v0.

## Purpose

Give outside reviewers a 90-second shortlist before they open the full proof path.

This file points to a maximum five proof artifacts that cover the current portfolio signal without asking the reviewer to read the whole repository.

It does not replace the full proof path.

## 90-second shortlist

1. `README.md`
   - Scope, non-goals, implementation status, and the current proof boundaries.
2. Uploaded PDF table adapter metadata provenance runtime proof
   - `docs/review/uploaded-pdf-table-adapter-metadata-provenance.md`
   - Product remote verification: `docs/review/uploaded-pdf-table-adapter-metadata-provenance-remote-verification.md`.
   - Runtime proof: `docs/review/uploaded-pdf-table-adapter-metadata-provenance-runtime-smoke.md`.
   - Runtime remote verification: `docs/review/uploaded-pdf-table-adapter-metadata-provenance-runtime-smoke-remote-verification.md`.
   - Route refresh: `docs/review/external-reader-proof-path-uploaded-pdf-table-adapter-metadata-provenance-runtime-route-refresh.md`.
   - Records `POST /documents/upload-chunks`, `POST /documents/{document_id}/retrieval-runs`, `GET /retrieval-runs`, `default_pdf_parser_table_adapter_metadata`, `table_adapter.extracted_table_rows -> [[Segment, Growth], [Enterprise, 12%]]`, `table_extraction_performed remains false`, and `source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only`.
   - Boundary: not new runtime evidence, not robust PDF extraction evidence, not table extraction evidence for arbitrary market PDFs, not Evidence Ledger generation, not external reviewer feedback, not hosted deployment evidence, and not product-complete.
   - Related Upload PDF quality preview coverage summary proof
   - `docs/review/upload-pdf-quality-preview-coverage-summary.md`
   - Runtime proof: `docs/review/upload-pdf-quality-preview-coverage-summary-runtime-smoke.md`.
   - Runtime remote verification: `docs/review/upload-pdf-quality-preview-coverage-summary-runtime-smoke-remote-verification.md`.
   - Route refresh: `docs/review/external-reader-proof-path-upload-pdf-quality-preview-coverage-summary-route-refresh.md`.
   - Predecessor summary proof: `docs/review/upload-pdf-quality-preview-summary.md`.
   - Records `quality_summary.page_coverage_ratio`, `quality_summary.extraction_status`, `partial_page_coverage_ratio=0.5`, `partial_extraction_status=partial_text`, `partial_warning_present=True`, `no_text_extraction_status=no_text`, `encrypted_extraction_status=password_required`, `summary_only_not_robust_pdf_extraction_evidence`, `document_count_delta=0`, and `pdf_encrypted_requires_password`.
   - Upload PDF quality preview summary proof
   - Summary runtime proof: `docs/review/upload-pdf-quality-preview-summary-runtime-smoke.md`.
   - Summary runtime remote verification: `docs/review/upload-pdf-quality-preview-summary-runtime-smoke-remote-verification.md`.
   - Summary route refresh: `docs/review/external-reader-proof-path-upload-pdf-quality-preview-summary-route-refresh.md`.
   - Summary records `quality_summary`, `digital_quality_summary_present=True`, `encrypted_quality_summary_present=True`, `summary_only_not_robust_pdf_extraction_evidence`, `document_count_delta=0`, and `pdf_encrypted_requires_password`.
   - PDF binary fixture parser/adapter smoke: `docs/review/pdf-binary-fixture-parser-adapter-smoke.md`.
   - Binary fixture smoke remote verification: `docs/review/pdf-binary-fixture-parser-adapter-smoke-remote-verification.md`.
   - Binary fixture smoke route refresh: `docs/review/external-reader-proof-path-pdf-binary-fixture-smoke-route-refresh.md`.
   - PDF binary fixture smoke preview runtime: `docs/review/pdf-binary-fixture-smoke-preview-runtime-smoke.md`.
   - Binary fixture smoke preview runtime remote verification: `docs/review/pdf-binary-fixture-smoke-preview-runtime-smoke-remote-verification.md`.
   - Binary fixture smoke preview route refresh: `docs/review/external-reader-proof-path-pdf-binary-fixture-smoke-preview-route-refresh.md`.
   - Records `binary_fixture_smoke_only_not_robust_pdf_extraction`, `fixture_count -> 2`, `passed_count -> 2`, `failed_count -> 0`, `parser -> pdf-pymupdf`, `digital_pdf_text_extraction -> true`, and `table_adapter.extracted_table_rows -> [[Segment, Growth], [Enterprise, 12%]]`.
   - Runtime preview records `GET /documents/pdf-binary-fixture-smoke-preview`, `fixture_source_boundary=repo_synthetic_binary_fixtures_only_no_arbitrary_upload`, `persistence_boundary=preview_only_not_persisted`, `document_count_delta=0`, and `agent_run_count=1`.
   - Boundary: not robust PDF extraction evidence, not OCR, not table extraction, not decryption evidence, not external reviewer feedback, not hosted deployment evidence, and not product-complete.
3. `docs/review/ops-dashboard-anchor-get-runtime-smoke.md`
   - Local Docker PostgreSQL plus live FastAPI HTTP proof that `GET /ops/dashboard` exposes clickable `data-method="GET"` inspection anchors and every unique dashboard href returns GET 200.
   - Docker environment current runtime check: `docs/review/docker-environment-current-runtime-check.md`.
   - Records `Docker version 29.4.3`, `GET /health -> 200`, `GET /ops/summary -> 200`, `noiseproof-agent-api-1`, `noiseproof-agent-db-1`, and `noiseproof-agent-clamav`; boundary: not hosted deployment evidence, not production readiness, not external reviewer feedback, and not product-complete.
   - Related raw-file guard ops proof: `docs/review/uploaded-raw-file-guard-ops-summary-runtime-smoke.md`.
   - Request refresh: `docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md`.
   - Browser proof: `docs/review/ops-dashboard-anchor-browser-smoke.md`.
   - Browser request refresh: `docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md`.
   - Related dashboard proof: `docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md`.
   - Related direct stage links runtime proof: `docs/review/workflow-direct-stage-links-runtime-smoke.md`.
   - Direct stage links request refresh: `docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md`.
   - Related stage event log runtime proof: `docs/review/workflow-stage-event-log-runtime-smoke.md`.
   - Stage event log request refresh: `docs/review/external-reviewer-workflow-stage-event-log-runtime-request-refresh.md`.
   - Related failed stage event runtime proof: `docs/review/workflow-failed-stage-event-runtime-smoke.md`.
   - Failed stage event request refresh: `docs/review/external-reviewer-workflow-failed-stage-event-runtime-request-refresh.md`.
   - Related workflow failure auto-created failure-case runtime proof: `docs/review/workflow-failure-auto-failure-case-creation-runtime-smoke.md`.
   - Workflow failure auto-creation request refresh: `docs/review/external-reviewer-workflow-failure-auto-creation-runtime-request-refresh.md`.
   - Related workflow failure auto-created failure-case dashboard runtime proof: `docs/review/workflow-failure-auto-created-failure-case-dashboard-runtime-smoke.md`.
   - Workflow failure auto-created failure-case dashboard request refresh: `docs/review/external-reviewer-workflow-failure-auto-created-dashboard-runtime-request-refresh.md`; records `dashboard_contains_auto_created_failure_case_id`, `dashboard_contains_workflow_parent_link`, `dashboard_contains_review_queue_linked_count`, and `not external reviewer feedback`.
   - Related uploaded PDF no-text failure candidate runtime proof: `docs/review/uploaded-pdf-no-text-failure-candidate-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-pdf-no-text-failure-candidate-runtime-request-refresh.md`; records `pdf_no_extractable_text`, `chunk_handoff_no_chunks`, and `not robust PDF extraction`.
   - Related persisted document failure candidate draft preview runtime proof: `docs/review/persisted-document-failure-candidate-draft-preview-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-persisted-document-failure-candidate-draft-runtime-request-refresh.md`; records `preview_only_not_persisted`, `failure_case_count_delta -> 0`, and `not automatic failure-case creation`.
   - Related persisted document failure candidate manual handoff runtime proof: `docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-persisted-document-failure-candidate-manual-handoff-runtime-request-refresh.md`; records `failure_case_count_delta -> 1`, human confirmation, and `not a confirm endpoint`.
4. `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md`
   - Owner-runtime proof that the ClamAV endpoint detects an owner-provided malicious test input without committing or logging the payload.
5. `docs/review/retrieval-run-linked-report-runtime-smoke.md`
   - Proof that report generation is linked to retrieval, Evidence Ledger, and Noise Gate records while refusing unsupported pre-report flow.

Then use:

```text
docs/review/external-feedback-intake-criteria.md
```

to decide whether a comment would count as external reviewer feedback.

## Why These Five

These artifacts show:

```text
service operation
reviewer navigation
PDF quality boundary visibility
malware-scanning boundary evidence
retrieval -> ledger -> gate -> report linkage
```

They are intentionally not exhaustive.

The full path remains:

```text
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-link-map.md
docs/application/portfolio-index.md
```

## Boundary

This is reviewer navigation only.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

It does not make any proof stronger than the linked artifacts.

## Latest Table-candidate Downstream Proof Routing

uploaded PDF table-candidate downstream runtime proof:

```text
docs/review/uploaded-pdf-table-candidate-downstream-provenance-runtime-smoke.md
docs/review/uploaded-pdf-table-candidate-downstream-provenance-remote-verification.md
docs/review/external-reviewer-pdf-table-candidate-downstream-runtime-request-refresh.md
retrieval_candidate_table_candidate_count -> 1
```

Boundary: reviewer navigation only; not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction, not table extraction, and not product-complete.
