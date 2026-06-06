# External-reader Proof Path

Status: compact proof index.

Phase marker: external-reader proof path index v0.

This page is the shortest repository-native path for an external reviewer who wants to inspect what NoiseProof Agent currently proves without reading the entire phase history.

## 5-minute path

For a shorter first pass, start with:

```text
docs/review/external-reviewer-shortlist.md
```

## Current Proof Route

Evidence quality risk ops proof:

```text
docs/review/evidence-quality-risk-ops-surface.md
docs/review/evidence-quality-risk-ops-surface-runtime-smoke.md
docs/review/evidence-quality-risk-ops-surface-runtime-smoke-remote-verification.md
docs/review/external-reader-proof-path-evidence-quality-risk-ops-route-refresh.md
```

Boundary: this current route points first-pass reviewers to the operations surface where persisted Evidence Ledger rows drive `weakly_supported_evidence_count`, `low_confidence_evidence_count`, `missing_source_date_evidence_count`, and `evidence_quality_risk_count` in `GET /ops/summary`, and where `GET /ops/dashboard` renders `Weak Evidence`, `Low Confidence Evidence`, `Missing Source Dates`, and `Evidence Quality Risk Rows`. This route alignment is not new runtime evidence. It is not a live issue body edit, not final truth adjudication, not retrieval quality evidence, not Evidence Ledger quality evidence, not embedding generation, not an LLM call, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Workflow proof bundle markdown export runtime proof:

```text
docs/review/workflow-proof-bundle-markdown-export.md
docs/review/workflow-proof-bundle-markdown-export-runtime-smoke.md
docs/review/external-reader-proof-path-workflow-markdown-runtime-route-refresh.md
```

Boundary: this current route points first-pass reviewers to the local runtime proof that `GET /ops/dashboard` exposes the `proof markdown` link and `GET /workflow-runs/{id}/proof-bundle/markdown` returns `200` with `text/markdown; charset=utf-8`. This route alignment is not new runtime evidence. It is not external reviewer feedback, not hosted deployment evidence, not distributed tracing, not hosted observability, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, not final truth adjudication, and not product-complete.

Focused uploaded PDF encrypted handoff ops proof:

```text
docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops.md
docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-runtime-smoke.md
docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-remote-verification.md
docs/review/external-reader-proof-path-encrypted-pdf-handoff-ops-route-refresh.md
docs/review/external-reader-proof-path-encrypted-pdf-handoff-ops-route-refresh-remote-verification.md
```

Boundary: this focused route proves that password-protected uploaded PDFs can be preserved as explicit failure metadata through `POST /documents/upload-chunks` and surfaced as `pdf_encrypted_failure_candidate_count` / `PDF Encrypted Failure Candidates` in operations views. This route alignment is not new runtime evidence, not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction, not OCR, not table extraction, not layout fidelity, not decryption, not password bypass, not customer validation, not Braincrew acceptance, and not product-complete.

Workflow proof bundle reviewer checklist dashboard runtime proof:

```text
docs/review/workflow-proof-bundle-reviewer-checklist-dashboard-discovery.md
docs/review/workflow-proof-bundle-reviewer-checklist-dashboard-runtime-smoke.md
docs/review/external-reader-proof-path-workflow-checklist-dashboard-runtime-route-refresh.md
```

Boundary: this predecessor route proves that the local operations dashboard can route a reviewer to the workflow proof bundle through a visible `reviewer checklist` link, and that the linked proof bundle returns four read-only checklist items: `detail_counts`, `lineage_links`, `trace_lookup`, and `failure_case_handoff`. This route is not external reviewer feedback, not hosted deployment evidence, not distributed tracing, not hosted observability, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, not final truth adjudication, and not product-complete.

Report markdown local inspection paths proof:

```text
docs/review/report-markdown-local-inspection-paths.md
docs/review/report-markdown-local-inspection-paths-runtime-smoke.md
docs/review/report-markdown-local-inspection-paths-runtime-smoke-remote-verification.md
docs/review/external-review-issue-body-report-markdown-local-inspection-route-refresh.md
```

Boundary: this predecessor report-inspection route proves that a persisted Report markdown export can show local inspection paths for the current report markdown export, report workflow-trace filter, workflow trace lookup, retrieval-run list, Evidence Ledger list, and Noise Gate list, while preserving stage input ids and source retrieval provenance. The issue-body refresh is owner-authored routing only. This route is not external reviewer feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, not final truth adjudication, and not product-complete.

Retrieval-run-linked Gate/Report semantic source provenance proof:

```text
docs/review/retrieval-run-linked-gate-report-semantic-source-provenance.md
docs/review/retrieval-run-linked-gate-report-semantic-source-provenance-runtime-smoke.md
docs/review/retrieval-run-linked-gate-report-semantic-source-provenance-runtime-smoke-remote-verification.md
docs/review/external-review-issue-body-gate-report-semantic-source-provenance-runtime-refresh.md
```

Boundary: this predecessor source-provenance route proves semantic source-provenance preservation from a persisted retrieval run through retrieval-run-linked Evidence Ledger metadata into downstream Noise Gate and Report warnings, stage input manifests, and agent-run traces. It is not external reviewer feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, not final truth adjudication, and not product-complete.

Retrieval-run-linked Evidence Ledger semantic source provenance proof:

```text
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance.md
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke.md
docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke-remote-verification.md
docs/review/external-review-issue-body-retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-refresh.md
docs/review/external-feedback-current-state-retrieval-run-linked-evidence-ledger-semantic-source-provenance-issue-verification-remote-verification.md
```

Boundary: this predecessor route proves source-provenance preservation from a persisted semantic retrieval run into the retrieval-run-linked Evidence Ledger handoff and reviewer routing. It is not external reviewer feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not final truth adjudication, and not product-complete.

Persisted Report markdown export proof:

```text
docs/review/persisted-report-markdown-export.md
GET /reports/{report_record_id}/markdown
docs/review/persisted-report-markdown-export-remote-verification.md
```

Boundary: this proof is a deterministic read/export surface over existing persisted `report_records` rows. It is not free-form report generation, not a new report-generation path, not an LLM call, not retrieval, not Evidence Ledger creation, not Noise Gate behavior, not Report record creation, not financial advice, not hosted deployment evidence, and not external reviewer feedback.

Read in this order:

1. `README.md`
   - Purpose, non-goals, implementation status, and current boundaries.
2. `docs/application/portfolio-index.md`
   - Repository map from system surface to proof artifacts.
3. `docs/review/failure-case-workflow-parent-linkage-proof-index.md`
   - Compact reader path for manual failure-case workflow parent linkage.
   - Related proof index: `docs/review/failure-case-workflow-review-queue-proof-index.md`
   - Purpose: compact reader path for the failed workflow review queue, dashboard surfacing, and fresh DB dashboard proof.
4. `docs/review/application-ready-review.md`
   - Current application-readiness judgment and claim boundaries.
5. `docs/application/braincrew-role-map.md`
   - Role mapping and application narrative.
6. `docs/review/portfolio-site-proof-artifact-route-verification.md`
   - Live portfolio route verification for the public NoiseProof proof surface.
7. `docs/review/demo-transcript-capture.md`
   - Self-authored local route transcript for collection planning, workflow preview, lineage, and dashboard inspection.
8. `docs/review/local-browser-screenshot-walkthrough.md`
   - Self-authored local browser screenshot walkthrough for the operations dashboard and workflow-run lineage link.
9. `docs/review/external-review-request.md`
   - Structured request packet for external critique. This is not feedback itself.
10. `docs/review/external-reviewer-brief.md`
    - 2-minute path for a reviewer before leaving feedback.
11. `docs/review/external-reviewer-live-proof-route-refresh.md`
    - Latest public portfolio proof route for reviewer orientation. This is not feedback itself.
12. `docs/review/external-reviewer-outreach-packet.md`
    - Copy-paste outreach messages for actual human reviewers. This is not feedback itself.
13. `docs/review/external-reviewer-link-map.md`
    - Direct GitHub and public route links for reviewers. This is not feedback itself.
14. `docs/review/uploaded-file-intake-manifest-runtime-smoke.md`
    - uploaded-file intake manifest proof with content hash and storage boundary. This is not raw file storage.
15. `docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md`
    - uploaded-file intake manifest persistence proof with manifest metadata persistence and no raw file storage.
16. `docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md`
    - uploaded-file parsed document persistence proof with document metadata/profile persistence and no raw file storage.
17. `docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md`
    - uploaded PDF downstream handoff proof with `parser -> pdf-pymupdf`, `digital_pdf_text_extraction -> true`, upload chunk preview, explicit upload-to-chunks persistence, listed chunk lookup, and upload retrieval preview.
    - related uploaded PDF no-text failure candidate runtime proof: `docs/review/uploaded-pdf-no-text-failure-candidate-runtime-smoke.md` records `pdf_no_extractable_text`, `chunk_handoff_no_chunks`, `chunk_count -> 0`, `page_text_char_counts -> [0]`, and `robust_pdf_extraction -> false` for a valid blank uploaded PDF; request refresh: `docs/review/external-reviewer-pdf-no-text-failure-candidate-runtime-request-refresh.md`; not robust PDF extraction, not OCR, not table extraction, not hosted deployment evidence, and not external reviewer feedback.
    - related uploaded PDF page diagnostics proof: `docs/review/uploaded-pdf-page-diagnostics-runtime-smoke.md` records `page_text_char_counts -> [39]`, `empty_page_count -> 0`, `text_block_count -> 1`, `image_block_count -> 0`, and `document_count_delta -> 0`.
    - related downstream page diagnostics provenance: `docs/review/uploaded-pdf-page-diagnostics-downstream-provenance.md` records page diagnostics flowing into explicit upload chunk metadata and document retrieval-run candidate metadata.
    - related downstream page diagnostics runtime smoke: `docs/review/uploaded-pdf-page-diagnostics-downstream-provenance-runtime-smoke.md` records local Docker/FastAPI HTTP evidence for page diagnostics flowing through document, chunk, retrieval, and candidate metadata.
    - related uploaded PDF page diagnostics downstream runtime proof: `docs/review/uploaded-pdf-page-diagnostics-downstream-provenance-runtime-smoke.md` records `retrieval_candidate_page_text_char_counts -> [39]`.
    - related uploaded PDF encrypted handoff ops proof: `docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops.md`, `docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-runtime-smoke.md`, and `docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-remote-verification.md` record `pdf_encrypted_failure_candidate_count`, `PDF Encrypted Failure Candidates`, and a password-required PDF failure-mode boundary; route refresh: `docs/review/external-reader-proof-path-encrypted-pdf-handoff-ops-route-refresh.md`; not robust PDF extraction, not decryption, not hosted deployment evidence, not external reviewer feedback, and not product-complete.
18. `docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md`
    - uploaded PDF retrieval-run provenance runtime proof with `POST /documents/upload-chunks`, `POST /documents/{document_id}/retrieval-runs`, `candidate_parsers -> pdf-pymupdf`, and `source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only`.
19. `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md`
    - uploaded-file chunk handoff proof with explicit `POST /documents/upload-chunks` and no raw uploaded byte storage.
20. `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`
    - uploaded-file retrieval persistence proof with explicit `POST /documents/{document_id}/retrieval-runs`, persisted `retrieval_runs`, and no Evidence Ledger generation.
21. `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md`
    - retrieval-run-linked Evidence Ledger proof with explicit `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`.
22. `docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md`
    - retrieval-run-linked Noise Gate proof with explicit `POST /retrieval-runs/{retrieval_run_id}/noise-gate` after linked ledger rows.
23. `docs/review/retrieval-run-linked-report-runtime-smoke.md`
    - retrieval-run-linked Report proof with explicit `POST /retrieval-runs/{retrieval_run_id}/report`, `pre_report_status: 409`, and `input_noise_gate_record_id`.
24. `docs/review/persisted-report-markdown-export.md`
    - persisted Report markdown export proof with explicit `GET /reports/{report_record_id}/markdown`; renders existing persisted report records as deterministic markdown and keeps the no-new-claims boundary.
    - related remote verification: `docs/review/persisted-report-markdown-export-remote-verification.md`.
25. `docs/review/embedding-endpoint-runtime-smoke.md`
    - caller-provided chunk embedding endpoint proof with explicit `POST /chunks/{chunk_id}/embeddings`, `GET /chunks/{chunk_id}/embeddings`, and generated-claim rejection `400`.
26. `docs/review/semantic-retrieval-persistence-runtime-smoke.md`
    - caller-provided semantic retrieval persistence proof with explicit `POST /documents/{document_id}/semantic-retrieval-runs`, `GET /retrieval-runs`, dimension mismatch `400`, and unchanged Evidence Ledger counts.
27. `docs/evaluation/semantic-retrieval-quality-report.md`
    - toy semantic retrieval quality report with visible misses and disagreement; not vector search quality evidence.
Related provider packet: `docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md`
    - embedding provider owner-runtime smoke packet with `api_calls_attempted: false`, `openai_api_key_printed: false`, and owner-provided `OPENAI_API_KEY` kept outside the repository; validator: `docs/review/embedding-model-live-provider-owner-runtime-smoke-validator.md`; post-run validation command: `docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-command.md`; response handoff: `docs/review/embedding-model-live-provider-owner-runtime-smoke-response-handoff-report.md`; command-template handoff alignment: `docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment.md`; handoff alignment CI remote verification: `docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment-ci-remote-verification.md`; request refresh: `docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-packet-request-refresh.md`; validator request refresh: `docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-validator-request-refresh.md`; handoff request refresh: `docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-handoff-alignment-request-refresh.md`; not live embedding generation proof, not hosted deployment evidence, not semantic retrieval quality evidence, and not external reviewer feedback.
27. `docs/review/uploaded-raw-file-storage-runtime-smoke.md`
    - uploaded raw file storage proof with explicit `POST /documents/upload-raw-files`, `GET /documents/upload-raw-files`, quarantined PostgreSQL BYTEA storage, no malware scanning, and no download endpoint.
28. `docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md`
    - uploaded raw file scan result endpoint proof with explicit `POST /documents/upload-raw-files/{raw_file_id}/scan-results`, `GET /documents/upload-raw-files/{raw_file_id}/scan-results`, `scan_verdict -> scan_error`, `response_has_raw_bytes -> false`, no malware scanning, and no download endpoint.
29. `docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md`
    - ClamAV adapter runtime smoke proof with deterministic fake-runner scenarios; no real ClamAV execution, no signature database evidence, no malware scanning, and no download endpoint.
30. `docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md`
    - uploaded raw file scan execution endpoint runtime proof with local Docker DB and live FastAPI HTTP; default scanner-unavailable returns failed / scan_error, no real ClamAV execution, no malware scanning, and no download endpoint.
31. `docs/review/uploaded-raw-file-download-endpoint-runtime-smoke.md`
    - guarded raw file download endpoint runtime smoke with local Docker DB and live FastAPI HTTP; no-scan download returns `409`, latest clean scan returns `200` bytes, later failed scan returns `409`; not hosted deployment evidence, not external reviewer feedback, and not production malware scanning evidence.
32. `docs/review/uploaded-raw-file-download-rate-limit-runtime-smoke.md`
    - guarded raw file download rate-limit runtime smoke with local Docker DB and live FastAPI HTTP; same-file no-scan attempts return `[409, 409, 409, 409, 409]` then `429`, while a separate clean file still downloads with `200`; not hosted deployment evidence, not external reviewer feedback, not distributed rate limiting, and not production authorization.
33. `docs/review/uploaded-raw-file-signature-validation-runtime-smoke.md`
    - raw file signature validation runtime smoke with local Docker DB and live FastAPI HTTP; spoofed CSV upload returns `201`, declared PDF mismatch returns `415`, blocked response has no raw bytes, and mismatch hash is not recently persisted; not hosted deployment evidence, not external reviewer feedback, not robust file-type detection, not malware scanning evidence, and not production authorization.
34. `docs/review/uploaded-raw-file-extension-allowlist-runtime-smoke.md`
    - raw file extension allowlist runtime smoke with local Docker DB and live FastAPI HTTP; allowed CSV upload returns `201`, `sample.exe.csv` double-extension upload returns `415`, responses include no raw bytes, and blocked content hash is not recently persisted; not hosted deployment evidence, not external reviewer feedback, not robust file-type detection, not malware scanning evidence, and not production authorization.
35. `docs/review/uploaded-raw-file-download-filename-safety-runtime-smoke.md`
    - raw file download filename safety runtime smoke with local Docker FastAPI; path-like and URL-encoded-control CSV filename input downloads with `local_v0_content_disposition_filename_safety_not_production`, a 120-character safe attachment filename, no path/dotdot/CRLF/injected-label content, and preserved `.csv`; not hosted deployment evidence, not external reviewer feedback, not malware detection proof, and not production authorization.
36. `docs/review/uploaded-raw-file-download-audit-runtime-smoke.md`
    - raw file download audit runtime smoke with local Docker FastAPI plus PostgreSQL; missing-scan `409`, rate-limited `[409, 409, 409, 409, 409, 429]`, and allowed `200` decisions persist to `raw_file_download_events`; not hosted deployment evidence, not external reviewer feedback, not malware detection proof, not production authorization, and not user identity.
37. `docs/review/uploaded-raw-file-download-approval-gate-behavior-runtime-smoke.md`
    - raw file download approval gate behavior runtime smoke with local Docker FastAPI plus PostgreSQL; latest-clean/no-approval returns `409` with `missing_download_approval`, non-active approval returns `409` with `revoked_or_expired_download_approval`, and active approval returns `200` with `download_approval_id` in audit metadata; not hosted deployment evidence, not external reviewer feedback, not production authorization, not user identity, and not signed URL support.
38. `docs/review/uploaded-raw-file-download-approval-input-guard-runtime-smoke.md`
    - raw file download approval input guard runtime smoke with local Docker FastAPI plus PostgreSQL; valid approval metadata creates/lists, unknown approval status returns `422`, and expired active approval returns `422`; not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated user identity, and not signed URL support.
39. `docs/review/uploaded-raw-file-download-approval-audit-metadata-runtime-smoke.md`
    - raw file download approval audit metadata runtime smoke with local Docker FastAPI plus PostgreSQL; active approval download returns `200`, allowed event metadata keeps approval id/status/expiry/latest-scan match and `operator_label_not_authenticated_identity`; not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated user identity, and not signed URL support.
40. `docs/review/uploaded-raw-file-download-readiness-runtime-smoke.md`
    - raw file download readiness runtime smoke with local Docker FastAPI plus PostgreSQL; readiness blocks before clean scan with `missing_clean_scan`, blocks after clean scan without active approval with `missing_download_approval`, allows after active approval, returns no raw bytes, consumes no rate limit, and writes no download audit event; not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated user identity, and not signed URL support.
41. `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md`
    - ClamAV endpoint malicious-detection owner-runtime smoke with local Docker FastAPI plus ClamAV; owner-provided stdin input yields `harness_status: verified_infected`, `scan_verdict: infected`, and `matched_signature: Eicar-Test-Signature`; payload is not committed or logged, local rows were cleaned up, and this is not hosted deployment evidence, not external reviewer feedback, and not production malware scanning evidence.
42. `docs/review/workflow-proof-bundle-read-model.md`
    - workflow proof bundle read model with `GET /workflow-runs/{id}/proof-bundle`, collecting existing workflow detail, derived lineage, and trace lookup surfaces; not new lineage storage, not distributed tracing, not hosted observability, and not external reviewer feedback.
43. `docs/review/workflow-proof-bundle-runtime-smoke.md`
    - workflow proof bundle runtime smoke with local Docker PostgreSQL plus live FastAPI HTTP; `GET /workflow-runs/{id}/proof-bundle` returns existing detail, lineage, and trace lookup surfaces for a deterministic workflow and keeps metadata-only workflows from claiming trace lookup; request refresh: `docs/review/external-reviewer-workflow-proof-bundle-request-refresh.md`; not distributed tracing, not hosted observability, not hosted deployment evidence, and not external reviewer feedback.
    - related direct stage links runtime smoke: `docs/review/workflow-direct-stage-links-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md`; records `direct_stage_link_count: 3` and link types `evidence_to_report`, `evidence_to_noise_gate`, and `noise_gate_to_report`; not distributed tracing, hosted observability, hosted deployment evidence, autonomous workflow execution, product-complete, or external reviewer feedback.
    - related stage event log runtime smoke: `docs/review/workflow-stage-event-log-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-stage-event-log-runtime-request-refresh.md`; records `detail_stage_event_count: 4`, `bundle_stage_event_count: 4`, stage names `retrieval,evidence_ledger,noise_gate,report`, and boundary `local_workflow_stage_event_log_not_distributed_tracing`; not distributed tracing, hosted observability, hosted deployment evidence, autonomous workflow execution, product-complete, or external reviewer feedback.
    - related failed stage event runtime smoke: `docs/review/workflow-failed-stage-event-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-failed-stage-event-runtime-request-refresh.md`; records `POST /workflow-runs/execute-preview -> 500`, `workflow_stage_event_count: 2`, `retrieval -> completed`, `evidence_ledger -> failed`, `failure_case_count_delta -> 0`, and `local_workflow_stage_failure_event_no_retry_no_auto_failure_case`; not retry behavior, automatic failure-case creation, hosted deployment evidence, distributed tracing, hosted observability, product-complete, or external reviewer feedback.
    - related workflow failure auto-created failure-case runtime smoke: `docs/review/workflow-failure-auto-failure-case-creation-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-failure-auto-creation-runtime-request-refresh.md`; records `POST /workflow-runs/execute-preview -> 500`, `failure_case_count_delta -> 1`, `auto_failure_case_id`, `auto_created_from_workflow_failure_local_v0`, and `local_workflow_stage_failure_event_auto_failure_case_local_v0`; not retry behavior, root-cause automation, complete workflow failure causality, hosted deployment evidence, product-complete, or external reviewer feedback.
    - related workflow failure auto-created failure-case dashboard runtime proof: `docs/review/workflow-failure-auto-created-failure-case-dashboard-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-failure-auto-created-dashboard-runtime-request-refresh.md`; records `GET /ops/dashboard -> 200`, `dashboard_contains_auto_created_failure_case_id -> true`, `dashboard_contains_workflow_parent_link -> true`, and `dashboard_contains_review_queue_linked_count -> true`; not retry behavior, root-cause automation, complete workflow failure causality, hosted deployment evidence, product-complete, or external reviewer feedback.
44. `docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md`
    - workflow proof bundle dashboard runtime smoke with local Docker PostgreSQL plus live FastAPI HTTP; `GET /ops/dashboard` includes the workflow `proof bundle` link and the linked `GET /workflow-runs/{id}/proof-bundle` route returns `200`; request refresh: `docs/review/external-reviewer-workflow-proof-bundle-dashboard-runtime-request-refresh.md`; not distributed tracing, hosted observability, hosted deployment evidence, live issue body edit, product-complete, or external reviewer feedback.
45. `docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md`
    - workflow failure-case persistence handoff runtime smoke with local Docker PostgreSQL plus live FastAPI HTTP; caller-triggered `POST /failure-cases/workflow-runs/{workflow_run_id}` persists one linked failure case, the review queue reports `failure_case_linked`, completed workflows return `409`, and duplicate handoffs return `409`; request refresh: `docs/review/external-reviewer-workflow-failure-case-persistence-runtime-request-refresh.md`; not background automation, hosted deployment evidence, complete workflow failure causality, product-complete, or external reviewer feedback.
46. `docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md`
    - workflow proof bundle failure-case links runtime smoke with local Docker PostgreSQL plus live FastAPI HTTP; linked failure cases appear through `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/proof-bundle`, while `GET /failure-cases?workflow_run_id={id}` filters out an unrelated failure case; request refresh: `docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md`; not automatic failure detection, background automation, hosted deployment evidence, complete workflow failure causality, product-complete, or external reviewer feedback.
47. `docs/review/workflow-dashboard-failure-case-counts-runtime-smoke.md`
    - workflow dashboard failure-case counts runtime smoke with local Docker PostgreSQL plus live FastAPI HTTP; `GET /ops/dashboard` shows the `Linked Failure Cases` workflow column, links a workflow with one linked failure case to `GET /failure-cases?workflow_run_id={id}`, and omits that filter link for an unlinked failed workflow; request refresh: `docs/review/external-reviewer-workflow-dashboard-failure-case-counts-runtime-request-refresh.md`; not automatic failure detection, background automation, hosted deployment evidence, complete workflow failure causality, product-complete, or external reviewer feedback.
48. `docs/review/ops-dashboard-anchor-get-runtime-smoke.md`
    - ops dashboard anchor GET runtime smoke with local Docker PostgreSQL plus live FastAPI HTTP; `GET /ops/dashboard` exposes clickable `data-method="GET"` anchors, `extracted_anchor_count: 38`, `unique_anchor_count: 25`, `all_extracted_dashboard_get_anchors_returned_200: true`, and `post_only_draft_preview_was_not_clickable: true`; request refresh: `docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md`; not browser automation evidence, hosted deployment evidence, product-complete, or external reviewer feedback.
49. `docs/review/ops-dashboard-anchor-browser-smoke.md`
    - ops dashboard anchor browser smoke with local Playwright browser automation; `GET /ops/dashboard` renders `browser_anchor_count: 27`, `browser_get_anchor_count: 27`, `browser_post_anchor_count: 0`, `post_only_draft_preview_anchor_count: 0`, `post_only_draft_preview_cue_visible: true`, and `all_browser_get_anchors_marked_get: true`; request refresh: `docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md`; not hosted deployment evidence, customer validation, product-complete, or external reviewer feedback.

## Optional source-level provenance

Use `docs/review/readme-proof-marker-archive.md` only when you need legacy README proof-marker continuity after README scanability cleanup.

This archive is source-level provenance, not product runtime evidence, not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

## Public Portfolio Surface

The live portfolio proof artifact is:

```text
https://svy04.github.io/proof-artifacts/noiseproof-agent-phase-ladder-2026-05-30/
```

Use `docs/review/portfolio-site-proof-artifact-route-verification.md` for the current route verification record.

Latest public proof route refresh:

```text
https://svy04.github.io/proof-artifacts/noiseproof-live-route-verification-2026-06-01/
```

Use `docs/review/external-reviewer-live-proof-route-refresh.md` for the latest reviewer-facing public route refresh.

This public route is a proof surface for the portfolio. It is not hosted deployment evidence for NoiseProof Agent.

## Demo Transcript

Use `docs/review/demo-transcript-capture.md` for the current self-authored route walkthrough.

It is useful for reader orientation, but it is not external reviewer feedback, not hosted deployment evidence, and not customer validation.

## Local Browser Screenshot

Use `docs/review/local-browser-screenshot-walkthrough.md` for the current visual walkthrough.

It records `GET /ops/dashboard` after a deterministic workflow preview and checks that the dashboard includes workflow runs and lineage links.

It is useful for local visual inspection, but it is not external reviewer feedback, not hosted deployment evidence, not customer validation, and not production observability.

## External Review Request

Use `docs/review/external-reviewer-brief.md` first if the reviewer only has a few minutes.

Use `docs/review/external-review-request.md` when asking a reviewer to inspect the proof path.

It points reviewers to `.github/ISSUE_TEMPLATE/external-review-feedback.md` and asks for critique on over-stated claims, missing evidence, and hiring signal.

Use `docs/review/external-reviewer-outreach-packet.md` when you need a copy-paste message for an FDE/product engineer, RAG/data engineer, or founder/operator reviewer.

Use `docs/review/external-reviewer-link-map.md` when a reviewer needs clickable links instead of repository-relative paths.

uploaded-file intake manifest proof:

```text
docs/review/uploaded-file-intake-manifest-preview.md
docs/review/uploaded-file-intake-manifest-runtime-smoke.md
docs/review/uploaded-file-intake-manifest-application-refresh.md
```

This proof is not raw file storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file intake manifest persistence proof:

```text
docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md
docs/review/uploaded-file-intake-manifest-persistence-application-refresh.md
```

This proof is manifest metadata only, not raw file storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file parsed document persistence proof:

```text
docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md
docs/review/uploaded-file-parsed-document-persistence-application-refresh.md
```

This proof is document metadata/profile only, not raw file storage, not parsed text persistence, not hosted deployment evidence, and not external reviewer feedback.

uploaded PDF downstream handoff proof:

```text
docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md
docs/review/uploaded-pdf-downstream-handoff-application-refresh.md
docs/review/external-reviewer-pdf-downstream-handoff-request-refresh.md
docs/review/external-review-issue-body-pdf-downstream-handoff-refresh.md
docs/review/external-feedback-current-state-pdf-downstream-handoff-issue-verification.md
```

This proof is uploaded digital PDF text only, not robust PDF extraction, not OCR, not table extraction, not layout fidelity, not raw file storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded PDF page diagnostics proof:

```text
docs/review/uploaded-pdf-page-diagnostics-runtime-smoke.md
docs/review/external-reviewer-pdf-page-diagnostics-runtime-request-refresh.md
page_text_char_counts -> [39]
```

This proof is preview-only uploaded digital PDF diagnostics with `empty_page_count -> 0`, `text_block_count -> 1`, `image_block_count -> 0`, and `document_count_delta -> 0`. It is not robust PDF extraction, not OCR, not table extraction, not layout fidelity, not raw file storage, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file chunk persistence proof:

```text
docs/review/uploaded-file-chunk-persistence-runtime-smoke.md
docs/review/uploaded-file-chunk-persistence-application-refresh.md
```

This proof is not automatic persistence from upload preview, not hosted deployment evidence, and not external reviewer feedback.

uploaded-file chunk handoff proof:

```text
docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md
```

This proof is explicit `POST /documents/upload-chunks`, not raw uploaded byte storage, not hosted deployment evidence, and not external reviewer feedback.

persisted document failure candidate draft preview runtime proof:

```text
docs/review/persisted-document-failure-candidate-draft-preview-runtime-smoke.md
docs/review/external-reviewer-persisted-document-failure-candidate-draft-runtime-request-refresh.md
```

This persisted document failure candidate draft preview runtime proof is explicit `POST /documents/upload-chunks` into `POST /documents/{document_id}/failure-case-draft-preview` with `preview_only_not_persisted`, `human_confirmation_required -> true`, `persisted_document_failure_case_candidate`, and `failure_case_count_delta -> 0`. The request refresh is request infrastructure only. It is not automatic failure-case creation, not hosted deployment evidence, not external reviewer feedback, not robust PDF extraction, not OCR, not table extraction, and not product-complete.

persisted document failure candidate manual handoff runtime proof:

```text
docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md
docs/review/external-reviewer-persisted-document-failure-candidate-manual-handoff-runtime-request-refresh.md
```

This persisted document failure candidate manual handoff runtime proof is explicit `POST /documents/upload-chunks` into `POST /documents/{document_id}/failure-case-draft-preview`, human changes `draft.fix_status` from `draft` to `open`, `POST /failure-cases -> 201`, and `GET /failure-cases -> 200` with `failure_case_count_delta -> 1`. The request refresh is request infrastructure only. It is not automatic failure-case creation, not a confirm endpoint, not hosted deployment evidence, not external reviewer feedback, not robust PDF extraction, not OCR, and not product-complete.

uploaded-file retrieval persistence proof:

```text
docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md
```

This proof is explicit `POST /documents/{document_id}/retrieval-runs` over persisted `document_chunks`, not Evidence Ledger generation, not hosted deployment evidence, and not external reviewer feedback.

uploaded PDF retrieval-run provenance proof:

```text
docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md
docs/review/external-reviewer-pdf-retrieval-run-provenance-request-refresh.md
```

This uploaded PDF retrieval-run provenance runtime proof is explicit `POST /documents/upload-chunks` into `POST /documents/{document_id}/retrieval-runs` with `candidate_parsers -> pdf-pymupdf` and `source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only`. The request refresh is request infrastructure only. It is not hosted deployment evidence, not external reviewer feedback, not robust PDF extraction, not OCR, not table extraction, not raw file storage, and not Evidence Ledger generation.

uploaded PDF retrieval-run-linked Evidence Ledger provenance proof:

```text
docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md
docs/review/external-reviewer-pdf-retrieval-run-linked-evidence-ledger-provenance-request-refresh.md
```

This uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime proof is explicit `POST /documents/upload-chunks` into `POST /documents/{document_id}/retrieval-runs`, `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, and `GET /evidence-ledgers?retrieval_run_id=` with `metadata_json.parser -> pdf-pymupdf`, `metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk`, and `ledger_retrieval_run_id_matches -> true`. The request refresh is request infrastructure only. It is not hosted deployment evidence, not external reviewer feedback, not robust PDF extraction, not OCR, not table extraction, not raw file storage, not Noise Gate behavior, and not report generation.

uploaded raw file storage proof:

```text
docs/review/uploaded-raw-file-storage-runtime-smoke.md
docs/review/uploaded-raw-file-storage-application-refresh.md
```

This proof is explicit `POST /documents/upload-raw-files` and `GET /documents/upload-raw-files` over quarantined PostgreSQL BYTEA storage, not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.

ClamAV adapter runtime smoke proof:

```text
docs/review/uploaded-raw-file-clamav-adapter-runtime-smoke.md
```

This proof exercises `ClamAvScannerAdapter` through deterministic fake-runner scenarios and reports `real_clamav_runtime_verified -> false`. It is not real ClamAV execution, not signature database evidence, not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.

uploaded raw file scan execution endpoint runtime proof:

```text
docs/review/uploaded-raw-file-scan-execution-endpoint-runtime-smoke.md
```

This proof shows local Docker DB plus live FastAPI HTTP evidence for `POST /documents/upload-raw-files/{raw_file_id}/scan`, `GET /documents/upload-raw-files/{raw_file_id}/scan-results`, default `scanner-unavailable`, and `scan_verdict -> scan_error`. It is not real ClamAV execution, not signature database evidence, not hosted deployment evidence, not external reviewer feedback, not malware scanning, and not a download endpoint.

raw file guard ops summary runtime smoke:

```text
docs/review/uploaded-raw-file-guard-ops-summary-runtime-smoke.md
docs/review/external-reviewer-raw-file-guard-ops-summary-request-refresh.md
```

This proof shows local Docker PostgreSQL plus live FastAPI HTTP evidence that raw upload, blocked missing-scan download, failed/clean scan metadata, active approval, allowed download, `/ops/summary` deltas, and `/ops/dashboard` labels work together. The request refresh is request infrastructure only. It is not live issue body edit, not hosted deployment evidence, not external reviewer feedback, not production authorization, not authenticated identity, and not signed URL support.

retrieval-run-linked Report proof:

```text
docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md
docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md
docs/review/retrieval-run-linked-report-runtime-smoke.md
```

This proof shows the persisted retrieval run handoff through `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, `POST /retrieval-runs/{retrieval_run_id}/noise-gate`, and `POST /retrieval-runs/{retrieval_run_id}/report`. The report smoke records `pre_report_status: 409` before a linked Noise Gate exists and `input_noise_gate_record_id` after the gate exists. It is not hosted deployment evidence, not external reviewer feedback, not LLM judgment, not embeddings, not semantic retrieval, not free-form final report generation, and not financial advice.

caller-provided chunk embedding endpoint proof:

```text
docs/review/embedding-endpoint-runtime-smoke.md
```

This proof shows local Docker DB plus live FastAPI HTTP evidence for `POST /chunks/{chunk_id}/embeddings`, `GET /chunks/{chunk_id}/embeddings`, and generated embedding claim rejection `400`. It is caller-provided vector persistence only. It is not embedding generation, not semantic retrieval implementation, not HNSW or IVFFlat index behavior, not vector search quality, not hosted deployment evidence, and not external reviewer feedback.

caller-provided semantic retrieval persistence proof:

```text
docs/review/semantic-retrieval-persistence-runtime-smoke.md
docs/review/semantic-retrieval-persistence-application-refresh.md
```

This proof shows local Docker DB plus live FastAPI HTTP evidence for `POST /documents/{document_id}/semantic-retrieval-runs -> 201`, `GET /retrieval-runs -> 200`, dimension mismatch `-> 400`, and unchanged Evidence Ledger counts. It is caller-provided semantic retrieval persistence only. It is not embedding generation, not vector search quality evidence, not Evidence Ledger generation from semantic retrieval, not hosted deployment evidence, and not external reviewer feedback.

toy semantic retrieval quality report:

```text
docs/evaluation/semantic-retrieval-quality-report.md
docs/review/semantic-retrieval-quality-report-application-refresh.md
```

This report shows toy fixture metric output for Hit@k, Recall@k, MRR@k, nDCG@k, missing embedding rate, semantic/lexical disagreement, and role coverage. It keeps `q-what-missing` visible. It is not vector search quality evidence, not a benchmark result, not a model comparison, not Evidence Ledger generation, not hosted deployment evidence, and not external reviewer feedback.

Public request issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

It is not external reviewer feedback.

## What This Path Proves

Allowed claim:

NoiseProof Agent is an inspectable local portfolio service with phased proof artifacts for data profiling, parser boundaries, chunking, lexical retrieval, caller-provided semantic retrieval persistence, toy semantic retrieval quality report output, evidence preview, gate preview, report preview, persisted proof records, workflow parent linkage, failure-case persistence, manual workflow parent provenance, and current application-facing boundaries.

Allowed claim:

Manual failure-case workflow parent linkage exists. A manually persisted `failure_cases` row can retain nullable `workflow_run_id` provenance to a `workflow_runs` parent, and that path has schema/API support, route-level smoke evidence, fresh DB evidence, dashboard surfacing, and a proof index.

## What This Path Does Not Prove

Forbidden claim:

NoiseProof Agent is production-ready, hosted, customer-validated, or a complete RAG/agent platform.

Forbidden claim:

NoiseProof Agent automatically creates failure cases from workflow failures or proves complete workflow failure causality.

Forbidden claim:

NoiseProof Agent has robust PDF extraction, embedding generation, semantic retrieval quality evidence, distributed tracing, market prediction quality, or free-form final answer generation.

## Boundary

This proof path adds no hosted deployment evidence, automatic failure detection, automatic failure-case creation beyond the local v0 workflow failure path, complete workflow failure causality, LLM calls, embeddings, semantic retrieval quality evidence, autonomous workflow execution, or free-form final answer generation.

This is not hosted deployment evidence.
This is not automatic failure-case creation beyond the local v0 workflow failure path.
This is not complete workflow failure causality.

## Next Gate

```text
external reviewer feedback v0
```

## Historical Table-candidate Downstream Proof Routing

uploaded PDF table-candidate downstream runtime proof:

```text
docs/review/uploaded-pdf-table-candidate-downstream-provenance-runtime-smoke.md
docs/review/uploaded-pdf-table-candidate-downstream-provenance-remote-verification.md
docs/review/external-reviewer-pdf-table-candidate-downstream-runtime-request-refresh.md
retrieval_candidate_table_candidate_count -> 1
```

Boundary: request routing only; not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction, not table extraction, and not product-complete.
