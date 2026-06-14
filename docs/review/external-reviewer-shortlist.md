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
   - Current local OTel runtime proof: `docs/review/local-otel-span-export-runtime-smoke.md`.
   - OTel route refresh: `docs/review/external-reader-proof-path-local-otel-span-export-runtime-route-refresh.md`.
   - Records `NOISEPROOF_ENABLE_OTEL_SPAN_EXPORT=true`, `x-noiseproof-otel-span-export: local_in_memory_enabled`, `span_export_enabled=true`, `span_count=4`, and `local_in_memory_otel_span_export_not_distributed_tracing`.
   - Boundary: not distributed tracing, not hosted observability, not external collector integration, not OpenTelemetry Collector deployment, not production monitoring, not external reviewer feedback, not hosted deployment evidence, and not product-complete.
   - Current semantic quality claim gate: `docs/review/semantic-quality-claim-gate.md`.
   - Claim gate remote verification: `docs/review/semantic-quality-claim-gate-remote-verification.md`.
   - Evaluation report: `docs/evaluation/semantic-retrieval-quality-report.md`.
   - Route refresh: `docs/review/external-reader-proof-path-semantic-quality-claim-gate-route-refresh.md`.
   - Records `status: blocked`, `can_claim_semantic_quality: false`, `semantic_quality_claim_blocked`, `claim_gate_only_not_vector_search_quality_evidence`, `toy_fixture_boundary`, `no_embedding_generation`, `missing_embeddings`, and `lexical_rescue_needed`.
   - Boundary: not vector search quality evidence, not embedding generation, not benchmark evidence, not retrieval tuning, not external reviewer feedback, not hosted deployment evidence, and not product-complete.
   - Current semantic retrieval diagnostic matrix: `docs/review/semantic-retrieval-quality-diagnostic-matrix.md`.
   - Remote verification: `docs/review/semantic-retrieval-quality-diagnostic-matrix-remote-verification.md`.
   - Evaluation report: `docs/evaluation/semantic-retrieval-quality-report.md`.
   - Route refresh: `docs/review/external-reader-proof-path-semantic-retrieval-quality-diagnostic-matrix-route-refresh.md`.
   - Records `q-what-missing`, `no_semantic_candidates_at_k`, `no_relevant_semantic_candidate_at_k`, `missing_required_information_roles_at_k`, `relevant_chunk_missing_embedding`, `lexical_retrieved_relevant_not_in_semantic_top_k`, CI run `27079764317`, and External Feedback Screen run `27079764318`.
   - Boundary: not vector search quality evidence, not embedding generation, not a benchmark result, not retrieval tuning, not external reviewer feedback, not hosted deployment evidence, and not product-complete.
2. Uploaded PDF table adapter Noise Gate provenance runtime proof
   - `docs/review/uploaded-pdf-table-adapter-noise-gate-provenance.md`
   - Product remote verification: `docs/review/uploaded-pdf-table-adapter-noise-gate-provenance-remote-verification.md`.
   - Runtime proof: `docs/review/uploaded-pdf-table-adapter-noise-gate-provenance-runtime-smoke.md`.
   - Runtime remote verification: `docs/review/uploaded-pdf-table-adapter-noise-gate-provenance-runtime-smoke-remote-verification.md`.
   - Route refresh: `docs/review/external-reader-proof-path-uploaded-pdf-table-adapter-noise-gate-provenance-runtime-route-refresh.md`.
   - Records `POST /documents/upload-chunks`, `POST /documents/{document_id}/retrieval-runs`, `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, `POST /retrieval-runs/{retrieval_run_id}/noise-gate`, `GET /noise-gates`, `default_pdf_parser_table_adapter_metadata`, `table_adapter.extracted_table_rows -> [['Segment', 'Growth'], ['Enterprise', '12%']]`, `table_extraction_performed -> False`, `source_pdf_table_adapter_provenance_boundary -> noise_gate_stage_input_manifest_from_evidence_ledger_entry_metadata`, `handoff_performs_pdf_table_extraction -> False`, CI run `27077666558`, and External Feedback Screen run `27077666546`.
   - Boundary: not new runtime evidence, not robust PDF extraction evidence, not table extraction evidence for arbitrary market PDFs, not Noise Gate quality evidence, not final truth adjudication, not final report generation, not external reviewer feedback, not hosted deployment evidence, and not product-complete.
   - Related Uploaded PDF table adapter Evidence Ledger provenance runtime proof
   - `docs/review/uploaded-pdf-table-adapter-evidence-ledger-provenance.md`
   - Runtime proof: `docs/review/uploaded-pdf-table-adapter-evidence-ledger-provenance-runtime-smoke.md`.
   - Runtime remote verification: `docs/review/uploaded-pdf-table-adapter-evidence-ledger-provenance-runtime-smoke-remote-verification.md`.
   - Route refresh: `docs/review/external-reader-proof-path-uploaded-pdf-table-adapter-evidence-ledger-provenance-runtime-route-refresh.md`.
   - Records `POST /documents/upload-chunks`, `POST /documents/{document_id}/retrieval-runs`, `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, `GET /evidence-ledgers?retrieval_run_id={retrieval_run_id}`, `default_pdf_parser_table_adapter_metadata`, `table_adapter.extracted_table_rows -> [['Segment', 'Growth'], ['Enterprise', '12%']]`, `table_extraction_performed remains false`, `source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk`, CI run `27076548950`, and External Feedback Screen run `27076548930`.
   - Boundary: not new runtime evidence, not robust PDF extraction evidence, not table extraction evidence for arbitrary market PDFs, not Evidence Ledger quality evidence, not final truth adjudication, not external reviewer feedback, not hosted deployment evidence, and not product-complete.
   - Related Uploaded PDF table adapter metadata provenance runtime proof
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
