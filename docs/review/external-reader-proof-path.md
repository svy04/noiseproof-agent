# External-reader Proof Path

Status: compact proof index.

Phase marker: external-reader proof path index v0.

This page is the shortest repository-native path for an external reviewer who wants to inspect what NoiseProof Agent currently proves without reading the entire phase history.

## 5-minute path

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
24. `docs/review/embedding-endpoint-runtime-smoke.md`
    - caller-provided chunk embedding endpoint proof with explicit `POST /chunks/{chunk_id}/embeddings`, `GET /chunks/{chunk_id}/embeddings`, and generated-claim rejection `400`.
25. `docs/review/semantic-retrieval-persistence-runtime-smoke.md`
    - caller-provided semantic retrieval persistence proof with explicit `POST /documents/{document_id}/semantic-retrieval-runs`, `GET /retrieval-runs`, dimension mismatch `400`, and unchanged Evidence Ledger counts.
26. `docs/evaluation/semantic-retrieval-quality-report.md`
    - toy semantic retrieval quality report with visible misses and disagreement; not vector search quality evidence.
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

This proof path adds no new runtime behavior, schema, migration, API endpoint, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure detection, automatic failure-case creation, automatic persistence from workflow failures, complete workflow failure causality, LLM calls, embeddings, semantic retrieval quality evidence, autonomous workflow execution, or free-form final answer generation.

This is not hosted deployment evidence.
This is not automatic failure-case creation.
This is not complete workflow failure causality.

## Next Gate

```text
external reviewer feedback v0
```
