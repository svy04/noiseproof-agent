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

architecture current-state refresh:

```text
docs/review/architecture-current-state-refresh.md
```

Boundary: this proof-surface correction separates implemented uploaded-file persistence, chunk/retrieval persistence, caller-provided embeddings, semantic retrieval persistence, and retrieval-run-linked Evidence Ledger / Noise Gate / Report handoffs from still-unproven robust PDF extraction, embedding generation, hosted deployment evidence, external reviewer feedback, endpoint malicious-detection runtime proof, and production semantic retrieval quality.

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
19. `docs/review/architecture-current-state-refresh.md`
20. `docs/application/braincrew-role-map.md`

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
