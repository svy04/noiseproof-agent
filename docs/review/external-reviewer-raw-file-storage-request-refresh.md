# External Reviewer Raw File Storage Request Refresh

Phase marker: external reviewer raw file storage request refresh v0.

## Purpose

This gate updates the external reviewer request path so a reviewer can inspect the uploaded raw file storage proof without reading the full phase history.

It is request infrastructure only.

It does not add runtime behavior.

It does not edit the live public issue body.

## Uploaded raw file storage proof

Reviewer-facing surfaces now point to:

- `docs/review/uploaded-raw-file-storage-runtime-smoke.md`
- `docs/review/uploaded-raw-file-storage-application-refresh.md`

The proof is narrow:

```text
The service can store original uploaded bytes in a quarantined PostgreSQL BYTEA table through POST /documents/upload-raw-files, list metadata through GET /documents/upload-raw-files, reject oversized uploads, and keep response bodies metadata-only with boundary = raw_upload_quarantine_db_bytea_no_download_endpoint.
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

This is not a download endpoint.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parser quality evidence, semantic retrieval quality evidence, Evidence Ledger generation, Critic / Noise Gate behavior, final report generation, LLM output, embeddings, semantic retrieval, automatic failure-case creation, or product-complete.

## Next gate

The next bounded request gate can update or verify the live public issue body so issue #1 points reviewers to the uploaded raw file storage proof:

```text
external review issue body raw file storage refresh v0
```
