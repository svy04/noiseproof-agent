# External Review Request

Status: external review request packet.

Phase marker: external review request packet v0.

Label: External review request packet.

This artifact prepares the next evidence gate without claiming that the gate is complete.

The current next gate is:

```text
external reviewer feedback v0
```

This page exists so an outside reviewer can inspect the current bounded proof path and leave critique in a structured form.

Shortest reviewer brief:

```text
docs/review/external-reviewer-brief.md
```

90-second reviewer shortlist:

```text
docs/review/external-reviewer-shortlist.md
```

Current failure-case workflow review queue proof index:

```text
docs/review/failure-case-workflow-review-queue-proof-index.md
```

Copy-paste outreach packet:

```text
docs/review/external-reviewer-outreach-packet.md
```

Direct reviewer link map:

```text
docs/review/external-reviewer-link-map.md
```

Latest workflow proof bundle runtime proof:

```text
docs/review/workflow-proof-bundle-runtime-smoke.md
docs/review/external-reviewer-workflow-proof-bundle-request-refresh.md
docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md
docs/review/external-reviewer-workflow-proof-bundle-dashboard-runtime-request-refresh.md
docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md
docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md
docs/review/workflow-dashboard-failure-case-counts-runtime-smoke.md
docs/review/external-reviewer-workflow-dashboard-failure-case-counts-runtime-request-refresh.md
docs/review/ops-dashboard-anchor-get-runtime-smoke.md
docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md
docs/review/ops-dashboard-anchor-browser-smoke.md
docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md
docs/review/workflow-direct-stage-links-runtime-smoke.md
docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md
```

Boundary: this proof records local Docker PostgreSQL plus live FastAPI HTTP evidence for `GET /workflow-runs/{id}/proof-bundle`, including `health_status: ok`, `execute_preview_status_code: 201`, `proof_bundle_status_code: 200`, `metadata_only_proof_bundle_status_code: 200`, `bundle_boundary: read_model_only_existing_records_no_new_storage`, and `metadata_only_trace_is_null: true`. The dashboard runtime proof adds `GET /ops/dashboard`, `dashboard_contains_proof_bundle_link: true`, and linked proof bundle status `200`. The failure-case links runtime proof adds `GET /workflow-runs/{id}`, `GET /failure-cases?workflow_run_id={id}`, `detail_failure_case_count: 1`, `bundle_failure_case_count: 1`, `filtered_failure_case_count: 1`, `unrelated_filtered_out: true`, and `proof_surface_has_failure_case_filter: true`. The dashboard failure-case counts runtime proof adds `dashboard_contains_linked_failure_cases_header: true`, `dashboard_contains_linked_failure_case_filter: true`, and `dashboard_omits_unlinked_failure_case_filter: true`. The ops dashboard anchor GET runtime proof adds `data-method="GET"`, `extracted_anchor_count: 38`, `unique_anchor_count: 25`, `all_extracted_dashboard_get_anchors_returned_200: true`, and `post_only_draft_preview_was_not_clickable: true`. The ops dashboard anchor browser proof adds Playwright browser automation, `browser_anchor_count: 27`, `browser_get_anchor_count: 27`, `browser_post_anchor_count: 0`, `post_only_draft_preview_anchor_count: 0`, `post_only_draft_preview_cue_visible: true`, and `all_browser_get_anchors_marked_get: true`. The direct stage links runtime proof adds `POST /workflow-runs/execute-preview`, `GET /workflow-runs/{id}/lineage`, `direct_stage_link_count: 3`, `evidence_to_report`, `evidence_to_noise_gate`, `noise_gate_to_report`, and `workflow_created_records_only_not_standalone_payload_lineage`. The request refresh is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not distributed tracing, not hosted observability, not autonomous workflow execution, not automatic failure detection, not background automation, not complete workflow failure causality, not customer validation, and not product-complete.

Latest workflow failure-case persistence runtime proof:

```text
docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md
docs/review/external-reviewer-workflow-failure-case-persistence-runtime-request-refresh.md
```

Boundary: this proof records local Docker PostgreSQL plus live FastAPI HTTP evidence for caller-triggered `POST /failure-cases/workflow-runs/{workflow_run_id}`, including `persistence_boundary -> caller_triggered_workflow_failure_case_persistence`, `queue_status_for_workflow -> failure_case_linked`, `completed_workflow_status_code -> 409`, and `duplicate_status_code -> 409`. The request refresh is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not background automation, not complete workflow failure causality, and not product-complete.

Latest embedding provider owner-runtime smoke packet:

```text
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-validator.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-command.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-response-handoff-report.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment.md
docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment-ci-remote-verification.md
docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-packet-request-refresh.md
docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-validator-request-refresh.md
docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-handoff-alignment-request-refresh.md
```

Boundary: this packet is a no-secret/no-call owner-runtime smoke contract with `api_calls_attempted: false` and `openai_api_key_printed: false`; the validator uses `--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>` and expects `accepted_owner_runtime_smoke: true` plus `missing_or_failed_checks: []` only after a future owner-runtime smoke report exists. The response handoff uses `--build-owner-runtime-smoke-report-from-response`, the packet now exposes `response_handoff_command`, and the CI verification is workflow screen only. This request path is not live embedding generation proof, not hosted deployment evidence, not semantic retrieval quality evidence, not external reviewer feedback, and not product-complete.

Root review guide:

```text
CONTRIBUTING.md
docs/review/external-review-root-guide.md
```

Live issue body verification:

```text
docs/review/external-review-issue-body-encoding-verification.md
docs/review/external-review-issue-body-root-guide-verification.md
docs/review/external-review-issue-body-link-map-verification.md
```

Issue template link-map refresh:

```text
docs/review/external-review-issue-template-link-map-refresh.md
```

Issue label verification:

```text
docs/review/external-review-issue-label-verification.md
```

uploaded-file intake manifest proof:

```text
docs/review/uploaded-file-intake-manifest-preview.md
docs/review/uploaded-file-intake-manifest-runtime-smoke.md
docs/review/uploaded-file-intake-manifest-application-refresh.md
```

Boundary: this proof is not raw file storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file intake manifest persistence proof:

```text
docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md
docs/review/uploaded-file-intake-manifest-persistence-application-refresh.md
```

Boundary: this proof is manifest metadata only, not raw file storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file parsed document persistence proof:

```text
docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md
docs/review/uploaded-file-parsed-document-persistence-application-refresh.md
```

Boundary: this proof is document metadata/profile only, not raw file storage, not parsed text persistence, not hosted deployment evidence, and not external reviewer feedback.

uploaded PDF downstream handoff proof:

```text
docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md
docs/review/uploaded-pdf-downstream-handoff-application-refresh.md
```

Boundary: this proof records `parser -> pdf-pymupdf` for uploaded digital PDF text flowing through upload preview, upload chunk preview, explicit upload-to-chunks persistence, listed chunk lookup, and upload retrieval preview. It is not robust PDF extraction, not OCR, not table extraction, not layout fidelity, not raw file storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded PDF retrieval-run provenance runtime proof:

```text
docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md
docs/review/external-reviewer-pdf-retrieval-run-provenance-request-refresh.md
```

Boundary: this proof records uploaded digital PDF bytes flowing through `POST /documents/upload-chunks`, `POST /documents/{document_id}/retrieval-runs`, and `GET /retrieval-runs` with `candidate_parsers -> pdf-pymupdf` and `source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only`. It is request infrastructure only when surfaced here, not robust PDF extraction, not OCR, not table extraction, not layout fidelity, not raw file storage, not hosted deployment evidence, not Evidence Ledger generation, and not external reviewer feedback.

uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime proof:

```text
docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md
docs/review/external-reviewer-pdf-retrieval-run-linked-evidence-ledger-provenance-request-refresh.md
```

Boundary: this proof records uploaded digital PDF bytes flowing through `POST /documents/upload-chunks`, `POST /documents/{document_id}/retrieval-runs`, `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, and `GET /evidence-ledgers?retrieval_run_id=` with `metadata_json.parser -> pdf-pymupdf`, `metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk`, and `ledger_retrieval_run_id_matches -> true`. It is request infrastructure only when surfaced here, not robust PDF extraction, not OCR, not table extraction, not layout fidelity, not raw file storage, not hosted deployment evidence, not Noise Gate behavior, not report generation, and not external reviewer feedback.

uploaded-file chunk persistence proof:

```text
docs/review/uploaded-file-chunk-persistence-runtime-smoke.md
docs/review/uploaded-file-chunk-persistence-application-refresh.md
```

Boundary: this proof is not automatic persistence from upload preview, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file chunk handoff proof:

```text
docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md
```

Boundary: this proof is explicit `POST /documents/upload-chunks`, not raw uploaded byte storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file retrieval persistence proof:

```text
docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md
```

Boundary: this proof is explicit `POST /documents/{document_id}/retrieval-runs` over persisted `document_chunks`, not Evidence Ledger generation, not hosted deployment evidence, and not external reviewer feedback.

retrieval-run-linked Report proof:

```text
docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md
docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md
docs/review/retrieval-run-linked-report-runtime-smoke.md
```

Boundary: this proof is explicit `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, `POST /retrieval-runs/{retrieval_run_id}/noise-gate`, and `POST /retrieval-runs/{retrieval_run_id}/report`; the report handoff records `pre_report_status: 409` and `input_noise_gate_record_id`, but it is not hosted deployment evidence, not external reviewer feedback, not LLM judgment, not embeddings, not semantic retrieval, not free-form final report generation, and not financial advice.

toy semantic retrieval quality report:

```text
docs/evaluation/semantic-retrieval-quality-report.md
docs/review/semantic-retrieval-quality-report-application-refresh.md
```

Boundary: this report is toy fixture metric output with `q-what-missing` kept visible. It is not vector search quality evidence, not a benchmark result, not a model comparison, not hosted deployment evidence, and not external reviewer feedback.

uploaded raw file storage proof:

```text
docs/review/uploaded-raw-file-storage-runtime-smoke.md
docs/review/uploaded-raw-file-storage-application-refresh.md
```

Boundary: this proof is explicit `POST /documents/upload-raw-files` and `GET /documents/upload-raw-files` over quarantined PostgreSQL BYTEA storage. It is not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.

uploaded raw file scan result endpoint proof:

```text
docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md
```

Boundary: this proof is explicit `POST /documents/upload-raw-files/{raw_file_id}/scan-results` and `GET /documents/upload-raw-files/{raw_file_id}/scan-results`, preserves `scan_verdict -> scan_error`, records `response_has_raw_bytes -> false`, and remains not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.

ClamAV adapter runtime smoke proof:

```text
docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md
```

Boundary: this proof is a deterministic fake-runner smoke for `ClamAvScannerAdapter` missing/clean/infected/timeout/error mappings. It reports `real_clamav_runtime_verified -> false`, and remains not hosted deployment evidence, not external reviewer feedback, not real ClamAV execution, not signature database evidence, not malware scanning, and not a download endpoint.

uploaded raw file scan execution endpoint runtime proof:

```text
docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md
```

Boundary: this proof is local Docker PostgreSQL plus live FastAPI HTTP evidence for `POST /documents/upload-raw-files/{raw_file_id}/scan`; the default scanner-unavailable result is `failed / scan_error`, and it remains not hosted deployment evidence, not external reviewer feedback, not real ClamAV execution, not signature database evidence, not malware scanning, and not a download endpoint.

ClamAV API endpoint malicious-detection owner-runtime smoke:

```text
docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md
```

Boundary: this proof is local Docker FastAPI plus ClamAV endpoint evidence for owner-provided stdin input. It records `harness_status: verified_infected`, `scan_verdict: infected`, `matched_signature: Eicar-Test-Signature`, `payload_committed_to_repo: false`, and `raw_payload_logged: false`. It is not hosted deployment evidence, not external reviewer feedback, not production malware scanning evidence, and not product-complete.

guarded raw file download endpoint runtime smoke:

```text
docs/review/uploaded-raw-file-download-endpoint-runtime-smoke.md
```

Boundary: this proof is local Docker PostgreSQL plus live FastAPI HTTP evidence for `GET /documents/upload-raw-files/{raw_file_id}/download`; no-scan download returns `409`, latest clean scan returns `200` bytes, and later failed scan returns `409`. It is not hosted deployment evidence, not external reviewer feedback, not production malware scanning evidence, not endpoint malicious-detection runtime proof, and not production authorization.

guarded raw file download rate-limit runtime smoke:

```text
docs/review/uploaded-raw-file-download-rate-limit-runtime-smoke.md
```

Boundary: this proof is local Docker PostgreSQL plus live FastAPI HTTP evidence for local v0 guarded raw file download rate limiting; same-file no-scan attempts return `[409, 409, 409, 409, 409]` then `429`, and a separate clean file still downloads with `200`. It is not hosted deployment evidence, not external reviewer feedback, not distributed rate limiting, not endpoint malicious-detection runtime proof, and not production authorization.

raw file signature validation runtime smoke:

```text
docs/review/uploaded-raw-file-signature-validation-runtime-smoke.md
```

Boundary: this proof is local Docker PostgreSQL plus live FastAPI HTTP evidence for local v0 raw file signature validation; spoofed CSV upload returns `201`, declared PDF mismatch returns `415`, the blocked response has no raw bytes, and the mismatch hash is not recently persisted. It is not hosted deployment evidence, not external reviewer feedback, not robust file-type detection, not malware scanning evidence, not endpoint malicious-detection runtime proof, and not production authorization.

raw file extension allowlist runtime smoke:

```text
docs/review/uploaded-raw-file-extension-allowlist-runtime-smoke.md
```

Boundary: this proof is local Docker PostgreSQL plus live FastAPI HTTP evidence for local v0 raw file extension allowlisting; allowed CSV upload returns `201`, `sample.exe.csv` double-extension block returns `415`, responses include no raw bytes, and the blocked content hash is not recently persisted. It is not hosted deployment evidence, not external reviewer feedback, not robust file-type detection, not malware scanning evidence, not endpoint malicious-detection runtime proof, and not production authorization.

raw file download filename safety runtime smoke:

```text
docs/review/uploaded-raw-file-download-filename-safety-runtime-smoke.md
```

Boundary: this proof is local Docker FastAPI evidence for local v0 guarded raw file download attachment filename safety; a path-like and URL-encoded-control CSV filename downloads with a 120-character safe attachment filename and `local_v0_content_disposition_filename_safety_not_production`. It is not hosted deployment evidence, not external reviewer feedback, not malware detection proof, not robust file serving, not endpoint malicious-detection runtime proof, and not production authorization.

raw file download audit runtime smoke:

```text
docs/review/uploaded-raw-file-download-audit-runtime-smoke.md
```

Boundary: this proof is local Docker FastAPI plus PostgreSQL evidence for local v0 guarded raw file download audit events; missing-scan `409`, rate-limited `[409, 409, 409, 409, 409, 429]`, and allowed `200` decisions persist to `raw_file_download_events`. It is not hosted deployment evidence, not external reviewer feedback, not malware detection proof, not endpoint malicious-detection runtime proof, not production authorization, and not user identity.

raw file download approval gate behavior runtime smoke:

```text
docs/review/uploaded-raw-file-download-approval-gate-behavior-runtime-smoke.md
```

Boundary: this proof is local Docker FastAPI plus PostgreSQL evidence for local v0 approval-gated raw file downloads; latest-clean/no-approval returns `409` with `missing_download_approval`, non-active approval returns `409` with `revoked_or_expired_download_approval`, and active approval returns `200` with `download_approval_id` in audit metadata. It is not hosted deployment evidence, not external reviewer feedback, not production authorization, not user identity, not signed URL support, and not product-complete.

raw file download approval input guard runtime smoke:

```text
docs/review/uploaded-raw-file-download-approval-input-guard-runtime-smoke.md
```

Boundary: this proof is local Docker FastAPI plus PostgreSQL evidence for local v0 approval input validation; valid approval metadata creates/lists, unknown approval status returns `422`, and already expired active approval returns `422`. It is not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

raw file download approval audit metadata runtime smoke:

```text
docs/review/uploaded-raw-file-download-approval-audit-metadata-runtime-smoke.md
```

Boundary: this proof is local Docker FastAPI plus PostgreSQL evidence for local v0 approval audit metadata; active approval download returns `200`, allowed event metadata keeps approval id/status/expiry/latest-scan match, and identity remains `operator_label_not_authenticated_identity`. It is not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

raw file download readiness runtime smoke:

```text
docs/review/uploaded-raw-file-download-readiness-runtime-smoke.md
```

Boundary: this proof is local Docker FastAPI plus PostgreSQL evidence for the read-only download readiness preflight; it blocks with `missing_clean_scan`, blocks with `missing_download_approval`, allows after active approval, returns no raw bytes, consumes no rate limit, and writes no download audit event. It is not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

raw file guard ops summary runtime smoke:

```text
docs/review/uploaded-raw-file-guard-ops-summary-runtime-smoke.md
docs/review/external-reviewer-raw-file-guard-ops-summary-request-refresh.md
```

Boundary: this proof is local Docker PostgreSQL plus live FastAPI HTTP evidence for raw upload, blocked missing-scan download, failed/clean scan metadata, active approval, allowed download, `/ops/summary` deltas, and `/ops/dashboard` labels. It is not a live issue body edit, not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated identity, not signed URL support, and not product-complete.

architecture current-state ClamAV proof boundary refresh:

```text
docs/review/architecture-current-state-clamav-proof-boundary-refresh.md
```

Boundary: this proof-surface correction recognizes the local ClamAV endpoint malicious-detection owner-runtime smoke while still not claiming production malware scanning evidence, hosted deployment evidence, external reviewer feedback, production authorization, or product completion.

## Review Path

Please read in this order:

1. `README.md`
2. `docs/review/external-reader-proof-path.md`
3. `docs/application/portfolio-index.md`
4. `docs/review/local-browser-screenshot-walkthrough.md`
5. `docs/review/uploaded-file-intake-manifest-runtime-smoke.md`
6. `docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md`
7. `docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md`
8. `docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md`
9. `docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md`
10. `docs/review/uploaded-file-chunk-persistence-runtime-smoke.md`
11. `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md`
12. `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`
13. `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md`
14. `docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md`
15. `docs/review/retrieval-run-linked-report-runtime-smoke.md`
16. `docs/evaluation/semantic-retrieval-quality-report.md`
17. `docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md`
18. `docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md`
19. `docs/review/uploaded-raw-file-guard-ops-summary-runtime-smoke.md`
20. `docs/review/architecture-current-state-clamav-proof-boundary-refresh.md`
21. `docs/application/braincrew-role-map.md`

Optional source-level provenance:

```text
docs/review/readme-proof-marker-archive.md
```

## Reviewer Questions

Please answer any of these with direct references to the artifacts you inspected:

```text
What would make this portfolio stronger?
What claim feels over-stated?
What is missing before you would trust this?
What evidence is easiest to inspect?
What evidence is too self-authored or too weak?
What role does this currently signal?
What role does it not yet prove?
What should be removed, compressed, or made more direct?
```

## Preferred Feedback Format

Use the GitHub issue template:

```text
.github/ISSUE_TEMPLATE/external-review-feedback.md
```

Public request issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Feedback intake criteria:

```text
docs/review/external-feedback-intake-criteria.md
```

Use `docs/review/external-reviewer-outreach-packet.md` when contacting an FDE/product engineer reviewer, RAG/data engineer reviewer, or founder/operator reviewer before they comment on issue #1.

Suggested sections:

```text
Reviewer role
Evidence inspected
Feedback
Claim boundary
Missing evidence
Hiring signal
Optional next action
```

## Allowed Claim

NoiseProof Agent now has a public, structured request packet for collecting external reviewer feedback on its portfolio proof path.

## Boundary

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not hosted deployment evidence.

This is not production RAG evidence.

This is not a claim that the portfolio is application-ready for every role.

This does not prove that any reviewer has inspected the repository.

The public issue above is a request surface only. It becomes external reviewer feedback only after an outside reviewer leaves a substantive comment that references inspected evidence.

## Next Gate

The next gate remains:

```text
external reviewer feedback v0
```
