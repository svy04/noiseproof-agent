---
name: External review feedback
about: Leave bounded feedback on the NoiseProof Agent portfolio proof path
title: "External review feedback: "
labels: ["external-review", "feedback"]
assignees: ""
---

## Reviewer role

<!-- Example: FDE, product engineer, backend engineer, RAG engineer, founder, hiring reviewer, domain expert. -->

## Evidence inspected

<!-- Link or list the artifacts you actually inspected. Please include only what you opened. -->

Fast links:

- Reviewer shortlist: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-shortlist.md
- Reviewer link map: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-link-map.md
- Root review guide: https://github.com/svy04/noiseproof-agent/blob/main/CONTRIBUTING.md
- README: https://github.com/svy04/noiseproof-agent/blob/main/README.md
- External-reader proof path: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reader-proof-path.md
- Portfolio index: https://github.com/svy04/noiseproof-agent/blob/main/docs/application/portfolio-index.md
- workflow proof bundle runtime smoke: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-proof-bundle-runtime-smoke.md
  - Request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-proof-bundle-request-refresh.md
  - Boundary: local Docker PostgreSQL plus live FastAPI HTTP proof for `GET /workflow-runs/{id}/proof-bundle`; not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not distributed tracing, not hosted observability, not new lineage storage, and not product-complete.
- workflow proof bundle dashboard runtime smoke: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md
  - Request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-proof-bundle-dashboard-runtime-request-refresh.md
  - Boundary: local Docker PostgreSQL plus live FastAPI HTTP proof that `GET /ops/dashboard` includes the workflow `proof bundle` link and the linked `GET /workflow-runs/{id}/proof-bundle` route returns `200`; not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not distributed tracing, not hosted observability, not new lineage storage, and not product-complete.
- ops dashboard anchor GET runtime smoke: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/ops-dashboard-anchor-get-runtime-smoke.md
  - Request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md
  - Boundary: local Docker PostgreSQL plus live FastAPI HTTP proof that `GET /ops/dashboard` exposed 38 clickable `data-method="GET"` anchors, 25 unique hrefs, and every unique href returned GET 200; not a live issue body edit, not browser automation evidence, not external reviewer feedback, not hosted deployment evidence, and not product-complete.
- ops dashboard anchor browser smoke: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/ops-dashboard-anchor-browser-smoke.md
  - Request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md
  - Boundary: local Playwright browser automation proof that `GET /ops/dashboard` rendered 27 clickable anchors, all 27 carried `data-method="GET"`, no `data-method="POST"` anchors existed, and `POST /failure-cases/draft-preview` remained a visible method cue rather than a clickable anchor; not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not customer validation, and not product-complete.
- workflow proof bundle failure-case links runtime smoke: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md
  - Request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md
  - Boundary: local Docker PostgreSQL plus live FastAPI HTTP proof that linked `failure_cases` appear in `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/proof-bundle`, while `GET /failure-cases?workflow_run_id={id}` filters out an unrelated failure case; not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not automatic failure detection, not background automation, and not complete workflow failure causality.
- workflow dashboard failure-case counts runtime smoke: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-dashboard-failure-case-counts-runtime-smoke.md
  - Request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-dashboard-failure-case-counts-runtime-request-refresh.md
  - Boundary: local Docker PostgreSQL plus live FastAPI HTTP proof that `GET /ops/dashboard` shows linked failure-case count/filter links, including `dashboard_contains_linked_failure_case_filter: true` and `dashboard_omits_unlinked_failure_case_filter: true`; not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not automatic failure detection, not background automation, and not complete workflow failure causality.
- workflow failure-case persistence handoff runtime smoke: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md
  - Request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-workflow-failure-case-persistence-runtime-request-refresh.md
  - Boundary: local Docker PostgreSQL plus live FastAPI HTTP proof for caller-triggered `POST /failure-cases/workflow-runs/{workflow_run_id}`, review queue `failure_case_linked`, completed-workflow `409`, and duplicate `409`; not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not background automation, and not complete workflow failure causality.
- embedding provider owner-runtime smoke packet: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md
  - Request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-packet-request-refresh.md
  - Validator: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-validator.md
  - Post-run validation command: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-command.md
  - Validator request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-validator-request-refresh.md
  - Response handoff: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-response-handoff-report.md
  - Command-template handoff alignment: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment.md
  - Handoff alignment CI remote verification: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment-ci-remote-verification.md
  - Handoff request refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-handoff-alignment-request-refresh.md
  - Boundary: no-secret/no-call owner-runtime smoke contract with `api_calls_attempted: false` and `openai_api_key_printed: false`; response handoff command `--build-owner-runtime-smoke-report-from-response`; packet field `response_handoff_command`; not live embedding generation proof, not hosted deployment evidence, not semantic retrieval quality evidence, and not external reviewer feedback.
- Local browser screenshot walkthrough: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/local-browser-screenshot-walkthrough.md
- uploaded-file intake manifest proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-intake-manifest-runtime-smoke.md
  - Boundary: not raw file storage, not hosted deployment evidence, and not external reviewer feedback.
- uploaded-file intake manifest persistence proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md
  - Boundary: manifest metadata only, not raw file storage, not hosted deployment evidence, and not external reviewer feedback.
- uploaded-file parsed document persistence proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md
  - Boundary: document metadata/profile only, not raw file storage, not parsed text persistence, not hosted deployment evidence, and not external reviewer feedback.
- uploaded PDF downstream handoff proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md
  - Boundary: `parser -> pdf-pymupdf`, digital PDF text only, not robust PDF extraction, not OCR, not table extraction, not hosted deployment evidence, and not external reviewer feedback.
- uploaded PDF retrieval-run provenance runtime proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md
  - Boundary: `candidate_parsers -> pdf-pymupdf`, `source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only`, not hosted deployment evidence, not robust PDF extraction, not Evidence Ledger generation, and not external reviewer feedback.
- uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md
  - Boundary: `metadata_json.parser -> pdf-pymupdf`, `metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk`, not hosted deployment evidence, not robust PDF extraction, not Noise Gate behavior, not report generation, and not external reviewer feedback.
- uploaded-file chunk persistence proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-chunk-persistence-runtime-smoke.md
  - Boundary: not automatic persistence from upload preview, not hosted deployment evidence, and not external reviewer feedback.
- uploaded-file chunk handoff proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md
  - Boundary: explicit `POST /documents/upload-chunks`, not raw uploaded byte storage, not hosted deployment evidence, and not external reviewer feedback.
- uploaded-file retrieval persistence proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md
  - Boundary: `POST /documents/{document_id}/retrieval-runs` over persisted `document_chunks`, not Evidence Ledger generation, not hosted deployment evidence, and not external reviewer feedback.
- retrieval-run-linked Evidence Ledger proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md
  - Boundary: `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, no LLM, no embeddings, no semantic retrieval, not hosted deployment evidence, and not external reviewer feedback.
- retrieval-run-linked Noise Gate proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md
  - Boundary: `POST /retrieval-runs/{retrieval_run_id}/noise-gate`, not report generation, not hosted deployment evidence, and not external reviewer feedback.
- retrieval-run-linked Report proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/retrieval-run-linked-report-runtime-smoke.md
  - Boundary: `POST /retrieval-runs/{retrieval_run_id}/report`, `pre_report_status: 409`, `input_noise_gate_record_id`, no free-form final report generation, not hosted deployment evidence, and not external reviewer feedback.
- toy semantic retrieval quality report: https://github.com/svy04/noiseproof-agent/blob/main/docs/evaluation/semantic-retrieval-quality-report.md
  - Boundary: toy fixture metric output with visible `q-what-missing`; not vector search quality evidence, not a benchmark result, not a model comparison, and not external reviewer feedback.
- uploaded raw file storage proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-storage-runtime-smoke.md
  - Boundary: `POST /documents/upload-raw-files` and `GET /documents/upload-raw-files` over quarantined PostgreSQL BYTEA storage; not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.
- uploaded raw file scan result endpoint proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md
  - Boundary: `POST /documents/upload-raw-files/{raw_file_id}/scan-results`, `GET /documents/upload-raw-files/{raw_file_id}/scan-results`, `scan_verdict -> scan_error`, and `response_has_raw_bytes -> false`; not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.
- ClamAV adapter runtime smoke proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md
  - Boundary: deterministic fake-runner smoke for adapter mappings; not real ClamAV execution, not signature database evidence, not hosted deployment evidence, not malware scanning, and not external reviewer feedback.
- uploaded raw file scan execution endpoint runtime proof: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md
  - Boundary: local Docker DB plus live FastAPI HTTP for upload, explicit scan execution, and scan-result listing; default scanner-unavailable returns failed / scan_error, not real ClamAV execution, not malware scanning, and not external reviewer feedback.
- raw file download readiness runtime smoke: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-download-readiness-runtime-smoke.md
  - Boundary: local Docker FastAPI plus PostgreSQL for read-only guarded download readiness; no-scan blocks with `missing_clean_scan`, clean scan without active approval blocks with `missing_download_approval`, active approval allows readiness, and the endpoint returns no raw bytes, consumes no rate limit, and writes no download audit event.
- raw file guard ops summary runtime smoke: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-raw-file-guard-ops-summary-runtime-smoke.md
  - Boundary: local Docker PostgreSQL plus live FastAPI HTTP for raw upload, blocked missing-scan download, failed/clean scan metadata, active approval, allowed download, `/ops/summary` deltas, and `/ops/dashboard` labels; not production authorization, authenticated identity, signed URL support, hosted deployment evidence, or external reviewer feedback.
- architecture current-state ClamAV proof boundary refresh: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/architecture-current-state-clamav-proof-boundary-refresh.md
  - Boundary: recognizes the local ClamAV endpoint malicious-detection owner-runtime smoke while still not claiming production malware scanning evidence, hosted deployment evidence, external reviewer feedback, production authorization, or product completion.
- Feedback intake criteria: https://github.com/svy04/noiseproof-agent/blob/main/docs/review/external-feedback-intake-criteria.md
- Public feedback issue: https://github.com/svy04/noiseproof-agent/issues/1

## Feedback

<!-- What is the most useful critique? What would make the portfolio stronger? -->

## Claim boundary

<!-- Which claim feels over-stated, unclear, or under-supported? -->

## Missing evidence

<!-- What is missing before you would trust this as a stronger portfolio artifact? -->

## Hiring signal

<!-- If relevant: what role does this currently signal, and what role does it not yet prove? -->

## Optional next action

<!-- What one follow-up artifact would most improve the reviewer path? -->
