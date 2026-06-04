# External Reviewer Link Map

Status: reviewer-facing link hygiene artifact.

Phase marker: external reviewer link map v0.

Label: External reviewer link map.

This artifact gives outside reviewers direct links to the shortest inspectable path. It reduces navigation friction before a reviewer leaves feedback, but it does not claim that any feedback has been received.

## Public Feedback Surface

Leave feedback here:

https://github.com/svy04/noiseproof-agent/issues/1

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
11. uploaded PDF retrieval-run provenance runtime proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md
   Boundary: `candidate_parsers -> pdf-pymupdf`, `source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only`, not hosted deployment evidence, not robust PDF extraction, not Evidence Ledger generation, and not external reviewer feedback.
12. uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md
   Boundary: `metadata_json.parser -> pdf-pymupdf`, `metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk`, not hosted deployment evidence, not robust PDF extraction, not Noise Gate behavior, not report generation, and not external reviewer feedback.
13. uploaded-file chunk persistence proof:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-chunk-persistence-runtime-smoke.md
   Boundary: not automatic persistence from upload preview, not hosted deployment evidence, and not external reviewer feedback.
14. uploaded-file chunk handoff proof:
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
26. architecture current-state refresh:
   https://github.com/svy04/noiseproof-agent/blob/main/docs/review/architecture-current-state-refresh.md
   Boundary: separates implemented upload/chunk/retrieval/evidence handoff surfaces from still-unproven robust PDF extraction, embedding generation, hosted deployment evidence, external reviewer feedback, endpoint malicious-detection runtime proof, and production semantic retrieval quality.
27. Feedback intake criteria:
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
