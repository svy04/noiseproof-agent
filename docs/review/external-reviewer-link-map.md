# External Reviewer Link Map

Status: reviewer-facing link hygiene artifact.

Phase marker: external reviewer link map v0.

Label: External reviewer link map.

This artifact gives outside reviewers direct links to the shortest inspectable path. It reduces navigation friction before a reviewer leaves feedback, but it does not claim that any feedback has been received.

## Latest Persisted Report Markdown Export Proof

- persisted Report markdown export proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/persisted-report-markdown-export.md
- Route:
  `GET /reports/{report_record_id}/markdown`
- Remote verification:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/persisted-report-markdown-export-remote-verification.md
- Request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-persisted-report-markdown-export-request-refresh.md
- Issue-body refresh record:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-review-issue-body-persisted-report-markdown-export-refresh.md
- Boundary: deterministic markdown export over existing persisted Report records only; not free-form report generation, not a new report-generation path, not an LLM call, not retrieval, not Evidence Ledger creation, not Noise Gate behavior, not Report record creation, not financial advice, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

## Latest Embedding Provider Owner-runtime Smoke Packet

- Smoke packet:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
- Validator:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-validator.md
- Post-run validation command:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-command.md
- Response handoff:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-response-handoff-report.md
- Command-template handoff alignment:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment.md
- Handoff alignment CI remote verification:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment-ci-remote-verification.md
- Request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-packet-request-refresh.md
- Validator request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-validator-request-refresh.md
- Handoff request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-handoff-alignment-request-refresh.md
- Boundary: no-secret/no-call owner-runtime smoke contract with `api_calls_attempted: false` and `openai_api_key_printed: false`; validator command `--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>` expects `accepted_owner_runtime_smoke: true` and `missing_or_failed_checks: []` only after a future owner-runtime report exists; response handoff command `--build-owner-runtime-smoke-report-from-response`; packet field `response_handoff_command`; CI verification is workflow screen only; not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not live embedding generation proof, not semantic retrieval quality evidence, and not product-complete.

## Latest Workflow Proof Bundle Runtime Proof

- Runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-proof-bundle-runtime-smoke.md
- Request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-proof-bundle-request-refresh.md
- Dashboard runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md
- Dashboard request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-proof-bundle-dashboard-runtime-request-refresh.md
- Failure-case links runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md
- Failure-case links request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md
- Dashboard failure-case counts runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-dashboard-failure-case-counts-runtime-smoke.md
- Dashboard failure-case counts request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-dashboard-failure-case-counts-runtime-request-refresh.md
- Ops dashboard anchor GET runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/ops-dashboard-anchor-get-runtime-smoke.md
- Ops dashboard anchor GET request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md
- Ops dashboard anchor browser proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/ops-dashboard-anchor-browser-smoke.md
- Ops dashboard anchor browser request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md
- Direct stage links runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-direct-stage-links-runtime-smoke.md
- Direct stage links request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md
- Stage event log runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-stage-event-log-runtime-smoke.md
- Stage event log request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-stage-event-log-runtime-request-refresh.md
- Failed stage event runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-failed-stage-event-runtime-smoke.md
- Failed stage event request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-failed-stage-event-runtime-request-refresh.md
- Workflow failure auto-created failure-case runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-failure-auto-failure-case-creation-runtime-smoke.md
- Workflow failure auto-creation request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-failure-auto-creation-runtime-request-refresh.md
- Workflow failure auto-created failure-case dashboard runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-failure-auto-created-failure-case-dashboard-runtime-smoke.md
- Workflow failure auto-created failure-case dashboard request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-failure-auto-created-dashboard-runtime-request-refresh.md
- Boundary: local Docker PostgreSQL plus live FastAPI HTTP evidence for `GET /workflow-runs/{id}/proof-bundle`, dashboard navigation from `GET /ops/dashboard` to the `proof bundle` link, linked failure-case visibility, direct workflow-created stage links, workflow stage event rows, failed stage event runtime evidence, local v0 workflow failure auto-creation with `failure_case_count_delta -> 1`, `auto_failure_case_id`, `auto_created_from_workflow_failure_local_v0`, and `local_workflow_stage_failure_event_auto_failure_case_local_v0`, plus workflow failure auto-created failure-case dashboard runtime proof with `GET /ops/dashboard -> 200`, `dashboard_contains_auto_created_failure_case_id`, `dashboard_contains_workflow_parent_link`, and `dashboard_contains_review_queue_linked_count`; not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not customer validation, not retry behavior, not root-cause automation, not distributed tracing, not hosted observability, not autonomous workflow execution, not automatic failure detection, not background automation, not complete workflow failure causality, and not product-complete.

## Latest Workflow Failure-case Persistence Runtime Proof

- Runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md
- Request refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-failure-case-persistence-runtime-request-refresh.md
- Boundary: local Docker PostgreSQL plus live FastAPI HTTP evidence for caller-triggered `POST /failure-cases/workflow-runs/{workflow_run_id}`, review queue `failure_case_linked`, completed-workflow `409`, and duplicate `409`; not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not background automation, not complete workflow failure causality, and not product-complete.

## Focused Uploaded PDF Encrypted Handoff Ops Proof

- Handoff ops proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops.md
- Runtime proof:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-runtime-smoke.md
- Remote verification:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-remote-verification.md
- Route refresh:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reader-proof-path-encrypted-pdf-handoff-ops-route-refresh.md
- Route refresh remote verification:
  https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reader-proof-path-encrypted-pdf-handoff-ops-route-refresh-remote-verification.md
- Route markers:
  `pdf_encrypted_failure_candidate_count`, `PDF Encrypted Failure Candidates`
- Boundary: password-protected PDF failure metadata and operations visibility only; not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction, not OCR, not table extraction, not layout fidelity, not decryption, not password bypass, and not product-complete.

## Public Feedback Surface

Leave feedback here:

https://github.com/svy04/noiseproof-agent/issues/1

## 90-second Shortlist

Start here before opening the full path:

https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-shortlist.md

## 2-minute Path

1. Reviewer brief:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-brief.md
2. Root review guide:
   https://github.com/svy04/noiseproof-agent/blob/main/CONTRIBUTING.md
3. README:
   https://github.com/svy04/noiseproof-agent/blob/main/README.md
4. External-reader proof path:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reader-proof-path.md
5. Portfolio index:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/application/portfolio-index.md
6. Local browser screenshot walkthrough:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/local-browser-screenshot-walkthrough.md
7. uploaded-file intake manifest proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-intake-manifest-runtime-smoke.md
   Boundary: not raw file storage, not hosted deployment evidence, and not external reviewer feedback.
8. uploaded-file intake manifest persistence proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md
   Boundary: manifest metadata only, not raw file storage, not hosted deployment evidence, and not external reviewer feedback.
9. uploaded-file parsed document persistence proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md
   Boundary: document metadata/profile only, not raw file storage, not parsed text persistence, not hosted deployment evidence, and not external reviewer feedback.
10. uploaded PDF downstream handoff proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md
   Boundary: `parser -> pdf-pymupdf`, digital PDF text only, not robust PDF extraction, not OCR, not table extraction, not hosted deployment evidence, and not external reviewer feedback.
11. uploaded PDF no-text failure candidate runtime proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-no-text-failure-candidate-runtime-smoke.md
   Request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-pdf-no-text-failure-candidate-runtime-request-refresh.md
   Boundary: `pdf_no_extractable_text`, `chunk_handoff_no_chunks`, `chunk_count -> 0`, and `page_text_char_counts -> [0]` for a valid blank uploaded PDF; not robust PDF extraction, not OCR, not table extraction, not hosted deployment evidence, and not external reviewer feedback.
12. uploaded PDF page diagnostics proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-page-diagnostics-runtime-smoke.md
   Boundary: `page_text_char_counts -> [39]`, `empty_page_count -> 0`, `text_block_count -> 1`, `image_block_count -> 0`, `document_count_delta -> 0`, not robust PDF extraction, not OCR, not table extraction, not hosted deployment evidence, and not external reviewer feedback.
13. uploaded PDF page diagnostics downstream runtime proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-page-diagnostics-downstream-provenance-runtime-smoke.md
   Boundary: `retrieval_candidate_page_text_char_counts -> [39]`, document/chunk/retrieval metadata provenance only, not robust PDF extraction, not OCR, not table extraction, not hosted deployment evidence, and not external reviewer feedback.
14. uploaded PDF retrieval-run provenance runtime proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md
   Boundary: `candidate_parsers -> pdf-pymupdf`, `source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only`, not hosted deployment evidence, not robust PDF extraction, not Evidence Ledger generation, and not external reviewer feedback.
15. uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md
   Boundary: `metadata_json.parser -> pdf-pymupdf`, `metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk`, not hosted deployment evidence, not robust PDF extraction, not Noise Gate behavior, not report generation, and not external reviewer feedback.
15. persisted document failure candidate draft preview runtime proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/persisted-document-failure-candidate-draft-preview-runtime-smoke.md
   Request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-persisted-document-failure-candidate-draft-runtime-request-refresh.md
   Boundary: `preview_only_not_persisted`, `failure_case_count_delta -> 0`, and persisted document `profile_json` handoff into a manual draft; not automatic failure-case creation, not hosted deployment evidence, and not external reviewer feedback.
15. persisted document failure candidate manual handoff runtime proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md
   Request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-persisted-document-failure-candidate-manual-handoff-runtime-request-refresh.md
   Boundary: `failure_case_count_delta -> 1` after human confirmation changes `draft.fix_status` from `draft` to `open`; not automatic failure-case creation, not a confirm endpoint, not hosted deployment evidence, and not external reviewer feedback.
15. uploaded-file chunk persistence proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-chunk-persistence-runtime-smoke.md
   Boundary: not automatic persistence from upload preview, not hosted deployment evidence, and not external reviewer feedback.
16. uploaded-file chunk handoff proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md
   Boundary: explicit `POST /documents/upload-chunks`, not raw uploaded byte storage, not hosted deployment evidence, and not external reviewer feedback.
15. uploaded-file retrieval persistence proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md
   Boundary: `POST /documents/{document_id}/retrieval-runs` over persisted `document_chunks`, not Evidence Ledger generation, not hosted deployment evidence, and not external reviewer feedback.
16. retrieval-run-linked Evidence Ledger proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md
   Boundary: `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, no LLM, no embeddings, no semantic retrieval, not hosted deployment evidence, and not external reviewer feedback.
17. retrieval-run-linked Noise Gate proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md
   Boundary: `POST /retrieval-runs/{retrieval_run_id}/noise-gate` after linked Evidence Ledger rows, not report generation, not hosted deployment evidence, and not external reviewer feedback.
18. retrieval-run-linked Report proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/retrieval-run-linked-report-runtime-smoke.md
   Boundary: `POST /retrieval-runs/{retrieval_run_id}/report` after linked Evidence Ledger and Noise Gate rows, `pre_report_status: 409`, `input_noise_gate_record_id`, no free-form final report generation, not hosted deployment evidence, and not external reviewer feedback.
19. toy semantic retrieval quality report:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/evaluation/semantic-retrieval-quality-report.md
   Boundary: toy fixture metric output with visible `q-what-missing`; not vector search quality evidence, not a benchmark result, not a model comparison, and not external reviewer feedback.
20. uploaded raw file storage proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-storage-runtime-smoke.md
   Boundary: `POST /documents/upload-raw-files` and `GET /documents/upload-raw-files` over quarantined PostgreSQL BYTEA storage; not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.
21. uploaded raw file scan result endpoint proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md
   Boundary: `POST /documents/upload-raw-files/{raw_file_id}/scan-results`, `GET /documents/upload-raw-files/{raw_file_id}/scan-results`, `scan_verdict -> scan_error`, and `response_has_raw_bytes -> false`; not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.
22. ClamAV adapter runtime smoke proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md
   Boundary: deterministic fake-runner smoke for `ClamAvScannerAdapter` mappings; not real ClamAV execution, not signature database evidence, not hosted deployment evidence, not malware scanning, and not external reviewer feedback.
23. uploaded raw file scan execution endpoint runtime proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md
   Boundary: local Docker DB plus live FastAPI HTTP for upload, explicit scan execution, and scan-result listing; default scanner-unavailable returns failed / scan_error, not real ClamAV execution, not malware scanning, and not external reviewer feedback.
24. guarded raw file download endpoint runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-download-endpoint-runtime-smoke.md
   Boundary: local Docker DB plus live FastAPI HTTP for guarded raw download; no-scan download returns `409`, latest clean scan returns `200` bytes, and later failed scan returns `409`; not hosted deployment evidence, not external reviewer feedback, and not production malware scanning evidence.
25. guarded raw file download rate-limit runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-download-rate-limit-runtime-smoke.md
   Boundary: local Docker DB plus live FastAPI HTTP for local v0 guarded raw file download rate limiting; same-file no-scan attempts return `[409, 409, 409, 409, 409]` then `429`, and a separate clean file still downloads with `200`; not hosted deployment evidence, not external reviewer feedback, not distributed rate limiting, and not production authorization.
26. raw file signature validation runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-signature-validation-runtime-smoke.md
   Boundary: local Docker DB plus live FastAPI HTTP for local v0 raw file signature validation; spoofed CSV upload returns `201`, declared PDF mismatch returns `415`, the blocked response has no raw bytes, and the mismatch hash is not recently persisted; not hosted deployment evidence, not external reviewer feedback, not robust file-type detection, not malware scanning evidence, and not production authorization.
27. raw file extension allowlist runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-extension-allowlist-runtime-smoke.md
   Boundary: local Docker DB plus live FastAPI HTTP for local v0 raw file extension allowlisting; allowed CSV upload returns `201`, `sample.exe.csv` double-extension block returns `415`, responses include no raw bytes, and the blocked content hash is not recently persisted; not hosted deployment evidence, not external reviewer feedback, not robust file-type detection, not malware scanning evidence, and not production authorization.
28. raw file download filename safety runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-download-filename-safety-runtime-smoke.md
   Boundary: local Docker FastAPI for local v0 guarded raw file download attachment filename safety; path-like and URL-encoded-control CSV filename input downloads with a 120-character safe attachment filename and `local_v0_content_disposition_filename_safety_not_production`; not hosted deployment evidence, not external reviewer feedback, not malware detection proof, not robust file serving, and not production authorization.
29. raw file download audit runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-download-audit-runtime-smoke.md
   Boundary: local Docker FastAPI plus PostgreSQL for local v0 guarded raw file download audit events; missing-scan `409`, rate-limited `[409, 409, 409, 409, 409, 429]`, and allowed `200` decisions persist to `raw_file_download_events`; not hosted deployment evidence, not external reviewer feedback, not malware detection proof, not production authorization, and not user identity.
30. raw file download approval gate behavior runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-download-approval-gate-behavior-runtime-smoke.md
   Boundary: local Docker FastAPI plus PostgreSQL for local v0 approval-gated raw file downloads; latest-clean/no-approval returns `409` with `missing_download_approval`, non-active approval returns `409` with `revoked_or_expired_download_approval`, and active approval returns `200` with `download_approval_id` in audit metadata; not hosted deployment evidence, not external reviewer feedback, not production authorization, not user identity, and not signed URL support.
31. raw file download approval input guard runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-download-approval-input-guard-runtime-smoke.md
   Boundary: local Docker FastAPI plus PostgreSQL for local v0 approval input validation; valid approval metadata creates/lists, unknown approval status returns `422`, and already expired active approval returns `422`; not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated user identity, and not signed URL support.
32. raw file download approval audit metadata runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-download-approval-audit-metadata-runtime-smoke.md
   Boundary: local Docker FastAPI plus PostgreSQL for local v0 approval audit metadata; active approval download returns `200`, allowed event metadata keeps approval id/status/expiry/latest-scan match, and identity remains `operator_label_not_authenticated_identity`; not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated user identity, and not signed URL support.
33. raw file download readiness runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-download-readiness-runtime-smoke.md
   Boundary: local Docker FastAPI plus PostgreSQL for local v0 download readiness preflight; before scan returns `missing_clean_scan`, after clean scan without active approval returns `missing_download_approval`, active approval returns `allowed`, no raw bytes are returned, no rate limit is consumed, and no download audit event is written; not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated user identity, and not signed URL support.
34. raw file guard ops summary runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-guard-ops-summary-runtime-smoke.md
   Boundary: local Docker PostgreSQL plus live FastAPI HTTP for raw upload, blocked missing-scan download, failed/clean scan metadata, active approval, allowed download, `/ops/summary` deltas, and `/ops/dashboard` labels; not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated identity, and not signed URL support.
35. architecture current-state ClamAV proof boundary refresh:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/architecture-current-state-clamav-proof-boundary-refresh.md
   Boundary: recognizes the local ClamAV endpoint malicious-detection owner-runtime smoke while still not claiming production malware scanning evidence, hosted deployment evidence, external reviewer feedback, production authorization, or product completion.
36. ClamAV API endpoint malicious-detection owner-runtime smoke:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md
   Boundary: local Docker FastAPI plus ClamAV endpoint evidence for owner-provided stdin input; `harness_status: verified_infected`, `scan_verdict: infected`, `matched_signature: Eicar-Test-Signature`, `payload_committed_to_repo: false`, and `raw_payload_logged: false`; not hosted deployment evidence, not external reviewer feedback, and not production malware scanning evidence.
37. Feedback intake criteria:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-feedback-intake-criteria.md

## Optional Public Portfolio Route

Latest public proof route:

https://svy04.github.io/proof-artifacts/noiseproof-live-route-verification-2026-06-01/

Repository route verification:

https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-live-proof-route-refresh.md

Live issue body verification:

https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-review-issue-body-encoding-verification.md

https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-review-issue-body-root-guide-verification.md

https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-review-issue-body-link-map-verification.md

## Review Questions

Please leave one evidence-referenced comment on issue #1.

Useful questions:

```text
Which claim feels over-stated?
Which artifact is easiest to inspect?
Which artifact is too self-authored or too weak?
What missing evidence would most improve trust?
Does this signal Forward Deployed Engineer work?
What does it not yet prove for Product Engineer?
What should be cut, compressed, or made more direct?
```

## Preferred Comment Shape

```text
Reviewer role:
Evidence inspected:
Feedback:
Claim boundary:
Missing evidence:
Hiring signal:
Optional next action:
```

## Allowed Claim

NoiseProof Agent has a direct link map for external reviewers so they can reach the proof path and public feedback issue without navigating the repository tree manually.

## Boundary

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not hosted deployment evidence.

This does not prove that any reviewer has inspected the repository.

This does not accept any issue comment into the proof path.

The next gate remains:

```text
external reviewer feedback v0
```

## Latest Table-candidate Downstream Proof Routing

uploaded PDF table-candidate downstream runtime proof:

```text
docs/review/uploaded-pdf-table-candidate-downstream-provenance-runtime-smoke.md
docs/review/uploaded-pdf-table-candidate-downstream-provenance-remote-verification.md
docs/review/external-reviewer-pdf-table-candidate-downstream-runtime-request-refresh.md
retrieval_candidate_table_candidate_count -> 1
```

Boundary: request routing only; not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction, not table extraction, and not product-complete.
