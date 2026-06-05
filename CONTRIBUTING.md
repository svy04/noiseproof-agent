# External Review Guide

This repository is currently asking for bounded external review of the NoiseProof Agent portfolio proof path.

The next evidence gate is:

```text
external reviewer feedback v0
```

## Fast Path

Please start here:

Shortest path first: `docs/review/external-reviewer-shortlist.md`

1. `README.md`
2. `docs/review/external-reader-proof-path.md`
3. `docs/review/external-reviewer-link-map.md`
4. `docs/application/portfolio-index.md`
5. `docs/review/workflow-proof-bundle-runtime-smoke.md`
   - workflow proof bundle runtime smoke via `GET /workflow-runs/{id}/proof-bundle`; request refresh: `docs/review/external-reviewer-workflow-proof-bundle-request-refresh.md`; not distributed tracing, hosted observability, hosted deployment evidence, external reviewer feedback, or product-complete.
   - dashboard runtime proof: `docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-proof-bundle-dashboard-runtime-request-refresh.md`; verifies `GET /ops/dashboard` includes the workflow `proof bundle` link and the linked proof bundle route returns `200`; not a live issue body edit, not distributed tracing, hosted observability, hosted deployment evidence, external reviewer feedback, or product-complete.
   - ops dashboard anchor GET runtime proof: `docs/review/ops-dashboard-anchor-get-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md`; verifies `GET /ops/dashboard` exposed 38 clickable `data-method="GET"` anchors, 25 unique hrefs, and every unique href returned GET 200; not a live issue body edit, browser automation evidence, hosted deployment evidence, external reviewer feedback, or product-complete.
   - ops dashboard anchor browser smoke: `docs/review/ops-dashboard-anchor-browser-smoke.md`; request refresh: `docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md`; verifies local Playwright browser automation opened `GET /ops/dashboard`, observed 27 clickable anchors, all 27 carried `data-method="GET"`, and `POST /failure-cases/draft-preview` remained a visible method cue rather than a clickable anchor; not a live issue body edit, hosted deployment evidence, external reviewer feedback, customer validation, design quality evidence, or product-complete.
   - workflow proof bundle failure-case links runtime proof: `docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md`; verifies linked `failure_cases` surface through `GET /workflow-runs/{id}`, `GET /workflow-runs/{id}/proof-bundle`, and `GET /failure-cases?workflow_run_id={id}` with `detail_failure_case_count: 1`, `bundle_failure_case_count: 1`, and `unrelated_filtered_out: true`; not a live issue body edit, automatic failure detection, background automation, hosted deployment evidence, external reviewer feedback, or complete workflow failure causality.
   - workflow dashboard failure-case counts runtime proof: `docs/review/workflow-dashboard-failure-case-counts-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-dashboard-failure-case-counts-runtime-request-refresh.md`; verifies `GET /ops/dashboard` shows linked failure-case count/filter links with `dashboard_contains_linked_failure_case_filter: true` and `dashboard_omits_unlinked_failure_case_filter: true`; not a live issue body edit, automatic failure detection, background automation, hosted deployment evidence, external reviewer feedback, or complete workflow failure causality.
   - workflow failure-case persistence runtime proof: `docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-failure-case-persistence-runtime-request-refresh.md`; verifies caller-triggered `POST /failure-cases/workflow-runs/{workflow_run_id}` persistence, review queue `failure_case_linked`, completed-workflow `409`, and duplicate `409`; not a live issue body edit, background automation, hosted deployment evidence, external reviewer feedback, or complete workflow failure causality.
   - provider smoke packet: `docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md`; validator: `docs/review/embedding-model-live-provider-owner-runtime-smoke-validator.md`; post-run validation command: `docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-command.md`; response handoff: `docs/review/embedding-model-live-provider-owner-runtime-smoke-response-handoff-report.md`; command-template handoff alignment: `docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment.md`; handoff alignment CI: `docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment-ci-remote-verification.md`; request refresh: `docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-packet-request-refresh.md`; validator request refresh: `docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-validator-request-refresh.md`; handoff request refresh: `docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-handoff-alignment-request-refresh.md`; `api_calls_attempted: false`, `openai_api_key_printed: false`, not live embedding generation proof, hosted deployment evidence, external reviewer feedback, or product-complete.
6. `docs/review/uploaded-file-intake-manifest-runtime-smoke.md`
   - uploaded-file intake manifest proof; not raw file storage, not hosted deployment evidence, and not external reviewer feedback.
7. `docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md`
   - uploaded-file intake manifest persistence proof; not raw file storage, not hosted deployment evidence, and not external reviewer feedback.
8. `docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md`
   - uploaded-file parsed document persistence proof; not raw file storage, not parsed text persistence, not hosted deployment evidence, and not external reviewer feedback.
9. `docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md`
   - uploaded PDF downstream handoff proof with `parser -> pdf-pymupdf`; digital PDF text only, not robust PDF extraction, not OCR, not table extraction, not hosted deployment evidence, and not external reviewer feedback.
10. `docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md`
   - uploaded PDF retrieval-run provenance runtime proof with `candidate_parsers -> pdf-pymupdf` and `source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only`; not hosted deployment evidence, not robust PDF extraction, not Evidence Ledger generation, and not external reviewer feedback.
11. `docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md`
   - uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime proof with `metadata_json.parser -> pdf-pymupdf` and `metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk`; not hosted deployment evidence, not robust PDF extraction, not Noise Gate behavior, not report generation, and not external reviewer feedback.
12. `docs/review/uploaded-file-chunk-persistence-runtime-smoke.md`
   - uploaded-file chunk persistence proof; not automatic persistence from upload preview, not hosted deployment evidence, and not external reviewer feedback.
13. `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md`
   - uploaded-file chunk handoff proof via `POST /documents/upload-chunks`; not raw uploaded byte storage, not hosted deployment evidence, and not external reviewer feedback.
14. `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`
   - uploaded-file retrieval persistence proof via `POST /documents/{document_id}/retrieval-runs`; not Evidence Ledger generation, not hosted deployment evidence, and not external reviewer feedback.
15. `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md`
   - retrieval-run-linked Evidence Ledger proof via `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`; no LLM, no embeddings, no semantic retrieval, not hosted deployment evidence, and not external reviewer feedback.
16. `docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md`
   - retrieval-run-linked Noise Gate proof via `POST /retrieval-runs/{retrieval_run_id}/noise-gate`; not report generation, not hosted deployment evidence, and not external reviewer feedback.
17. `docs/review/retrieval-run-linked-report-runtime-smoke.md`
   - retrieval-run-linked Report proof via `POST /retrieval-runs/{retrieval_run_id}/report`; records `pre_report_status: 409` and `input_noise_gate_record_id`, not hosted deployment evidence, and not external reviewer feedback.
18. `docs/evaluation/semantic-retrieval-quality-report.md`
   - toy semantic retrieval quality report; keeps `q-what-missing` visible, not vector search quality evidence, not a benchmark result, and not external reviewer feedback.
19. `docs/review/uploaded-raw-file-storage-runtime-smoke.md`
   - uploaded raw file storage proof via `POST /documents/upload-raw-files` and `GET /documents/upload-raw-files`; not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.
20. `docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md`
   - uploaded raw file scan result endpoint proof via `POST /documents/upload-raw-files/{raw_file_id}/scan-results` and `GET /documents/upload-raw-files/{raw_file_id}/scan-results`; `scan_verdict -> scan_error`, not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.
21. `docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md`
   - ClamAV adapter runtime smoke proof through fake runners; not real ClamAV execution, not signature database evidence, not hosted deployment evidence, not malware scanning, and not external reviewer feedback.
22. `docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md`
   - explicit raw upload scan execution endpoint proof via local Docker DB and live FastAPI HTTP; default scanner-unavailable returns failed / scan_error, not real ClamAV execution, not malware scanning, and not external reviewer feedback.
23. `docs/review/external-feedback-intake-criteria.md`

Public feedback issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Useful Review Questions

Please leave one evidence-referenced comment that names what you inspected.

Useful critique can answer one of these:

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

## Boundary

This guide is not external reviewer feedback.

This guide is not customer validation.

This guide is not Braincrew acceptance.

This guide is not hosted deployment evidence.

Self-authored comments, generic praise, issue status updates, bot summaries, and CI checks do not close the `external reviewer feedback v0` gate.

The gate advances only when an outside reviewer leaves substantive, evidence-referenced feedback that satisfies:

```text
docs/review/external-feedback-intake-criteria.md
```
