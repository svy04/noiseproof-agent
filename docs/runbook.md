# Runbook: NoiseProof Agent

## Current Status

Phase 572 adds persisted report markdown export v0: `GET /reports/{report_record_id}/markdown` renders an existing persisted `report_records` row as deterministic `text/markdown`, including claim, source ids, evidence spans, confidence, limitations, contradictions, next data needed, stage input manifest, warnings, and an explicit no-new-claims boundary. Unknown ids return `404` with `Report record not found`. This is a read/export surface only; it does not generate new claims, call an LLM, run retrieval, create Evidence Ledger rows, create new Report records, provide financial advice, or implement free-form reports. See `docs/review/persisted-report-markdown-export.md`.

Phase 573 adds persisted report markdown export remote verification v0: `docs/review/persisted-report-markdown-export-remote-verification.md` records remote GitHub Actions success for head `b477ec855ed922119391d81ea0cac9f9213c38f3`, with CI run `27022884406` (`api-smoke -> success`) and External Feedback Screen run `27022884394` (`screen -> success`). This is remote workflow evidence only, not external reviewer feedback, hosted deployment evidence, free-form report generation, financial advice, or product-complete.

Phase 574 adds external reviewer persisted report markdown export request refresh v0: `docs/review/external-reviewer-persisted-report-markdown-export-request-refresh.md` points reviewer-facing request surfaces to `docs/review/persisted-report-markdown-export.md`, `GET /reports/{report_record_id}/markdown`, and the remote verification record. This is request infrastructure only, not a live issue body edit, external reviewer feedback, hosted deployment evidence, free-form report generation, or product-complete.

Phase 575 adds external review issue body persisted report markdown export refresh v0: `docs/review/external-review-issue-body-persisted-report-markdown-export-refresh.md` records the owner-authored issue #1 body routing update for the persisted Report markdown export proof. This is an owner-authored issue edit only, not external reviewer feedback, hosted deployment evidence, customer validation, Braincrew acceptance, free-form report generation, or product-complete.

Phase 576 adds external feedback current-state persisted Report markdown export issue verification v0: `docs/review/external-feedback-current-state-persisted-report-markdown-export-issue-verification.md` records that the current issue body still exposes `docs/review/persisted-report-markdown-export.md`, `GET /reports/{report_record_id}/markdown`, the request refresh, and the issue-body refresh record, while screening found `candidate_count=0`, `draft_count=0`, and only a `self_authored_comment`. This keeps external reviewer feedback v0 pending.

Phase 577 adds external feedback current-state persisted Report markdown export issue verification remote verification v0: `docs/review/external-feedback-current-state-persisted-report-markdown-export-issue-verification-remote-verification.md` records remote workflow success on head `57b6bd9eadce2b9b21d6ec2a3471210f5ad46403`: CI run `27024339169` (`api-smoke -> success`) and External Feedback Screen run `27024339136` (`screen -> success`). This is remote workflow evidence only, not external reviewer feedback, hosted deployment evidence, customer validation, Braincrew acceptance, free-form report generation, or product-complete.

Phase 578 adds external review issue body BOM removal refresh v0: `docs/review/external-review-issue-body-bom-removal-refresh.md` records the owner-authored issue #1 body repair that changed the first codepoint from `65279` to `35` using a `utf8_no_bom_body_file`, while preserving the persisted Report markdown export proof and `GET /reports/{report_record_id}/markdown` routing. This is request-surface hygiene only, not external reviewer feedback, hosted deployment evidence, customer validation, Braincrew acceptance, or product-complete.

Phase 579 adds external feedback current-state issue body BOM removal issue verification v0: `docs/review/external-feedback-current-state-issue-body-bom-removal-issue-verification.md` records that issue #1 now starts with codepoint `35`, has no leading BOM, still exposes the persisted Report markdown export proof and `GET /reports/{report_record_id}/markdown`, and still has only a self-authored non-qualifying comment with `candidate_count=0` and `draft_count=0`.

Phase 580 adds external feedback current-state issue body BOM removal issue verification remote verification v0: `docs/review/external-feedback-current-state-issue-body-bom-removal-issue-verification-remote-verification.md` records remote workflow success on head `db316bf07baa4d6058e4249e24ad4d8349d1459b`: CI run `27025500388` (`api-smoke -> success`) and External Feedback Screen run `27025500574` (`screen -> success`). This is remote workflow evidence only, not external reviewer feedback, hosted deployment evidence, customer validation, Braincrew acceptance, free-form report generation, or product-complete.

Phase 336 adds architecture current-state refresh v0: `docs/architecture.md` now separates implemented uploaded-file persistence, chunk/retrieval persistence, caller-provided embeddings, semantic retrieval persistence, and retrieval-run-linked Evidence Ledger / Noise Gate / Report handoffs from still-unproven robust PDF extraction, embedding generation, hosted deployment evidence, external reviewer feedback, endpoint malicious-detection runtime proof, and production semantic retrieval quality. See `docs/review/architecture-current-state-refresh.md`.

Phase 337 adds external reviewer architecture current-state request refresh v0: `docs/review/external-review-request.md`, `docs/review/external-reviewer-link-map.md`, and `.github/ISSUE_TEMPLATE/external-review-feedback.md` now link to `docs/review/architecture-current-state-refresh.md`. This is request infrastructure only, not external reviewer feedback, hosted deployment evidence, or endpoint malicious-detection runtime proof.

Phase 338 adds external review issue body architecture current-state refresh v0: issue #1 now links to `docs/review/architecture-current-state-refresh.md` and `docs/review/external-reviewer-architecture-current-state-request-refresh.md`. Observed issue markers were `updatedAt: 2026-06-04T04:27:19Z`, `first_codepoint: 35`, and `comment_count: 1`. This is an owner-authored issue body edit only, not external reviewer feedback, hosted deployment evidence, or endpoint malicious-detection runtime proof.

Phase 339 adds external feedback current-state architecture issue verification v0: current issue #1 still has `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and only a self-authored non-qualifying comment after the architecture current-state issue-body refresh. This does not close external reviewer feedback v0 and is not hosted deployment evidence, endpoint malicious-detection runtime proof, or production semantic retrieval quality.

Phase 436 adds architecture current-state ClamAV proof boundary refresh v0: `docs/architecture.md` and current reviewer-facing surfaces now recognize `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md` as local ClamAV endpoint malicious-detection owner-runtime proof with `harness_status: verified_infected`, `scan_verdict: infected`, and `matched_signature: Eicar-Test-Signature`, while still not claiming production malware scanning evidence, hosted deployment evidence, external reviewer feedback, production authorization, or product completeness. See `docs/review/architecture-current-state-clamav-proof-boundary-refresh.md`.

Phase 437 adds readme latest-marker current-state refresh v0: the README top implementation status now points to `Architecture ClamAV proof boundary refresh v0`, `ClamAV API endpoint malicious-detection owner runtime smoke v0`, `External review issue body readability refresh v0`, and `Latest external-feedback state: pending; only self-authored issue comment is present`. This is README current-state alignment only, not external reviewer feedback, hosted deployment evidence, production malware scanning evidence, production authorization, or product completion. See `docs/review/readme-latest-marker-current-state-refresh.md`.

Phase 500 adds readme latest-marker embedding handoff current-state refresh v0: the README top implementation status now points to `Embedding provider handoff alignment issue-body refresh v0` and `Latest external-feedback state: pending after handoff issue verification; candidate_count=0; self-authored comment only`. This is README current-state alignment only, not external reviewer feedback, hosted deployment evidence, live embedding generation proof, semantic retrieval quality evidence, or product completion. See `docs/review/readme-latest-marker-embedding-handoff-current-state-refresh.md`.

Phase 438 adds uploaded raw file download readiness preview v0: `GET /documents/upload-raw-files/{raw_file_id}/download-readiness` returns a read-only preflight decision for scan/quarantine/active-approval readiness before raw bytes are served. It returns no raw bytes, consumes no download rate-limit attempt, and writes no download audit event. This is local v0 preflight behavior, not production authorization, authenticated user identity, signed URL support, hosted deployment evidence, external reviewer feedback, or product completion. See `docs/review/uploaded-raw-file-download-readiness-preview.md`.

Phase 439 adds uploaded raw file download readiness runtime smoke v0: local Docker FastAPI plus PostgreSQL verified `GET /documents/upload-raw-files/{raw_file_id}/download-readiness` before scan (`missing_clean_scan`), after clean scan without approval (`missing_download_approval`), and after clean scan plus active approval (`allowed`). The smoke observed `raw_bytes_returned: false`, `rate_limit_consumed: false`, and `events_after_readiness_count: 0`. This is local runtime evidence only, not production authorization, authenticated user identity, signed URL support, hosted deployment evidence, external reviewer feedback, or product completion. See `docs/review/uploaded-raw-file-download-readiness-runtime-smoke.md`.

Phase 440 adds external reviewer readiness-runtime request refresh v0: `docs/review/external-reviewer-readiness-runtime-request-refresh.md` makes the readiness runtime smoke discoverable from reviewer-facing repository paths, including the external-reader proof path, review request packet, reviewer brief, link map, issue template, Braincrew role map, and portfolio index. This is request-surface refresh only, not a live issue body edit, not external reviewer feedback, not hosted evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

Phase 441 adds external review issue body readiness-runtime refresh v0: `docs/review/external-review-issue-body-readiness-runtime-refresh.md` records the owner-authored issue #1 body edit pointing reviewers to the readiness runtime smoke and request refresh. Observed markers: `starts_with_request=true`, `first_codepoint=35`, `has_readiness_runtime_proof=true`, `has_readiness_runtime_request_refresh=true`, `has_missing_clean_scan=true`, `has_missing_download_approval=true`, `has_readiness_allowed=true`, `has_no_raw_bytes_boundary=true`, and `comment_count=1`. This is a live request update only, not external reviewer feedback, not hosted evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

Phase 442 adds external feedback current-state readiness-runtime issue verification v0: `docs/review/external-feedback-current-state-readiness-runtime-issue-verification.md` records the current issue #1 screen after the readiness-runtime issue-body refresh. The issue body has the readiness runtime proof and request-refresh links, but the only comment is owner-authored; screening produced `candidate_count=0`, acceptance drafting produced `draft_count=0`, and external reviewer feedback remains pending.

Phase 443 adds uploaded raw file guard ops summary v0: `GET /ops/summary` and `GET /ops/dashboard` now surface raw-file guard counts for uploaded raw files, scan results, clean/error scans, download approvals, active approvals, download events, blocked downloads, and allowed downloads. This is local operations metadata only, not download readiness call persistence, raw byte exposure, production authorization, authenticated user identity, signed URL support, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/uploaded-raw-file-guard-ops-summary.md`.

Phase 444 adds uploaded raw file guard ops summary runtime smoke v0: local Docker PostgreSQL plus live FastAPI HTTP verified `GET /health`, raw upload `201`, missing-scan download `409`, failed scan metadata, clean scan metadata, active approval, allowed download `200`, expected `/ops/summary` counter deltas, and `/ops/dashboard` metric labels. This is local runtime evidence only, not production authorization, authenticated identity, signed URL support, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/uploaded-raw-file-guard-ops-summary-runtime-smoke.md`.

Phase 445 adds external reviewer raw-file guard ops summary request refresh v0: reviewer-facing repository paths now link to `docs/review/uploaded-raw-file-guard-ops-summary-runtime-smoke.md` and its request-refresh record. This is request-surface refresh only, not live issue body edit, external reviewer feedback, hosted deployment evidence, production authorization, authenticated identity, signed URL support, or product-complete. See `docs/review/external-reviewer-raw-file-guard-ops-summary-request-refresh.md`.

Phase 446 adds external review issue body raw-file guard ops summary refresh v0: issue #1 now points reviewers to the raw-file guard ops summary runtime smoke and request refresh. This is owner-authored issue body routing only, not external reviewer feedback, hosted deployment evidence, production authorization, authenticated identity, signed URL support, or product-complete. See `docs/review/external-review-issue-body-raw-file-guard-ops-summary-refresh.md`.

Phase 447 adds external feedback current-state raw-file guard ops summary issue verification v0: current issue #1 has the raw-file guard ops summary proof/request links, but the only comment is owner-authored, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending. See `docs/review/external-feedback-current-state-raw-file-guard-ops-summary-issue-verification.md`.

Phase 448 adds workflow proof bundle read model v0: `GET /workflow-runs/{id}/proof-bundle` collects the existing workflow detail, derived lineage, and trace lookup surfaces into one reviewer-readable response. This is a read model over existing records only; it adds no table, migration, persisted lineage fact, distributed tracing, hosted observability, external reviewer feedback, hosted deployment evidence, or product-complete claim. See `docs/review/workflow-proof-bundle-read-model.md`.

Phase 449 adds workflow proof bundle runtime smoke v0: `docs/review/workflow-proof-bundle-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP evidence for `GET /workflow-runs/{id}/proof-bundle` after a deterministic workflow preview and for a metadata-only workflow row with no trace id. Observed values include `health_status: ok`, `execute_preview_status_code: 201`, `proof_bundle_status_code: 200`, `metadata_only_proof_bundle_status_code: 200`, `detail_retrieval_run_count: 1`, `lineage_missing_reference_count: 0`, `trace_evidence_ledger_entry_count: 1`, `metadata_only_workflow_trace_id_is_null: true`, and `metadata_only_trace_is_null: true`. This is local runtime evidence only, not distributed tracing, hosted observability, external reviewer feedback, hosted deployment evidence, or product-complete.

Phase 450 adds external reviewer workflow proof bundle request refresh v0: `docs/review/external-reviewer-workflow-proof-bundle-request-refresh.md` makes the workflow proof bundle runtime smoke discoverable from reviewer-facing repository paths, including the external-reader proof path, review request packet, reviewer brief, link map, issue template, portfolio index, README, GOAL, and this runbook. This is request-surface refresh only, not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not distributed tracing, not hosted observability, not new lineage storage, and not product-complete.

Phase 451 adds external review issue body workflow proof bundle refresh v0: issue #1 now points reviewers to `docs/review/workflow-proof-bundle-runtime-smoke.md`, `docs/review/external-reviewer-workflow-proof-bundle-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-proof-bundle-refresh.md`. Observed markers include `starts_with_request=true`, `first_codepoint=35`, `has_workflow_proof_bundle_runtime_proof=true`, `has_workflow_proof_bundle_request_refresh=true`, `has_workflow_proof_bundle_issue_body_refresh=true`, `has_health_status_ok=true`, `has_execute_preview_status_201=true`, `has_proof_bundle_status_200=true`, `has_metadata_only_proof_bundle_status_200=true`, `has_bundle_boundary=true`, `has_metadata_only_trace_null=true`, `has_external_feedback_boundary=true`, and `comment_count=1`. This is owner-authored issue body routing only, not external reviewer feedback, hosted deployment evidence, distributed tracing, hosted observability, new lineage storage, customer validation, Braincrew acceptance, or product-complete.

Phase 452 adds external feedback current-state workflow proof bundle issue verification v0: current issue #1 has the workflow proof bundle runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending. See `docs/review/external-feedback-current-state-workflow-proof-bundle-issue-verification.md`.

Phase 453 adds workflow proof bundle dashboard link v0: `GET /ops/dashboard` workflow rows now link to the existing `GET /workflow-runs/{id}/proof-bundle` read model using the label `proof bundle`. This is dashboard navigation only, not a new endpoint, schema, migration, lineage storage, distributed tracing, hosted observability, external reviewer feedback, hosted deployment evidence, or product-complete. See `docs/review/workflow-proof-bundle-dashboard-link.md`.

Phase 454 adds workflow proof bundle dashboard runtime smoke v0: local Docker PostgreSQL plus live FastAPI HTTP verified `GET /ops/dashboard` returns `200`, includes the workflow `proof bundle` link, and `GET /workflow-runs/{id}/proof-bundle` returns `200` with `bundle_boundary=read_model_only_existing_records_no_new_storage`. This is local runtime evidence only, not new endpoint behavior, schema, migration, new lineage storage, distributed tracing, hosted observability, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md`.

Phase 455 adds external reviewer workflow proof bundle dashboard runtime request refresh v0: reviewer-facing repository paths now point to `docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md` and `docs/review/external-reviewer-workflow-proof-bundle-dashboard-runtime-request-refresh.md`. This is request-surface refresh only, not a live issue body edit, runtime behavior, schema, migration, new lineage storage, distributed tracing, hosted observability, hosted deployment evidence, external reviewer feedback, or product-complete.

Phase 505 adds external reviewer workflow failure-case persistence runtime request refresh v0: reviewer-facing repository paths now point to `docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md` and `docs/review/external-reviewer-workflow-failure-case-persistence-runtime-request-refresh.md`. This is request-surface refresh only, not a live issue body edit, runtime behavior, schema, migration, background automation, hosted deployment evidence, external reviewer feedback, complete workflow failure causality, or product-complete.

Phase 506 adds external review issue body workflow failure-case persistence runtime refresh v0: issue #1 now points reviewers to `docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md`, `docs/review/external-reviewer-workflow-failure-case-persistence-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-failure-case-persistence-runtime-refresh.md`. Observed markers include `starts_with_request=true`, `first_codepoint=35`, `has_workflow_failure_case_persistence_runtime_proof=true`, `has_workflow_failure_case_persistence_request_refresh=true`, `has_workflow_failure_case_persistence_issue_body_refresh=true`, `has_persistence_boundary=true`, `has_queue_status_failure_case_linked=true`, `has_completed_workflow_409=true`, `has_duplicate_409=true`, and `comment_count=1`. This is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, background automation, complete workflow failure causality, or product-complete.

Phase 507 adds external feedback current-state workflow failure-case persistence runtime issue verification v0: current issue #1 has the workflow failure-case persistence runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending. See `docs/review/external-feedback-current-state-workflow-failure-case-persistence-runtime-issue-verification.md`.

Phase 508 adds workflow proof bundle failure-case links v0: `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/proof-bundle` now include linked `failure_cases` plus `failure_case_count`, and `GET /failure-cases?workflow_run_id={id}` filters failure cases by workflow parent. This is a read model only, not automatic failure detection, background automation, complete workflow failure causality, root-cause automation, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/workflow-proof-bundle-failure-case-links.md`.

Phase 509 adds workflow proof bundle failure-case links runtime smoke v0: local Docker PostgreSQL plus live FastAPI HTTP verified `detail_failure_case_count: 1`, `bundle_failure_case_count: 1`, `filtered_failure_case_count: 1`, `unrelated_filtered_out: true`, and `proof_surface_has_failure_case_filter: true` for linked failure cases surfaced through `GET /workflow-runs/{id}`, `GET /workflow-runs/{id}/proof-bundle`, and `GET /failure-cases?workflow_run_id={id}`. This is local runtime evidence only, not automatic failure detection, background automation, complete workflow failure causality, root-cause automation, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md`.

Phase 510 adds external reviewer workflow proof bundle failure-case links runtime request refresh v0: reviewer-facing repository paths now point to `docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md` and `docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md`. This is request-surface refresh only, not a live issue body edit, runtime behavior, schema, migration, hosted deployment evidence, external reviewer feedback, automatic failure detection, background automation, complete workflow failure causality, or product-complete.

Phase 511 adds external review issue body workflow proof bundle failure-case links runtime refresh v0: issue #1 now points reviewers to `docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md`, `docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-proof-bundle-failure-case-links-runtime-refresh.md`. Observed markers include `starts_with_request=true`, `first_codepoint=35`, `has_workflow_proof_bundle_failure_case_links_runtime_proof=true`, `has_workflow_proof_bundle_failure_case_links_request_refresh=true`, `has_workflow_proof_bundle_failure_case_links_issue_body_refresh=true`, `has_detail_failure_case_count=true`, `has_bundle_failure_case_count=true`, `has_filtered_failure_case_count=true`, `has_unrelated_filtered_out=true`, `has_proof_surface_has_failure_case_filter=true`, and `comment_count=1`. This is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, automatic failure detection, background automation, complete workflow failure causality, or product-complete.

Phase 512 adds external feedback current-state workflow proof bundle failure-case links runtime issue verification v0: current issue #1 has the workflow proof bundle failure-case links runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending. See `docs/review/external-feedback-current-state-workflow-proof-bundle-failure-case-links-runtime-issue-verification.md`.

Phase 513 adds workflow dashboard failure-case counts v0: `GET /ops/dashboard` workflow rows now show a `Linked Failure Cases` column, link nonzero counts to `GET /failure-cases?workflow_run_id={id}`, and leave unlinked workflow rows as plain `0`. This is a dashboard read model over existing records only, not automatic failure detection, background automation, complete workflow failure causality, root-cause automation, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/workflow-dashboard-failure-case-counts.md`.

Phase 514 adds workflow dashboard failure-case counts runtime smoke v0: local Docker PostgreSQL plus live FastAPI HTTP verified `GET /ops/dashboard` returns `200`, includes the `Linked Failure Cases` workflow column, links a workflow with one linked failure case to `GET /failure-cases?workflow_run_id={id}`, and omits that filter link for an unlinked failed workflow. This is local runtime evidence only, not automatic failure detection, background automation, complete workflow failure causality, root-cause automation, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/workflow-dashboard-failure-case-counts-runtime-smoke.md`.

Phase 515 adds external reviewer workflow dashboard failure-case counts runtime request refresh v0: reviewer-facing repository paths now point to `docs/review/workflow-dashboard-failure-case-counts-runtime-smoke.md` and `docs/review/external-reviewer-workflow-dashboard-failure-case-counts-runtime-request-refresh.md`. This is request-surface refresh only, not a live issue body edit, runtime behavior, schema, migration, hosted deployment evidence, external reviewer feedback, automatic failure detection, background automation, complete workflow failure causality, or product-complete.

Phase 516 adds external review issue body workflow dashboard failure-case counts runtime refresh v0: issue #1 now points reviewers to `docs/review/workflow-dashboard-failure-case-counts-runtime-smoke.md`, `docs/review/external-reviewer-workflow-dashboard-failure-case-counts-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-dashboard-failure-case-counts-runtime-refresh.md`. Observed markers include `starts_with_request=true`, `first_codepoint=35`, `has_workflow_dashboard_failure_case_counts_runtime_proof=true`, `has_workflow_dashboard_failure_case_counts_request_refresh=true`, `has_workflow_dashboard_failure_case_counts_issue_body_refresh=true`, `has_dashboard_contains_linked_failure_cases_header=true`, `has_dashboard_contains_linked_failure_case_filter=true`, `has_dashboard_omits_unlinked_failure_case_filter=true`, and `comment_count=1`. This is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, automatic failure detection, background automation, complete workflow failure causality, or product-complete.

Phase 517 adds external feedback current-state workflow dashboard failure-case counts runtime issue verification v0: current issue #1 has the workflow dashboard failure-case counts runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending. See `docs/review/external-feedback-current-state-workflow-dashboard-failure-case-counts-runtime-issue-verification.md`.

Phase 456 adds external review issue body workflow proof bundle dashboard runtime refresh v0: issue #1 body now points reviewers to `docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md`, `docs/review/external-reviewer-workflow-proof-bundle-dashboard-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-proof-bundle-dashboard-runtime-refresh.md`. This is owner-authored issue routing only, not outside reviewer feedback, runtime behavior, schema, migration, new lineage storage, distributed tracing, hosted observability, hosted deployment evidence, or product-complete.

Phase 457 adds external feedback current-state workflow proof bundle dashboard runtime issue verification v0: current issue #1 has the dashboard runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending. See `docs/review/external-feedback-current-state-workflow-proof-bundle-dashboard-runtime-issue-verification.md`.

Phase 458 adds external reviewer shortlist v0: `docs/review/external-reviewer-shortlist.md` gives outside reviewers a 90-second shortlist with a maximum five proof artifacts before the full proof path. This is reviewer navigation only, not external reviewer feedback, hosted deployment evidence, customer validation, Braincrew acceptance, or product-complete.

Phase 459 adds external review issue body shortlist refresh v0: issue #1 body now starts its Fast Path with `docs/review/external-reviewer-shortlist.md`. This is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, customer validation, Braincrew acceptance, or product-complete. See `docs/review/external-review-issue-body-shortlist-refresh.md`.

Phase 460 adds external feedback current-state shortlist issue verification v0: current issue #1 starts its Fast Path with `docs/review/external-reviewer-shortlist.md`, but the only screened comment is owner-authored, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending. See `docs/review/external-feedback-current-state-shortlist-issue-verification.md`.

Phase 340 adds uploaded PDF text extraction v0: `POST /documents/upload-preview` can pass uploaded PDF bytes through PyMuPDF and return `parser: pdf-pymupdf`, `digital_pdf_text_extraction: true`, `robust_pdf_extraction: false`, and `preview_only_not_persisted`. This is digital PDF text only; it is not OCR, table extraction, layout fidelity, robust PDF extraction, raw file storage, hosted deployment evidence, or external reviewer feedback.

Phase 540 adds uploaded PDF page diagnostics v0: `POST /documents/upload-preview` now exposes page-level PyMuPDF diagnostics for uploaded digital PDFs, including `page_text_char_counts`, `extracted_page_count`, `empty_page_count`, `text_block_count`, `image_block_count`, and `extraction_scope=digital_text_page_diagnostics`. This is diagnostics over digital text extraction only; it is not OCR, table extraction, layout fidelity, robust PDF extraction, hosted deployment evidence, or external reviewer feedback.

Phase 541 adds uploaded PDF page diagnostics runtime smoke v0: `docs/review/uploaded-pdf-page-diagnostics-runtime-smoke.md` records local Docker/FastAPI HTTP evidence that `POST /documents/upload-preview` returns `parser -> pdf-pymupdf`, `page_text_char_counts -> [39]`, `empty_page_count -> 0`, `text_block_count -> 1`, `image_block_count -> 0`, and `document_count_delta -> 0` for a preview-only uploaded digital PDF. This is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, parsed text persistence, or product-complete.

Phase 542 adds external reviewer PDF page diagnostics runtime request refresh v0: `CONTRIBUTING.md`, the external review issue template, request packet, reviewer brief, link map, external-reader proof path, portfolio index, README, GOAL, and runbook now point reviewers to `docs/review/uploaded-pdf-page-diagnostics-runtime-smoke.md`. This is request infrastructure only; it does not edit the live public issue body and is not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, parsed text persistence, or product-complete.

Phase 543 adds external reviewer PDF page diagnostics runtime issue-body refresh v0: live issue #1 now points reviewers to `docs/review/uploaded-pdf-page-diagnostics-runtime-smoke.md`, `docs/review/external-reviewer-pdf-page-diagnostics-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-pdf-page-diagnostics-runtime-refresh.md`; observed `updatedAt` is `2026-06-05T11:08:19Z`, `comment_count` remains `1`, and the issue body contains `page_text_char_counts -> [39]`. This is an owner-authored issue body edit only; it is not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, parsed text persistence, or product-complete.

Phase 544 adds external feedback current-state PDF page diagnostics runtime issue verification v0: `docs/review/external-feedback-current-state-pdf-page-diagnostics-runtime-issue-verification.md` records that issue #1 still points to the PDF page diagnostics runtime proof while the only screened comment remains self-authored with `comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, `classification: non_qualifying`, and `status: pending`. External reviewer feedback remains pending.

Phase 545 adds uploaded PDF page diagnostics downstream provenance v0: `POST /documents/upload-chunks` now carries PDF page diagnostics such as `page_text_char_counts`, `empty_page_count`, `text_block_count`, and `image_block_count` into document and chunk metadata, and `POST /documents/{document_id}/retrieval-runs` summarizes those diagnostics from candidate chunk metadata. This is route-level implementation proof only; it is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, or product-complete.

Phase 546 adds uploaded PDF page diagnostics downstream provenance runtime smoke v0: `docs/review/uploaded-pdf-page-diagnostics-downstream-provenance-runtime-smoke.md` records local Docker/FastAPI HTTP evidence that `POST /documents/upload-chunks` and `POST /documents/{document_id}/retrieval-runs` preserve page diagnostics through document profile metadata, chunk metadata, retrieval metadata, and retrieval candidate metadata. Observed markers include `document_profile_page_text_char_counts -> [39]`, `chunk_metadata_page_text_char_counts -> [39]`, `retrieval_metadata_page_text_char_counts -> [39]`, and `retrieval_candidate_page_text_char_counts -> [39]`. This is local runtime evidence only; it is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, or product-complete.

Phase 547 adds external reviewer PDF page diagnostics downstream runtime request refresh v0: `CONTRIBUTING.md`, the external review issue template, request packet, reviewer brief, link map, external-reader proof path, portfolio index, README, GOAL, and runbook now point reviewers to `docs/review/uploaded-pdf-page-diagnostics-downstream-provenance-runtime-smoke.md`. This is request infrastructure only; it does not edit the live public issue body and is not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, or product-complete.

Phase 548 adds external reviewer PDF page diagnostics downstream runtime issue-body refresh v0: issue #1 now points reviewers to `docs/review/uploaded-pdf-page-diagnostics-downstream-provenance-runtime-smoke.md`, `docs/review/external-reviewer-pdf-page-diagnostics-downstream-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-pdf-page-diagnostics-downstream-runtime-refresh.md`. Observed markers include `updatedAt: 2026-06-05T11:49:28Z`, `starts_with_request=true`, `first_codepoint=35`, `has_pdf_page_diagnostics_downstream_runtime_proof=true`, `has_pdf_page_diagnostics_downstream_request_refresh=true`, `has_pdf_page_diagnostics_downstream_issue_body_record=true`, `has_retrieval_candidate_page_counts=true`, and `comment_count=1`. This is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, report generation, or product-complete.

Phase 549 adds external feedback current-state PDF page diagnostics downstream runtime issue verification v0: `docs/review/external-feedback-current-state-pdf-page-diagnostics-downstream-runtime-issue-verification.md` records that issue #1 still points to the downstream runtime proof while the only screened comment remains self-authored by `svy04`, with `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, `classification: non_qualifying`, `reason: self_authored_comment`, and `status: pending`. External reviewer feedback remains pending.

Phase 550 adds readme latest-marker PDF downstream current-state refresh v0: the README top implementation status now points to `PDF page diagnostics downstream runtime issue-body refresh v0` and `Latest external-feedback state: pending after PDF page diagnostics downstream issue verification; candidate_count=0; self-authored comment only`. This is README current-state alignment only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, live embedding generation proof, or product-complete. See `docs/review/readme-latest-marker-pdf-downstream-current-state-refresh.md`.

Phase 551 adds readme latest-marker PDF downstream current-state remote verification v0: `docs/review/readme-latest-marker-pdf-downstream-current-state-remote-verification.md` records remote GitHub Actions success for head `308d8e91f46f1f40bb2ef704c7792d12e4809a86`, with CI run `27013838611` (`api-smoke -> success`) and External Feedback Screen run `27013838639` (`screen -> success`). This is remote workflow evidence only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, live embedding generation proof, or product-complete.

Phase 552 adds uploaded PDF no-text failure candidate handoff v0: `POST /documents/upload-chunks` now preserves `failure_case_candidate.failure_type=pdf_no_extractable_text`, `chunk_handoff_no_chunks`, `page_text_char_counts=[0]`, `empty_page_count=1`, `extracted_page_count=0`, and `robust_pdf_extraction=false` in document metadata when an uploaded PDF can be opened but has no embedded digital text. This is local route behavior only, not robust PDF extraction, OCR, table extraction, layout fidelity, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/uploaded-pdf-no-text-failure-candidate-handoff.md`.

Phase 553 adds uploaded PDF no-text failure candidate runtime smoke v0: local Docker/FastAPI HTTP verified `GET /health -> 200` and `POST /documents/upload-chunks -> 201` for a valid blank uploaded PDF, preserving `pdf_no_extractable_text`, `chunk_handoff_no_chunks`, `chunk_count=0`, `page_text_char_counts=[0]`, `empty_page_count=1`, `extracted_page_count=0`, `robust_pdf_extraction=false`, `raw_file_storage=false`, and `parsed_text_storage=false`. This is local runtime evidence only, not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, or product-complete. See `docs/review/uploaded-pdf-no-text-failure-candidate-runtime-smoke.md`.

Phase 554 adds external reviewer PDF no-text failure candidate runtime request refresh v0: reviewer-facing request surfaces now point to `docs/review/uploaded-pdf-no-text-failure-candidate-runtime-smoke.md` so reviewers can inspect `pdf_no_extractable_text`, `chunk_handoff_no_chunks`, `chunk_count=0`, `page_text_char_counts=[0]`, and `robust_pdf_extraction=false` for a valid blank uploaded PDF. This is request infrastructure only, not a live issue body edit, hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, or product-complete. See `docs/review/external-reviewer-pdf-no-text-failure-candidate-runtime-request-refresh.md`.

Phase 555 adds external reviewer PDF no-text failure candidate runtime issue-body refresh v0: issue #1 now routes reviewers to `docs/review/uploaded-pdf-no-text-failure-candidate-runtime-smoke.md`, the request refresh, and the issue-body refresh record from the `Latest Proof To Inspect` section. Observed live issue markers: `updatedAt: 2026-06-05T12:45:27Z`, `comment_count: 1`, `starts_with_request: true`, and `has_pdf_no_text_failure_candidate_runtime_proof: true`. This is an owner-authored issue body edit only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, or product-complete. See `docs/review/external-review-issue-body-pdf-no-text-failure-candidate-runtime-refresh.md`.

Phase 556 adds external feedback current-state PDF no-text failure candidate runtime issue verification v0: issue #1 still has the no-text PDF runtime proof, request refresh, and issue-body refresh links, but the only screened comment remains owner-authored by `svy04`, with `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, `classification: non_qualifying`, `reason: self_authored_comment`, and `status: pending`. External reviewer feedback remains pending. See `docs/review/external-feedback-current-state-pdf-no-text-failure-candidate-runtime-issue-verification.md`.

Phase 557 adds uploaded PDF no-text ops summary dashboard v0: `/ops/summary` now exposes `chunk_handoff_no_chunks_count` and `pdf_no_text_failure_candidate_count`, and `/ops/dashboard` shows `No-text PDF Handoffs` and `PDF No-text Failure Candidates`. These counts are metadata-derived from document `profile_json`; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, automatic failure-case creation, or product-complete. See `docs/review/uploaded-pdf-no-text-ops-summary-dashboard.md`.

Phase 558 adds uploaded PDF no-text ops summary dashboard runtime smoke v0: local Docker/FastAPI HTTP verified `GET /health -> 200`, `POST /documents/upload-chunks -> 201`, `GET /ops/summary -> 200`, and `GET /ops/dashboard -> 200`; after uploading a valid blank PDF, `chunk_handoff_no_chunks_count` and `pdf_no_text_failure_candidate_count` both increased by `1`, and the dashboard contained `No-text PDF Handoffs`, `PDF No-text Failure Candidates`, and the metadata-derived boundary. This is local runtime evidence only, not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, automatic failure-case creation, or product-complete. See `docs/review/uploaded-pdf-no-text-ops-summary-dashboard-runtime-smoke.md`.

Phase 559 adds persisted document failure candidate draft preview v0: `POST /documents/{document_id}/failure-case-draft-preview` turns a persisted document `profile_json.failure_case_candidate` into a preview-only failure-case draft with `human_confirmation_required=true`, without re-uploading the file and without creating `failure_cases`. This is not automatic failure-case creation, external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, or product-complete. See `docs/review/persisted-document-failure-candidate-draft-preview.md`.

Phase 560 adds persisted document failure candidate draft preview runtime smoke v0: local Docker/FastAPI HTTP verified `GET /health -> 200`, `POST /documents/upload-chunks -> 201`, `POST /documents/{document_id}/failure-case-draft-preview -> 200`, and `GET /failure-cases -> 200`; the preview returned `preview_only_not_persisted`, `human_confirmation_required=true`, `pdf_no_extractable_text`, `persisted_document_failure_case_candidate`, and `failure_case_count_delta=0`. This is local runtime evidence only, not automatic failure-case creation, external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, or product-complete. See `docs/review/persisted-document-failure-candidate-draft-preview-runtime-smoke.md`.

Phase 561 adds external reviewer persisted document failure candidate draft runtime request refresh v0: reviewer-facing request surfaces now point to `docs/review/persisted-document-failure-candidate-draft-preview-runtime-smoke.md` and `docs/review/external-reviewer-persisted-document-failure-candidate-draft-runtime-request-refresh.md` so reviewers can inspect `preview_only_not_persisted`, `human_confirmation_required=true`, `persisted_document_failure_case_candidate`, and `failure_case_count_delta=0`. This is request infrastructure only, not a live issue body edit, external reviewer feedback, hosted deployment evidence, automatic failure-case creation, robust PDF extraction, OCR, or product-complete.

Phase 562 adds external reviewer persisted document failure candidate draft runtime issue-body refresh v0: issue #1 now routes reviewers to `docs/review/persisted-document-failure-candidate-draft-preview-runtime-smoke.md`, the request refresh, and the issue-body refresh record from the `Latest Proof To Inspect` section. Observed live issue markers: `updatedAt: 2026-06-05T13:42:17Z`, `comment_count: 1`, `starts_with_request: true`, `first_codepoint: 35`, and `has_persisted_document_failure_candidate_draft_runtime_proof: true`. This is an owner-authored issue body edit only, not external reviewer feedback, hosted deployment evidence, automatic failure-case creation, robust PDF extraction, OCR, or product-complete. See `docs/review/external-review-issue-body-persisted-document-failure-candidate-draft-runtime-refresh.md`.

Phase 563 adds external feedback current-state persisted document failure candidate draft runtime issue verification v0: issue #1 still has the persisted document failure candidate draft runtime proof, request refresh, and issue-body refresh links, but the only screened comment remains owner-authored by `svy04`, with `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, `classification: non_qualifying`, `reason: self_authored_comment`, and `status: pending`. External reviewer feedback remains pending. See `docs/review/external-feedback-current-state-persisted-document-failure-candidate-draft-runtime-issue-verification.md`.

Phase 564 adds persisted document failure candidate manual handoff smoke v0: route-level smoke verifies `POST /documents/upload-chunks`, `POST /documents/{document_id}/failure-case-draft-preview`, human confirmation by changing `draft.fix_status` from `draft` to `open`, `POST /failure-cases -> 201`, and `GET /failure-cases -> 200`. This reuses the existing manual persistence path and does not add automatic failure-case creation, a confirm endpoint, hosted deployment evidence, robust PDF extraction, OCR, or product-complete. See `docs/review/persisted-document-failure-candidate-manual-handoff-smoke.md`.

Phase 565 adds persisted document failure candidate manual handoff runtime smoke v0: local Docker/FastAPI HTTP verified `GET /health -> 200`, `POST /documents/upload-chunks -> 201`, `POST /documents/{document_id}/failure-case-draft-preview -> 200`, `POST /failure-cases -> 201`, and `GET /failure-cases -> 200`; after human confirmation changed `draft.fix_status` from `draft` to `open`, `failure_case_count_delta -> 1`. This reuses the existing manual persistence path and does not add automatic failure-case creation, a confirm endpoint, hosted deployment evidence, robust PDF extraction, OCR, or product-complete. See `docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md`.

Phase 566 adds external reviewer persisted document failure candidate manual handoff runtime request refresh v0: reviewer-facing request surfaces now point to `docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md` and `docs/review/external-reviewer-persisted-document-failure-candidate-manual-handoff-runtime-request-refresh.md` so reviewers can inspect `POST /failure-cases -> 201`, `failure_case_count_delta -> 1`, and the human confirmation step from `draft` to `open`. This is request infrastructure only, not a live issue body edit, external reviewer feedback, hosted deployment evidence, automatic failure-case creation, a confirm endpoint, robust PDF extraction, OCR, or product-complete.

Phase 567 adds external reviewer persisted document failure candidate manual handoff runtime issue-body refresh v0: issue #1 now routes reviewers to `docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md`, the request refresh, and the issue-body refresh record from the `Latest Proof To Inspect` section. Observed live issue markers: `updatedAt: 2026-06-05T14:15:36Z`, `comment_count: 1`, `starts_with_request: true`, `first_codepoint: 35`, and `has_persisted_document_failure_candidate_manual_handoff_runtime_proof: true`. This is an owner-authored issue body edit only, not external reviewer feedback, hosted deployment evidence, automatic failure-case creation, a confirm endpoint, robust PDF extraction, OCR, or product-complete. See `docs/review/external-review-issue-body-persisted-document-failure-candidate-manual-handoff-runtime-refresh.md`.

Phase 341 adds uploaded PDF downstream handoff v0: `POST /documents/upload-chunk-preview`, `POST /documents/upload-chunks`, and `POST /documents/upload-retrieval-preview` reuse the same PyMuPDF digital text extraction path for uploaded PDF bytes before chunking or lexical retrieval. This is digital PDF text only; it is not OCR, table extraction, layout fidelity, robust PDF extraction, raw file storage, hosted deployment evidence, or external reviewer feedback.

Phase 342 adds uploaded PDF downstream handoff runtime smoke v0: local Docker PostgreSQL plus live FastAPI HTTP observed uploaded digital PDF bytes flowing through `POST /documents/upload-preview`, `POST /documents/upload-chunk-preview`, `POST /documents/upload-chunks`, `GET /documents/{document_id}/chunks`, and `POST /documents/upload-retrieval-preview` with `parser -> pdf-pymupdf`, `digital_pdf_text_extraction -> true`, and `replacement_decode_warning_present -> false`. This is local runtime evidence only; it is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, or raw file storage.

Phase 343 adds uploaded PDF downstream handoff application refresh v0: README, GOAL, runbook, portfolio index, Braincrew role map, application-ready review, and external-reader proof path now surface `docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md`. This is application packaging only; it is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, or raw file storage.

Phase 344 adds external reviewer PDF downstream handoff request refresh v0: `CONTRIBUTING.md`, the external review issue template, request packet, reviewer brief, link map, portfolio index, README, GOAL, and runbook now point reviewers to `docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md`. This is request infrastructure only; it is not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, or raw file storage.

Phase 345 adds external reviewer PDF downstream handoff issue-body refresh v0: live issue #1 now points reviewers to `docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md` and `docs/review/external-reviewer-pdf-downstream-handoff-request-refresh.md`; observed `updatedAt` is `2026-06-04T05:53:43Z`, `first_codepoint` is `35`, and `comment_count` remains `1`. This is an owner-authored issue body edit only; it is not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, or raw file storage.

Phase 346 adds external feedback current-state PDF downstream handoff issue verification v0: current issue #1 still has `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and only a self-authored non-qualifying comment after the PDF downstream handoff issue-body refresh. This does not close external reviewer feedback v0 and is not hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity evidence, or raw file storage.

Phase 347 adds uploaded PDF retrieval-run provenance v0: PDF-derived `POST /documents/upload-chunks` rows now keep `parser: pdf-pymupdf`, `digital_pdf_text_extraction: true`, and `robust_pdf_extraction: false` in chunk metadata, and `POST /documents/{document_id}/retrieval-runs` summarizes candidate provenance with `candidate_source_types`, `candidate_parsers`, and `source_provenance_boundary`. This is route-level proof only; it is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

Phase 348 adds uploaded PDF retrieval-run provenance runtime smoke v0: local Docker PostgreSQL plus live FastAPI HTTP observed uploaded digital PDF bytes flowing through `POST /documents/upload-chunks`, `POST /documents/{document_id}/retrieval-runs`, and `GET /retrieval-runs` with `parser -> pdf-pymupdf`, `retrieval_candidate_parsers -> pdf-pymupdf`, `retrieval_digital_pdf_text_extraction -> true`, `retrieval_robust_pdf_extraction -> false`, and `source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only`. This is local runtime evidence only; it is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

Phase 349 adds external reviewer PDF retrieval-run provenance request refresh v0: `CONTRIBUTING.md`, the external review issue template, request packet, reviewer brief, link map, external-reader proof path, portfolio index, README, GOAL, and runbook now point reviewers to `docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md` with `candidate_parsers -> pdf-pymupdf` and `source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only`. This is request infrastructure only; it does not edit the live public issue body and is not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

Phase 350 adds external reviewer PDF retrieval-run provenance issue-body refresh v0: live issue #1 now points reviewers to `docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md` and `docs/review/external-reviewer-pdf-retrieval-run-provenance-request-refresh.md`; observed `updatedAt` is `2026-06-04T06:48:07Z`, `first_codepoint` is `35`, and `comment_count` remains `1`. This is an owner-authored issue body edit only; it is not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

Phase 351 adds external feedback current-state PDF retrieval-run provenance issue verification v0: current issue #1 still has `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and only a self-authored non-qualifying comment after the PDF retrieval-run provenance issue-body refresh. This does not close external reviewer feedback v0 and is not hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity evidence, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

Phase 352 adds uploaded PDF retrieval-run-linked Evidence Ledger provenance v0: retrieval-run-linked Evidence Ledger entries now persist candidate chunk parser/source provenance in `metadata_json`, including `metadata_json.parser -> pdf-pymupdf`, `metadata_json.digital_pdf_text_extraction -> true`, `metadata_json.robust_pdf_extraction -> false`, and `metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk`. This is route-level/schema proof only; it is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity evidence, raw file storage, full parsed text persistence, Noise Gate behavior, or report generation.

Phase 353 adds uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime smoke v0: local Docker PostgreSQL plus live FastAPI HTTP observed `POST /documents/upload-chunks`, `POST /documents/{document_id}/retrieval-runs`, `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, and `GET /evidence-ledgers?retrieval_run_id=` after applying `018_evidence_ledger_metadata_json.sql`. It observed `metadata_json.parser -> pdf-pymupdf`, `metadata_json.digital_pdf_text_extraction -> true`, `metadata_json.robust_pdf_extraction -> false`, `metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk`, and `ledger_retrieval_run_id_matches -> true`. This is local runtime evidence only; it is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity evidence, raw file storage, full parsed text persistence, Noise Gate behavior, or report generation.

Phase 354 adds external reviewer PDF retrieval-run-linked Evidence Ledger provenance request refresh v0: `CONTRIBUTING.md`, the external review issue template, request packet, reviewer brief, link map, external-reader proof path, portfolio index, README, GOAL, and runbook now point reviewers to `docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md` with `metadata_json.parser -> pdf-pymupdf` and `metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk`. This is request infrastructure only; it does not edit the live public issue body and is not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Noise Gate behavior, or report generation.

Phase 355 adds external reviewer PDF retrieval-run-linked Evidence Ledger provenance issue-body refresh v0: live issue #1 now points reviewers to `docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md` and `docs/review/external-reviewer-pdf-retrieval-run-linked-evidence-ledger-provenance-request-refresh.md`; observed `updatedAt` is `2026-06-04T07:43:00Z`, `first_codepoint` is `35`, and `comment_count` remains `1`. This is an owner-authored issue body edit only; it is not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Noise Gate behavior, or report generation.

Phase 356 adds external feedback current-state PDF retrieval-run-linked Evidence Ledger provenance issue verification v0: current issue #1 still has `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and only a self-authored non-qualifying comment after the PDF retrieval-run-linked Evidence Ledger provenance issue-body refresh. This does not close external reviewer feedback v0 and is not hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity evidence, raw file storage, full parsed text persistence, Noise Gate behavior, or report generation.

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

Phase 38.6 adds a workflow proof bundle read model: `GET /workflow-runs/{id}/proof-bundle` is a convenience response over existing workflow detail, lineage, and trace lookup records. It is not distributed tracing, not hosted observability, and not new lineage storage.

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

Phase 357 adds failure-case workflow review queue v0: `GET /failure-cases/workflow-review-queue` returns failed, blocked, and needs-revision workflow parents with either `needs_failure_case_review` or `failure_case_linked`. This is a read model only; it does not create failure_cases, keeps the human confirmation boundary at `POST /failure-cases/draft-preview` plus manual persistence, and is not complete workflow failure causality.

Phase 358 adds failure-case workflow review queue runtime smoke verification v0: local fresh migrated Docker DB plus live FastAPI HTTP observed `POST /workflow-runs`, `POST /failure-cases`, and `GET /failure-cases/workflow-review-queue` with `pending_review_count: 1`, `linked_failure_case_count: 1`, `needs_failure_case_review`, `failure_case_linked`, and `read_model_only_no_automatic_failure_case_creation`. This is local runtime evidence only; it does not create failure_cases, is not hosted deployment evidence, is not external reviewer feedback, and is not complete workflow failure causality.

Phase 359 adds failure-case workflow review queue dashboard surfacing review v0: `docs/review/failure-case-workflow-review-queue-dashboard-surfacing-review.md` selects a compact `Failure-case Workflow Review Queue` section for future `GET /ops/dashboard` rendering, with `pending_review_count`, `linked_failure_case_count`, `needs_failure_case_review`, `failure_case_linked`, and a draft preview POST cue. This review gate does not change dashboard HTML and is not automatic failure-case creation.

Phase 360 adds failure-case workflow review queue dashboard surfacing v0: `GET /ops/dashboard` now renders a compact `Failure-case Workflow Review Queue` section using the existing `build_failure_case_workflow_review_queue` read model. It shows `pending_review_count`, `linked_failure_case_count`, `needs_failure_case_review`, `failure_case_linked`, workflow links, stage/error metadata, and a draft preview POST cue. This dashboard surface does not create failure_cases and is not complete workflow failure causality.

Phase 518 adds workflow review queue dashboard draft-preview method boundary v0: `GET /ops/dashboard` now renders `POST /failure-cases/draft-preview` plus `draft preview requires an explicit POST request` instead of a clickable GET-looking draft-preview anchor. This is dashboard method-boundary hardening only, not automatic failure-case creation, background automation, complete workflow failure causality, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/workflow-review-queue-dashboard-draft-preview-method-boundary.md`.

Phase 519 adds ops dashboard GET-only link method boundary v0: `GET /ops/dashboard` now states `Dashboard links are GET-only inspection routes.` and `POST-only actions render as method cues, not anchors.` The route test verifies workflow detail links remain clickable while `POST /failure-cases/draft-preview` remains a method cue rather than an href. This is not a route behavior change, automatic failure-case creation, background automation, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/ops-dashboard-get-only-link-method-boundary.md`.

Phase 520 adds ops dashboard anchor method metadata v0: every clickable `GET /ops/dashboard` anchor now carries `data-method="GET"` so dashboard inspection links are machine-readable, while POST-only actions remain method cues. This is dashboard anchor metadata only, not a route behavior change, automatic failure-case creation, background automation, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/ops-dashboard-anchor-method-metadata.md`.

Phase 521 adds ops dashboard anchor GET smoke v0: local FastAPI test-client smoke extracts every clickable `data-method="GET"` anchor from `GET /ops/dashboard` and verifies each unique href resolves as a GET 200 inspection route. POST-only actions remain non-clickable method cues. This is not browser automation evidence, hosted deployment evidence, external reviewer feedback, or product-complete. See `docs/review/ops-dashboard-anchor-get-smoke.md`.

Phase 522 adds ops dashboard anchor GET runtime smoke v0: local Docker PostgreSQL plus live FastAPI HTTP evidence verified `GET /ops/dashboard` exposed 38 clickable `data-method="GET"` anchors, 25 unique hrefs, and every unique href returned GET 200. POST-only draft preview remained non-clickable. This is not hosted deployment evidence, browser automation evidence, external reviewer feedback, or product-complete. See `docs/review/ops-dashboard-anchor-get-runtime-smoke.md`.

Phase 523 adds external reviewer ops dashboard anchor GET runtime request refresh v0: reviewer-facing repository paths now point to `docs/review/ops-dashboard-anchor-get-runtime-smoke.md` and `docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md`. This is request-surface refresh only, not a live issue body edit, hosted deployment evidence, browser automation evidence, external reviewer feedback, or product-complete.

Phase 524 adds external review issue body ops dashboard anchor GET runtime refresh v0: issue #1 now points reviewers to `docs/review/ops-dashboard-anchor-get-runtime-smoke.md`, `docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-ops-dashboard-anchor-get-runtime-refresh.md`. Observed `starts_with_request=true`, `first_codepoint=35`, `has_ops_dashboard_anchor_get_runtime_proof=true`, `has_ops_dashboard_anchor_get_request_refresh=true`, `has_all_extracted_dashboard_get_anchors_returned_200=true`, `has_post_only_draft_preview_not_clickable=true`, and `comment_count=1`. This is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, browser automation evidence, customer validation, or product-complete.

Phase 525 adds external feedback current-state ops dashboard anchor GET runtime issue verification v0: current issue #1 has the ops dashboard anchor GET runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending. See `docs/review/external-feedback-current-state-ops-dashboard-anchor-get-runtime-issue-verification.md`.

Phase 526 adds ops dashboard anchor browser smoke v0: local Playwright browser automation opened `GET /ops/dashboard`, captured `docs/review/media/ops-dashboard-anchor-browser-smoke.png`, and observed `browser_anchor_count=27`, `browser_get_anchor_count=27`, `browser_post_anchor_count=0`, `post_only_draft_preview_anchor_count=0`, `post_only_draft_preview_cue_visible=true`, and `all_browser_get_anchors_marked_get=true`. This is local browser automation evidence only, not hosted deployment evidence, external reviewer feedback, customer validation, design quality evidence, or product-complete. See `docs/review/ops-dashboard-anchor-browser-smoke.md`.

Phase 527 adds external reviewer ops dashboard anchor browser smoke request refresh v0: reviewer-facing repository paths now point to `docs/review/ops-dashboard-anchor-browser-smoke.md` and `docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md`. This is request-surface refresh only, not a live issue body edit, hosted deployment evidence, external reviewer feedback, customer validation, design quality evidence, or product-complete.

Phase 528 adds external review issue body ops dashboard anchor browser smoke refresh v0: issue #1 now points reviewers to `docs/review/ops-dashboard-anchor-browser-smoke.md`, `docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md`, and `docs/review/external-review-issue-body-ops-dashboard-anchor-browser-smoke-refresh.md`. Observed `starts_with_request=true`, `first_codepoint=35`, `has_ops_dashboard_anchor_browser_proof=true`, `has_ops_dashboard_anchor_browser_request_refresh=true`, `has_browser_anchor_count=true`, `has_browser_get_anchor_count=true`, `has_browser_post_anchor_count_zero=true`, `has_post_only_draft_preview_anchor_count_zero=true`, `has_post_only_draft_preview_cue_visible=true`, and `comment_count=1`. This is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, customer validation, design quality evidence, or product-complete.

Phase 529 adds external feedback current-state ops dashboard anchor browser smoke issue verification v0: `docs/review/external-feedback-current-state-ops-dashboard-anchor-browser-smoke-issue-verification.md` records the live issue #1 state after the browser proof issue-body refresh. Observed `starts_with_request=true`, `first_codepoint=35`, `has_ops_dashboard_anchor_browser_proof=true`, `has_ops_dashboard_anchor_browser_request_refresh=true`, `has_ops_dashboard_anchor_browser_issue_body_refresh=true`, `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, `classification=non_qualifying`, and `reason=self_authored_comment`. External reviewer feedback remains pending. This is current-state issue verification only, not external reviewer feedback, hosted deployment evidence, customer validation, design quality evidence, or product-complete.

Phase 530 adds workflow direct stage links v0: `db/migrations/023_workflow_stage_links.sql` creates `noise_gate_evidence_links`, `report_evidence_links`, and `report_noise_gate_links`; `POST /workflow-runs/execute-preview` records direct local stage links for workflow-created Evidence Ledger, Noise Gate, and Report records; `GET /workflow-runs/{id}/lineage` exposes them as `direct_stage_links` with `summary.direct_stage_link_count`. Boundary: workflow-created records only, standalone gate/report endpoints remain payload-only unless they create explicit stage links, not distributed tracing, not hosted observability, not autonomous workflow execution, and not product-complete. See `docs/review/workflow-direct-stage-links.md`.

Phase 531 adds workflow direct stage links runtime smoke v0: `docs/review/workflow-direct-stage-links-runtime-smoke.md` records local Docker PostgreSQL migration evidence for `023_workflow_stage_links.sql` and live FastAPI HTTP evidence that `POST /workflow-runs/execute-preview` followed by `GET /workflow-runs/{id}/lineage` returns `direct_stage_link_count=3`, link types `evidence_to_report`, `evidence_to_noise_gate`, and `noise_gate_to_report`, plus `direct_stage_link_table`. This is local runtime evidence only, not hosted deployment evidence, external reviewer feedback, distributed tracing, hosted observability, or product-complete.

Phase 532 adds external reviewer workflow direct stage links runtime request refresh v0: reviewer-facing repository paths now point to `docs/review/workflow-direct-stage-links-runtime-smoke.md` and `docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md`. This is request-surface refresh only, not a live issue body edit, runtime behavior, schema, migration, hosted deployment evidence, external reviewer feedback, distributed tracing, hosted observability, autonomous workflow execution, or product-complete.

Phase 533 adds external review issue body workflow direct stage links runtime refresh v0: issue #1 now points reviewers to `docs/review/workflow-direct-stage-links-runtime-smoke.md`, `docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-direct-stage-links-runtime-refresh.md`. Observed `starts_with_request=true`, `first_codepoint=35`, `has_workflow_direct_stage_links_runtime_proof=true`, `has_workflow_direct_stage_links_request_refresh=true`, `has_workflow_direct_stage_links_issue_body_refresh=true`, `has_direct_stage_link_count=true`, `has_evidence_to_report=true`, `has_evidence_to_noise_gate=true`, `has_noise_gate_to_report=true`, and `comment_count=1`. This is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, distributed tracing, hosted observability, autonomous workflow execution, customer validation, Braincrew acceptance, or product-complete.

Phase 534 adds external feedback current-state workflow direct stage links runtime issue verification v0: `docs/review/external-feedback-current-state-workflow-direct-stage-links-runtime-issue-verification.md` records the live issue #1 state after the direct stage links issue-body refresh. Observed `starts_with_request=true`, `first_codepoint=35`, `has_workflow_direct_stage_links_runtime_proof=true`, `has_workflow_direct_stage_links_request_refresh=true`, `has_workflow_direct_stage_links_issue_body_refresh=true`, `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, `classification=non_qualifying`, and `reason=self_authored_comment`. External reviewer feedback remains pending. This is current-state issue verification only, not external reviewer feedback, hosted deployment evidence, customer validation, Braincrew acceptance, or product-complete.

Phase 535 adds workflow stage event log v0: `db/migrations/024_workflow_stage_events.sql` creates `workflow_stage_events`; deterministic `POST /workflow-runs/execute-preview` records local stage events for retrieval, Evidence Ledger, Noise Gate, and Report; `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/proof-bundle` expose `stage_events` and `summary.workflow_stage_event_count`. Boundary: `local_workflow_stage_event_log_not_distributed_tracing`, not distributed tracing, not OpenTelemetry, not hosted observability, not autonomous workflow execution, and not product-complete. See `docs/review/workflow-stage-event-log.md`.

Phase 536 adds workflow stage event log runtime smoke v0: `docs/review/workflow-stage-event-log-runtime-smoke.md` records local Docker PostgreSQL evidence that `024_workflow_stage_events.sql` is applied with `Pending migrations: 0`, plus live FastAPI HTTP evidence that `POST /workflow-runs/execute-preview`, `GET /workflow-runs/{id}`, and `GET /workflow-runs/{id}/proof-bundle` return `detail_stage_event_count=4`, `bundle_stage_event_count=4`, stage names `retrieval,evidence_ledger,noise_gate,report`, and boundary `local_workflow_stage_event_log_not_distributed_tracing`. This is local runtime evidence only, not hosted deployment evidence, external reviewer feedback, distributed tracing, hosted observability, autonomous workflow execution, or product-complete.

Phase 537 adds external reviewer workflow stage event log runtime request refresh v0: reviewer-facing repository paths now point to `docs/review/workflow-stage-event-log-runtime-smoke.md` and `docs/review/external-reviewer-workflow-stage-event-log-runtime-request-refresh.md`. This is request-surface refresh only, not a live issue body edit, runtime behavior, schema, migration, hosted deployment evidence, external reviewer feedback, distributed tracing, hosted observability, autonomous workflow execution, or product-complete.

Phase 538 adds external review issue body workflow stage event log runtime refresh v0: issue #1 now points reviewers to `docs/review/workflow-stage-event-log-runtime-smoke.md`, `docs/review/external-reviewer-workflow-stage-event-log-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-stage-event-log-runtime-refresh.md`. Observed `starts_with_request=true`, `first_codepoint=35`, `has_workflow_stage_event_log_runtime_proof=true`, `has_workflow_stage_event_log_request_refresh=true`, `has_workflow_stage_event_log_issue_body_refresh=true`, `has_detail_stage_event_count=true`, `has_bundle_stage_event_count=true`, `has_stage_names=true`, `has_local_workflow_stage_event_log_boundary=true`, and `comment_count=1`. This is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, distributed tracing, hosted observability, autonomous workflow execution, customer validation, Braincrew acceptance, or product-complete.

Phase 539 adds external feedback current-state workflow stage event log runtime issue verification v0: `docs/review/external-feedback-current-state-workflow-stage-event-log-runtime-issue-verification.md` records the live issue #1 state after the stage event log issue-body refresh. Observed `starts_with_request=true`, `first_codepoint=35`, `has_workflow_stage_event_log_runtime_proof=true`, `has_workflow_stage_event_log_request_refresh=true`, `has_workflow_stage_event_log_issue_body_refresh=true`, `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, `classification=non_qualifying`, and `reason=self_authored_comment`. External reviewer feedback remains pending. This is current-state issue verification only, not external reviewer feedback, hosted deployment evidence, customer validation, Braincrew acceptance, or product-complete.

Phase 361 adds failure-case workflow review queue fresh-db dashboard smoke verification v0: `docs/review/failure-case-workflow-review-queue-fresh-db-dashboard-smoke-verification.md` records local fresh migrated Docker DB dashboard evidence for `GET /ops/dashboard` with `pending_review_count: 1`, `linked_failure_case_count: 1`, `needs_failure_case_review`, `failure_case_linked`, `dashboard_contains_draft_preview: true`, and `dashboard_did_not_create_failure_cases: true`. This is local runtime smoke evidence only; it is not hosted deployment evidence, external reviewer feedback, automatic failure-case creation, or complete workflow failure causality.

Phase 364 adds external review issue body workflow review queue proof index refresh v0: `docs/review/external-review-issue-body-workflow-review-queue-proof-index-refresh.md` records that GitHub issue #1 now links to the workflow review queue proof index and fresh DB dashboard smoke proof. Observed state: `has_workflow_review_queue_proof_index_link: true`, `has_workflow_review_queue_fresh_db_dashboard_smoke_link: true`, `comment_count: 1`, `candidate_count: 0`, and `self_authored_comment`. This is an owner-authored request-surface edit only and does not close external reviewer feedback v0.

Phase 365 adds external feedback current-state workflow review queue proof index issue verification v0: `docs/review/external-feedback-current-state-workflow-review-queue-proof-index-issue-verification.md` records the live issue #1 state after the proof-index issue-body refresh. Observed state: `starts_with_request: true`, `first_codepoint: 35`, `has_workflow_review_queue_proof_index_link: true`, `has_workflow_review_queue_fresh_db_dashboard_smoke_link: true`, `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and `self_authored_comment`. This is live request-surface evidence only and does not close external reviewer feedback v0.

Phase 366 adds uploaded raw file download endpoint review v0: `docs/review/uploaded-raw-file-download-endpoint-review.md` records the source-first decision that any future `GET /documents/upload-raw-files/{raw_file_id}/download` route must be scan-first, require the latest clean scan result, avoid storage-key exposure, and keep authorization boundary plus download rate limit explicit. This is review-only; it is not endpoint code, not a download endpoint, not malware scanning evidence, and not product-complete.

Phase 367 adds guarded raw file download endpoint v0: `GET /documents/upload-raw-files/{raw_file_id}/download` now returns raw bytes only when the latest scan result is `completed / clean`; missing scan evidence or a latest non-clean result returns `409` with `latest clean scan result required`. The response sets `X-Content-Type-Options: nosniff`, `X-NoiseProof-Download-Boundary: scan_first_latest_clean_result_required`, and `X-NoiseProof-Authorization-Boundary: local_v0_no_auth_not_production`. This is local API behavior only, not production malware scanning evidence, hosted deployment evidence, external reviewer feedback, production authorization, distributed rate limiting, or product-complete.

Phase 368 adds guarded raw file download endpoint runtime smoke v0: `docs/review/uploaded-raw-file-download-endpoint-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP evidence for upload -> no-scan download `409` -> clean scan metadata -> download `200` with `scan_first_latest_clean_result_required` and `local_v0_no_auth_not_production` headers -> later failed scan metadata -> download `409`. This is local runtime smoke only, not hosted deployment evidence, external reviewer feedback, production malware scanning evidence, production authorization, enforced rate limiting, or product-complete.

Phase 369 adds external reviewer guarded download request refresh v0: `docs/review/external-reviewer-guarded-download-request-refresh.md` updates reviewer-facing repository surfaces so `docs/review/uploaded-raw-file-download-endpoint-runtime-smoke.md` is visible from the proof path, review request, reviewer brief, link map, portfolio index, Braincrew role map, and application-ready review. This is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not production malware scanning evidence, and not product-complete.

Phase 370 adds external review issue body guarded download refresh v0: `docs/review/external-review-issue-body-guarded-download-refresh.md` records the owner-authored issue #1 body update that points reviewers to `docs/review/uploaded-raw-file-download-endpoint-runtime-smoke.md` and `docs/review/external-reviewer-guarded-download-request-refresh.md`. This is not external reviewer feedback, not hosted deployment evidence, not production malware scanning evidence, not production authorization, not enforced download rate limiting, and not product-complete.

Phase 371 adds external feedback current-state guarded download issue verification v0: `docs/review/external-feedback-current-state-guarded-download-issue-verification.md` records the live issue #1 state after the guarded download issue-body refresh. Observed state: `starts_with_request: true`, `first_codepoint: 35`, `has_guarded_download_proof: true`, `has_guarded_download_request_refresh: true`, `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and `self_authored_comment`. This is live request-surface evidence only and does not close external reviewer feedback v0.

Phase 372 adds uploaded raw file download rate limit review v0: `docs/review/uploaded-raw-file-download-rate-limit-review.md` records the source-first decision to keep production authorization separate and select a future local in-memory fixed-window rate limit for `GET /documents/upload-raw-files/{raw_file_id}/download`. This is review-only; it is not endpoint code, not an enforced rate limit, not production authorization, not hosted deployment evidence, and not product-complete.

Phase 373 adds uploaded raw file download rate limit local v0: `docs/review/uploaded-raw-file-download-rate-limit-local.md` records local API behavior for an in-memory fixed-window limit on `GET /documents/upload-raw-files/{raw_file_id}/download`: 5 attempts per 60 seconds per raw_file_id/client-host key, `429` when exceeded, no raw bytes in the 429 response, and `X-NoiseProof-Download-Rate-Limit-Boundary: local_v0_in_memory_fixed_window_not_production`. This is not distributed rate limiting, production authorization, hosted deployment evidence, or product-complete.

Phase 374 adds uploaded raw file download rate limit runtime smoke v0: `docs/review/uploaded-raw-file-download-rate-limit-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP evidence for guarded raw file download rate limiting: no-scan same-file attempts produce `[409, 409, 409, 409, 409]` then `429`, the 429 response has no raw bytes, and a separate clean file still downloads with `200`, `local_v0_in_memory_fixed_window_not_production`, `local_v0_no_auth_not_production`, and `nosniff`. This is not distributed rate limiting, production authorization, hosted deployment evidence, or product-complete.

Phase 375 adds external reviewer rate-limit request refresh v0: `docs/review/external-reviewer-rate-limit-request-refresh.md` updates reviewer-facing repository surfaces so `docs/review/uploaded-raw-file-download-rate-limit-runtime-smoke.md` is visible from the proof path, review request, reviewer brief, link map, portfolio index, Braincrew role map, and application-ready review. This is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not distributed rate limiting, not production authorization, and not product-complete.

Phase 376 adds external review issue body rate-limit refresh v0: `docs/review/external-review-issue-body-rate-limit-refresh.md` records the owner-authored issue #1 body update that points reviewers to `docs/review/uploaded-raw-file-download-rate-limit-runtime-smoke.md` and `docs/review/external-reviewer-rate-limit-request-refresh.md`. This is not external reviewer feedback, not hosted deployment evidence, not distributed rate limiting, not production authorization, not endpoint malicious-detection runtime proof, and not product-complete.

Phase 377 adds external feedback current-state rate-limit issue verification v0: `docs/review/external-feedback-current-state-rate-limit-issue-verification.md` records the live issue #1 state after the rate-limit issue-body refresh. Observed state: `starts_with_request: true`, `first_codepoint: 35`, `has_rate_limit_proof: true`, `has_rate_limit_request_refresh: true`, `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and `self_authored_comment`. This is live request-surface evidence only and does not close external reviewer feedback v0.

Phase 378 adds uploaded raw file signature validation review v0: `docs/review/uploaded-raw-file-signature-validation-review.md` records the source-first decision to keep upload file-type checks as a future local magic-prefix allowlist boundary. This is review-only; it is not endpoint code, not an enforced signature validator, not malware scanning evidence, not production authorization, and not product-complete.

Phase 379 adds uploaded raw file signature validation local v0: `docs/review/uploaded-raw-file-signature-validation-local.md` records local API behavior for a magic-prefix allowlist check before `POST /documents/upload-raw-files` persists bytes. It accepts CSV even when `Content-Type` says `application/pdf`, blocks declared PDF without a `%PDF-` prefix with `415`, and returns no raw bytes in the error detail. This is not robust file-type detection, malware scanning evidence, production authorization, hosted proof, or product-complete.

Phase 380 adds uploaded raw file signature validation runtime smoke v0: `docs/review/uploaded-raw-file-signature-validation-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP evidence for the local v0 signature check: spoofed CSV upload returns `201`, declared PDF mismatch returns `415`, the blocked response has no raw bytes, and the mismatch hash is not present in recent raw uploads. This is not robust file-type detection, malware scanning evidence, production authorization, hosted deployment evidence, or product-complete.

Phase 381 adds external reviewer signature-validation request refresh v0: `docs/review/external-reviewer-signature-validation-request-refresh.md` updates reviewer-facing repository surfaces so `docs/review/uploaded-raw-file-signature-validation-runtime-smoke.md` is visible from the proof path, review request, reviewer brief, link map, and portfolio index. This is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not robust file-type detection, not malware scanning evidence, and not production authorization.

Phase 382 adds external review issue body signature-validation refresh v0: `docs/review/external-review-issue-body-signature-validation-refresh.md` records the owner-authored issue #1 body update that points reviewers to `docs/review/uploaded-raw-file-signature-validation-runtime-smoke.md` and `docs/review/external-reviewer-signature-validation-request-refresh.md`. This is not external reviewer feedback, not hosted deployment evidence, not robust file-type detection, not malware scanning evidence, not production authorization, not endpoint malicious-detection runtime proof, and not product-complete.

Phase 383 adds external feedback current-state signature-validation issue verification v0: `docs/review/external-feedback-current-state-signature-validation-issue-verification.md` records the live issue #1 state after the signature-validation issue-body refresh. Observed state: `starts_with_request: true`, `first_codepoint: 35`, `has_signature_validation_proof: true`, `has_signature_validation_request_refresh: true`, `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and `self_authored_comment`. This is live request-surface evidence only and does not close external reviewer feedback v0.

Phase 384 adds uploaded raw file extension allowlist review v0: `docs/review/uploaded-raw-file-extension-allowlist-review.md` records a source-first decision to add a future local filename extension allowlist before raw upload persistence. The selected boundary is `local_v0_extension_allowlist_not_production`; this is review-only, not endpoint code, not an enforced extension validator, not robust file-type detection, not malware scanning evidence, and not production authorization.

Phase 385 adds uploaded raw file extension allowlist local v0: `docs/review/uploaded-raw-file-extension-allowlist-local.md` records local API behavior for extension validation before raw upload persistence. `POST /documents/upload-raw-files` records `extension_boundary: local_v0_extension_allowlist_not_production` on accepted CSV uploads and blocks `sample.exe.csv` as `suspicious double extension` with `415` and no raw bytes. This is local v0 endpoint code only, not robust file-type detection, malware scanning evidence, production authorization, hosted proof, or product-complete.

Phase 386 adds uploaded raw file extension allowlist runtime smoke v0: `docs/review/uploaded-raw-file-extension-allowlist-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP evidence for extension allowlisting: allowed CSV upload returns `201` with extension boundary warnings, `sample.exe.csv` returns `415` as `suspicious double extension`, raw bytes are absent from responses, and the blocked content hash is not present in recent raw uploads. This is not robust file-type detection, malware scanning evidence, production authorization, hosted deployment evidence, or product-complete.

Phase 387 adds external reviewer extension-allowlist request refresh v0: `docs/review/external-reviewer-extension-allowlist-request-refresh.md` updates reviewer-facing repository surfaces so `docs/review/uploaded-raw-file-extension-allowlist-runtime-smoke.md` is visible from the proof path, review request, reviewer brief, link map, and portfolio index. This is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not robust file-type detection, not malware scanning evidence, and not production authorization.

Phase 388 adds external review issue body extension-allowlist refresh v0: `docs/review/external-review-issue-body-extension-allowlist-refresh.md` records the owner-authored issue #1 body update that points reviewers to `docs/review/uploaded-raw-file-extension-allowlist-runtime-smoke.md` and `docs/review/external-reviewer-extension-allowlist-request-refresh.md`. This is not external reviewer feedback, not hosted deployment evidence, not robust file-type detection, not malware scanning evidence, not production authorization, not endpoint malicious-detection runtime proof, and not product-complete.

Phase 389 adds external feedback current-state extension-allowlist issue verification v0: `docs/review/external-feedback-current-state-extension-allowlist-issue-verification.md` records the live issue #1 state after the extension-allowlist issue-body refresh. Observed state: `starts_with_request: true`, `first_codepoint: 35`, `has_extension_allowlist_proof: true`, `has_extension_allowlist_request_refresh: true`, `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and `self_authored_comment`. This is live request-surface evidence only and does not close external reviewer feedback v0.

Phase 390 adds uploaded raw file download filename safety local v0: `docs/review/uploaded-raw-file-download-filename-safety-local.md` records local API behavior for guarded raw file download attachment filenames. `GET /documents/upload-raw-files/{raw_file_id}/download` now returns `X-NoiseProof-Download-Filename-Boundary: local_v0_content_disposition_filename_safety_not_production`; the filename helper URL-decodes metadata filenames, ignores path components, restricts characters to a conservative ASCII subset, caps names at 120 characters, preserves short extensions where possible, and falls back to `raw-file-<uuid>.bin` when normalization empties the candidate. This is local v0 endpoint behavior only, not production authorization, hosted proof, robust file serving, or product-complete.

Phase 391 adds uploaded raw file download filename safety runtime smoke v0: `docs/review/uploaded-raw-file-download-filename-safety-runtime-smoke.md` records local Docker FastAPI proof for a path-like, URL-encoded-control, overlong CSV filename flowing through upload -> manual clean scan metadata -> guarded download. Observed output includes `filename_boundary local_v0_content_disposition_filename_safety_not_production`, `safe_filename_length 120`, and safe checks for no path, no dotdot, no CRLF, no injected label, `.csv` suffix preserved, and `lte_120`. This is local runtime proof only, not production authorization, hosted proof, malware detection proof, or product-complete.

Phase 392 adds external reviewer filename-safety request refresh v0: `docs/review/external-reviewer-filename-safety-request-refresh.md` updates reviewer-facing repository surfaces so `docs/review/uploaded-raw-file-download-filename-safety-runtime-smoke.md` is visible from the proof path, review request, reviewer brief, link map, Braincrew role map, and portfolio index. This is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not production authorization, not malware detection proof, and not product-complete.

Phase 393 adds external review issue body filename-safety refresh v0: `docs/review/external-review-issue-body-filename-safety-refresh.md` records the owner-authored issue #1 body update that points reviewers to `docs/review/uploaded-raw-file-download-filename-safety-runtime-smoke.md` and `docs/review/external-reviewer-filename-safety-request-refresh.md`. Observed state: `starts_with_request: true`, `first_codepoint: 35`, `has_filename_safety_proof: true`, `has_filename_safety_request_refresh: true`, `comment_count: 1`, and labels `external-review,feedback`. This is not external reviewer feedback, not hosted deployment evidence, not production authorization, not malware detection proof, and not product-complete.

Phase 394 adds external feedback current-state filename-safety issue verification v0: `docs/review/external-feedback-current-state-filename-safety-issue-verification.md` records the live issue #1 state after the filename-safety issue-body refresh. Observed state: `starts_with_request: true`, `first_codepoint: 35`, `has_filename_safety_proof: true`, `has_filename_safety_request_refresh: true`, `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and `self_authored_comment`. This is live request-surface evidence only and does not close external reviewer feedback v0.

Phase 395 adds uploaded raw file download authorization audit review v0: `docs/review/uploaded-raw-file-download-authorization-audit-review.md` records a source-first decision to add `raw_file_download_events` before any production authorization claim. The planned event captures `raw_file_id`, `latest_scan_result_id`, `download_result`, `blocked_reason`, status, local v0 boundary strings, and metadata. This is review-only, not endpoint code, not schema, not user identity, not hosted deployment evidence, and not production authorization.

Phase 396 adds uploaded raw file download audit schema v0: `docs/review/uploaded-raw-file-download-audit-schema.md` records the local v0 audit table, repository methods, and `GET /documents/upload-raw-files/{raw_file_id}/download-events` inspectability surface. Guarded downloads now persist events for missing-scan 409, rate-limited 429, and allowed 200 paths. This is audit persistence only, not production authorization, not user identity, not hosted deployment evidence, and not product-complete.

Phase 397 adds uploaded raw file download audit runtime smoke v0: `docs/review/uploaded-raw-file-download-audit-runtime-smoke.md` records local Docker FastAPI plus PostgreSQL proof that `raw_file_download_events` are created and listed for missing-scan 409, rate-limited `[409, 409, 409, 409, 409, 429]`, and allowed 200 download decisions. The allowed event linked the latest clean scan result and preserved `audit-allowed.csv` as metadata. This is local runtime evidence only, not production authorization, not user identity, not hosted deployment evidence, not malware detection proof, and not product-complete.

Phase 398 adds external reviewer download-audit request refresh v0: `docs/review/external-reviewer-download-audit-request-refresh.md` updates reviewer-facing repository surfaces so `docs/review/uploaded-raw-file-download-audit-runtime-smoke.md` is visible from the proof path, review request, reviewer brief, link map, Braincrew role map, and portfolio index. This is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not production authorization, not user identity, not malware detection proof, and not product-complete.

Phase 399 adds external review issue body download-audit refresh v0: `docs/review/external-review-issue-body-download-audit-refresh.md` records the owner-authored issue #1 body update that points reviewers to `docs/review/uploaded-raw-file-download-audit-runtime-smoke.md` and `docs/review/external-reviewer-download-audit-request-refresh.md`. Observed state: `starts_with_request: true`, `first_codepoint: 35`, `has_download_audit_proof: true`, `has_download_audit_request_refresh: true`, `comment_count: 1`, and labels `external-review,feedback`. This is not external reviewer feedback, not hosted deployment evidence, not production authorization, not user identity, not malware detection proof, and not product-complete.

Phase 400 adds external feedback current-state download-audit issue verification v0: `docs/review/external-feedback-current-state-download-audit-issue-verification.md` records the live issue #1 state after the download-audit issue-body refresh. Observed state: `starts_with_request: true`, `first_codepoint: 35`, `has_download_audit_proof: true`, `has_download_audit_request_refresh: true`, `comment_count: 1`, `screened_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, and `self_authored_comment`. This is live request-surface evidence only and does not close external reviewer feedback v0.

Phase 401 adds uploaded raw file download authorization gate review v0: `docs/review/uploaded-raw-file-download-authorization-gate-review.md` uses OWASP Authorization, API1/BOLA, API5/BFLA, and File Upload guidance to choose a future local manual approval schema before any production authorization claim. Selected next gate: `uploaded raw file download approval schema v0` with planned `raw_file_download_approvals`; `approved_by_label` remains an operator-provided label, not authenticated user identity. This is review-only, not endpoint code, not schema, not production authorization, not user identity, not signed URL support, and not product-complete.

Phase 402 adds uploaded raw file download approval schema v0: `db/migrations/021_raw_file_download_approvals.sql`, `db/init/001_schema.sql`, and `docs/review/uploaded-raw-file-download-approval-schema.md` define `raw_file_download_approvals` as a local manual approval table. `approved_by_label` is an operator-provided label, not authenticated user identity. Download route behavior is unchanged. This is schema-only, not endpoint code, not repository code, not production authorization, not user identity, not signed URL support, and not product-complete.

Phase 403 adds uploaded raw file download approval schema runtime verification v0: `docs/review/uploaded-raw-file-download-approval-schema-runtime-verification.md` records local Docker DB evidence that migration `021_raw_file_download_approvals.sql` applied and migration runner status reached `Applied migrations: 20`, `Pending migrations: 0`. DB introspection observed 12 columns, 5 indexes, and 7 constraints on `raw_file_download_approvals`. This is schema verification only, not endpoint code, not repository code, not production authorization, not user identity, and not product-complete.

Phase 404 adds uploaded raw file download approval repository review v0: `docs/review/uploaded-raw-file-download-approval-repository-review.md` selects the next repository-only boundary for local manual approval rows: `RawFileDownloadApprovalCreate`, `RawFileDownloadApprovalOut`, `create_raw_file_download_approval`, and `list_raw_file_download_approvals`. `approved_by_label` remains an operator-provided label, not authenticated user identity. This is review-only, not repository code, not endpoint code, not download route behavior, not production authorization, not user identity, not signed URL support, and not product-complete.

Phase 405 adds uploaded raw file download approval repository v0: `docs/review/uploaded-raw-file-download-approval-repository.md` implements repository-only caller-provided manual approval row persistence with `RawFileDownloadApprovalCreate`, `RawFileDownloadApprovalOut`, `create_raw_file_download_approval`, and `list_raw_file_download_approvals`. `approved_by_label` remains an operator-provided label, not authenticated user identity. This is not endpoint code, not download route behavior, not production authorization, not user identity, not signed URL support, and not product-complete.

Phase 406 adds uploaded raw file download approval endpoint review v0: `docs/review/uploaded-raw-file-download-approval-endpoint-review.md` selects metadata-only create/list routes for manual approval rows: `POST /documents/upload-raw-files/{raw_file_id}/download-approvals` and `GET /documents/upload-raw-files/{raw_file_id}/download-approvals`. The future endpoint should reject path body raw_file_id mismatch. This is review-only, not endpoint code, not download route behavior, not approval enforcement, not production authorization, not user identity, not signed URL support, and not product-complete.

Phase 407 adds uploaded raw file download approval endpoint v0: `docs/review/uploaded-raw-file-download-approval-endpoint.md` implements metadata-only create/list routes for manual approval rows. The route rejects path/body mismatch and preserves local approval/identity boundary strings. Route tests also confirm the download route still requires latest clean scan result even when approval metadata exists. This is not approval enforcement, not production authorization, not user identity, not signed URL support, not hosted evidence, and not product-complete.

Phase 408 adds uploaded raw file download approval endpoint runtime smoke v0: `docs/review/uploaded-raw-file-download-approval-endpoint-runtime-smoke.md` records local Docker FastAPI plus PostgreSQL proof that approval metadata create/list works over HTTP. Observed flow: health `200`, upload `201`, scan metadata `201`, approval metadata `201`, approval list `200`, and raw download `409` because the latest scan verdict was `scan_error`. This proves approval metadata did not override latest clean scan guard. This is local runtime evidence only, not approval enforcement, not production authorization, not user identity, not signed URL support, not hosted evidence, and not product-complete.

Phase 409 adds uploaded raw file download approval gate behavior review v0: `docs/review/uploaded-raw-file-download-approval-gate-behavior-review.md` uses OWASP authorization and upload-security sources to choose a helper-first path before changing raw download route behavior. Selected next gate: `find_active_raw_file_download_approval`, with a future rule of latest clean scan and active approval. Future block reasons include `missing_download_approval` and `revoked_or_expired_download_approval`; future audit may record `download_approval_id in metadata_json` before adding a column. This is review-only, not route behavior, not approval enforcement, not production authorization, not user identity, and not product-complete.

Phase 410 adds uploaded raw file download approval helper v0: `docs/review/uploaded-raw-file-download-approval-helper.md` implements repository-only `find_active_raw_file_download_approval`. The helper returns one row matching raw file id, latest scan result id, `approval_status = approved`, `expires_at > now`, and `revoked_at IS NULL`. This is not route behavior, not approval enforcement, not production authorization, not user identity, and not product-complete.

Phase 411 adds uploaded raw file download approval gate behavior v0: `docs/review/uploaded-raw-file-download-approval-gate-behavior.md` wires `find_active_raw_file_download_approval` into the raw download route. Guarded raw downloads now require latest clean scan and active approval. Missing approval and expired/revoked approval attempts are blocked with `missing_download_approval` or `revoked_or_expired_download_approval`; allowed audit metadata records `download_approval_id`. This is local v0 route behavior, not production authorization, not user identity, not signed URL support, not hosted evidence, and not product-complete.

Phase 412 adds uploaded raw file download approval gate behavior runtime smoke v0: `docs/review/uploaded-raw-file-download-approval-gate-behavior-runtime-smoke.md` records local Docker FastAPI plus PostgreSQL proof that guarded raw downloads now block latest-clean-scan/no-approval attempts with `missing_download_approval`, block latest-clean-scan/non-active-approval attempts with `revoked_or_expired_download_approval`, and allow latest-clean-scan/active-approval downloads with `download_approval_id` in audit metadata. Migration runner applied `022_raw_file_download_event_approval_block_reasons.sql` and reached `Applied migrations: 21`, `Pending migrations: 0`. This is local runtime evidence only, not production authorization, not user identity, not signed URL support, not hosted evidence, and not product-complete.

Phase 413 adds external reviewer approval-gate request refresh v0: `docs/review/external-reviewer-approval-gate-request-refresh.md` makes the approval gate behavior runtime smoke discoverable from reviewer-facing repository paths, including the external-reader proof path, review request packet, reviewer brief, link map, Braincrew role map, and portfolio index. This is a request-surface refresh only, not a live issue body edit, not external reviewer feedback, not hosted evidence, not production authorization, not user identity, and not product-complete.

Phase 414 adds external review issue body approval-gate refresh v0: `docs/review/external-review-issue-body-approval-gate-refresh.md` records the owner-authored issue #1 body edit pointing reviewers to the approval gate behavior runtime smoke and request refresh. Observed markers: `starts_with_request=true`, `first_codepoint=35`, `has_approval_gate_proof=true`, `has_approval_gate_request_refresh=true`, and `comment_count=1`. This is a live request update only, not external reviewer feedback, not hosted evidence, not production authorization, not user identity, not signed URL support, and not product-complete.

Phase 415 adds external feedback current-state approval-gate issue verification v0: `docs/review/external-feedback-current-state-approval-gate-issue-verification.md` records the live issue #1 current state after the approval-gate issue-body refresh. The issue body has the approval proof and request-refresh links, but the only comment is owner-authored; screening produced `candidate_count=0`, acceptance drafting produced `draft_count=0`, and external reviewer feedback remains pending.

Phase 416 adds uploaded raw file download approval input guard v0: `docs/review/uploaded-raw-file-download-approval-input-guard.md` records local v0 API/model validation for manual approval metadata. `RawFileDownloadApprovalCreate` now rejects unknown `approval_status` values and rejects already expired `approved` approvals before they can become active approval rows; `RawFileDownloadApprovalOut` remains separate so historical expired approved rows can still be listed as audit records. Focused verification: `uv run pytest tests/test_routes.py -q -k "download_approval"` -> `5 passed, 134 deselected, 1 warning`. This is local input validation only, not production authorization, not authenticated user identity, not signed URL support, not hosted evidence, and not product-complete.

Phase 417 adds uploaded raw file download approval input guard runtime smoke v0: `docs/review/uploaded-raw-file-download-approval-input-guard-runtime-smoke.md` records local Docker FastAPI plus PostgreSQL evidence after rebuilding the API container. Observed: health `ok`, scan metadata `completed/clean`, valid approval status `approved`, approval list count `1`, unknown approval status `422`, and already expired active approval `422`. This is local runtime evidence only, not production authorization, not authenticated user identity, not signed URL support, not hosted evidence, and not product-complete.

Phase 418 adds external reviewer approval-input guard request refresh v0: `docs/review/external-reviewer-approval-input-guard-request-refresh.md` makes the approval input guard runtime smoke discoverable from reviewer-facing repository paths, including the external-reader proof path, review request packet, reviewer brief, link map, Braincrew role map, and portfolio index. This is request-surface refresh only, not a live issue body edit, not external reviewer feedback, not hosted evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

Phase 419 adds external review issue body approval-input guard refresh v0: `docs/review/external-review-issue-body-approval-input-guard-refresh.md` records the owner-authored issue #1 body edit pointing reviewers to the approval input guard runtime smoke and request refresh. Observed markers: `starts_with_request=true`, `first_codepoint=35`, `has_approval_input_guard_proof=true`, `has_approval_input_guard_request_refresh=true`, `has_unknown_status_422=true`, `has_expired_approved_422=true`, and `comment_count=1`. This is a live request update only, not external reviewer feedback, not hosted evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

Phase 420 adds external feedback current-state approval-input guard issue verification v0: `docs/review/external-feedback-current-state-approval-input-guard-issue-verification.md` records the live issue #1 current state after the approval-input guard issue-body refresh. The issue body has the approval input guard proof and request-refresh links, but the only comment is owner-authored; screening produced `candidate_count=0`, acceptance drafting produced `draft_count=0`, and external reviewer feedback remains pending.

Phase 421 adds uploaded raw file download approval audit metadata v0: `docs/review/uploaded-raw-file-download-approval-audit-metadata.md` records local v0 allowed download audit metadata enrichment. Allowed raw file download events now include `approval_status`, `approval_expires_at`, `approval_latest_scan_result_id`, and `approval_scan_result_matches_latest` in addition to the approval id, approval boundary, identity boundary, and operator label. This is local audit metadata only, not production authorization, not authenticated user identity, not signed URL support, not hosted evidence, and not product-complete.

Phase 422 adds uploaded raw file download approval audit metadata runtime smoke v0: `docs/review/uploaded-raw-file-download-approval-audit-metadata-runtime-smoke.md` records local Docker FastAPI plus PostgreSQL evidence after rebuilding the API container. Observed: health `ok`, clean scan metadata, active approval `approved`, download `200`, allowed event `200`, approval id match, approval status `approved`, approval expiry present, approval latest scan result id match, approval scan-result match `true`, and identity boundary `operator_label_not_authenticated_identity`. This is local runtime evidence only, not production authorization, not authenticated user identity, not signed URL support, not hosted evidence, and not product-complete.

Phase 423 adds external reviewer approval-audit-metadata request refresh v0: `docs/review/external-reviewer-approval-audit-metadata-request-refresh.md` makes the approval audit metadata runtime smoke discoverable from reviewer-facing repository paths, including the external-reader proof path, review request packet, reviewer brief, link map, Braincrew role map, and portfolio index. This is request-surface refresh only, not a live issue body edit, not external reviewer feedback, not hosted evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

Phase 424 adds external review issue body approval-audit-metadata refresh v0: `docs/review/external-review-issue-body-approval-audit-metadata-refresh.md` records the owner-authored issue #1 body edit pointing reviewers to the approval audit metadata runtime smoke and request refresh. Observed markers: `starts_with_request=true`, `first_codepoint=35`, `has_approval_audit_metadata_proof=true`, `has_approval_audit_metadata_request_refresh=true`, `has_event_download_approval_id_matches=true`, `has_event_approval_scan_result_matches_latest=true`, and `comment_count=1`. This is a live request update only, not external reviewer feedback, not hosted evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

Phase 425 adds external feedback current-state approval-audit-metadata issue verification v0: `docs/review/external-feedback-current-state-approval-audit-metadata-issue-verification.md` records the live issue #1 current state after the approval-audit-metadata issue-body refresh. The issue body has the approval audit metadata proof and request-refresh links, but the only comment is owner-authored; screening produced `candidate_count=0`, acceptance drafting produced `draft_count=0`, and external reviewer feedback remains pending.

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
- parser adapter stubs for markdown, CSV, HTML/URL, PDF text-only fallback, unknown source types, and Phase 340 uploaded PDF text extraction
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
- Workflow Direct Stage Links v0
- `db/migrations/023_workflow_stage_links.sql`
- `noise_gate_evidence_links`, `report_evidence_links`, and `report_noise_gate_links`
- `GET /workflow-runs/{id}/lineage` now exposes `direct_stage_links`
- direct local stage links are recorded for workflow-created records only
- standalone gate/report endpoints remain payload-only unless they create explicit stage links
- Workflow Lineage Read Model v0
- `GET /workflow-runs/{id}/lineage`
- derived read model over existing workflow child records, `stage_input_manifest`, and direct workflow stage link rows
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
- workflow direct stage links now exist for workflow-created records only
- standalone gate/report endpoints remain payload-only unless they create explicit stage links
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

- raw upload quarantine storage exists; download endpoint and malware scanning do not
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
    "Embedding generation, semantic retrieval quality evidence, distributed tracing, and final report generation beyond deterministic previews are still not implemented."
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

JSON PDF parse-preview still accepts already-extracted text through the text-only fallback. Upload-preview can extract digital PDF text with PyMuPDF from uploaded PDF bytes. Robust PDF extraction is not claimed.

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

Export a persisted Report record as deterministic Markdown:

```bash
curl http://localhost:8000/reports/<report_record_id>/markdown
```

Expected Markdown markers:

```text
# Claim-bounded Report
Report record id: <report_record_id>
Status: generated
Boundary: This markdown export is deterministic.
Claim: Enterprise demand grew
Sources: doc-demand
Evidence: Enterprise demand grew 12% in 2026.
```

Unknown ids return `404` with `Report record not found`. This export reads an existing `report_records` row; it does not generate new claims, call an LLM, run retrieval, create Evidence Ledger rows, create Report records, provide financial advice, or implement free-form reports.
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

Phase marker: uploaded file intake manifest persistence runtime smoke v0.

Observed local smoke path:

```text
docker compose config
docker compose up -d db
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8032
POST /documents/upload-intake-manifests
GET /documents/upload-intake-manifests
```

Observed result:

```text
Applied migrations: 11
Pending migrations: 0
manifest row persisted with manifest_only_no_raw_file_storage
storage_decision = do_not_persist_raw_upload_yet
replayable = false
```

This is local runtime evidence, not hosted deployment evidence. The next product gate is `uploaded file intake manifest persistence application refresh v0`.

Phase marker: uploaded file intake manifest persistence application refresh v0.

Application-facing refresh:

```text
docs/review/uploaded-file-intake-manifest-persistence-application-refresh.md
```

This refresh points reviewer-facing artifacts to the local runtime smoke for `POST /documents/upload-intake-manifests` and `GET /documents/upload-intake-manifests`. It keeps `manifest_only_no_raw_file_storage` and `do_not_persist_raw_upload_yet` explicit. It is not hosted deployment evidence, not external reviewer feedback, not Braincrew acceptance, and not raw file storage.

Phase marker: external reviewer upload-manifest persistence request refresh v0.

Use `docs/review/external-reviewer-upload-manifest-persistence-request-refresh.md` when checking why the reviewer request path now points to uploaded-file intake manifest persistence proof.

This is request infrastructure only. It does not update the live public issue body and is not external reviewer feedback. The next request gate is `external reviewer upload-manifest persistence issue-body refresh v0`.

Phase marker: external reviewer upload-manifest persistence issue-body refresh v0.

Use `docs/review/external-review-issue-body-upload-manifest-persistence-refresh.md` when checking the live issue #1 body update that points reviewers to uploaded-file intake manifest persistence proof.

Observed live issue markers:

```text
first_codepoint=35
uploaded-file intake manifest persistence proof
docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md
manifest_only_no_raw_file_storage
```

This is an owner-authored issue edit, not external reviewer feedback.

Phase marker: uploaded file parsed document persistence v0.

Use `POST /documents/upload-parsed-documents` to persist uploaded-file document metadata and parser/profile output into the existing `documents` table without storing raw uploaded bytes or parsed text.

Endpoint smoke command:

```bash
curl -F "source_type=markdown" -F "title=Uploaded market note" -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown" http://localhost:8000/documents/upload-parsed-documents
curl http://localhost:8000/documents
```

Expected boundary:

```text
status = parsed_metadata_only
persistence_boundary = document_metadata_and_profile_only_no_raw_file_storage
raw_file_storage = false
parsed_text_storage = false
```

This endpoint creates a `documents` row with upload filename, source URI, parser name, parser metadata, profile summary, parse warnings, and upload byte count. It does not store raw uploaded bytes, does not persist parsed text, does not create chunks, does not create retrieval runs, does not generate Evidence Ledger entries, and does not claim robust PDF extraction.

Phase marker: uploaded file parsed document persistence runtime smoke v0.

Observed local smoke path:

```text
docker compose config
docker compose up -d db
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8033
GET /health
POST /documents/upload-parsed-documents
GET /documents
docker compose down
```

Observed result:

```text
Applied migrations: 11
Pending migrations: 0
POST /documents/upload-parsed-documents -> 201
GET /documents -> 200
status -> parsed_metadata_only
persistence_boundary -> document_metadata_and_profile_only_no_raw_file_storage
raw_file_storage -> false
parsed_text_storage -> false
```

This is local runtime evidence, not hosted deployment evidence, not external reviewer feedback, not Braincrew acceptance, and not raw file storage.

Phase marker: uploaded file parsed document persistence application refresh v0.

Application-facing refresh:

```text
docs/review/uploaded-file-parsed-document-persistence-application-refresh.md
```

This refresh points README, GOAL, runbook, portfolio index, Braincrew role map, and application-ready review surfaces to `docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md`. It is not hosted deployment evidence, not external reviewer feedback, not Braincrew acceptance, not robust PDF extraction, not raw file storage, and not parsed text persistence.

Phase marker: external reviewer parsed-document persistence request refresh v0.

Use `docs/review/external-reviewer-parsed-document-persistence-request-refresh.md` when checking why the reviewer request path now points to uploaded-file parsed document persistence proof.

This is request infrastructure only. It does not update the live public issue body and is not external reviewer feedback. The next request gate is `external reviewer parsed-document persistence issue-body refresh v0`.

## External reviewer parsed-document persistence issue-body refresh

Phase marker: external reviewer parsed-document persistence issue-body refresh v0.

This is an owner-authored live public issue #1 body update. It points reviewers to uploaded-file parsed document persistence proof while keeping the external reviewer feedback gate open.

Verification artifact:

```text
docs/review/external-review-issue-body-parsed-document-persistence-refresh.md
```

Boundary:

```text
not external reviewer feedback
not raw file storage
not hosted deployment evidence
not parsed text persistence
```

## Uploaded file chunk persistence review

Phase marker: uploaded file chunk persistence review v0.

Use `docs/review/uploaded-file-chunk-persistence-review.md` before adding chunk persistence schema. This is review-only and selects `document_chunks` as the next candidate persistence boundary.

Current boundary:

```text
no migration
no endpoint
no raw file storage
not full parsed text persistence
no embeddings
```

Next bounded product gate:

```text
uploaded file chunk persistence schema v0
```

## Uploaded file chunk persistence schema

Phase marker: uploaded file chunk persistence schema v0.

Schema files:

```text
db/init/001_schema.sql
db/migrations/013_document_chunks.sql
```

This creates `document_chunks` with `document_id`, `chunk_strategy`, `chunk_index`, `chunk_text`, `metadata_json`, and `persistence_boundary = chunk_text_only_no_raw_file_storage`.

Current boundary:

```text
schema-only
no endpoint
no repository code
no chunk rows
no embeddings
not raw file storage
not full parsed text persistence
```

Next bounded product gate:

```text
uploaded file chunk persistence repository review v0
```

## Uploaded file chunk persistence repository review

Phase marker: uploaded file chunk persistence repository review v0.

Use `docs/review/uploaded-file-chunk-persistence-repository-review.md` before adding repository code for `document_chunks`.

Selected boundary:

```text
DocumentChunkCreate
create_document_chunk(payload)
list_document_chunks(document_id, limit)
```

Current boundary:

```text
review-only
no repository code
no endpoint
no chunk rows
no embeddings
```

Next bounded product gate:

```text
uploaded file chunk persistence repository v0
```

## Uploaded file chunk persistence repository

Phase marker: uploaded file chunk persistence repository v0.

Repository surface:

```text
DocumentChunkCreate
create_document_chunk(payload)
list_document_chunks(document_id, limit)
```

Boundary:

```text
no endpoint
not automatic persistence from upload preview
no embeddings
no retrieval persistence
not raw file storage
not full parsed text persistence
```

Next bounded product gate:

```text
uploaded file chunk persistence endpoint review v0
```

## Uploaded file chunk persistence endpoint review

Phase marker: uploaded file chunk persistence endpoint review v0.

Use `docs/review/uploaded-file-chunk-persistence-endpoint-review.md` before adding route code for persisted document chunks.

Selected endpoint boundary:

```text
POST /documents/{document_id}/chunks
GET /documents/{document_id}/chunks
```

Selected repository calls:

```text
DocumentChunkCreate
DocumentChunkOut
create_document_chunk(payload)
list_document_chunks(document_id, limit)
```

Boundary:

```text
review-only
no endpoint code
not automatic persistence from upload preview
no embeddings
no retrieval persistence
not raw file storage
not full parsed text persistence
```

Next bounded product gate:

```text
uploaded file chunk persistence endpoint v0
```

## Uploaded file chunk persistence endpoint

Phase marker: uploaded file chunk persistence endpoint v0.

Persist one derived chunk row for an existing document:

```bash
curl -X POST http://localhost:8000/documents/{document_id}/chunks \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"source_uri\":\"upload://sample.md\",\"filename\":\"sample.md\",\"chunk_strategy\":\"fixed-window\",\"chunk_index\":0,\"chunk_text\":\"Revenue increased in Q1.\",\"character_start\":0,\"character_end\":24,\"metadata_json\":{\"strategy\":\"fixed-window\"}}"
```

List persisted chunks for a document:

```bash
curl http://localhost:8000/documents/{document_id}/chunks
```

Boundary:

```text
persistence_boundary = chunk_text_only_no_raw_file_storage
not automatic persistence from upload preview
no embeddings
no retrieval persistence
not raw file storage
not full parsed text persistence
```

Next bounded product gate:

```text
uploaded file chunk persistence runtime smoke v0
```

## Uploaded file chunk persistence runtime smoke

Phase marker: uploaded file chunk persistence runtime smoke v0.

Observed local runtime evidence:

```text
Applied migrations: 12
Pending migrations: 0
POST /documents/{document_id}/chunks -> persisted chunk_text_only_no_raw_file_storage
GET /documents/{document_id}/chunks -> chunk_count 1
POST /documents/upload-chunk-preview -> preview_only_not_persisted
chunk_count_after_upload_preview -> 1
document_chunk_count -> 1
```

Artifact:

```text
docs/review/uploaded-file-chunk-persistence-runtime-smoke.md
```

Boundary:

```text
not automatic persistence from upload preview
no embeddings
no retrieval persistence
not raw file storage
not full parsed text persistence
```

Next bounded product gate:

```text
uploaded file chunk persistence application refresh v0
```

## Uploaded file chunk persistence application refresh

Phase marker: uploaded file chunk persistence application refresh v0.

Application-facing artifact:

```text
docs/review/uploaded-file-chunk-persistence-application-refresh.md
```

This refresh surfaces the local runtime smoke for explicit document-scoped chunk persistence in README, GOAL, runbook, portfolio, Braincrew role map, and application-ready review.

Allowed claim:

```text
local Docker DB plus FastAPI HTTP evidence exists for manual document-scoped chunk persistence through POST /documents/{document_id}/chunks and GET /documents/{document_id}/chunks
```

Boundary:

```text
not automatic persistence from upload preview
not hosted deployment evidence
not external reviewer feedback
not product-complete
no embeddings
no retrieval persistence
```

Next bounded request gate:

```text
external reviewer chunk persistence request refresh v0
```

## External reviewer chunk persistence request refresh

Phase marker: external reviewer chunk persistence request refresh v0.

Use `docs/review/external-reviewer-chunk-persistence-request-refresh.md` when checking why the reviewer request path now points to uploaded-file chunk persistence proof.

Reviewer proof path:

```text
docs/review/uploaded-file-chunk-persistence-runtime-smoke.md
docs/review/uploaded-file-chunk-persistence-application-refresh.md
```

This is request infrastructure only. It does not update the live public issue body and is not external reviewer feedback. The next request gate is `external reviewer chunk persistence issue-body refresh v0`.

Boundary:

```text
not automatic persistence from upload preview
not hosted deployment evidence
not external reviewer feedback
no retrieval persistence
no embeddings
```

## External reviewer chunk persistence issue-body refresh

Phase marker: external reviewer chunk persistence issue-body refresh v0.

This is an owner-authored live public issue #1 body update. It points reviewers to uploaded-file chunk persistence proof while keeping the external reviewer feedback gate open.

Verification artifact:

```text
docs/review/external-review-issue-body-chunk-persistence-refresh.md
```

Observed live markers:

```text
first_codepoint -> 35
uploaded-file chunk persistence proof -> present
9. uploaded-file chunk persistence proof -> present
not automatic persistence from upload preview -> present
```

Boundary:

```text
not external reviewer feedback
not automatic persistence from upload preview
not hosted deployment evidence
no retrieval persistence
no embeddings
```

## External feedback current-state chunk issue verification

Phase marker: external feedback current-state chunk issue verification v0.

Use `docs/review/external-feedback-current-state-chunk-issue-verification.md` when checking the live issue #1 feedback state after the uploaded-file chunk persistence issue-body refresh.

Observed current-state screen:

```text
comment_count: 1
candidate_count: 0
draft_count: 0
self_authored_comment
```

Boundary:

```text
not external reviewer feedback
does not close external reviewer feedback v0
not customer validation
not Braincrew acceptance
not hosted deployment evidence
```

## Uploaded Raw File Storage

Phase 247 adds uploaded raw file storage v0 as a quarantine-only raw upload persistence boundary.

The phase marker is:

```text
uploaded raw file storage v0
```

Review artifact:

```text
docs/review/uploaded-raw-file-storage.md
```

API:

```text
POST /documents/upload-raw-files
GET /documents/upload-raw-files
```

Fresh schema and migration:

```text
db/init/001_schema.sql
db/migrations/016_uploaded_raw_files.sql
uploaded_raw_files
```

Persistence boundary:

```text
raw_upload_quarantine_db_bytea_no_download_endpoint
```

Local smoke shape:

```powershell
curl.exe -s -X POST "http://127.0.0.1:8000/documents/upload-raw-files" `
  -F "source_type=csv" `
  -F "file=@.\examples\messy-market-data\sample-market.csv;type=text/csv"

curl.exe -s "http://127.0.0.1:8000/documents/upload-raw-files"
```

Test command:

```bash
cd apps/api
uv run pytest tests/test_routes.py -q -k "upload_raw_file"
```

Expected route-test result:

```text
2 passed
```

Behavior checked:

```text
raw bytes are persisted in PostgreSQL BYTEA
response metadata exposes content hash, size, and internal storage_key
raw_bytes are not returned by POST or GET responses
original filename is recorded as metadata only and is not used as a storage key
oversized uploads over max_raw_upload_bytes are rejected with 413
```

Claim boundary:

```text
not malware scanning
not download endpoint
not robust PDF extraction
not parser quality evidence
not semantic retrieval evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Uploaded Raw File Storage Runtime Smoke

Phase 248 records uploaded raw file storage runtime smoke v0.

Use this proof artifact:

```text
docs/review/uploaded-raw-file-storage-runtime-smoke.md
```

Observed local runtime path:

```text
docker compose config
docker compose up -d db
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run uvicorn app.main:create_app --factory --host 127.0.0.1 --port 8048
GET /health
POST /documents/upload-raw-files
GET /documents/upload-raw-files
oversized upload -> 413
```

Observed result:

```text
db status -> healthy
Applied migrations: 15
Pending migrations: 0
post_status -> stored_quarantined
boundary -> raw_upload_quarantine_db_bytea_no_download_endpoint
backend -> postgres_bytea
response_has_raw_bytes -> false
storage_key_contains_filename -> false
oversized upload -> 413
```

Boundary:

```text
local runtime evidence only
not hosted deployment evidence
not external reviewer feedback
not malware scanning
not a download endpoint
not robust PDF extraction
not parser quality evidence
not semantic retrieval evidence
not Evidence Ledger generation
not product-complete
```

## Uploaded Raw File Storage Application Refresh

Phase marker: uploaded raw file storage application refresh v0.

Use this refresh artifact:

```text
docs/review/uploaded-raw-file-storage-application-refresh.md
```

Primary runtime proof:

```text
docs/review/uploaded-raw-file-storage-runtime-smoke.md
```

Application-facing surfaces updated:

```text
README.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
docs/application/braincrew-role-map.md
docs/review/application-ready-review.md
```

Boundary:

```text
documentation/application refresh only
not hosted deployment evidence
not external reviewer feedback
not malware scanning
not a download endpoint
not robust PDF extraction
not product-complete
```

## External Reviewer Raw File Storage Request Refresh

Phase marker: external reviewer raw file storage request refresh v0.

Use this refresh artifact:

```text
docs/review/external-reviewer-raw-file-storage-request-refresh.md
```

Reviewer-facing proof target:

```text
docs/review/uploaded-raw-file-storage-runtime-smoke.md
docs/review/uploaded-raw-file-storage-application-refresh.md
```

This request refresh points external reviewer surfaces to the uploaded raw file storage proof for:

```text
POST /documents/upload-raw-files
GET /documents/upload-raw-files
raw_upload_quarantine_db_bytea_no_download_endpoint
```

Boundary:

```text
not external reviewer feedback
not hosted deployment evidence
not malware scanning
not a download endpoint
not live issue-body verification
```

## External Review Issue Body Raw File Storage Refresh

Phase marker: external review issue body raw file storage refresh v0.

Use this refresh artifact:

```text
docs/review/external-review-issue-body-raw-file-storage-refresh.md
```

Public issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed live issue markers after owner-authored edit:

```text
updatedAt: 2026-06-02T23:57:53Z
first_codepoint: 35
startsWith: ## Request
has_raw_proof: true
has_runtime_link: true
has_request_refresh_link: true
has_no_malware_scanning: true
has_no_download_endpoint: true
has_old_global_raw_negation: false
comment_count: 1
owner_comment_count: 1
```

Boundary:

```text
owner-authored issue edit only
not external reviewer feedback
not hosted deployment evidence
not malware scanning
not a download endpoint
does not close external reviewer feedback v0
```

## External Feedback Current-state Raw File Storage Issue Verification

Phase marker: external feedback current-state raw file storage issue verification v0.

Use this current-state verification artifact:

```text
docs/review/external-feedback-current-state-raw-file-storage-issue-verification.md
```

Observed issue and screener markers:

```text
updatedAt: 2026-06-02T23:57:53Z
first_codepoint: 35
startsWith: ## Request
comment_count: 1
owner_comment_count: 1
candidate_count: 0
draft_count: 0
self_authored_comment
non_qualifying
```

Screening commands:

```powershell
$env:PYTHONPATH='.'
python -m packages.review.external_feedback_cli --input <issue.json> --repository-owner svy04
python -m packages.review.external_feedback_acceptance_cli --input <screen.json>
```

Boundary:

```text
current-state screen only
not external reviewer feedback
not hosted deployment evidence
not malware scanning
not a download endpoint
does not close external reviewer feedback v0
```

## Uploaded Raw File Storage Safety Review

Phase marker: uploaded raw file storage safety review v0.

Use this source-first review artifact:

```text
docs/review/uploaded-raw-file-storage-safety-review.md
```

Current decision:

```text
quarantine-only raw storage remains
do not add a download endpoint yet
uploaded raw file scan result schema review v0
```

Source basis:

```text
OWASP File Upload Cheat Sheet
OWASP Unrestricted File Upload
ClamAV Scanning
FastAPI Request Files
```

Missing before download:

```text
allowed extension and type policy
file signature validation
malware scan verdict
retention and deletion policy
download authorization policy
```

Boundary:

```text
review-only
not malware scanning
not a download endpoint
not hosted deployment evidence
not ClamAV integration
```

## Uploaded Raw File Scan Result Schema Review

Phase marker: uploaded raw file scan result schema review v0.

Use this review artifact:

```text
docs/review/uploaded-raw-file-scan-result-schema-review.md
```

Selected future table:

```text
raw_file_scan_results
```

Selected future link:

```text
raw_file_id -> uploaded_raw_files(id)
```

Required future columns:

```text
scanner_name
scanner_version
signature_db_version
scan_started_at
scan_finished_at
scan_status
scan_verdict
matched_signature
error_message
metadata_json
```

Selected next gate:

```text
uploaded raw file scan result schema v0
```

Boundary:

```text
review-only
not malware scanning
not runtime evidence
not a download endpoint
not ClamAV integration
not schema migration yet
```

## Uploaded Raw File Scan Result Schema

Phase marker: uploaded raw file scan result schema v0.

Use this schema artifact:

```text
docs/review/uploaded-raw-file-scan-result-schema.md
```

Schema files:

```text
db/init/001_schema.sql
db/migrations/017_raw_file_scan_results.sql
```

Added table:

```text
raw_file_scan_results
```

Parent link:

```text
raw_file_id -> uploaded_raw_files(id)
```

Status vocabulary:

```text
pending
running
completed
failed
skipped
```

Verdict vocabulary:

```text
pending
clean
suspicious
infected
scan_error
skipped
```

Important boundary:

```text
scan_error is not clean
```

Selected next gate:

```text
uploaded raw file scan result repository review v0
```

Boundary:

```text
schema-only
not malware scanning
not scanner execution
not ClamAV integration
not a download endpoint
not runtime evidence
```

## Uploaded Raw File Scan Result Repository Review

Phase marker: uploaded raw file scan result repository review v0.

Use this review artifact:

```text
docs/review/uploaded-raw-file-scan-result-repository-review.md
```

Selected repository surface:

```text
RawFileScanResultCreate
create_raw_file_scan_result
list_raw_file_scan_results
```

Persistence target:

```text
raw_file_scan_results
```

Parent table:

```text
uploaded_raw_files
```

Selected filters:

```text
raw_file_id
scan_status
scan_verdict
limit
```

Important boundary:

```text
scan_error is not clean
do not run scanners in repository code
do not add an endpoint in this gate
```

Selected next gate:

```text
uploaded raw file scan result repository v0
```

Boundary:

```text
review-only
not repository code
not malware scanning
not scanner execution
not ClamAV integration
not a download endpoint
not runtime evidence
```

## Uploaded Raw File Scan Result Repository

Phase marker: uploaded raw file scan result repository v0.

Use this artifact:

```text
docs/review/uploaded-raw-file-scan-result-repository.md
```

Added code:

```text
RawFileScanResultCreate
RawFileScanResultOut
create_raw_file_scan_result
list_raw_file_scan_results
```

Persistence target:

```text
raw_file_scan_results
```

Filters:

```text
raw_file_id
scan_status
scan_verdict
limit
```

Important boundary:

```text
scan_error is not clean
repository code does not run scanners
repository code does not expose raw uploaded bytes
```

Selected next gate:

```text
uploaded raw file scan result endpoint review v0
```

Boundary:

```text
repository code only
not endpoint code
not malware scanning
not scanner execution
not ClamAV integration
not a download endpoint
not runtime evidence
```

## Uploaded Raw File Scan Result Endpoint Review

Phase marker: uploaded raw file scan result endpoint review v0.

Use this review artifact:

```text
docs/review/uploaded-raw-file-scan-result-endpoint-review.md
```

Selected routes:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan-results
GET /documents/upload-raw-files/{raw_file_id}/scan-results
```

Selected route behavior:

```text
metadata-only
path raw_file_id is authoritative parent id
POST calls create_raw_file_scan_result
GET calls list_raw_file_scan_results
```

Important boundary:

```text
scan_error is not clean
do not run scanners in endpoint code
do not add a download endpoint in this gate
```

Selected next gate:

```text
uploaded raw file scan result endpoint v0
```

Boundary:

```text
review-only
not endpoint code
not malware scanning
not scanner execution
not ClamAV integration
not a download endpoint
not runtime evidence
```

## Uploaded Raw File Scan Result Endpoint

Phase marker: uploaded raw file scan result endpoint v0.

Use this artifact:

```text
docs/review/uploaded-raw-file-scan-result-endpoint.md
```

Routes:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan-results
GET /documents/upload-raw-files/{raw_file_id}/scan-results
```

Expected behavior:

```text
POST stores caller-provided scan result metadata
GET lists scan result metadata for one raw_file_id
path/body raw_file_id mismatch returns 400
responses exclude raw_bytes
responses exclude download_url
```

Important boundary:

```text
scan_error is not clean
endpoint does not run scanners
endpoint does not expose raw uploaded bytes
```

Selected next gate:

```text
uploaded raw file scan result endpoint runtime smoke v0
```

Boundary:

```text
endpoint code only
metadata-only scan result persistence
not malware scanning
not scanner execution
not ClamAV integration
not a download endpoint
not runtime evidence
```

## Uploaded Raw File Scan Result Endpoint Runtime Smoke

Phase marker: uploaded raw file scan result endpoint runtime smoke v0.

Use this artifact:

```text
docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md
```

Runtime environment:

```text
Docker version 29.4.3
Docker Compose version v5.1.3
FastAPI on http://127.0.0.1:8033
```

Observed migration state:

```text
Applied migrations: 16
Pending migrations: 0
```

Observed HTTP checks:

```text
GET /health -> 200
POST /documents/upload-raw-files -> 201
POST /documents/upload-raw-files/{raw_file_id}/scan-results -> 201
GET /documents/upload-raw-files/{raw_file_id}/scan-results -> 200
path/body mismatch -> 400
```

Observed response boundary:

```text
scan_verdict -> scan_error
response_has_raw_bytes -> false
download_url_present -> false
```

Selected next gate:

```text
external reviewer scan-result endpoint request refresh v0
```

Boundary:

```text
local runtime smoke only
not malware scanning
not scanner execution
not ClamAV integration
not a download endpoint
not hosted deployment evidence
```

## External Reviewer Scan-result Endpoint Request Refresh

Phase marker: external reviewer scan-result endpoint request refresh v0.

Use this artifact:

```text
docs/review/external-reviewer-scan-result-endpoint-request-refresh.md
```

Reviewer-facing proof:

```text
uploaded raw file scan result endpoint proof
docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md
POST /documents/upload-raw-files/{raw_file_id}/scan-results
GET /documents/upload-raw-files/{raw_file_id}/scan-results
scan_verdict -> scan_error
response_has_raw_bytes -> false
```

Updated request surfaces:

```text
CONTRIBUTING.md
.github/ISSUE_TEMPLATE/external-review-feedback.md
docs/review/external-review-request.md
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
```

Selected next gate:

```text
external review issue body scan-result endpoint refresh v0
```

Boundary:

```text
request infrastructure only
not external reviewer feedback
not hosted deployment evidence
not malware scanning
not a download endpoint
```

## External Review Issue Body Scan-result Endpoint Refresh

Phase marker: external review issue body scan-result endpoint refresh v0.

Use this refresh artifact:

```text
docs/review/external-review-issue-body-scan-result-endpoint-refresh.md
```

Public issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed live issue markers:

```text
first_codepoint: 35
startsWith: ## Request
comment_count: 1
owner_comment_count: 1
uploaded raw file scan result endpoint proof
docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md
docs/review/external-reviewer-scan-result-endpoint-request-refresh.md
POST /documents/upload-raw-files/{raw_file_id}/scan-results
GET /documents/upload-raw-files/{raw_file_id}/scan-results
path/body mismatch -> 400
scan_verdict -> scan_error
response_has_raw_bytes -> false
```

This is an owner-authored issue edit. It is not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

## External Feedback Current-state Scan-result Endpoint Issue Verification

Phase marker: external feedback current-state scan-result endpoint issue verification v0.

Use this current-state verification artifact:

```text
docs/review/external-feedback-current-state-scan-result-endpoint-issue-verification.md
```

Observed live issue and screening state:

```text
updatedAt: 2026-06-03T02:07:48Z
first_codepoint: 35
startsWith: ## Request
comment_count: 1
candidate_count: 0
draft_count: 0
self_authored_comment
non_qualifying
uploaded raw file scan result endpoint proof
docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md
docs/review/external-review-issue-body-scan-result-endpoint-refresh.md
POST /documents/upload-raw-files/{raw_file_id}/scan-results
GET /documents/upload-raw-files/{raw_file_id}/scan-results
path/body mismatch -> 400
scan_verdict -> scan_error
response_has_raw_bytes -> false
```

This is a current-state screen only. It does not close external reviewer feedback v0.

## Uploaded Raw File Scanner Adapter Review

Phase marker: uploaded raw file scanner adapter review v0.

Use this review artifact:

```text
docs/review/uploaded-raw-file-scanner-adapter-review.md
```

Selected future boundary:

```text
ScannerAdapter
ScanAdapterRequest
ScanAdapterResult
raw_file_id
content_sha256
temporary_scan_path
scan_status
scan_verdict
```

Required failure mapping:

```text
missing_scanner_binary -> scan_error
timeout -> scan_error
do not write clean when the scanner is unavailable
```

Boundary:

```text
review-only
do not add ClamAV in this gate
do not add a download endpoint
not malware scanning
not scanner execution
not file signature validation
```

Next product gate:

```text
uploaded raw file scanner adapter v0
```

## Uploaded Raw File Scanner Adapter

Phase marker: uploaded raw file scanner adapter v0.

Use this artifact:

```text
docs/review/uploaded-raw-file-scanner-adapter.md
```

Added package:

```text
packages/ingestion/scanning/__init__.py
packages/ingestion/scanning/adapter.py
```

Core types:

```text
ScanAdapterRequest
ScanAdapterResult
ScannerAdapter
ScannerUnavailableAdapter
build_scan_error_result
```

Covered failure mapping:

```text
missing_scanner_binary -> failed / scan_error
timeout -> failed / scan_error
temporary_scan_path is not persisted
```

Focused test:

```bash
uv run pytest -q tests/test_raw_file_scanning.py
```

Boundary:

```text
not ClamAV integration
not malware scanning
not scanner process execution
not file signature validation
not a download endpoint
```

Next product gate:

```text
uploaded raw file ClamAV adapter review v0
```

## Uploaded Raw File ClamAV Adapter Review

Phase marker: uploaded raw file ClamAV adapter review v0.

Use this review artifact:

```text
docs/review/uploaded-raw-file-clamav-adapter-review.md
```

Selected future adapter:

```text
ClamAvScannerAdapter
clamscan first
clamdscan later
shutil.which
temporary_scan_path required
```

Required conservative mappings:

```text
missing clamscan -> failed / scan_error
timeout -> failed / scan_error
unknown return code -> failed / scan_error
```

Safety rules:

```text
do not use --remove
do not open daemon TCP sockets
not malware scanning
not scanner execution
```

Next product gate:

```text
uploaded raw file ClamAV adapter v0
```

## Uploaded Raw File ClamAV Adapter

Phase marker: uploaded raw file ClamAV adapter v0.

Use this artifact:

```text
docs/review/uploaded-raw-file-clamav-adapter.md
```

Added code:

```text
packages/ingestion/scanning/clamav.py
ClamAvScannerAdapter
```

Covered mappings:

```text
missing clamscan -> failed / scan_error
missing temporary_scan_path -> failed / scan_error
timeout -> failed / scan_error
unknown return code -> failed / scan_error
clean output -> completed / clean
FOUND output -> completed / infected
no --remove
```

Focused test:

```bash
uv run pytest -q tests/test_raw_file_scanning.py -k "clamav_adapter"
```

Boundary:

```text
not ClamAV installation
not runtime ClamAV verification
not malware scanning evidence
not scanner endpoint behavior
not a download endpoint
```

Next product gate:

```text
uploaded raw file ClamAV adapter runtime smoke v0
```

## Uploaded Raw File ClamAV Adapter Runtime Smoke

Phase marker: uploaded raw file ClamAV adapter runtime smoke v0.

Use this artifact:

```text
docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md
```

Run the deterministic smoke command from `apps/api`:

```bash
uv run python -m app.services.clamav_adapter_smoke_command
```

Expected boundary fields:

```text
smoke_status -> passed
real_clamav_runtime_verified -> false
binary_probe_only -> true
```

Covered scenarios:

```text
missing_binary
clean_output
infected_output
timeout
unknown_return_code
```

Boundary:

```text
not malware scanning evidence
not ClamAV installation evidence
not signature database evidence
not endpoint behavior
not download behavior
```

Next product gate:

```text
external reviewer ClamAV adapter runtime smoke request refresh v0
```

## External Reviewer ClamAV Adapter Runtime Smoke Request Refresh

Phase marker: external reviewer ClamAV adapter runtime smoke request refresh v0.

Use this artifact:

```text
docs/review/external-reviewer-clamav-adapter-runtime-smoke-request-refresh.md
```

Reviewer-facing proof:

```text
docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md
real_clamav_runtime_verified -> false
binary_probe_only -> true
```

Boundary:

```text
request infrastructure only
not external reviewer feedback
not live issue body edit
not real ClamAV execution
not signature database evidence
not malware scanning
```

Next request gate:

```text
external review issue body ClamAV adapter runtime smoke refresh v0
```

## External Review Issue Body ClamAV Adapter Runtime Smoke Refresh

Phase marker: external review issue body ClamAV adapter runtime smoke refresh v0.

Use this artifact:

```text
docs/review/external-review-issue-body-clamav-adapter-runtime-smoke-refresh.md
```

Observed live issue body markers:

```text
updatedAt: 2026-06-03T03:02:59Z
first_codepoint: 35
startsWith: ## Request
comment_count: 1
owner_comment_count: 1
```

Issue body now includes:

```text
docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md
docs/review/external-reviewer-clamav-adapter-runtime-smoke-request-refresh.md
real_clamav_runtime_verified -> false
binary_probe_only -> true
not real ClamAV execution
not signature database evidence
not malware scanning
```

Boundary:

```text
owner-authored issue edit
not external reviewer feedback
not hosted deployment evidence
not real ClamAV execution
not malware scanning
not a download endpoint
```

Next issue-state gate:

```text
external feedback current-state ClamAV adapter runtime smoke issue verification v0
```

## External Feedback Current-state ClamAV Adapter Runtime Smoke Issue Verification

Phase marker: external feedback current-state ClamAV adapter runtime smoke issue verification v0.

Use this current-state verification artifact:

```text
docs/review/external-feedback-current-state-clamav-adapter-runtime-smoke-issue-verification.md
```

Observed current-state screen:

```text
state: OPEN
updatedAt: 2026-06-03T03:02:59Z
first_codepoint: 35
startsWith: ## Request
comment_count: 1
owner_comment_count: 1
candidate_count: 0
draft_count: 0
self_authored_comment
non_qualifying
ClamAV adapter runtime smoke proof
docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md
```

Boundary:

```text
current-state screen only
not external reviewer feedback
not hosted deployment evidence
not real ClamAV execution
not signature database evidence
not malware scanning
not a download endpoint
```

Next evidence gate:

```text
external reviewer feedback v0 remains pending, or select the next source-first product gate
```

## Uploaded Raw File Scan Execution Review

Phase marker: uploaded raw file scan execution review v0.

Use this review artifact:

```text
docs/review/uploaded-raw-file-scan-execution-review.md
```

Selected future endpoint:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan
```

Do not overload:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan-results
```

Selected boundary:

```text
scan-results = caller-provided metadata
scan = configured scanner adapter execution
no raw bytes in response
no download endpoint
scan_error is never clean
no --remove
no shell=True
```

Next product gate:

```text
uploaded raw file scan execution endpoint v0
```

## Uploaded Raw File Scan Execution Endpoint

Phase marker: uploaded raw file scan execution endpoint v0.

Use this proof artifact:

```text
docs/review/uploaded-raw-file-scan-execution-endpoint.md
```

Endpoint:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan
```

Default configuration:

```text
NOISEPROOF_SCANNER=unavailable
RAW_FILE_SCANNER_TIMEOUT_SECONDS=30
```

Default response boundary:

```text
scanner_name = scanner-unavailable
scan_status = failed
scan_verdict = scan_error
failure_reason = scanner_not_configured
```

Run targeted tests from `apps/api`:

```bash
uv run pytest -q tests/test_routes.py -k "scan_execution"
```

Expected local result:

```text
3 passed, 108 deselected, 1 warning
```

Boundary:

```text
no raw bytes in response
no download endpoint
no temp path in persisted metadata
not real ClamAV execution
not malware scanning evidence
```

Next product gate:

```text
uploaded raw file scan execution endpoint runtime smoke v0
```

## Uploaded Raw File Scan Execution Endpoint Runtime Smoke

Phase marker: uploaded raw file scan execution endpoint runtime smoke v0.

Use this proof artifact:

```text
docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md
```

Runtime path:

```text
docker compose up -d db
uv run python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof --status
uv run uvicorn app.main:create_app --factory --host 127.0.0.1 --port 8010
```

Smoke flow:

```text
GET /health
POST /documents/upload-raw-files
POST /documents/upload-raw-files/{raw_file_id}/scan
GET /documents/upload-raw-files/{raw_file_id}/scan-results
```

Observed result:

```text
health_status: ok
scan_status: failed
scan_verdict: scan_error
scanner_name: scanner-unavailable
failure_reason: scanner_not_configured
temporary_scan_path_present: true
raw_bytes_key_leaked: false
temporary_scan_path_key_leaked: false
download_url_key_leaked: false
listed_scan_result_count: 1
real_clamav_runtime_verified: false
malware_scanning_evidence: false
```

Boundary:

```text
local Docker DB and live FastAPI HTTP proof only
not real ClamAV execution
not ClamAV signature database evidence
not malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
```

Next evidence gate:

```text
external reviewer scan execution endpoint request refresh v0
```

## External Reviewer Scan Execution Endpoint Request Refresh

Phase marker: external reviewer scan execution endpoint request refresh v0.

Use this request refresh artifact:

```text
docs/review/external-reviewer-scan-execution-endpoint-request-refresh.md
```

Reviewer-facing surfaces now point to:

```text
docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md
```

Updated request surfaces:

```text
CONTRIBUTING.md
.github/ISSUE_TEMPLATE/external-review-feedback.md
docs/review/external-review-request.md
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
docs/application/portfolio-index.md
README.md
docs/GOAL.md
docs/runbook.md
```

Boundary:

```text
request infrastructure only
not external reviewer feedback
not hosted deployment evidence
not real ClamAV execution
not malware scanning evidence
not a live issue body edit
```

Next evidence gate:

```text
external review issue body scan execution endpoint refresh v0
```

## External Review Issue Body Scan Execution Endpoint Refresh

Phase marker: external review issue body scan execution endpoint refresh v0.

Use this issue-body refresh artifact:

```text
docs/review/external-review-issue-body-scan-execution-endpoint-refresh.md
```

Live issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed after edit:

```text
updatedAt: 2026-06-03T03:42:56Z
has_scan_execution_proof: true
has_scan_execution_request_refresh: true
starts_with_request: true
first_codepoint: 35
comment_count: 1
```

Boundary:

```text
owner-authored issue edit only
not external reviewer feedback
not hosted deployment evidence
not real ClamAV execution
not malware scanning evidence
not a download endpoint
```

Next evidence gate:

```text
external feedback current-state scan execution endpoint issue verification v0
```

## External Feedback Current-state Scan Execution Endpoint Issue Verification

Phase marker: external feedback current-state scan execution endpoint issue verification v0.

Use this current-state screen artifact:

```text
docs/review/external-feedback-current-state-scan-execution-endpoint-issue-verification.md
```

Observed current state:

```text
issue_state: OPEN
updatedAt: 2026-06-03T03:42:56Z
has_scan_execution_proof: true
has_scan_execution_request_refresh: true
starts_with_request: true
first_codepoint: 35
comment_count: 1
candidate_count: 0
screened_comment_count: 1
first_classification: non_qualifying
first_reason: self_authored_comment
acceptance_status: pending
draft_count: 0
does_not_close_gate: true
next_gate: external reviewer feedback v0
```

Boundary:

```text
current-state screen only
not external reviewer feedback
not hosted deployment evidence
not real ClamAV execution
not malware scanning evidence
not a download endpoint
```

Next evidence gate:

```text
external reviewer feedback v0 remains pending, or select the next source-first product gate
```

## Uploaded Raw File ClamAV Runtime Verification Review

Phase marker: uploaded raw file ClamAV runtime verification review v0.

Use this review artifact:

```text
docs/review/uploaded-raw-file-clamav-runtime-verification-review.md
```

Selected next product gate:

```text
dockerized ClamAV EICAR runtime smoke v0
```

Selected boundary:

```text
use official ClamAV Docker docs
use EICAR test file, not real malware
do not commit EICAR into the repository
record image tag and image id or digest
record signature database state
do not switch API default from scanner-unavailable
do not add Docker-backed adapter yet
```

Not claimed:

```text
not runtime evidence
not malware scanning evidence
not API endpoint verification with real ClamAV
not hosted deployment evidence
not external reviewer feedback
```

Next product gate:

```text
dockerized ClamAV EICAR runtime smoke v0
```

## Uploaded Raw File Dockerized ClamAV EICAR Runtime Smoke

Phase marker: dockerized ClamAV EICAR runtime smoke v0.

Use this proof artifact:

```text
docs/review/uploaded-raw-file-dockerized-clamav-eicar-runtime-smoke.md
```

Observed result:

```text
docker_available: true
clamav_image: clamav/clamav:stable
clamav_image_id: sha256:d4000290254603e7ee45d4904425c7d98c015af727f402756198fe41a31e7777
clamav_repo_digest: clamav/clamav@sha256:d4000290254603e7ee45d4904425c7d98c015af727f402756198fe41a31e7777
clamscan_version: ClamAV 1.5.2/28017/Sun May 31 06:27:13 2026
signature_database_observed: true
test_file_type: eicar
test_file_committed_to_repo: false
clamscan_return_code: 1
eicar_detected: true
temporary_scan_file_deleted: true
host_eicar_file_written: false
real_clamav_runtime_verified: true
malware_scanning_evidence: false
api_endpoint_verified_with_real_clamav: false
clamscan_output: /tmp/eicar.com: Eicar-Test-Signature FOUND
```

Boundary:

```text
real Dockerized ClamAV runtime verified for EICAR only
not production malware scanning evidence
not API endpoint verification with real ClamAV
not hosted deployment evidence
not external reviewer feedback
```

Next product gate:

```text
ClamAV API integration boundary review v0
```

## ClamAV API Integration Boundary Review

Phase marker: ClamAV API integration boundary review v0.

Use this review artifact:

```text
docs/review/clamav-api-integration-boundary-review.md
```

Decision:

```text
do not change API scanner default yet
do not add Docker CLI execution to POST /documents/upload-raw-files/{raw_file_id}/scan
do not claim endpoint runtime proof with real ClamAV yet
select ClamAV service boundary review v0
```

Alternatives considered:

```text
host clamscan
docker run per scan request
ClamAV daemon/service boundary
```

Boundary:

```text
review-only
not API endpoint integration
not endpoint runtime proof with real ClamAV
not malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
```

Next product gate:

```text
ClamAV service boundary review v0
```

## ClamAV Service Boundary Review

Phase marker: ClamAV service boundary review v0.

Use this review artifact:

```text
docs/review/clamav-service-boundary-review.md
```

Decision:

```text
review ClamAV compose service boundary before code
do not expose clamd TCP to host/public networks
do not use Docker CLI per API request
do not switch NOISEPROOF_SCANNER=clamav by default
do not claim endpoint runtime proof with real ClamAV yet
```

Next product gate:

```text
ClamAV compose service review v0
```

## ClamAV Compose Service Review

Phase marker: ClamAV compose service review v0.

Use this review artifact:

```text
docs/review/clamav-compose-service-review.md
```

Decision:

```text
select a future internal-only clamav compose service
do not publish clamd ports to the host
depends_on must not be treated as scanner readiness evidence
signature database readiness must be visible
prefer streamed bytes over API temp-path scanning
do not switch NOISEPROOF_SCANNER=clamav by default
```

Next product gate:

```text
ClamAV compose service implementation v0
```

## ClamAV Compose Service Implementation

Phase marker: ClamAV compose service implementation v0.

Use this implementation note:

```text
docs/review/clamav-compose-service-implementation.md
```

Implemented:

```text
optional clamav service behind scanner profile
clamav/clamav:stable image
expose 3310 without host port publishing
noiseproof_clamav_db signature database volume
clamdscan --ping=1 healthcheck
NOISEPROOF_SCANNER remains unavailable by default
```

Config-only verification target:

```text
docker compose --profile scanner config
```

Next product gate:

```text
ClamAV compose service config verification v0
```

## ClamAV Compose Service Config Verification

Phase marker: ClamAV compose service config verification v0.

Use this verification artifact:

```text
docs/review/clamav-compose-service-config-verification.md
```

Observed command:

```text
docker compose --profile scanner config -> exit 0
```

Observed rendered shape:

```text
profiles: scanner
expose: 3310
healthcheck: clamdscan --ping=1
clamav ports published to host: false
real_clamav_runtime_verified: false
api_endpoint_verified_with_real_clamav: false
```

Next product gate:

```text
ClamAV compose service runtime smoke v0
```

## ClamAV Compose Service Runtime Smoke

Phase marker: ClamAV compose service runtime smoke v0.

Use this runtime artifact:

```text
docs/review/clamav-compose-service-runtime-smoke.md
```

Observed commands:

```text
docker compose --profile scanner up -d clamav -> exit 0
docker inspect -f '{{.State.Health.Status}}' noiseproof-agent-clamav -> healthy
docker compose --profile scanner exec -T clamav clamdscan --ping=1 -> PONG
docker compose --profile scanner exec -T clamav clamdscan --version -> ClamAV 1.5.2/28017/Sun May 31 06:27:13 2026
```

Observed boundaries:

```text
container_health: healthy
clamd_ping_verified: true
signature_database_observed: true
real_clamav_runtime_verified: true
api_endpoint_verified_with_real_clamav: false
malware_scanning_evidence: false
```

Next product gate:

```text
ClamAV compose EICAR runtime smoke v0
```

## ClamAV Compose EICAR Runtime Smoke

Phase marker: ClamAV compose EICAR runtime smoke v0.

Use this runtime artifact:

```text
docs/review/clamav-compose-eicar-runtime-smoke.md
```

Observed output:

```text
Eicar-Test-Signature FOUND
clamdscan_return_code: 1
eicar_detected: true
temporary_scan_file_deleted: true
host_eicar_file_written: false
production_malware_scanning_evidence: false
```

Next product gate:

```text
ClamAV service scanner adapter review v0
```

## ClamAV Service Scanner Adapter Review

Phase marker: ClamAV service scanner adapter review v0.

Use this review artifact:

```text
docs/review/clamav-service-scanner-adapter-review.md
```

Decision:

```text
select ClamdScannerAdapter
use INSTREAM over the internal Docker network
do not pass API temporary paths to clamd
do not require clamdscan as an API subprocess dependency
map unavailable, timeout, protocol error, and scanner error to failed / scan_error
NOISEPROOF_SCANNER=unavailable remains the default
```

Next product gate:

```text
ClamAV service scanner adapter v0
```

## ClamAV Service Scanner Adapter

Phase marker: ClamAV service scanner adapter v0.

Use this implementation artifact:

```text
docs/review/clamav-service-scanner-adapter.md
```

Implemented:

```text
ClamdScannerAdapter
zINSTREAM command
length-prefixed INSTREAM chunks
timeout -> failed / scan_error
clamd_unavailable -> failed / scan_error
clamd_unexpected_response -> failed / scan_error
no raw temporary scan path in result metadata
```

Verification:

```text
uv run pytest tests/test_raw_file_scanning.py -q -k clamd_adapter
4 passed, 7 deselected
```

Next product gate:

```text
ClamAV API service network boundary review v0
```

## ClamAV API Service Network Boundary Review

Phase marker: ClamAV API service network boundary review v0.

Use this review artifact:

```text
docs/review/clamav-api-service-network-boundary-review.md
```

Decision:

```text
host-local API process cannot rely on the Compose service name clamav
do not publish clamd TCP to the host
do not set CLAMD_HOST=localhost
API must run inside the Compose network before service-host integration
NOISEPROOF_SCANNER=unavailable remains the default
```

Next product gate:

```text
ClamAV API compose service review v0
```

## ClamAV API Compose Service Review

Phase marker: ClamAV API compose service review v0.

Use this review artifact:

```text
docs/review/clamav-api-compose-service-review.md
```

Decision:

```text
select a future profiled api Compose service
API service joins the same Compose network as clamav
CLAMD_HOST=clamav
CLAMD_PORT=3310
NOISEPROOF_SCANNER=unavailable remains the default
scanner opt-in must be explicit
do not publish clamd TCP to the host
```

Next product gate:

```text
ClamAV API compose service implementation v0
```

## ClamAV API Compose Service Implementation

Phase marker: ClamAV API compose service implementation v0.

Use this implementation artifact:

```text
docs/review/clamav-api-compose-service-implementation.md
```

Implemented:

```text
apps/api/Dockerfile
docker-compose.yml api service
api profile
DATABASE_URL points at db service hostname
CLAMD_HOST=clamav
CLAMD_PORT=3310
NOISEPROOF_SCANNER=unavailable remains the default
```

Next product gate:

```text
ClamAV API compose service config verification v0
```

## ClamAV API Compose Service Config Verification

Phase marker: ClamAV API compose service config verification v0.

Use this verification artifact:

```text
docs/review/clamav-api-compose-service-config-verification.md
```

Observed command:

```text
docker compose --profile api --profile scanner config -> exit 0
```

Observed rendered shape:

```text
service: api
profiles: api
DATABASE_URL: postgresql://noiseproof:noiseproof@db:5432/noiseproof
CLAMD_HOST: clamav
CLAMD_PORT: "3310"
NOISEPROOF_SCANNER: unavailable
api_runtime_started: false
api_endpoint_verified_with_real_clamav: false
```

Next product gate:

```text
ClamAV API compose service runtime smoke v0
```

## ClamAV API Compose Service Runtime Smoke

Phase marker: ClamAV API compose service runtime smoke v0.

Use this verification artifact:

```text
docs/review/clamav-api-compose-service-runtime-smoke.md
```

Observed commands:

```text
docker compose --profile api up -d api -> exit 0
curl.exe -s -i http://localhost:8000/health -> 200
```

Observed runtime shape:

```text
api_container_running: true
GET /health -> 200
"status":"ok"
NOISEPROOF_SCANNER: unavailable
api_scan_endpoint_verified_with_real_clamav: false
malware_scanning_evidence: false
```

Boundary:

```text
not scan endpoint proof
not endpoint runtime proof with real ClamAV
scanner default remains unavailable
not production malware scanning evidence
```

Next product gate:

```text
ClamAV API endpoint scanner opt-in review v0
```

## ClamAV API Endpoint Scanner Opt-in Review

Phase marker: ClamAV API endpoint scanner opt-in review v0.

Use this review artifact:

```text
docs/review/clamav-api-endpoint-scanner-opt-in-review.md
```

Selected future code boundary:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan
current code: NOISEPROOF_SCANNER=clamav -> ClamAvScannerAdapter
next code gate: NOISEPROOF_SCANNER=clamd -> ClamdScannerAdapter
default remains NOISEPROOF_SCANNER=unavailable
CLAMD_HOST=clamav
CLAMD_PORT=3310
scanner_not_configured
```

Boundary:

```text
review-only
not endpoint runtime proof with real ClamAV
not malware scanning evidence
not scanner default switch
```

Next product gate:

```text
ClamAV API endpoint scanner opt-in implementation v0
```

## ClamAV API Endpoint Scanner Opt-in Implementation

Phase marker: ClamAV API endpoint scanner opt-in implementation v0.

Use this implementation artifact:

```text
docs/review/clamav-api-endpoint-scanner-opt-in-implementation.md
```

Implemented boundary:

```text
POST /documents/upload-raw-files/{raw_file_id}/scan
NOISEPROOF_SCANNER=clamd -> ClamdScannerAdapter
NOISEPROOF_SCANNER=clamav -> ClamAvScannerAdapter
default remains NOISEPROOF_SCANNER=unavailable
CLAMD_HOST=clamav
CLAMD_PORT=3310
```

Verification:

```powershell
cd apps/api
uv run pytest tests/test_routes.py -q -k get_scanner_adapter_selects_clamd_only_for_explicit_opt_in
```

Boundary:

```text
not endpoint runtime proof with real ClamAV
not malware scanning evidence
not scanner default switch
```

Next product gate:

```text
ClamAV API endpoint scanner opt-in runtime smoke v0
```

## ClamAV API Endpoint Scanner Opt-in Runtime Smoke

Phase marker: ClamAV API endpoint scanner opt-in runtime smoke v0.

Use this runtime artifact:

```text
docs/review/clamav-api-endpoint-scanner-opt-in-runtime-smoke.md
```

Runtime setup:

```powershell
$env:NOISEPROOF_SCANNER='clamd'
$env:CLAMD_HOST='clamav'
$env:CLAMD_PORT='3310'
docker compose --profile api --profile scanner up -d --build api clamav
```

Observed endpoint smoke:

```text
compose_up_api_clamd_exit=0
GET /health -> 200
POST /documents/upload-raw-files -> 201
POST /documents/upload-raw-files/{raw_file_id}/scan -> 201
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: clean
clamd_response: stream: OK
api_endpoint_verified_with_real_clamav: true
malicious_detection_verified: false
```

Boundary:

```text
clean-file endpoint runtime proof only
not malware detection proof
not EICAR-through-API proof
not production malware scanning evidence
```

Next product gate:

```text
ClamAV API endpoint malicious-detection runtime review v0
```

## ClamAV API Endpoint Malicious-detection Runtime Review

Phase marker: ClamAV API endpoint malicious-detection runtime review v0.

Use this review artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-runtime-review.md
```

Current proof boundary:

```text
clean-file endpoint proof exists
malicious_detection_verified: false
EICAR-through-API proof is still pending
```

Safety rules:

```text
do not store the EICAR payload in the repository
do not bypass OS security controls
record only detection result and matched signature
not malware detection proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Runtime Blocked

Phase marker: ClamAV API endpoint malicious-detection runtime blocked v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-runtime-blocked.md
```

Observed boundary:

```text
runtime smoke not completed
host command was rejected before endpoint request
EICAR-through-API proof remains pending
payload_committed_to_repo: false
```

Boundary:

```text
do not bypass OS security controls
not malware detection proof
not production malware scanning evidence
```

Next product gate:

```text
ClamAV API endpoint malicious-detection test harness review v0
```

## ClamAV API Endpoint Malicious-detection Test Harness Review

Phase marker: ClamAV API endpoint malicious-detection test harness review v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-test-harness-review.md
```

Selected harness boundary:

```text
review-only
owner-provided runtime-only test signature
NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1
NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT
payload_committed_to_repo: false
do not store the test signature payload or an encoded form in the repository
do not bypass OS security controls
blocked_by_environment
not malware detection proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection test harness v0
```

## ClamAV API Endpoint Malicious-detection Test Harness

Phase marker: ClamAV API endpoint malicious-detection test harness v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-test-harness.md
```

Implementation module:

```text
app.services.clamav_api_malicious_detection_harness
```

Default safe command:

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness
```

Expected default status:

```text
not_configured
payload_committed_to_repo: false
raw_payload_logged: false
not malware detection proof
```

Opt-in variables for a future runtime-only smoke:

```text
NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1
NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT
```

Next product gate:

```text
ClamAV API endpoint malicious-detection harness default smoke v0
```

## ClamAV API Endpoint Malicious-detection Harness Default Smoke

Phase marker: ClamAV API endpoint malicious-detection harness default smoke v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-harness-default-smoke.md
```

Observed default command:

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness
```

Observed default result:

```text
exit_code: 0
harness_status: not_configured
api_calls_attempted: false
malicious_detection_verified: false
payload_committed_to_repo: false
raw_payload_logged: false
not malware detection proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## External Review Issue Body Owner-runtime Input Discovery Refresh

Phase marker: external review issue body owner-runtime input discovery refresh v0.

Use this artifact when checking why issue #1 now points reviewers to the owner-runtime input discovery CI remote verification proof:

```text
docs/review/external-review-issue-body-owner-runtime-input-discovery-refresh.md
```

Live issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

The owner-authored issue body edit adds:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-input-discovery-ci-remote-verification.md
run_id: 26927767832
owner_runtime_input_missing
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

This is request-surface hygiene only. It is not external reviewer feedback, not hosted deployment evidence, not endpoint malicious-detection runtime proof, and does not include a test signature payload.

## External Review Issue Body BOM Cleanup

Phase marker: external review issue body BOM cleanup v0.

Use this artifact when checking why issue #1 starts directly with `## Request` again after the owner-runtime input discovery refresh:

```text
docs/review/external-review-issue-body-bom-cleanup.md
```

Observed live issue cleanup:

```text
previous_first_codepoint: 65279
starts_with_request: true
first_codepoint: 35
```

The cleanup preserved:

```text
docs/review/external-review-issue-body-owner-runtime-input-discovery-refresh.md
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-input-discovery-ci-remote-verification.md
```

This is request-surface readability hygiene only. It is not external reviewer feedback, not hosted deployment evidence, not endpoint malicious-detection runtime proof, and does not include a test signature payload.

## CI Node24 Actions Runtime Opt-in

## ClamAV API Endpoint Malicious-detection Stdin Input Review

Phase marker: ClamAV API endpoint malicious-detection stdin input review v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-stdin-input-review.md
```

Decision:

```text
review-only
stdin-only owner input path
owner-provided runtime smoke remains pending
NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT remains supported
do not use this review to supply a test signature
payload_committed_to_repo: false
raw_payload_logged: false
not malware detection proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection stdin input harness v0
```

## ClamAV API Endpoint Malicious-detection Stdin Input Harness

Phase marker: ClamAV API endpoint malicious-detection stdin input harness v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-stdin-input-harness.md
```

Implemented command option:

```text
--signature-stdin
```

Expected behavior:

```text
input_source: stdin
empty stdin remains not_configured
payload_committed_to_repo: false
raw_payload_logged: false
fake-client tests only
not malware detection proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection stdin default smoke v0
```

## ClamAV API Endpoint Malicious-detection Stdin Default Smoke

Phase marker: ClamAV API endpoint malicious-detection stdin default smoke v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-stdin-default-smoke.md
```

Observed command:

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness --signature-stdin
```

Observed result:

```text
exit_code: 0
harness_status: not_configured
input_source: stdin
api_calls_attempted: false
malicious_detection_verified: false
payload_committed_to_repo: false
raw_payload_logged: false
owner-provided runtime smoke remains pending
not malware detection proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Preflight

Phase marker: ClamAV API endpoint malicious-detection owner-runtime preflight v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-preflight.md
```

Observed runtime state:

```text
docker compose --profile api --profile scanner ps
GET /health -> 200
NOISEPROOF_SCANNER=clamd
CLAMD_HOST=clamav
CLAMD_PORT=3310
ClamAV service healthy
clamd PING -> PONG
owner-provided test signature absent
no scan endpoint request was made
owner-provided runtime smoke remains pending
not malware detection proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-input Guard

Phase marker: ClamAV API endpoint malicious-detection owner-input guard v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-input-guard.md
```

Observed command:

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness --signature-stdin --require-owner-input
```

Observed result:

```text
exit_code: 4
required_owner_input_missing: true
harness_status: not_configured
api_calls_attempted: false
malicious_detection_verified: false
payload_committed_to_repo: false
raw_payload_logged: false
owner-provided runtime smoke remains pending
not malware detection proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Packet

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke packet v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-packet.md
```

Observed command:

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness --print-owner-runtime-smoke-packet
```

Observed packet:

```text
packet_status: ready_for_owner_input
required_input: owner-provided runtime-only test signature via stdin
command_template
command_templates
runtime_report_handling
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: infected
matched_signature: Eicar-Test-Signature
api_calls_attempted: false
payload_committed_to_repo: false
raw_payload_logged: false
does not call the scan endpoint
not malware detection proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Validator

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke validator v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-validator.md
```

Command:

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness \
  --validate-owner-runtime-smoke-report path/to/owner-runtime-smoke-report.json
```

Accepted validator markers:

```text
validation_status: accepted
accepted_owner_runtime_smoke: true
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: infected
matched_signature: Eicar-Test-Signature
payload_committed_to_repo: false
raw_payload_logged: false
metadata validation only
not production malware scanning evidence
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Validator Leak-field Hardening

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke validator leak-field hardening v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-validator-leak-field-hardening.md
```

Expected rejection markers:

```text
validation_status: rejected
accepted_owner_runtime_smoke: false
forbidden_payload_fields
forbidden payload field present
test_signature_text
encoded_payload
redacted-placeholder not echoed
metadata validation only
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Report Contract

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke report contract v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-report-contract.md
```

Command:

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness \
  --print-owner-runtime-smoke-report-contract
```

Expected markers:

```text
contract_status: ready_for_owner_runtime_report
accepted_report
accepted_scan_result_summary
forbidden_payload_fields
accepted_validator_output
rejected_validator_output
does not call the scan endpoint
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Report Schema

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke report schema v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-report-schema.md
```

Command:

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness \
  --print-owner-runtime-smoke-report-schema
```

Expected markers:

```text
https://json-schema.org/draft/2020-12/schema
additionalProperties: false
forbidden_payload_fields
validator remains authoritative
validator_replacement: false
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Validator Strict-shape Alignment

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke validator strict-shape alignment v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-validator-strict-shape-alignment.md
```

Expected rejection markers:

```text
additionalProperties: false
validation_status: rejected
accepted_owner_runtime_smoke: false
unexpected_fields
template_status
scan_result_summary.extra_note
unexpected field present
schema and validator alignment only
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Cross-shell Packet

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke cross-shell packet v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-cross-shell-packet.md
```

Expected packet markers:

```text
command_templates
posix
powershell
owner-provided-runtime-only-signature-file-outside-repo
runtime-report-path-outside-repo
runtime_report_handling
write_report_outside_repo: true
validate_metadata_only: true
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Report Path Guard

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke report path guard v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-report-path-guard.md
```

Expected validator rejection markers:

```text
--validate-owner-runtime-smoke-report
report_path_boundary
report_path_allowed: false
required_location: outside_repository
report path must be outside repository
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Output Path Guard

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke output path guard v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-output-path-guard.md
```

Expected harness rejection markers:

```text
--signature-stdin --require-owner-input --output
output_path_rejected
output_path_boundary
output_path_allowed: false
required_location: outside_repository
output path must be outside repository
api_calls_attempted: false
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Validator Handoff Report

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke validator handoff report v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-validator-handoff-report.md
```

Expected handoff markers:

```text
--signature-stdin --require-owner-input --owner-runtime-smoke-report --output
--validate-owner-runtime-smoke-report
emit_validator_handoff_report: true
validator-accepted metadata shape
phase_marker not emitted
payload_length_bytes not emitted
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Command-template Handoff Alignment

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke command-template handoff alignment v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-command-template-handoff-alignment.md
```

Expected packet markers:

```text
singular command_template
--owner-runtime-smoke-report
--output <runtime-report-path-outside-repo>
validator handoff report
emit_validator_handoff_report: true
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Post-run Validation Command

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke post-run validation command v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-post-run-validation-command.md
```

Expected packet markers:

```text
post_run_validation_command
--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
accepted_owner_runtime_smoke
validator metadata only
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Post-run Validation Cross-shell Commands

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke post-run validation cross-shell commands v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-post-run-validation-cross-shell-commands.md
```

Expected packet markers:

```text
post_run_validation_commands
posix
powershell
--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
--validate-owner-runtime-smoke-report '<runtime-report-path-outside-repo>'
validator metadata only
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Post-run Validation Success Criteria

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke post-run validation success criteria v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-post-run-validation-success-criteria.md
```

Expected packet markers:

```text
post_run_validation_success_criteria
validation_status: accepted
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
validator metadata only
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Empty-marker Guard

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke empty-marker guard v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-empty-marker-guard.md
```

Observed guard behavior:

```text
quote-only stdin
BOM-only stdin
""
exit_code: 4
harness_status: not_configured
required_owner_input_missing: true
api_calls_attempted: false
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Verification:

```bash
cd apps/api
uv run pytest tests/test_clamav_api_malicious_detection_harness.py -q -k "quote_only_stdin"
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Signature-file Input

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke signature-file input v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-signature-file-input.md
```

Preferred runtime-only input command:

```text
NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1 uv run python -m app.services.clamav_api_malicious_detection_harness --signature-file <owner-provided-runtime-only-signature-file-outside-repo> --require-owner-input --owner-runtime-smoke-report --output <runtime-report-path-outside-repo>
```

Expected guard markers:

```text
signature_file_path_allowed: false
required_location: outside_repository
accepted_input_sources: file, stdin
input_source: file or stdin
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Verification:

```bash
cd apps/api
uv run pytest tests/test_clamav_api_malicious_detection_harness.py -q -k "signature_file"
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Signature-file Read Guard

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke signature-file read guard v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-signature-file-read-guard.md
```

Expected read-failure markers:

```text
signature_file_read_failed
signature_file_readable: false
raw_exception_logged: false
api_calls_attempted: false
exit_code: 8
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Verification:

```bash
cd apps/api
uv run pytest tests/test_clamav_api_malicious_detection_harness.py -q -k "missing_signature_file or directory_signature_file"
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Current-readiness Recheck

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke current-readiness recheck v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-current-readiness-recheck.md
```

Observed readiness markers:

```text
docker_server_version: 29.4.3
docker_compose_version: v5.1.3
api_scanner: clamd
api_health_status: ok
clamd_ping: PONG
owner_runtime_signature_input_present: false
api_scan_request_attempted: false
malicious_detection_verified: false
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Verification commands used:

```bash
docker --version
docker compose version
docker info --format '{{json .ServerVersion}}'
docker compose --profile api --profile scanner ps
docker compose --profile api --profile scanner exec -T api printenv NOISEPROOF_SCANNER CLAMD_HOST CLAMD_PORT
Invoke-RestMethod -Uri 'http://localhost:8000/health' -Method Get
docker compose --profile api --profile scanner exec -T clamav clamdscan --ping=1
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke

Phase marker: clamav api endpoint malicious-detection owner runtime smoke v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md
```

Observed local Docker/API/clamd markers:

```text
NOISEPROOF_SCANNER=clamd
clamd PING -> PONG
harness_status: verified_infected
malicious_detection_verified: true
api_calls_attempted: true
input_source: stdin
scanner_name: clamav-clamd
scan_status: completed
scan_verdict: infected
matched_signature: Eicar-Test-Signature
validation_status: accepted
accepted_owner_runtime_smoke: true
report_inside_repo: false
payload_committed_to_repo: false
raw_payload_logged: false
remaining_raw: 0
remaining_scans: 0
```

Boundary:

```text
does not include the test signature payload
not production malware scanning evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## External Reviewer ClamAV Malicious-detection Request Refresh

Phase marker: external reviewer clamav malicious-detection request refresh v0.

Use this artifact:

```text
docs/review/external-reviewer-clamav-malicious-detection-request-refresh.md
```

Linked runtime proof:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md
harness_status: verified_infected
scan_verdict: infected
matched_signature: Eicar-Test-Signature
payload_committed_to_repo: false
raw_payload_logged: false
```

Boundary:

```text
not live issue body edit
not external reviewer feedback
not hosted deployment evidence
not production malware scanning evidence
```

## External Review Issue Body ClamAV Malicious-detection Refresh

Phase marker: external review issue body clamav malicious-detection refresh v0.

Use this artifact:

```text
docs/review/external-review-issue-body-clamav-malicious-detection-refresh.md
```

Observed live issue markers:

```text
https://github.com/svy04/noiseproof-agent/issues/1
starts_with_request: true
first_codepoint: 35
has_clamav_malicious_detection_proof: true
has_clamav_malicious_detection_request_refresh: true
has_external_feedback_boundary: true
comment_count: 1
```

Boundary:

```text
owner-authored issue body edit only
does not close external reviewer feedback v0
not external reviewer feedback
not hosted deployment evidence
not production malware scanning evidence
```

## External Feedback Current-state ClamAV Malicious-detection Issue Verification

Phase marker: external feedback current-state clamav malicious-detection issue verification v0.

Use this artifact:

```text
docs/review/external-feedback-current-state-clamav-malicious-detection-issue-verification.md
```

Observed live issue markers:

```text
updatedAt: 2026-06-04T18:22:31Z
starts_with_request: true
first_codepoint: 35
has_clamav_malicious_detection_proof: true
has_clamav_malicious_detection_request_refresh: true
comment_count: 1
screened_comment_count: 1
candidate_count: 0
draft_count: 0
classification: non_qualifying
reason: self_authored_comment
does_not_close_gate: true
```

Boundary:

```text
not external reviewer feedback
not hosted deployment evidence
not production malware scanning evidence
external reviewer feedback remains pending
```

## External Review Issue Body Readability Refresh

Phase marker: external review issue body readability refresh v0.

Use this artifact:

```text
docs/review/external-review-issue-body-readability-refresh.md
```

Observed live issue markers:

```text
updatedAt: 2026-06-04T18:34:51Z
starts_with_request: true
first_codepoint: 35
has_fast_path: true
has_latest_proof: true
has_feedback_format: true
has_boundaries: true
has_literal_crlf_text: false
body_length: 3808
body_length_under_12000: true
has_clamav_malicious_detection_proof: true
comment_count: 1
```

Boundary:

```text
owner-authored issue body edit only
not external reviewer feedback
not hosted deployment evidence
not production malware scanning evidence
```

## External Feedback Current-state Issue Body Readability Verification

Phase marker: external feedback current-state issue body readability verification v0.

Use this artifact:

```text
docs/review/external-feedback-current-state-issue-body-readability-verification.md
```

Observed live issue markers:

```text
updatedAt: 2026-06-04T18:34:51Z
starts_with_request: true
first_codepoint: 35
has_fast_path: true
has_latest_proof: true
has_feedback_format: true
has_boundaries: true
has_literal_crlf_text: false
body_length: 3808
body_length_under_12000: true
comment_count: 1
screened_comment_count: 1
candidate_count: 0
draft_count: 0
classification: non_qualifying
reason: self_authored_comment
does_not_close_gate: true
```

Boundary:

```text
not external reviewer feedback
not hosted deployment evidence
external reviewer feedback remains pending
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Input Discovery

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke input discovery v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-input-discovery.md
```

Discovery command:

```bash
cd apps/api
uv run python -m app.services.clamav_api_malicious_detection_harness --discover-owner-runtime-input
```

Expected no-input markers:

```text
owner_runtime_input_missing
discoverable_input_sources: file, stdin, environment
accepted_input_sources: file, stdin
signature_text_env.validator_accepted: false
stdin.validator_accepted: true
input_payload_inspected: false
api_calls_attempted: false
raw_payload_logged: false
value_logged: false
path_logged: false
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Exit code:

```text
0 when owner runtime input is discoverable
4 when owner runtime input is missing
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Input-source Contract Alignment

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke input-source contract alignment v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-input-source-contract-alignment.md
```

Current contract:

```text
discoverable_input_sources: file, stdin, environment
accepted_input_sources: file, stdin
signature_text_env.validator_accepted: false
stdin.validator_accepted: true
input_source must be one of: file, stdin
```

This is contract-alignment proof only. It does not run the owner runtime smoke, does not include a test signature payload, does not call the API, and is not endpoint malicious-detection runtime proof.

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Input-source Contract CI Check

Phase marker: ClamAV API endpoint malicious-detection owner runtime input-source contract ci check v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-input-source-contract-ci-check.md
```

The CI step remains:

```text
Check ClamAV owner runtime input discovery no-payload missing state
```

It now asserts:

```text
discoverable_input_sources: file, stdin, environment
accepted_input_sources: file, stdin
signature_text_env.validator_accepted: false
stdin.validator_accepted: true
```

This is CI contract guard evidence only. It does not run the owner runtime smoke, does not include a test signature payload, does not call the API, and is not endpoint malicious-detection runtime proof.

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## External Review Issue Body Owner-runtime Input-source Contract Refresh

Phase marker: external review issue body owner-runtime input-source contract refresh v0.

Use this artifact:

```text
docs/review/external-review-issue-body-owner-runtime-input-source-contract-refresh.md
```

The live issue body now points reviewers to:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-input-source-contract-ci-check.md
```

The refresh records:

```text
run_id: 26929243011
head: 2c4da65
discoverable_input_sources=file,stdin,environment
accepted_input_sources=file,stdin
first_codepoint: 35
```

This is owner-authored issue-body request infrastructure only. It does not run the owner runtime smoke, does not include a test signature payload, does not call the API, and is not endpoint malicious-detection runtime proof.

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## External Feedback Current-state Owner-runtime Input-source Contract Issue Verification

Phase marker: external feedback current-state owner-runtime input-source contract issue verification v0.

Use this artifact:

```text
docs/review/external-feedback-current-state-owner-runtime-input-source-contract-issue-verification.md
```

The current-state screen records:

```text
updatedAt: 2026-06-04T03:53:20Z
starts_with_request: true
first_codepoint: 35
has_input_source_contract_ci_link: true
comment_count: 1
screened_comment_count: 1
candidate_count: 0
draft_count: 0
self_authored_comment
non_qualifying
does_not_close_gate: true
```

This is live issue screening evidence only. It does not run the owner runtime smoke, does not include a test signature payload, does not call the API, is not endpoint malicious-detection runtime proof, and does not close external reviewer feedback v0.

Next gates:

```text
external reviewer feedback v0
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0 if owner-provided runtime input exists
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Input Discovery CI Check

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke input discovery ci check v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-input-discovery-ci-check.md
```

CI step:

```text
Check ClamAV owner runtime input discovery no-payload missing state
```

Expected markers:

```text
expected_status=4
owner_runtime_input_missing
input_payload_inspected: false
api_calls_attempted: false
raw_payload_logged: false
does not include a test signature payload
not endpoint malicious-detection runtime proof
```

Verification:

```bash
cd apps/api
uv run pytest tests/test_docs.py -q -k "input_discovery_ci_check"
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## ClamAV API Endpoint Malicious-detection Owner-runtime Smoke Input Discovery CI Remote Verification

Phase marker: ClamAV API endpoint malicious-detection owner runtime smoke input discovery ci remote verification v0.

Use this artifact:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke-input-discovery-ci-remote-verification.md
```

Remote evidence:

```text
run_id: 26927767832
job_id: 79441163152
head: 3089f02
workflow: CI
job: api-smoke
job_conclusion: success
step_number: 8
Check ClamAV owner runtime input discovery no-payload missing state
step_conclusion: success
owner_runtime_input_missing
not endpoint malicious-detection runtime proof
```

Verification:

```bash
gh run view 26927767832 --repo svy04/noiseproof-agent --json databaseId,headSha,conclusion,status,event,workflowName,createdAt,updatedAt,url,jobs
cd apps/api
uv run pytest tests/test_docs.py -q -k "input_discovery_ci_remote_verification"
```

Next product gate:

```text
ClamAV API endpoint malicious-detection owner-provided runtime smoke v0
```

## CI Node24 Actions Runtime Opt-in

Phase marker: ci node24 actions runtime opt-in v0.

Use this artifact:

```text
docs/review/ci-node24-actions-runtime-opt-in.md
```

Configured workflows:

```text
.github/workflows/ci.yml
.github/workflows/external-feedback-screen.yml
```

Expected workflow env:

```text
FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"
```

Boundary:

```text
workflow runtime compatibility only
not product runtime evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## CI Node24 Actions Runtime Remote Verification

Phase marker: ci node24 actions runtime remote verification v0.

Use this artifact:

```text
docs/review/ci-node24-actions-runtime-remote-verification.md
```

Verified remote runs:

```text
remote run: 26870586255
workflow: CI
head: c3c6908
job: api-smoke
conclusion: success

remote run: 26870586219
workflow: External Feedback Screen
head: c3c6908
job: screen
conclusion: success
```

Observed annotation:

```text
Node.js 20 is deprecated
being forced to run on Node.js 24
annotation still present
```

Boundary:

```text
workflow runtime compatibility only
not product runtime evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## CI Node24 Action Version Refresh

Phase marker: ci node24 action version refresh v0.

Use this artifact:

```text
docs/review/ci-node24-action-version-refresh.md
```

Configured workflow action references:

```text
.github/workflows/ci.yml
  actions/checkout@v6
  actions/setup-python@v6
  astral-sh/setup-uv@v8.2.0

.github/workflows/external-feedback-screen.yml
  actions/checkout@v6
  actions/setup-python@v6
  actions/upload-artifact@v7
```

Boundary:

```text
workflow runtime compatibility only
remote annotation result remains unverified until the next push
not product runtime evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## CI Node24 Action Version Remote Verification

Phase marker: ci node24 action version remote verification v0.

Use this artifact:

```text
docs/review/ci-node24-action-version-remote-verification.md
```

Verified remote runs:

```text
remote run: 26969000702
workflow: CI
head: 83fb603
job: api-smoke
job id: 79579051552
conclusion: success

remote run: 26969000663
workflow: External Feedback Screen
head: 83fb603
job: screen
job id: 79579051531
conclusion: success
```

Observed result:

```text
check-run annotations: []
Node.js 20 forced-runtime warning observed: no
```

Boundary:

```text
workflow runtime compatibility only
not product runtime evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## TestClient Dependency Warning Cleanup

Phase marker: testclient dependency warning cleanup v0.

Use this artifact:

```text
docs/review/testclient-dependency-warning-cleanup.md
```

Configured test dependency and warning guard:

```text
apps/api/pyproject.toml
  httpx2>=2.3.0
  error::starlette.exceptions.StarletteDeprecationWarning
```

Local verification:

```text
uv run python -W error::DeprecationWarning -c "from fastapi.testclient import TestClient; print(TestClient)"
uv run pytest -q
```

Boundary:

```text
test dependency hygiene only
remote warning result remains unverified until the next push
not product runtime evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## TestClient Dependency Warning Remote Verification

Phase marker: testclient dependency warning remote verification v0.

Use this artifact:

```text
docs/review/testclient-dependency-warning-remote-verification.md
```

Verified remote runs:

```text
remote run: 26969672909
workflow: CI
head: 29f1afa
job: api-smoke
job id: 79581346237
conclusion: success

remote run: 26969672911
workflow: External Feedback Screen
head: 29f1afa
job: screen
job id: 79581346224
conclusion: success
```

Observed result:

```text
check-run annotations: []
StarletteDeprecationWarning observed: no
TestClient fallback warning observed: no
generic `warning` text still appears in unrelated checkout hints and external-feedback JSON fields
```

Boundary:

```text
test dependency hygiene evidence only
not product runtime evidence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Uploaded file chunk persistence handoff review

Phase marker: uploaded file chunk persistence handoff review v0.

Use `docs/review/uploaded-file-chunk-persistence-handoff-review.md` when checking why the next product gate should be an explicit upload-to-chunks handoff endpoint instead of mutating the existing preview route.

Selected next product gate:

```text
uploaded file chunk persistence handoff endpoint v0
POST /documents/upload-chunks
```

Boundary:

```text
review-only
existing upload chunk preview remains preview-only
uses existing documents and document_chunks tables
not automatic persistence from upload preview
no raw uploaded byte storage
no full parsed text persistence
no embeddings
no retrieval persistence
```

## Uploaded file chunk persistence handoff endpoint

Phase marker: uploaded file chunk persistence handoff endpoint v0.

Use `POST /documents/upload-chunks` when you want an explicit uploaded-file-to-document-chunks handoff. This is separate from `POST /documents/upload-chunk-preview`, which remains preview-only.

```bash
curl -F "source_type=markdown" \
  -F "title=Uploaded market note" \
  -F "strategy=fixed-window" \
  -F "max_characters=120" \
  -F "overlap=0" \
  -F "file=@examples/messy-market-data/sample-note.md;type=text/markdown" \
  http://localhost:8000/documents/upload-chunks
```

Expected boundary:

```text
POST /documents/upload-chunks -> 201
UploadChunkPersistenceOut
creates a document row
creates document_chunks rows
explicit_upload_to_chunks_no_raw_file_storage
chunk_text_only_no_raw_file_storage
no raw uploaded byte storage
no full parsed text persistence
no embeddings
no retrieval persistence
```

This route-level implementation is not hosted deployment evidence. The next bounded proof gate is a local runtime smoke.

## Uploaded file chunk persistence handoff runtime smoke

Phase marker: uploaded file chunk persistence handoff runtime smoke v0.

This smoke uses Docker because NoiseProof's persistence claims depend on PostgreSQL/pgvector behavior, migration status, and live FastAPI HTTP calls against a database service rather than only in-memory route tests.

```powershell
docker compose config
docker compose up -d db
docker compose ps
cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55432/noiseproof"
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8034
```

Observed boundary:

```text
Applied migrations: 12
Pending migrations: 0
GET /health -> 200
POST /documents/upload-chunks -> 201
GET /documents -> 200
GET /documents/{document_id}/chunks -> 200
document_count_after_upload_chunks -> 4
chunk_count_after_upload_chunks -> 5
chunk_count_for_created_document -> 4
explicit_upload_to_chunks_no_raw_file_storage
chunk_text_only_no_raw_file_storage
no raw uploaded byte storage
no full parsed text persistence
no embeddings
no retrieval persistence
```

This is local runtime evidence only, not hosted deployment evidence or external reviewer feedback.

## Uploaded file chunk persistence handoff application refresh

Phase marker: uploaded file chunk persistence handoff application refresh v0.

Use `docs/review/uploaded-file-chunk-persistence-handoff-application-refresh.md` when checking how the upload-to-chunks handoff proof is surfaced in the application package.

This refresh points README, GOAL, runbook, portfolio index, Braincrew role map, and application-ready review surfaces to:

```text
docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md
POST /documents/upload-chunks
GET /documents/{document_id}/chunks
explicit_upload_to_chunks_no_raw_file_storage
chunk_text_only_no_raw_file_storage
```

This is documentation-only application packaging. It adds no runtime behavior, raw uploaded byte storage, full parsed text persistence, embeddings, retrieval persistence, hosted deployment evidence, external reviewer feedback, or product-complete claim.

## External reviewer chunk handoff request refresh

Phase marker: external reviewer chunk handoff request refresh v0.

Use `docs/review/external-reviewer-chunk-handoff-request-refresh.md` when checking why reviewer-facing request surfaces now point to the uploaded-file chunk handoff proof.

Reviewer-facing surfaces should include:

```text
uploaded-file chunk handoff proof
docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md
POST /documents/upload-chunks
explicit_upload_to_chunks_no_raw_file_storage
chunk_text_only_no_raw_file_storage
not external reviewer feedback
not hosted deployment evidence
```

This is request infrastructure only.

## External reviewer chunk handoff issue-body refresh

Phase marker: external reviewer chunk handoff issue-body refresh v0.

Use `docs/review/external-review-issue-body-chunk-handoff-refresh.md` when checking the owner-authored issue #1 body refresh.

The live issue body should include:

```text
uploaded-file chunk handoff proof
docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md
POST /documents/upload-chunks
explicit_upload_to_chunks_no_raw_file_storage
chunk_text_only_no_raw_file_storage
```

This is an owner-authored issue edit only, not external reviewer feedback.

## External feedback current-state chunk handoff issue verification

Phase marker: external feedback current-state chunk handoff issue verification v0.

Use `docs/review/external-feedback-current-state-chunk-handoff-issue-verification.md` when checking the live issue state after the uploaded-file chunk handoff issue-body refresh.

The live issue screen observed:

```text
updatedAt: 2026-06-02T00:37:18Z
first_codepoint: 35
comment_count: 1
candidate_count: 0
draft_count: 0
self_authored_comment
uploaded-file chunk handoff proof
docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md
POST /documents/upload-chunks
explicit_upload_to_chunks_no_raw_file_storage
chunk_text_only_no_raw_file_storage
```

This is a current-state screen only. It does not close external reviewer feedback v0.

## Uploaded file retrieval persistence review

Phase marker: uploaded file retrieval persistence review v0.

Use `docs/review/uploaded-file-retrieval-persistence-review.md` before adding retrieval persistence over uploaded-file chunks.

Selected future boundary:

```text
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
existing retrieval_runs table
existing document_chunks table
source_table = document_chunks
metadata_json.candidate_chunk_ids
no new retrieval_candidates table
```

This is review-only. It adds no runtime behavior, endpoint code, schema, migration, embeddings, semantic retrieval, Evidence Ledger generation, Noise Gate generation, report generation, financial advice behavior, hosted deployment evidence, external reviewer feedback, or product-complete claim.

## Uploaded file retrieval persistence endpoint

Phase marker: uploaded file retrieval persistence endpoint v0.

Use `POST /documents/{document_id}/retrieval-runs` after a document already has persisted `document_chunks` rows.

Example:

```bash
curl -X POST http://localhost:8000/documents/$DOCUMENT_ID/retrieval-runs \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which chunk supports enterprise demand growth?\",\"strategy\":\"fixed-window\",\"top_k\":3}"
```

Expected boundary markers:

```text
existing document_chunks table
existing retrieval_runs table
metadata_json.source_table = document_chunks
metadata_json.document_id
metadata_json.candidate_chunk_ids
document_chunk_retrieval_run_only_no_evidence_ledger
lexical only
no new retrieval_candidates table
no embeddings
no semantic retrieval
no Evidence Ledger generation
not financial advice
```

This endpoint creates a retrieval run row and candidate chunk references only. It does not create Evidence Ledger entries, Noise Gate records, report records, embeddings, semantic retrieval records, hosted deployment evidence, external reviewer feedback, or product-complete proof.

Next proof gate: uploaded file retrieval persistence runtime smoke v0.

## Uploaded file retrieval persistence runtime smoke

Phase marker: uploaded file retrieval persistence runtime smoke v0.

This smoke uses Docker because NoiseProof's retrieval persistence claim depends on PostgreSQL/pgvector behavior, migration status, and live FastAPI HTTP calls against a database service.

```powershell
docker compose up -d db
docker compose ps
cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55432/noiseproof"
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8035
```

Observed boundary:

```text
Applied migrations: 12
Pending migrations: 0
GET /health -> 200
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
GET /retrieval-runs -> 200
upload_chunk_count -> 4
retrieval_result_count -> 2
retrieval_missing_evidence_count -> 0
metadata_source_table -> document_chunks
metadata_candidate_chunk_ids -> 3bbef26c-44a2-467a-8255-55be7791bb0a,687cc699-2c34-4eae-a90a-79cf1ad86b54
latest_listed_id_matches -> True
first_candidate_source_table -> document_chunks
no Evidence Ledger generation
not financial advice
```

This is local runtime evidence only. It is not hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, production readiness, Evidence Ledger generation, semantic retrieval, embeddings, or financial advice.

Next packaging gate: uploaded file retrieval persistence application refresh v0.

## Uploaded file retrieval persistence application refresh

Phase marker: uploaded file retrieval persistence application refresh v0.

This refresh is documentation-only application packaging for the uploaded-file retrieval persistence runtime smoke.

Primary proof:

```text
docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md
```

Application-facing artifact:

```text
docs/review/uploaded-file-retrieval-persistence-application-refresh.md
```

Surfaces refreshed:

```text
README.md
docs/GOAL.md
docs/application/portfolio-index.md
docs/application/braincrew-role-map.md
docs/review/application-ready-review.md
docs/review/readme-proof-marker-archive.md
```

Boundary:

```text
no runtime behavior added
no Evidence Ledger generation
no embeddings
no semantic retrieval
not hosted deployment evidence
not external reviewer feedback
not financial advice
```

Next reviewer-facing gate: external reviewer retrieval persistence request refresh v0.

## External reviewer retrieval persistence request refresh

Phase marker: external reviewer retrieval persistence request refresh v0.

Use `docs/review/external-reviewer-retrieval-persistence-request-refresh.md` when checking why reviewer-facing request surfaces now point to the uploaded-file retrieval persistence proof.

Reviewer-facing surfaces refreshed:

```text
CONTRIBUTING.md
.github/ISSUE_TEMPLATE/external-review-feedback.md
docs/review/external-review-request.md
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
docs/application/portfolio-index.md
```

Proof label:

```text
uploaded-file retrieval persistence proof
```

Proof artifact:

```text
docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md
```

Boundary:

```text
request infrastructure only
does not edit the live public issue body
not external reviewer feedback
not hosted deployment evidence
no Evidence Ledger generation
not semantic retrieval
not financial advice
```

Next live issue-body gate: external reviewer retrieval persistence issue-body refresh v0.

## External reviewer retrieval persistence issue-body refresh

Phase marker: external reviewer retrieval persistence issue-body refresh v0.

Use `docs/review/external-review-issue-body-retrieval-persistence-refresh.md` when checking the owner-authored issue #1 body refresh.

Observed live issue markers:

```text
updatedAt: 2026-06-02T04:14:29Z
first_codepoint: 35
startsWith: ## Request
comment_count: 1
owner_comment_count: 1
uploaded-file retrieval persistence proof body marker
docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md body marker
POST /documents/{document_id}/retrieval-runs body marker
metadata_json.candidate_chunk_ids body marker
metadata_source_table = document_chunks body marker
```

Boundary:

```text
owner-authored issue edit
not external reviewer feedback
not hosted deployment evidence
no Evidence Ledger generation
not semantic retrieval
not financial advice
```

Next evidence gate remains: external reviewer feedback v0.

## External feedback current-state retrieval persistence issue verification

Phase marker: external feedback current-state retrieval persistence issue verification v0.

Use `docs/review/external-feedback-current-state-retrieval-persistence-issue-verification.md` when checking the live issue state after the uploaded-file retrieval persistence issue-body refresh.

Observed live issue and screening state:

```text
issue_state: OPEN
updatedAt: 2026-06-02T04:14:29Z
first_codepoint: 35
startsWith: ## Request
comment_count: 1
candidate_count: 0
draft_count: 0
self_authored_comment
non_qualifying
```

Issue body markers:

```text
uploaded-file retrieval persistence proof
docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md
POST /documents/{document_id}/retrieval-runs
metadata_json.candidate_chunk_ids
metadata_source_table = document_chunks
no Evidence Ledger generation
not hosted deployment evidence
not external reviewer feedback
```

Boundary:

```text
not external reviewer feedback
does not close external reviewer feedback v0
not customer validation
not Braincrew acceptance
not hosted deployment evidence
```

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

Do not claim persisted chunks, embeddings, DB persistence for collection plans, distributed tracing, hosted observability, or free-form answer generation exists until those stages are implemented and verified with examples. `workflow_runs` can be created, listed, viewed on the dashboard, created by a deterministic execution-preview endpoint, and inspected through `GET /workflow-runs/{id}`. That preview runs retrieval -> evidence -> gate -> report deterministically, Phase 29 attaches those child records to nullable `workflow_run_id` fields while still carrying `workflow_trace_id`, and Phase 30 exposes those child records from the parent workflow detail response. Phase 31 records `stage_input_manifest` on deterministic workflow-created Noise Gate and Report rows so persisted upstream ids are visible, Phase 32 exposes `GET /workflow-runs/{id}/lineage`, and Phase 530 records direct local stage links for workflow-created records in `noise_gate_evidence_links`, `report_evidence_links`, and `report_noise_gate_links`. Standalone gate/report endpoints remain payload-only unless they create explicit stage links. The current dashboard is a plain operations view over existing metadata, not a polished product UI. Direct `agent_run_id` child-record linkage exists for persisted Evidence Ledger, Noise Gate, and Report records, but it remains local service provenance rather than distributed tracing.
## Retrieval-run-linked Evidence Ledger Endpoint

Phase 202 adds a bounded handoff from persisted retrieval runs to persisted Evidence Ledger rows. Phase 203 records the local Docker DB plus live FastAPI HTTP smoke for that handoff.

Endpoint:

```text
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
```

Minimal local sequence:

```powershell
docker compose up -d db
cd apps/api
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000
```

In another shell, create a document with chunks, create a document-scoped retrieval run, then hand the persisted retrieval run to the Evidence Ledger:

```powershell
$document = Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/documents -ContentType 'application/json' -Body '{"source_type":"markdown","source_uri":"upload://sample.md","filename":"sample.md","title":"Sample market note"}'
$chunk = Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/documents/$($document.id)/chunks" -ContentType 'application/json' -Body '{"source_type":"markdown","source_uri":"upload://sample.md","filename":"sample.md","chunk_strategy":"fixed-window","chunk_index":0,"chunk_text":"Enterprise demand growth reached 12% in 2026.","metadata_json":{"header_path":["Demand"]}}'
$retrieval = Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/documents/$($document.id)/retrieval-runs" -ContentType 'application/json' -Body '{"question":"Which chunk supports enterprise demand growth?","strategy":"fixed-window","top_k":2}'
$ledger = Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/retrieval-runs/$($retrieval.id)/evidence-ledger"
$ledger.entries[0].retrieval_run_id
```

Expected boundary markers:

- `stored_entry_count` is greater than zero when candidate chunks exist.
- `entries[].retrieval_run_id` matches the persisted retrieval run id.
- warnings mention persisted `retrieval_run`, no LLM, no embeddings, no semantic retrieval, and no final truth judgment.

This is not a Noise Gate, not a report, not hosted deployment evidence, not external reviewer feedback, and not financial advice.

## Retrieval-run-linked Noise Gate Endpoint

Phase 204 adds a bounded handoff from persisted retrieval runs and linked Evidence Ledger rows to persisted Noise Gate records. Phase 205 records the local Docker DB plus live FastAPI HTTP smoke for that handoff.

Endpoint:

```text
POST /retrieval-runs/{retrieval_run_id}/noise-gate
```

Minimal local sequence:

```powershell
docker compose up -d db
cd apps/api
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@127.0.0.1:55432/noiseproof'
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8032
```

In another shell, create a document with chunks, create a document-scoped retrieval run, confirm the gate does not run before ledger rows exist, then create the linked ledger and gate:

```powershell
$base='http://127.0.0.1:8032'
$document = Invoke-RestMethod -Method Post -Uri "$base/documents" -ContentType 'application/json' -Body '{"source_type":"markdown","source_uri":"upload://phase204-smoke.md","filename":"phase204-smoke.md","title":"Phase 204 smoke note"}'
$chunk = Invoke-RestMethod -Method Post -Uri "$base/documents/$($document.id)/chunks" -ContentType 'application/json' -Body '{"source_type":"markdown","source_uri":"upload://phase204-smoke.md","filename":"phase204-smoke.md","chunk_strategy":"fixed-window","chunk_index":0,"chunk_text":"Enterprise demand growth reached 12% in 2026.","metadata_json":{"header_path":["Demand"]}}'
$retrieval = Invoke-RestMethod -Method Post -Uri "$base/documents/$($document.id)/retrieval-runs" -ContentType 'application/json' -Body '{"question":"Which chunk supports enterprise demand growth?","strategy":"fixed-window","top_k":1}'
try { Invoke-RestMethod -Method Post -Uri "$base/retrieval-runs/$($retrieval.id)/noise-gate" } catch { [int]$_.Exception.Response.StatusCode }
$ledger = Invoke-RestMethod -Method Post -Uri "$base/retrieval-runs/$($retrieval.id)/evidence-ledger"
$gate = Invoke-RestMethod -Method Post -Uri "$base/retrieval-runs/$($retrieval.id)/noise-gate"
$gate.stage_input_manifest.retrieval_run_id
$gate.stage_input_manifest.input_evidence_ledger_entry_ids
```

Expected boundary markers:

- pre-ledger `POST /retrieval-runs/{retrieval_run_id}/noise-gate` returns `409`.
- `evidence_entry_count` matches the linked ledger entry count.
- `stage_input_manifest.retrieval_run_id` matches the persisted retrieval run id.
- `stage_input_manifest.input_evidence_ledger_entry_ids` references the persisted Evidence Ledger row ids.
- warnings mention retrieval-run-linked Evidence Ledger rows, no LLM, no embeddings, no semantic retrieval, no report generation, and no financial advice.

This is not report generation, not automatic failure-case creation, not hosted deployment evidence, not external reviewer feedback, and not financial advice.

## Retrieval-run-linked Report Endpoint

Phase 206 adds a bounded handoff from persisted retrieval runs, linked Evidence Ledger rows, and linked Noise Gate records to persisted Report records. Phase 207 records the local Docker DB plus live FastAPI HTTP smoke for that handoff.

Endpoint:

```text
POST /retrieval-runs/{retrieval_run_id}/report
```

Minimal local sequence:

```powershell
docker compose up -d db
cd apps/api
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@127.0.0.1:55432/noiseproof'
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8033
```

In another shell, create a retrieval run, create linked Evidence Ledger rows, confirm the report does not persist before a linked Noise Gate exists, then create the gate and report:

```powershell
$base='http://127.0.0.1:8033'
$document = Invoke-RestMethod -Method Post -Uri "$base/documents" -ContentType 'application/json' -Body '{"source_type":"markdown","source_uri":"upload://phase206-smoke.md","filename":"phase206-smoke.md","title":"Phase 206 smoke note"}'
$chunk = Invoke-RestMethod -Method Post -Uri "$base/documents/$($document.id)/chunks" -ContentType 'application/json' -Body '{"source_type":"markdown","source_uri":"upload://phase206-smoke.md","filename":"phase206-smoke.md","chunk_strategy":"fixed-window","chunk_index":0,"chunk_text":"Enterprise demand growth reached 12% in 2026.","metadata_json":{"header_path":["Demand"]}}'
$retrieval = Invoke-RestMethod -Method Post -Uri "$base/documents/$($document.id)/retrieval-runs" -ContentType 'application/json' -Body '{"question":"Which chunk supports enterprise demand growth?","strategy":"fixed-window","top_k":1}'
$ledger = Invoke-RestMethod -Method Post -Uri "$base/retrieval-runs/$($retrieval.id)/evidence-ledger"
try { Invoke-RestMethod -Method Post -Uri "$base/retrieval-runs/$($retrieval.id)/report" } catch { [int]$_.Exception.Response.StatusCode }
$gate = Invoke-RestMethod -Method Post -Uri "$base/retrieval-runs/$($retrieval.id)/noise-gate"
$report = Invoke-RestMethod -Method Post -Uri "$base/retrieval-runs/$($retrieval.id)/report"
$report.stage_input_manifest.retrieval_run_id
$report.stage_input_manifest.input_noise_gate_record_id
$report.stage_input_manifest.input_evidence_ledger_entry_ids
```

Expected boundary markers:

- pre-gate `POST /retrieval-runs/{retrieval_run_id}/report` returns `409`.
- `evidence_entry_count` matches the linked ledger entry count.
- `stage_input_manifest.retrieval_run_id` matches the persisted retrieval run id.
- `stage_input_manifest.input_noise_gate_record_id` references the linked Noise Gate record id.
- `stage_input_manifest.input_evidence_ledger_entry_ids` references the persisted Evidence Ledger row ids.
- warnings mention retrieval-run-linked Noise Gate and Evidence Ledger rows, no LLM, no embeddings, no semantic retrieval, no failure-case creation, and no financial advice.

This is not free-form final report generation, not automatic failure-case creation, not hosted deployment evidence, not external reviewer feedback, and not financial advice.

## External Reviewer Report Handoff Refresh

Phase 208 updates the reviewer-facing request surfaces so outside reviewers can find the latest retrieval-run-linked Report proof without walking the whole repository history.

Proof links to check:

```text
docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md
docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md
docs/review/retrieval-run-linked-report-runtime-smoke.md
```

The phase marker is:

```text
external reviewer report handoff request refresh v0
```

Phase 209 records the owner-authored public issue #1 body refresh:

```text
docs/review/external-review-issue-body-report-handoff-refresh.md
external reviewer report handoff issue-body refresh v0
```

Phase 210 records the current live issue state after that refresh:

```text
docs/review/external-feedback-current-state-report-handoff-issue-verification.md
external feedback current-state report handoff issue verification v0
```

Expected issue-state boundary:

```text
comment_count: 1
candidate_count: 0
draft_count: 0
self_authored_comment
non_qualifying
```

This is not external reviewer feedback, not hosted deployment evidence, not customer validation, not Braincrew acceptance, and not product-complete.

## Application-ready Report Handoff Checklist Refresh

Phase 211 refreshes `docs/review/application-ready-review.md` so the application-ready checklist names the current linked Noise Gate and Report proof rows.

The phase marker is:

```text
application-ready report handoff checklist refresh v0
```

Rows expected in the checklist:

```text
retrieval-run-linked Noise Gate persistence exists
retrieval-run-linked Report persistence exists
```

This is documentation-only checklist hygiene. It is not external reviewer feedback, not hosted deployment evidence, not customer validation, not Braincrew acceptance, and not product-complete.

## Retrieval-run-linked Proof Surface Regression Coverage

Phase 212 adds a docs regression guard for the retrieval-run-linked proof chain.

The phase marker is:

```text
retrieval-run-linked proof surface regression coverage v0
```

The coverage artifact is:

```text
docs/review/retrieval-run-linked-proof-surface-regression-coverage.md
```

It keeps these endpoint docs and runtime smoke docs together:

```text
docs/review/retrieval-run-linked-evidence-ledger-endpoint.md
docs/review/retrieval-run-linked-noise-gate-endpoint.md
docs/review/retrieval-run-linked-report-endpoint.md
docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md
docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md
docs/review/retrieval-run-linked-report-runtime-smoke.md
```

This is documentation regression coverage only. It is not runtime behavior, not external reviewer feedback, not hosted deployment evidence, not customer validation, not Braincrew acceptance, and not product-complete.

## Semantic Retrieval Readiness Review

Phase 213 is a source-first review before any semantic retrieval work.

The phase marker is:

```text
semantic retrieval readiness review v0
```

Primary sources:

```text
https://github.com/pgvector/pgvector
https://sbert.net/docs/quickstart.html
https://www.postgresql.org/docs/current/static/pgtrgm.html
```

Selected next product gate:

```text
embedding schema review v0
```

Do not implement embeddings in this gate. Do not add HNSW, IVFFlat, vector indexes, semantic retrieval, or model dependencies until the schema boundary is reviewed.

## Embedding Schema Review

Phase 214 is a review-only schema decision before any embedding migration.

The phase marker is:

```text
embedding schema review v0
```

Review artifact:

```text
docs/review/embedding-schema-review.md
```

Selected future table boundary:

```text
chunk_embeddings
```

Selected next product gate:

```text
embedding schema migration v0
```

Do not add a vector column in this gate. Do not add embedding generation, semantic retrieval, HNSW, IVFFlat, model dependencies, or retrieval ranking behavior until the migration and runtime gates explicitly open.

## Embedding Schema Migration

Phase 215 is a schema-only migration gate.

The phase marker is:

```text
embedding schema migration v0
```

Review artifact:

```text
docs/review/embedding-schema-migration.md
```

Migration file:

```text
db/migrations/015_chunk_embeddings.sql
```

Fresh DB schema mirror:

```text
db/init/001_schema.sql
```

This gate adds `chunk_embeddings` only as a schema boundary. It does not generate embeddings, create repository functions, create API endpoints, run semantic retrieval, or add HNSW/IVFFlat indexes.

Next verification gate:

```text
embedding schema runtime verification v0
```

## Embedding Schema Runtime Verification

Phase 216 records local Docker PostgreSQL/pgvector runtime evidence.

The phase marker is:

```text
embedding schema runtime verification v0
```

Review artifact:

```text
docs/review/embedding-schema-runtime-verification.md
```

Observed migration runner status:

```text
Applied migrations: 0
Pending migrations: 14
Applied migrations: 14
Pending migrations: 0
```

Observed schema target:

```text
015_chunk_embeddings.sql
chunk_embeddings
embedding vector
embedding_model
```

This is local runtime evidence only. It is not embedding generation, not semantic retrieval implementation, not hosted deployment evidence, and not external reviewer feedback.

## Embedding Repository Review

Phase 217 is a review-only repository boundary gate.

The phase marker is:

```text
embedding repository review v0
```

Review artifact:

```text
docs/review/embedding-repository-review.md
```

Selected next boundary:

```text
ChunkEmbeddingCreate
create_chunk_embedding
list_chunk_embeddings
```

This review adds no repository code. It selects a metadata/persistence boundary only. Do not generate embeddings in repository code.

## Embedding Repository v0

Phase 218 adds metadata/persistence-only repository code for caller-provided vectors.

The phase marker is:

```text
embedding repository v0
```

Review artifact:

```text
docs/review/embedding-repository.md
```

Implemented code:

```text
ChunkEmbeddingCreate
create_chunk_embedding
list_chunk_embeddings
```

Smoke check:

```powershell
cd C:\Users\admin\Desktop\noiseproof-agent\apps\api
uv run pytest tests/test_db.py -q -k "chunk_embedding"
```

This repository boundary is metadata/persistence only. It accepts a caller-provided vector and stores it in `chunk_embeddings`; it does not create an endpoint, generate embeddings, perform semantic retrieval, or add HNSW/IVFFlat index behavior.

## Embedding Endpoint Review

Phase 219 is a review-only endpoint boundary gate.

The phase marker is:

```text
embedding endpoint review v0
```

Review artifact:

```text
docs/review/embedding-endpoint-review.md
```

Selected future routes:

```text
POST /chunks/{chunk_id}/embeddings
GET /chunks/{chunk_id}/embeddings
```

Selected repository handoff:

```text
ChunkEmbeddingCreate
ChunkEmbeddingOut
create_chunk_embedding
list_chunk_embeddings
embedding_source = caller_provided_vector
```

This review adds no endpoint code. Do not generate embeddings, run semantic retrieval, create HNSW/IVFFlat index behavior, generate Evidence Ledger rows, or call external model APIs in this gate.

## Embedding Endpoint v0

Phase 220 adds route-level caller-provided chunk embedding persistence.

The phase marker is:

```text
embedding endpoint v0
```

Review artifact:

```text
docs/review/embedding-endpoint.md
```

Routes:

```text
POST /chunks/{chunk_id}/embeddings
GET /chunks/{chunk_id}/embeddings
```

Local test:

```powershell
cd C:\Users\admin\Desktop\noiseproof-agent\apps\api
uv run pytest tests/test_routes.py -q -k "chunk_embedding_endpoint"
```

The endpoint accepts caller-provided vector payloads only and adds `caller_provided_embedding_only_no_generation` to metadata. It rejects generated embedding claims and dimension mismatches. It is not embedding generation, not semantic retrieval implementation, not HNSW or IVFFlat index behavior, and not Evidence Ledger generation.

## Embedding Endpoint Runtime Smoke

Phase 221 records local Docker DB plus live FastAPI HTTP evidence for caller-provided chunk embedding persistence.

The phase marker is:

```text
embedding endpoint runtime smoke v0
```

Review artifact:

```text
docs/review/embedding-endpoint-runtime-smoke.md
```

Observed:

```text
Docker container: noiseproof-agent-embedding-endpoint-db-64179
Applied migrations: 14
Pending migrations: 0
POST /chunks/{chunk_id}/embeddings -> 201
GET /chunks/{chunk_id}/embeddings -> 200
generated embedding claim -> 400
caller_provided_embedding_only_no_generation
```

The runtime smoke found and fixed a pgvector response serialization issue: pgvector returned vector text, so repository output now normalizes `chunk_embeddings.embedding` into `list[float]` before FastAPI response validation.

## Embedding Endpoint Application Refresh

Phase 222 surfaces the embedding endpoint runtime smoke in application-facing docs.

The phase marker is:

```text
embedding endpoint application refresh v0
```

Review artifact:

```text
docs/review/embedding-endpoint-application-refresh.md
```

Primary proof:

```text
docs/review/embedding-endpoint-runtime-smoke.md
```

Claim boundary:

```text
caller-provided chunk embedding endpoint exists
not embedding generation
not semantic retrieval implementation
not hosted deployment evidence
```

## Semantic Retrieval Implementation Review

Phase 223 selects the next semantic retrieval implementation boundary without adding runtime behavior.

The phase marker is:

```text
semantic retrieval implementation review v0
```

Review artifact:

```text
docs/review/semantic-retrieval-implementation-review.md
```

Selected next gate:

```text
semantic retrieval preview endpoint v0
```

Implementation boundary selected by the review:

```text
POST /documents/{document_id}/semantic-retrieval-preview
caller-provided query vector
chunk_embeddings.embedding <=> query_embedding
exact cosine ranking first
```

Claim boundary:

```text
no embedding generation
no HNSW or IVFFlat index
no LLM calls
not persisted semantic retrieval
not hosted deployment evidence
```

## Semantic Retrieval Preview Endpoint

Phase 224 adds a preview-only endpoint for semantic retrieval over existing chunk and embedding rows.

The phase marker is:

```text
semantic retrieval preview endpoint v0
```

Review artifact:

```text
docs/review/semantic-retrieval-preview-endpoint.md
```

Endpoint:

```text
POST /documents/{document_id}/semantic-retrieval-preview
```

Local smoke shape after a document, chunks, and caller-provided chunk embeddings exist:

```bash
curl -X POST http://localhost:8000/documents/<document_id>/semantic-retrieval-preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which chunk is closest to demand growth?\",\"query_embedding\":[1.0,0.0],\"embedding_model\":\"local-test-model\",\"embedding_dimension\":2,\"limit\":5}"
```

Expected response markers:

```text
retrieval_mode = semantic_preview
persistence_boundary = preview_only_not_persisted
ranking_boundary = exact_cosine_caller_provided_query_vector
metadata_json.candidate_chunk_ids
missing_embedding_chunk_ids
```

Claim boundary:

```text
caller-provided query vector only
not retrieval_runs persistence
not embedding generation
not Evidence Ledger generation
not vector search quality evidence
not hosted deployment evidence
```

## Semantic Retrieval Persistence Endpoint

Phase 227 implements the endpoint selected by the semantic retrieval persistence review.

The phase marker is:

```text
semantic retrieval persistence endpoint v0
```

Review artifact:

```text
docs/review/semantic-retrieval-persistence-endpoint.md
```

Endpoint:

```text
POST /documents/{document_id}/semantic-retrieval-runs
```

Request:

```json
{
  "question": "Which chunk is closest to demand growth?",
  "query_embedding": [1.0, 0.0],
  "embedding_model": "local-test-model",
  "embedding_dimension": 2,
  "limit": 2
}
```

Expected behavior:

```text
creates one retrieval_runs row
strategy = semantic-cosine
metadata_json.retrieval_mode = semantic_persisted
metadata_json.candidate_chunk_ids
metadata_json.candidate_embedding_ids
metadata_json.missing_embedding_chunk_ids
metadata_json.persistence_boundary = semantic_retrieval_run_only_no_evidence_ledger
```

Claim boundary:

```text
not runtime smoke evidence
not embedding generation
not Evidence Ledger generation
not vector search quality evidence
not hosted deployment evidence
```

## Semantic Retrieval Persistence Runtime Smoke

Phase 228 verifies the semantic retrieval persistence endpoint against local Docker PostgreSQL/pgvector and live FastAPI HTTP.

The phase marker is:

```text
semantic retrieval persistence runtime smoke v0
```

Review artifact:

```text
docs/review/semantic-retrieval-persistence-runtime-smoke.md
```

Environment:

```text
local Docker DB plus live FastAPI HTTP
noiseproof-agent-db on localhost:55432
FastAPI on 127.0.0.1:8038
Applied migrations: 14
Pending migrations: 0
```

Observed endpoint checks:

```text
GET /health -> 200
POST /documents/{document_id}/semantic-retrieval-runs -> 201
GET /retrieval-runs -> 200
retrieval_run_count_after = retrieval_run_count_before + 1
dimension mismatch -> 400
evidence_ledger_count_unchanged -> true
metadata_json.retrieval_mode = semantic_persisted
```

Claim boundary:

```text
not embedding generation
not Evidence Ledger generation
not vector search quality evidence
not hosted deployment evidence
```

## Semantic Retrieval Persistence Application Refresh

Phase 229 surfaces the semantic retrieval persistence runtime proof in application-facing docs.

The phase marker is:

```text
semantic retrieval persistence application refresh v0
```

Review artifact:

```text
docs/review/semantic-retrieval-persistence-application-refresh.md
```

Primary runtime proof:

```text
docs/review/semantic-retrieval-persistence-runtime-smoke.md
```

Allowed claim:

```text
caller-provided semantic retrieval persistence has local runtime proof
```

Claim boundary:

```text
not embedding generation
not vector search quality evidence
not Evidence Ledger generation from semantic retrieval
not hosted deployment evidence
```

## Semantic Retrieval Quality Review

Phase 230 selects the smallest semantic retrieval quality-evaluation boundary before any quality claim.

The phase marker is:

```text
semantic retrieval quality review v0
```

Review artifact:

```text
docs/review/semantic-retrieval-quality-review.md
```

Sources checked:

```text
TREC / NIST retrieval evaluation
BEIR
Sentence Transformers InformationRetrievalEvaluator
docs/research/meaningful-information-collection.md
```

Candidate metrics:

```text
Hit@k
Recall@k
MRR@k
nDCG@k
missing_embedding_rate
semantic_vs_lexical_disagreement
role_coverage_at_k
```

Next gate:

```text
semantic retrieval quality fixture v0
```

Claim boundary:

```text
not embedding generation
not vector search quality evidence
not benchmark result
not model comparison
not Evidence Ledger generation
```

## Semantic Retrieval Quality Fixture

Phase 231 adds the small local fixture selected by the semantic retrieval quality review.

The phase marker is:

```text
semantic retrieval quality fixture v0
```

Fixture path:

```text
examples/semantic-retrieval-quality/README.md
examples/semantic-retrieval-quality/manifest.json
examples/semantic-retrieval-quality/corpus.json
examples/semantic-retrieval-quality/queries.json
```

Loader:

```text
packages/ingestion/retrieval/quality_fixture.py
```

Fixture contents:

```text
4 queries
6 corpus chunks
8 qrels
caller-provided 3-dimensional toy vectors
one missing embedding case
information-role labels
```

Smoke check:

```bash
uv run pytest tests/test_semantic_quality_fixture.py -q
```

Claim boundary:

```text
not embedding generation
not vector search quality evidence
not benchmark result
not model comparison
not Evidence Ledger generation
```

## Semantic Retrieval Quality Evaluator

Phase 232 adds a tiny evaluator over the local semantic retrieval quality fixture.

The phase marker is:

```text
semantic retrieval quality evaluator v0
```

Evaluator:

```text
packages/ingestion/retrieval/quality_metrics.py
evaluate_semantic_quality
```

Metrics:

```text
Hit@k
Recall@k
MRR@k
nDCG@k
missing_embedding_rate
semantic_vs_lexical_disagreement
role_coverage_at_k
```

Claim boundary:

```text
toy_fixture_metric_only_not_search_quality
not embedding generation
not vector search quality evidence
not benchmark result
not model comparison
not Evidence Ledger generation
```

Smoke check:

```bash
uv run pytest tests/test_semantic_quality_evaluator.py -q
```

## Semantic Retrieval Quality Report

Phase 233 records the toy fixture evaluator output as a bounded evaluation report.

The phase marker is:

```text
semantic retrieval quality report v0
```

Report:

```text
docs/evaluation/semantic-retrieval-quality-report.md
```

Recorded aggregate output:

```text
Hit@k = 0.75
Recall@k = 0.375
MRR@k = 0.375
nDCG@k = 0.198
missing_embedding_rate = 0.1667
semantic_vs_lexical_disagreement = 0.9167
role_coverage_at_k = 0.625
```

Important failure kept visible:

```text
q-what-missing retrieves no relevant semantic candidate in this toy fixture
```

Claim boundary:

```text
not embedding generation
not vector search quality evidence
not benchmark result
not model comparison
not Evidence Ledger generation
```

## Semantic Retrieval Quality Report Application Refresh

Phase 234 surfaces the toy report in application-facing docs without treating it as quality evidence.

The phase marker is:

```text
semantic retrieval quality report application refresh v0
```

Refresh artifact:

```text
docs/review/semantic-retrieval-quality-report-application-refresh.md
```

Primary report:

```text
docs/evaluation/semantic-retrieval-quality-report.md
```

Application surfaces updated:

```text
docs/application/portfolio-index.md
docs/application/braincrew-role-map.md
docs/review/application-ready-review.md
docs/review/external-reader-proof-path.md
```

Claim boundary:

```text
toy fixture metric output only
not vector search quality evidence
not benchmark result
not model comparison
not production semantic retrieval quality
```

## Semantic Retrieval Quality Report Reviewer Request Refresh

Phase marker: semantic retrieval quality report reviewer request refresh v0.

Use `docs/review/semantic-retrieval-quality-report-reviewer-request-refresh.md` when checking why reviewer-facing request surfaces now point to the toy semantic retrieval quality report.

Reviewer-facing surfaces:

```text
CONTRIBUTING.md
.github/ISSUE_TEMPLATE/external-review-feedback.md
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
```

Report:

```text
docs/evaluation/semantic-retrieval-quality-report.md
```

This is request infrastructure only. It does not update the live public issue body and is not external reviewer feedback. The next request gate is `semantic retrieval quality report reviewer issue-body refresh v0`.

Boundary:

```text
toy semantic retrieval quality report
not vector search quality evidence
not hosted deployment evidence
not Braincrew acceptance
```

## Semantic Retrieval Quality Report Issue Body Refresh

Phase marker: semantic retrieval quality report reviewer issue-body refresh v0.

Use `docs/review/semantic-retrieval-quality-report-issue-body-refresh.md` when checking the live owner-authored issue body update that points issue #1 to the toy semantic retrieval quality report.

Public issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed after edit:

```text
has_report = true
has_boundary = true
has_q = true
comment_count = 1
```

This is an owner-authored issue edit only. It is not external reviewer feedback, not hosted deployment evidence, and not Braincrew acceptance.

## External Feedback Current-state Semantic Quality Report Issue Verification

Phase marker: external feedback current-state semantic quality report issue verification v0.

Use `docs/review/external-feedback-current-state-semantic-quality-report-issue-verification.md` when checking the live issue state after the semantic quality report issue-body refresh.

Observed:

```text
state = OPEN
labels = external-review, feedback
comment_count = 1
self_authored_comments = 1
candidate_count = 0
draft_count = 0
has_report = true
has_boundary = true
has_q = true
```

This is a current-state screen only. It is not external reviewer feedback and does not close external reviewer feedback v0.

## Semantic Retrieval Quality Report Proof Surface Regression Coverage

Phase marker: semantic retrieval quality report proof surface regression coverage v0.

Use `docs/review/semantic-retrieval-quality-report-proof-surface-regression-coverage.md` when checking that the semantic retrieval quality report chain still links the review, fixture, metric code, report, application refresh, reviewer request refresh, live issue-body refresh, and current-state screen.

This is documentation/test regression coverage only. It is not embedding generation, not vector search quality evidence, not a benchmark result, not a model comparison, not hosted deployment evidence, and not external reviewer feedback.

The visible miss marker remains:

```text
q-what-missing
```

## Semantic Retrieval Quality Report Proof Surface Final Scan

Phase marker: semantic retrieval quality report proof surface final scan v0.

Use `docs/review/semantic-retrieval-quality-report-proof-surface-final-scan.md` when checking that application-facing semantic retrieval quality report surfaces do not turn toy fixture metrics into a positive quality claim.

Observed scan result:

```text
stale_positive_quality_claim_count: 0
```

This is documentation scan evidence only. It is not vector search quality evidence, not a benchmark result, not a model comparison, not hosted deployment evidence, and not external reviewer feedback.

## Semantic Retrieval Quality Report Regeneration Command

Phase marker: semantic retrieval quality report regeneration command v0.

Use `docs/review/semantic-retrieval-quality-report-regeneration-command.md` when checking how to regenerate `docs/evaluation/semantic-retrieval-quality-report.md` from explicit local fixture inputs.

Run from `apps/api`:

```bash
uv run python -m app.services.semantic_quality_report_command \
  --fixture ../../examples/semantic-retrieval-quality \
  --rankings ../../examples/semantic-retrieval-quality/rankings.json \
  --output ../../docs/evaluation/semantic-retrieval-quality-report.md \
  --k 2
```

This is byte-for-byte regeneration plumbing only. It is not embedding generation, not vector search quality evidence, not a benchmark result, not a model comparison, and not external reviewer feedback.

## Semantic Retrieval Quality Report Regeneration Failure Boundary

Phase marker: semantic retrieval quality report regeneration failure boundary v0.

Use `docs/review/semantic-retrieval-quality-report-regeneration-failure-boundary.md` when checking how the report regeneration command handles a malformed rankings fixture.

Expected failure markers:

```text
exit code 2
semantic_quality_report_regeneration_failed
semantic_rankings
not vector search quality evidence
no traceback
```

This is command failure handling only. It is not vector search quality evidence, not a benchmark result, not a model comparison, and not external reviewer feedback.

## Semantic Retrieval Quality Report Check Mode

Phase marker: semantic retrieval quality report check mode v0.

Use `docs/review/semantic-retrieval-quality-report-check-mode.md` when checking whether the committed toy semantic retrieval quality report still matches byte-for-byte regeneration.

Run from `apps/api`:

```bash
uv run python -m app.services.semantic_quality_report_command \
  --fixture ../../examples/semantic-retrieval-quality \
  --rankings ../../examples/semantic-retrieval-quality/rankings.json \
  --output ../../docs/evaluation/semantic-retrieval-quality-report.md \
  --k 2 \
  --check
```

Current marker: `semantic_quality_report_current`.

Stale marker: `semantic_quality_report_stale`, exit code 3, `byte-for-byte regeneration mismatch`.

This is staleness detection only. It is not vector search quality evidence, not a benchmark result, not a model comparison, and not external reviewer feedback.

## Semantic Retrieval Quality Report CI Check

Phase marker: semantic retrieval quality report ci check v0.

Use `docs/review/semantic-retrieval-quality-report-ci-check.md` when checking why CI runs the semantic retrieval quality report staleness command.

The GitHub Actions step is named:

```text
Check semantic retrieval quality report staleness
```

It runs the existing check-only command:

```bash
uv run python -m app.services.semantic_quality_report_command \
  --fixture ../../examples/semantic-retrieval-quality \
  --rankings ../../examples/semantic-retrieval-quality/rankings.json \
  --output ../../docs/evaluation/semantic-retrieval-quality-report.md \
  --k 2 \
  --check
```

Current marker: `semantic_quality_report_current`.

This is CI staleness protection only. It is not vector search quality evidence, not a benchmark result, not a model comparison, and not external reviewer feedback.

## Semantic Retrieval Quality Report CI Remote Verification

Phase marker: semantic retrieval quality report ci remote verification v0.

Use `docs/review/semantic-retrieval-quality-report-ci-remote-verification.md` when checking the remote GitHub Actions evidence for the semantic retrieval quality report staleness step.

Verified remote run:

```text
remote run: 26846871670
job: api-smoke
job id: 79168651555
head: 5c9ac05
step number: 7
step name: Check semantic retrieval quality report staleness
conclusion: success
```

This is remote CI execution evidence for staleness protection only. It is not vector search quality evidence, not a benchmark result, not a model comparison, not hosted deployment evidence, and not external reviewer feedback.

## Semantic Retrieval Quality Report CI Remote Issue-body Refresh

Phase marker: semantic retrieval quality report ci remote issue-body refresh v0.

Use `docs/review/semantic-retrieval-quality-report-ci-remote-issue-body-refresh.md` when checking why issue #1 now points reviewers to the semantic quality CI remote verification proof.

Observed live issue markers after the owner-authored edit:

```text
has_ci_remote_verification_link: true
comment_count: 1
candidate_count: 0
self_authored_comment
```

This is an owner-authored request-surface refresh only. It is not vector search quality evidence, not a benchmark result, not a model comparison, not hosted deployment evidence, and not external reviewer feedback.

## Semantic Retrieval Persistence Review

Phase 226 selects the persistence boundary for semantic retrieval candidates.

The phase marker is:

```text
semantic retrieval persistence review v0
```

Review artifact:

```text
docs/review/semantic-retrieval-persistence-review.md
```

Selected next endpoint:

```text
POST /documents/{document_id}/semantic-retrieval-runs
```

Implementation rule:

```text
do not overload POST /documents/{document_id}/retrieval-runs
```

Selected persistence target:

```text
existing retrieval_runs table
metadata_json.candidate_chunk_ids
metadata_json.candidate_embedding_ids
metadata_json.missing_embedding_chunk_ids
```

The semantic preview endpoint remains:

```text
preview_only_not_persisted
```

Claim boundary:

```text
review-only
not endpoint code
not embedding generation
not Evidence Ledger generation
not hosted deployment evidence
```

## Semantic Retrieval Preview Runtime Smoke

Phase 225 verifies the semantic retrieval preview endpoint against local Docker PostgreSQL/pgvector and live FastAPI HTTP.

The phase marker is:

```text
semantic retrieval preview runtime smoke v0
```

Review artifact:

```text
docs/review/semantic-retrieval-preview-runtime-smoke.md
```

Environment:

```text
Docker version 29.4.3
Docker Compose version v5.1.3
noiseproof-agent-db healthy on localhost:55432
```

Migration runner note:

```text
uv run python -m app.migration_runner
```

will fail if `DATABASE_URL` is not present in the process environment. For smoke reproduction, pass the URL explicitly:

```bash
uv run python -m app.migration_runner \
  --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
```

Observed final migration state:

```text
Applied migrations: 14
Pending migrations: 0
```

Observed endpoint checks:

```text
GET /health -> 200
POST /documents/{document_id}/semantic-retrieval-preview -> 200
dimension mismatch -> 400
retrieval_runs_unchanged -> true
```

Claim boundary:

```text
not retrieval_runs persistence
not embedding generation
not Evidence Ledger generation
not vector search quality evidence
not hosted deployment evidence
```

## Deterministic Text Embedding Preview

Phase marker: deterministic text embedding preview v0.

Review artifact:

```text
docs/review/deterministic-text-embedding-preview.md
```

Endpoint:

```text
POST /chunks/embedding-preview
```

Example payload:

```json
{
  "text": "Enterprise demand growth reached 12% in Q1.",
  "embedding_dimension": 8
}
```

Expected response markers:

```text
embedding_model: local-hash-embedding-preview-v0
embedding_status: preview_generated
metadata_json.embedding_source: deterministic_local_hash_embedding_preview
metadata_json.persistence_boundary: preview_only_not_persisted
metadata_json.quality_boundary: not_semantic_quality_evidence
```

Focused verification:

```bash
cd apps/api
uv run pytest -q tests/test_routes.py -k "text_embedding_preview"
uv run pytest -q tests/test_docs.py -k "deterministic_text_embedding_preview"
```

Claim boundary:

```text
not a semantic embedding model
no external model
no LLM
not persisted
does not modify chunk_embeddings
not vector search quality evidence
not semantic retrieval quality evidence
```

## Trace Context Header Propagation

Phase marker: trace context header propagation v0.

Review artifact:

```text
docs/review/trace-context-header-propagation.md
```

Every response includes:

```text
traceparent
x-noiseproof-trace-source
x-noiseproof-trace-boundary
```

Expected boundary header:

```text
x-noiseproof-trace-boundary: local_header_propagation_no_distributed_tracing
```

Focused verification:

```bash
cd apps/api
uv run pytest -q tests/test_routes.py -k "trace_context_header"
uv run pytest -q tests/test_docs.py -k "trace_context_header_propagation"
```

Manual smoke example:

```bash
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000
curl -i http://127.0.0.1:8000/health
curl -i -H "traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01" http://127.0.0.1:8000/health
```

Claim boundary:

```text
not distributed tracing
no OpenTelemetry
no hosted observability
no trace export
no span storage
no cross-service trace proof
```

## Trace Context Header Runtime Smoke

Phase marker: trace context header runtime smoke v0.

Review artifact:

```text
docs/review/trace-context-header-runtime-smoke.md
```

Observed live HTTP checks:

```text
uvicorn on 127.0.0.1:8011
GET /health without traceparent -> 200
GET /health with valid traceparent -> 200
GET /health with invalid traceparent -> 200
```

Observed source markers:

```text
generated_traceparent
incoming_traceparent
invalid_traceparent_generated_fallback
local_header_propagation_no_distributed_tracing
```

Claim boundary:

```text
local uvicorn/curl evidence only
not hosted observability
not distributed tracing
not cross-service trace proof
```

## Embedding Provider Source Review

Phase marker: embedding provider source review v0.

Review artifact:

```text
docs/review/embedding-provider-source-review.md
```

Primary sources:

```text
https://platform.openai.com/docs/guides/embeddings
https://platform.openai.com/docs/api-reference/embeddings/create
```

Selected future default candidate:

```text
provider: openai
embedding_model: text-embedding-3-small
embedding_dimension: 1536
encoding_format: float
```

Alternative future candidate:

```text
embedding_model: text-embedding-3-large
embedding_dimension: 3072
```

Configuration boundary:

```text
OPENAI_API_KEY
```

Claim boundary:

```text
source review only
not implemented
no API call
no cost-incurring runtime path
actual embedding model generation remains unproven
```

## Embedding Model Provider Disabled Path

Phase marker: embedding model provider disabled-path v0.

Review artifact:

```text
docs/review/embedding-model-provider-disabled-path.md
```

Endpoint:

```text
POST /chunks/embedding-model-preview
```

Expected states:

```text
disabled_missing_api_key
configured_no_call
```

Focused verification:

```bash
cd apps/api
uv run pytest -q tests/test_routes.py -k "embedding_model_preview"
uv run pytest -q tests/test_docs.py -k "embedding_model_provider_disabled_path"
```

Claim boundary:

```text
no provider call
no embedding vector is generated
no_network_call
no_cost_incurred
preview_only_not_persisted
actual embedding model generation remains unproven
```

## Embedding Model Provider Live-call Review

Phase marker: embedding model provider live-call review v0.

Review artifact:

```text
docs/review/embedding-model-provider-live-call-review.md
```

Reviewed future call surface:

```text
POST /chunks/embedding-model-preview
```

Required future guard:

```text
allow_provider_call
```

Required future implementation checks:

```text
OPENAI_API_KEY
input text hash
provider response dimension check
secret redaction
timeout
no automatic persistence
```

Required future test boundary:

```text
mocked client first
no live provider call in CI
```

Claim boundary:

```text
not implemented
no API call
no dependency
no network call
no cost-incurring path
actual embedding model generation remains unproven
```

## Embedding Model Mocked-provider Call

Phase marker: embedding model mocked-provider call v0.

Review artifact:

```text
docs/review/embedding-model-mocked-provider-call.md
```

Endpoint:

```text
POST /chunks/embedding-model-preview
```

Mocked success state:

```text
allow_provider_call: true
embedding_status: mocked_provider_generated
metadata_json.network_boundary: mocked_provider_call_only
metadata_json.provider_call_boundary: mocked_provider_client
metadata_json.provider_response_dimension_check: passed
metadata_json.persistence_boundary: preview_only_not_persisted
```

Failure state:

```text
provider response dimension mismatch
```

Focused verification:

```bash
cd apps/api
uv run pytest -q tests/test_routes.py -k "embedding_model_preview"
uv run pytest -q tests/test_docs.py -k "embedding_model_mocked_provider_call"
```

Claim boundary:

```text
no live OpenAI provider call
no live provider call in CI
no network call
no live API cost
no automatic persistence
actual live embedding model generation remains unproven
```

## External Feedback Current-state Embedding Provider Owner-runtime Smoke Handoff Alignment Issue Verification

Phase marker: external feedback current-state embedding provider owner-runtime smoke handoff alignment issue verification v0.

Review artifact:

```text
docs/review/external-feedback-current-state-embedding-provider-owner-runtime-smoke-handoff-alignment-issue-verification.md
```

Related issue-body refresh:

```text
docs/review/external-review-issue-body-embedding-provider-owner-runtime-smoke-handoff-alignment-refresh.md
```

Observed issue state:

```text
updatedAt: 2026-06-05T03:16:50Z
starts_with_request: true
first_codepoint: 35
has_embedding_provider_response_handoff: true
has_embedding_provider_command_template_handoff_alignment: true
has_embedding_provider_handoff_alignment_ci_remote_verification: true
has_embedding_provider_handoff_alignment_request_refresh: true
comment_count: 1
screened_comment_count: 1
candidate_count: 0
draft_count: 0
status: pending
```

Comment screening:

```text
classification: non_qualifying
reason: self_authored_comment
does_not_close_gate: true
```

Boundary:

```text
current-state issue verification only
not external reviewer feedback
not live embedding generation proof
not hosted deployment evidence
external reviewer feedback remains pending
```

## External Review Issue Body Embedding Provider Owner-runtime Smoke Handoff Alignment Refresh

Phase marker: external review issue body embedding provider owner-runtime smoke handoff alignment refresh v0.

Review artifact:

```text
docs/review/external-review-issue-body-embedding-provider-owner-runtime-smoke-handoff-alignment-refresh.md
```

Live issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed issue markers:

```text
starts_with_request: true
first_codepoint: 35
has_embedding_provider_response_handoff: true
has_embedding_provider_command_template_handoff_alignment: true
has_embedding_provider_handoff_alignment_ci_remote_verification: true
has_embedding_provider_handoff_alignment_request_refresh: true
has_build_owner_runtime_smoke_report_from_response_command: true
has_response_handoff_command_marker: true
comment_count: 1
```

Boundary:

```text
owner-authored issue body routing only
not external reviewer feedback
not live embedding generation proof
not hosted deployment evidence
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Implementation Review

Phase marker: embedding model live-provider implementation review v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-implementation-review.md
```

Future call surface:

```text
POST /chunks/embedding-model-preview
```

Official source URLs:

```text
https://platform.openai.com/docs/guides/embeddings
https://platform.openai.com/docs/api-reference/embeddings/create
```

Required future implementation gate:

```text
allow_provider_call
OPENAI_API_KEY
timeout
secret redaction
provider response dimension check
usage metadata
no live provider call in CI
manual owner runtime smoke
```

Future manual owner runtime smoke must record:

```text
exact command
model
configured dimension
returned vector length
provider response dimension check result
usage metadata presence
secret_exposed: false
preview_only_not_persisted
```

Claim boundary:

```text
not implemented
no live OpenAI provider call
no network call
no API cost
no automatic persistence
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Code Review

Phase marker: embedding model live-provider code review v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-code-review.md
```

Current insertion point:

```text
apps/api/app/services/embedding_model_preview.py
get_embedding_provider_client returns None
preview_embedding_model_provider
```

Selected future code boundary:

```text
OpenAI Python SDK
client.embeddings.create
provider adapter interface
apps/api/app/services/openai_embedding_provider.py
```

Required future adapter settings:

```text
OPENAI_API_KEY
timeout_seconds
embedding_model
embedding_dimension
encoding_format: float
```

Required future implementation boundaries:

```text
structured provider error boundary
provider response dimension check
usage metadata
secret_exposed: false
no live provider call in CI
preview_only_not_persisted
```

Dependency boundary:

```text
dependency addition deferred
no OpenAI dependency added in this phase
```

Claim boundary:

```text
no runtime behavior
no live provider call
no API cost
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Dependency Review

Phase marker: embedding model live-provider dependency review v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-dependency-review.md
```

Official source URLs:

```text
https://platform.openai.com/docs/libraries
https://platform.openai.com/docs/api-reference/embeddings/create
https://platform.openai.com/docs/guides/embeddings
```

Registry observation:

```text
python -m pip index versions openai
observed_latest: openai==2.41.0
```

Dependency boundary:

```text
dependency candidate only
do not install in this phase
apps/api/pyproject.toml unchanged
uv.lock unchanged
```

Future dependency check commands:

```bash
uv add "openai==2.41.0"
uv lock --dry-run
uv run pytest -q tests/test_routes.py -k "embedding_model_preview"
uv run pytest -q tests/test_docs.py -k "embedding_model_live_provider"
```

Required future no-live-call checks:

```text
no live provider call in CI
no real OPENAI_API_KEY required for tests
default endpoint remains disabled/configured-no-call
actual live embedding model generation remains unproven until owner runtime smoke
```

Claim boundary:

```text
no runtime behavior
no dependency installed
no lockfile change
no live provider call
no API cost
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Dependency Addition

Phase marker: embedding model live-provider dependency addition v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-dependency-addition.md
```

Command:

```bash
cd apps/api
uv add "openai==2.41.0"
```

Changed files:

```text
apps/api/pyproject.toml
apps/api/uv.lock
```

Added dependency:

```text
openai==2.41.0
```

Observed lockfile additions:

```text
openai==2.41.0
distro==1.9.0
jiter==0.15.0
sniffio==1.3.1
tqdm==4.67.3
```

Claim boundary:

```text
dependency metadata only
no app code changed
no route behavior changed
no runtime behavior change
no live provider call in CI
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Adapter Disabled-code

Phase marker: embedding model live-provider adapter disabled-code v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-adapter-disabled-code.md
```

Implemented code:

```text
apps/api/app/services/openai_embedding_provider.py
OpenAIEmbeddingProviderClient
EmbeddingProviderError
```

SDK call shape:

```text
client.embeddings.create
```

Current route boundary:

```text
apps/api/app/services/embedding_model_preview.py
get_embedding_provider_client returns None
route remains unwired
```

Focused verification:

```bash
cd apps/api
uv run pytest -q tests/test_openai_embedding_provider.py
uv run pytest -q tests/test_routes.py -k "embedding_model_preview"
uv run pytest -q tests/test_docs.py -k "embedding_model_live_provider_adapter_disabled_code"
```

Claim boundary:

```text
adapter code exists
no route wiring
no live provider call in CI
no default live provider call
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Route Wiring Review

Phase marker: embedding model live-provider route wiring review v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-route-wiring-review.md
```

Current route boundary:

```text
get_embedding_provider_client remains None by default
```

Future owner-runtime opt-in gate:

```text
NOISEPROOF_ENABLE_OPENAI_PROVIDER=true
OPENAI_API_KEY configured
allow_provider_call=true
CI is not true
```

Required future default behavior:

```text
NOISEPROOF_ENABLE_OPENAI_PROVIDER absent -> None
NOISEPROOF_ENABLE_OPENAI_PROVIDER=false -> None
CI=true -> None
allow_provider_call=false -> no provider call
```

Claim boundary:

```text
no runtime behavior
no route wiring
no live provider call in CI
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Route Wiring Opt-in Disabled

Phase marker: embedding model live-provider route wiring opt-in-disabled v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-route-wiring-opt-in-disabled.md
```

Implemented dependency boundary:

```text
NOISEPROOF_ENABLE_OPENAI_PROVIDER=true
OPENAI_API_KEY configured
CI is not true
OPENAI_PROVIDER_TIMEOUT_SECONDS positive
```

Default safety behavior:

```text
NOISEPROOF_ENABLE_OPENAI_PROVIDER absent -> provider client remains disabled
NOISEPROOF_ENABLE_OPENAI_PROVIDER=false -> provider client remains disabled
OPENAI_API_KEY missing -> provider client remains disabled
CI=true -> provider client remains disabled
allow_provider_call=false -> no provider call
```

Local no-live-call checks:

```bash
cd apps/api
uv run pytest -q tests/test_embedding_provider_wiring.py
uv run pytest -q tests/test_routes.py -k "embedding_model_preview"
```

Manual owner-runtime live call remains a later gate.

Claim boundary:

```text
owner-runtime opt-in only
no live provider call in CI
no default live provider call
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Owner-runtime Smoke Packet

Phase marker: embedding model live-provider owner-runtime smoke packet v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
```

No-secret packet command:

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness --print-owner-runtime-smoke-packet
```

Packet boundary:

```text
api_calls_attempted: false
openai_api_key_printed: false
secret_committed_to_repo: false
secret_logged: false
```

Future owner-runtime environment:

```text
NOISEPROOF_ENABLE_OPENAI_PROVIDER=true
OPENAI_API_KEY configured outside the repository
CI=false
```

Future owner-runtime success criteria:

```text
http_status: 200
embedding_status: owner_runtime_provider_generated
embedding_length: 1536
provider_response_dimension_check: passed
usage_metadata_present: true
secret_exposed: false
persistence_boundary: preview_only_not_persisted
```

Current local observation:

```text
OPENAI_API_KEY_PRESENT=false
NOISEPROOF_ENABLE_OPENAI_PROVIDER_PRESENT=false
```

Claim boundary:

```text
packet only
no live OpenAI provider call
live embedding generation proof remains pending
external reviewer feedback remains pending
```

## External Reviewer Embedding Provider Owner-runtime Smoke Packet Request Refresh

Phase marker: external reviewer embedding provider owner-runtime smoke packet request refresh v0.

Review artifact:

```text
docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-packet-request-refresh.md
```

Highlighted packet:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
```

Reviewer-facing surfaces updated:

```text
CONTRIBUTING.md
.github/ISSUE_TEMPLATE/external-review-feedback.md
README.md
docs/GOAL.md
docs/application/portfolio-index.md
docs/review/external-reader-proof-path.md
docs/review/external-review-request.md
docs/review/external-reviewer-brief.md
docs/review/external-reviewer-link-map.md
docs/runbook.md
```

Boundary:

```text
not a live issue body edit
not external reviewer feedback
not hosted deployment evidence
not live embedding generation proof
not product-complete
```

## External Review Issue Body Embedding Provider Owner-runtime Smoke Packet Refresh

Phase marker: external review issue body embedding provider owner-runtime smoke packet refresh v0.

Review artifact:

```text
docs/review/external-review-issue-body-embedding-provider-owner-runtime-smoke-packet-refresh.md
```

Live issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed state after issue body edit:

```text
starts_with_request: true
first_codepoint: 35
has_embedding_provider_owner_runtime_smoke_packet: true
has_embedding_provider_request_refresh: true
has_embedding_provider_issue_body_refresh: true
has_api_calls_attempted_false: true
has_openai_api_key_printed_false: true
has_live_embedding_generation_boundary: true
has_external_feedback_boundary: true
comment_count: 1
body_length: 4734
```

Boundary:

```text
owner-authored issue routing only
not external reviewer feedback
not hosted deployment evidence
not live embedding generation proof
not product-complete
```

## External Feedback Current-state Embedding Provider Owner-runtime Smoke Packet Issue Verification

Phase marker: external feedback current-state embedding provider owner-runtime smoke packet issue verification v0.

Review artifact:

```text
docs/review/external-feedback-current-state-embedding-provider-owner-runtime-smoke-packet-issue-verification.md
```

Observed issue state:

```text
starts_with_request: true
first_codepoint: 35
has_embedding_provider_owner_runtime_smoke_packet: true
has_embedding_provider_request_refresh: true
has_embedding_provider_issue_body_refresh: true
has_external_feedback_boundary: true
comment_count: 1
screened_comment_count: 1
candidate_count: 0
draft_count: 0
status: pending
reason: self_authored_comment
```

Boundary:

```text
current-state issue verification only
not external reviewer feedback
not hosted deployment evidence
not live embedding generation proof
external reviewer feedback v0 gate remains pending
```

## Embedding Model Live-provider Owner-runtime Input Discovery

Phase marker: embedding model live-provider owner-runtime input discovery v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-input-discovery.md
```

No-secret discovery command:

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness --discover-owner-runtime-input
```

Current local observation:

```text
OPENAI_API_KEY_PRESENT=false
NOISEPROOF_ENABLE_OPENAI_PROVIDER_PRESENT=false
owner_runtime_input_status: missing_openai_api_key
api_calls_attempted: false
openai_api_key_printed: false
```

Boundary:

```text
owner-runtime input discovery only
not live embedding generation proof
actual live embedding model generation remains unproven
external reviewer feedback remains pending
```

## Embedding Model Live-provider Owner-runtime Input Discovery CI Check

Phase marker: embedding model live-provider owner-runtime input discovery ci check v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-input-discovery-ci-check.md
```

CI step:

```text
Check embedding provider owner runtime input discovery missing state
```

CI command:

```bash
uv run python -m app.services.embedding_model_live_provider_harness --discover-owner-runtime-input
```

Expected CI guard values:

```text
owner_runtime_input_status: missing_openai_api_key
api_calls_attempted: false
openai_api_key_printed: false
secret_logged: false
secret_committed_to_repo: false
```

Boundary:

```text
CI missing-input guard only
not live embedding generation proof
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Owner-runtime Input Discovery CI Remote Verification

Phase marker: embedding model live-provider owner-runtime input discovery ci remote verification v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-input-discovery-ci-remote-verification.md
```

Remote CI evidence:

```text
workflow: CI
run_id: 26988305027
head_sha: 1b4e42b508c9357c58b45f1fed9a990fe542cdb1
job_name: api-smoke
conclusion: success
step_number: 9
step_name: Check embedding provider owner runtime input discovery missing state
step_conclusion: success
```

Boundary:

```text
remote CI missing-input guard evidence only
not live embedding generation proof
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Owner-runtime Smoke Validator

Phase marker: embedding model live-provider owner-runtime smoke validator v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-validator.md
```

Validator command:

```bash
uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

Accepted report markers:

```text
embedding_status: owner_runtime_provider_generated
embedding_length: 1536
provider_response_dimension_check: passed
openai_api_key_printed: false
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
```

Boundary:

```text
metadata validator only
report path must remain outside the repository
not live embedding generation proof by itself
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Owner-runtime Smoke Post-run Validation Command

Phase marker: embedding model live-provider owner-runtime smoke post-run validation command v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-command.md
```

Updated packet artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
```

Post-run validation command:

```bash
uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

Success criteria:

```text
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
```

Boundary:

```text
packet refresh only
not live embedding generation proof
actual live embedding model generation remains unproven
```

## External Reviewer Embedding Provider Owner-runtime Smoke Validator Request Refresh

Phase marker: external reviewer embedding provider owner-runtime smoke validator request refresh v0.

Review artifact:

```text
docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-validator-request-refresh.md
```

Reviewer-facing validation path:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-validator.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-command.md
```

Post-run validation command:

```bash
uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

Success criteria:

```text
accepted_owner_runtime_smoke: true
missing_or_failed_checks: []
```

Boundary:

```text
request-surface refresh only
not live embedding generation proof
not external reviewer feedback
not hosted deployment evidence
not product-complete
actual live embedding model generation remains unproven
```

## External Review Issue Body Embedding Provider Owner-runtime Smoke Validator Refresh

Phase marker: external review issue body embedding provider owner-runtime smoke validator refresh v0.

Live issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Review artifact:

```text
docs/review/external-review-issue-body-embedding-provider-owner-runtime-smoke-validator-refresh.md
```

Issue body now points reviewers to:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-validator.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-command.md
docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-validator-request-refresh.md
docs/review/external-review-issue-body-embedding-provider-owner-runtime-smoke-validator-refresh.md
```

Observed issue state:

```text
updatedAt: 2026-06-05T01:27:45Z
starts_with_request: true
first_codepoint: 35
has_embedding_provider_owner_runtime_smoke_validator: true
has_embedding_provider_owner_runtime_smoke_post_run_validation: true
has_embedding_provider_validator_request_refresh: true
has_embedding_provider_validator_issue_body_refresh: true
has_validate_owner_runtime_smoke_report_command: true
has_validator_success_criteria: true
comment_count: 1
```

Boundary:

```text
owner-authored issue routing only
not live embedding generation proof
not external reviewer feedback
not hosted deployment evidence
not product-complete
actual live embedding model generation remains unproven
```

## External Feedback Current-state Embedding Provider Owner-runtime Smoke Validator Issue Verification

Phase marker: external feedback current-state embedding provider owner-runtime smoke validator issue verification v0.

Review artifact:

```text
docs/review/external-feedback-current-state-embedding-provider-owner-runtime-smoke-validator-issue-verification.md
```

Related issue-body refresh:

```text
docs/review/external-review-issue-body-embedding-provider-owner-runtime-smoke-validator-refresh.md
```

Observed issue state:

```text
updatedAt: 2026-06-05T01:27:45Z
starts_with_request: true
first_codepoint: 35
has_embedding_provider_owner_runtime_smoke_validator: true
has_embedding_provider_owner_runtime_smoke_post_run_validation: true
has_embedding_provider_validator_request_refresh: true
has_embedding_provider_validator_issue_body_refresh: true
comment_count: 1
screened_comment_count: 1
candidate_count: 0
draft_count: 0
status: pending
```

Comment screening:

```text
classification: non_qualifying
reason: self_authored_comment
does_not_close_gate: true
```

Boundary:

```text
current-state issue verification only
not live embedding generation proof
not external reviewer feedback
not hosted deployment evidence
not product-complete
external reviewer feedback v0 gate remains pending
```

## Embedding Model Live-provider Owner-runtime Smoke Post-run Validation Cross-shell Commands

Phase marker: embedding model live-provider owner-runtime smoke post-run validation cross-shell commands v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-cross-shell-commands.md
```

Updated packet artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
```

Post-run validation commands:

```text
post_run_validation_commands
posix: uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
powershell: uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report '<runtime-report-path-outside-repo>'
```

Boundary:

```text
validator metadata only
not live embedding generation proof
not external reviewer feedback
not hosted deployment evidence
not product-complete
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Owner-runtime Smoke Report Contract

Phase marker: embedding model live-provider owner-runtime smoke report contract v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-report-contract.md
```

Command:

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness --print-owner-runtime-smoke-report-contract
```

Contract markers:

```text
contract_status: ready_for_owner_runtime_report
accepted_report
required_top_level_fields
forbidden_secret_fields
accepted_validator_output
rejected_validator_output
```

Boundary:

```text
contract only
does not read OPENAI_API_KEY
does not print OPENAI_API_KEY
does not call the OpenAI provider
does not persist embeddings
not live embedding generation proof
not external reviewer feedback
not hosted deployment evidence
not product-complete
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Owner-runtime Smoke Report Schema

Phase marker: embedding model live-provider owner-runtime smoke report schema v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-report-schema.md
```

Command:

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness --print-owner-runtime-smoke-report-schema
```

Schema markers:

```text
schema_status: ready_for_owner_runtime_report
$schema: https://json-schema.org/draft/2020-12/schema
additionalProperties: false
required
properties
```

Boundary:

```text
schema only
does not read OPENAI_API_KEY
does not print OPENAI_API_KEY
does not call the OpenAI provider
does not persist embeddings
not live embedding generation proof
not external reviewer feedback
not hosted deployment evidence
not product-complete
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Owner-runtime Smoke Report Contract Alignment

Phase marker: embedding model live-provider owner-runtime smoke report contract alignment v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-report-contract-alignment.md
```

Command:

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness --check-owner-runtime-smoke-report-contract-alignment
```

Alignment markers:

```text
alignment_status: aligned
contract_fields_match_validator_expected_fields
schema_required_fields_match_contract
schema_properties_match_contract_constants
accepted_report_passes_validator
```

Boundary:

```text
schema/contract/validator alignment only
does not read OPENAI_API_KEY
does not print OPENAI_API_KEY
does not call the OpenAI provider
does not persist embeddings
not live embedding generation proof
not external reviewer feedback
not hosted deployment evidence
not product-complete
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Owner-runtime Smoke Report Contract Alignment CI Remote Verification

Phase marker: embedding model live-provider owner-runtime smoke report contract alignment ci remote verification v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-report-contract-alignment-ci-remote-verification.md
```

Observed CI run:

```text
run_id: 26991391227
workflow_name: CI
head_sha: 4dd79f75099989dd155a3dce71000e1b72e7c870
job_name: api-smoke
job_id: 79652102152
conclusion: success
```

Relevant successful step:

```text
Run API smoke tests
```

Related workflow:

```text
related_external_feedback_screen_run_id: 26991391234
related_external_feedback_screen_conclusion: success
related_external_feedback_screen_boundary: workflow screen success only, not external reviewer feedback
```

Boundary:

```text
remote CI verification only
does not read OPENAI_API_KEY
does not print OPENAI_API_KEY
does not call the OpenAI provider
does not persist embeddings
not live embedding generation proof
not external reviewer feedback
not hosted deployment evidence
not product-complete
actual live embedding model generation remains unproven
```

## External Review Issue Body Embedding Provider Report Alignment Refresh

Phase marker: external review issue body embedding provider report alignment refresh v0.

Review artifact:

```text
docs/review/external-review-issue-body-embedding-provider-report-alignment-refresh.md
```

Issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
updatedAt: 2026-06-05T02:30:13Z
```

Observed body checks:

```text
starts_with_request: true
first_codepoint: 35
has_embedding_provider_report_contract: true
has_embedding_provider_report_schema: true
has_embedding_provider_report_contract_alignment: true
has_embedding_provider_report_contract_alignment_ci_remote_verification: true
```

Boundary:

```text
owner-authored issue body routing only
not external reviewer feedback
not live embedding generation proof
not hosted deployment evidence
not product-complete
external reviewer feedback remains pending
```

## External Feedback Current-state Embedding Provider Report Alignment Issue Verification

Phase marker: external feedback current-state embedding provider report alignment issue verification v0.

Review artifact:

```text
docs/review/external-feedback-current-state-embedding-provider-report-alignment-issue-verification.md
```

Observed issue state:

```text
updatedAt: 2026-06-05T02:30:13Z
starts_with_request: true
first_codepoint: 35
has_embedding_provider_report_contract_alignment: true
has_embedding_provider_report_contract_alignment_ci_remote_verification: true
comment_count: 1
screened_comment_count: 1
candidate_count: 0
draft_count: 0
status: pending
```

Comment screening:

```text
classification: non_qualifying
reason: self_authored_comment
does_not_close_gate: true
```

Boundary:

```text
current-state issue verification only
not external reviewer feedback
not live embedding generation proof
not hosted deployment evidence
not product-complete
external reviewer feedback remains pending
```

## Embedding Model Live-provider Owner-runtime Smoke Response Handoff Report

Phase marker: embedding model live-provider owner-runtime smoke response handoff report v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-response-handoff-report.md
```

Command:

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness --build-owner-runtime-smoke-report-from-response <owner-runtime-response-json-outside-repo> --output <runtime-report-path-outside-repo>
```

Expected response capture fields:

```text
http_status: 200
response_body
embedding_status: owner_runtime_provider_generated
embedding_model: text-embedding-3-small
embedding_length: 1536
provider_response_dimension_check: passed
```

Post-run validation:

```bash
uv run python -m app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

Expected validator marker:

```text
accepted_owner_runtime_smoke: true
```

Boundary:

```text
response-to-report handoff only
does not call the OpenAI provider
does not persist embeddings
does not write embedding vectors into the validator report
not live embedding generation proof
not external reviewer feedback
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Owner-runtime Smoke Packet Command-template Handoff Alignment CI Remote Verification

Phase marker: embedding model live-provider owner-runtime smoke packet command-template handoff alignment ci remote verification v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment-ci-remote-verification.md
```

Observed CI run:

```text
workflow: CI
run_id: 26992724568
head_sha: fb271d1e59dfde93cb805440554952dc44a43fa4
job: api-smoke
conclusion: success
```

Observed successful step:

```text
Run API smoke tests
```

Observed External Feedback Screen run:

```text
workflow: External Feedback Screen
run_id: 26992724578
conclusion: success
```

Boundary:

```text
remote CI evidence only
workflow screen only
not external reviewer feedback
not live embedding generation proof
not hosted deployment evidence
actual live embedding model generation remains unproven
```

## External Reviewer Embedding Provider Owner-runtime Smoke Handoff Alignment Request Refresh

Phase marker: external reviewer embedding provider owner-runtime smoke handoff alignment request refresh v0.

Review artifact:

```text
docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-handoff-alignment-request-refresh.md
```

Reviewer-facing handoff path:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-response-handoff-report.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment-ci-remote-verification.md
```

Key markers:

```text
--build-owner-runtime-smoke-report-from-response
response_handoff_command
response_handoff_commands
workflow screen only
```

Boundary:

```text
request-surface refresh only
not a live issue body edit
not external reviewer feedback
not live embedding generation proof
not hosted deployment evidence
actual live embedding model generation remains unproven
```

## Embedding Model Live-provider Owner-runtime Smoke Packet Command-template Handoff Alignment

Phase marker: embedding model live-provider owner-runtime smoke packet command-template handoff alignment v0.

Review artifact:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment.md
```

Packet command:

```bash
cd apps/api
uv run python -m app.services.embedding_model_live_provider_harness --print-owner-runtime-smoke-packet
```

Expected packet fields:

```text
response_handoff_command
response_handoff_commands
runtime_report_handling.emit_response_handoff_report: true
runtime_report_handling.write_response_capture_outside_repo: true
```

Expected handoff command template:

```bash
uv run python -m app.services.embedding_model_live_provider_harness --build-owner-runtime-smoke-report-from-response <owner-runtime-response-json-outside-repo> --output <runtime-report-path-outside-repo>
```

Boundary:

```text
command-template metadata only
does not call the OpenAI provider
does not read OPENAI_API_KEY
does not print OPENAI_API_KEY
response capture path must be outside repository
report output path must be outside repository
not live embedding generation proof
not external reviewer feedback
actual live embedding model generation remains unproven
```

## README Upload Handoff Claim-boundary Refresh

Phase marker: readme upload handoff claim-boundary refresh v0.

Review artifact:

```text
docs/review/readme-upload-handoff-claim-boundary-refresh.md
```

README claim boundary:

```text
explicit uploaded-file-to-chunks handoff exists through `POST /documents/upload-chunks`
implicit upload-preview auto-persistence remains intentionally unclaimed
```

Boundary:

```text
README cleanup only
not a new product runtime gate
not automatic upload-preview persistence
not hosted deployment evidence
not external reviewer feedback
not product-complete
```

## Raw File Download Operator-token Guard

Phase marker: raw file download operator-token guard v0.

Review artifact:

```text
docs/review/raw-file-download-operator-token-guard.md
```

Opt-in environment variable:

```text
NOISEPROOF_RAW_FILE_DOWNLOAD_OPERATOR_TOKEN
```

Download request header:

```text
X-NoiseProof-Operator-Token
```

Expected missing-token response when the environment variable is configured:

```text
403
operator token required before raw file download
local_v0_operator_token_header_not_production
```

Boundary:

```text
local v0 operator-token guard only
do not commit token values
not production authorization
not authenticated user identity
not hosted deployment evidence
not product-complete
```

## README Latest-marker Persisted Document Failure Candidate Manual Handoff Current-state Remote Verification

Phase marker: readme latest-marker persisted document failure candidate manual handoff current-state remote verification v0.

Review artifact:

```text
docs/review/readme-latest-marker-persisted-document-failure-candidate-manual-handoff-current-state-remote-verification.md
```

Remote verification:

```text
head_sha: 448f171512a7aaaf71686d04969b402ccf7c1fce
CI run 27021345997 -> api-smoke -> success
External Feedback Screen run 27021346012 -> screen -> success
```

Boundary:

```text
workflow screen only
not external reviewer feedback
not hosted deployment evidence
not product-complete
```

## Application-ready Persisted Document Failure Candidate Manual Handoff Refresh

Phase marker: application-ready persisted document failure candidate manual handoff refresh v0.

Review artifact:

```text
docs/review/application-ready-persisted-document-failure-candidate-manual-handoff-refresh.md
```

Linked proof:

```text
docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md
docs/review/external-feedback-current-state-persisted-document-failure-candidate-manual-handoff-runtime-issue-verification.md
```

Boundary:

```text
application-facing documentation only
not automatic failure-case creation
not a confirm endpoint
not hosted deployment evidence
not product-complete
```

## README Latest-marker Persisted Document Failure Candidate Manual Handoff Current-state Refresh

Phase marker: readme latest-marker persisted document failure candidate manual handoff current-state refresh v0.

Review artifact:

```text
docs/review/readme-latest-marker-persisted-document-failure-candidate-manual-handoff-current-state-refresh.md
```

README top markers:

```text
Latest reviewer-routing marker: Persisted document failure candidate manual handoff runtime issue-body refresh v0
Latest external-feedback state: pending after persisted document failure candidate manual handoff issue verification; candidate_count=0; self-authored comment only
```

Boundary:

```text
README current-state alignment only
external-feedback remains pending
not automatic failure-case creation
not a confirm endpoint
not hosted deployment evidence
not product-complete
```

## Workflow Failure-case Persistence Handoff

Phase marker: workflow failure-case persistence handoff v0.

Review artifact:

```text
docs/review/workflow-failure-case-persistence-handoff.md
```

Endpoint:

```text
POST /failure-cases/workflow-runs/{workflow_run_id}
```

Expected persistence boundary:

```text
caller_triggered_workflow_failure_case_persistence
```

Expected behavior:

```text
failed / blocked / needs_revision workflow_run -> one linked failure_cases row
completed workflow_run -> 409
duplicate linked failure case -> 409
```

Boundary:

```text
caller-triggered handoff only
not background automation
not root-cause automation
not complete workflow failure causality
not LLM-backed repair
not product-complete
```

## Workflow Failure-case Persistence Handoff Runtime Smoke

Phase marker: workflow failure-case persistence handoff runtime smoke v0.

Review artifact:

```text
docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md
```

Observed local runtime path:

```text
Docker PostgreSQL healthy on localhost:55432
FastAPI live on 127.0.0.1:8044
GET /health -> 200
POST /workflow-runs -> 201
POST /failure-cases/workflow-runs/{workflow_run_id} -> 201
GET /failure-cases -> 200
GET /failure-cases/workflow-review-queue -> 200
queue_status_for_workflow -> failure_case_linked
completed_workflow_status_code -> 409
duplicate_status_code -> 409
```

Boundary:

```text
local Docker plus live HTTP evidence only
not hosted deployment evidence
not external reviewer feedback
not background automation
not complete workflow failure causality
not product-complete
```

## External Feedback Current-state Persisted Document Failure Candidate Manual Handoff Runtime Issue Verification

Phase marker: external feedback current-state persisted document failure candidate manual handoff runtime issue verification v0.

Review artifact:

```text
docs/review/external-feedback-current-state-persisted-document-failure-candidate-manual-handoff-runtime-issue-verification.md
```

Screening commands:

```powershell
gh issue view 1 --repo svy04/noiseproof-agent --json number,title,state,body,comments,updatedAt,url,labels
uv run python -m packages.review.external_feedback_cli --input <captured-issue-json> --repository-owner svy04
uv run python -m packages.review.external_feedback_acceptance_cli --input <screening-json>
```

Current boundary:

```text
candidate_count=0
draft_count=0
self_authored_comment
external reviewer feedback remains pending
not external reviewer feedback
not hosted deployment evidence
not product-complete
```

## Workflow Failed Stage Event

Phase marker: workflow failed stage event v0.

Review artifact:

```text
docs/review/workflow-failed-stage-event.md
```

Covered regression:

```text
POST /workflow-runs/execute-preview
simulated Evidence Ledger persistence failure
GET /workflow-runs/{workflow_run_id}
```

Expected local inspection shape:

```text
retrieval -> completed
evidence_ledger -> failed
workflow_stage_event_count -> 2
failed_stage_boundary -> local_workflow_stage_failure_event_no_retry_no_auto_failure_case
failure_case_count_delta -> 0
```

Verification:

```powershell
cd apps/api
uv run pytest -q tests/test_routes.py::test_workflow_execute_preview_records_failed_stage_event_when_stage_errors
```

Boundary:

```text
local workflow failure observability only
not retry behavior
not automatic failure-case creation
not root-cause automation
not distributed tracing
not hosted observability
not external reviewer feedback
not product-complete
```
