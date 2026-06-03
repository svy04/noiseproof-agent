# External Reviewer Scan-result Endpoint Request Refresh

Status: request infrastructure only.

Phase marker: external reviewer scan-result endpoint request refresh v0.

## Purpose

This gate updates the external reviewer request path so a reviewer can inspect the uploaded raw file scan result endpoint proof without reading the full phase history.

It is request infrastructure only.

It does not add runtime behavior.

It does not edit the live public issue body.

## Uploaded raw file scan result endpoint proof

Reviewer-facing surfaces now point to:

- `docs/review/uploaded-raw-file-scan-result-endpoint-runtime-smoke.md`

The proof is narrow:

```text
The service can store a quarantined raw uploaded file, persist caller-provided scan result metadata through POST /documents/upload-raw-files/{raw_file_id}/scan-results, list scan result metadata through GET /documents/upload-raw-files/{raw_file_id}/scan-results, preserve scan_verdict -> scan_error, reject path/body mismatch -> 400, and keep response_has_raw_bytes -> false.
```

## Updated request surfaces

- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/external-review-feedback.md`
- `docs/review/external-review-request.md`
- `docs/review/external-reader-proof-path.md`
- `docs/review/external-reviewer-brief.md`
- `docs/review/external-reviewer-link-map.md`
- `docs/application/portfolio-index.md`
- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`

## Boundaries

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not malware scanning.

This is not scanner execution.

This is not ClamAV integration.

This is not a download endpoint.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next gate

The next bounded request gate can update or verify the live public issue body so issue #1 points reviewers to the scan result endpoint proof:

```text
external review issue body scan-result endpoint refresh v0
```
