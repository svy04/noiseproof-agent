# External Reviewer Parsed-document Persistence Request Refresh

Phase marker: external reviewer parsed-document persistence request refresh v0.

## Purpose

This gate updates the external reviewer request path so a reviewer can inspect the uploaded-file parsed document persistence proof without reading the full phase history.

It is request infrastructure only.

It does not add runtime behavior.

It does not edit the live public issue body.

## Uploaded-file parsed document persistence proof

Reviewer-facing surfaces now point to:

- `docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md`
- `docs/review/uploaded-file-parsed-document-persistence-application-refresh.md`

The proof is narrow:

```text
The service can persist uploaded-file document metadata and parser/profile output through POST /documents/upload-parsed-documents, then read that row through GET /documents. It keeps status = parsed_metadata_only and persistence_boundary = document_metadata_and_profile_only_no_raw_file_storage.
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

This is not raw file storage.

This is not hosted deployment evidence.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parsed text persistence, chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, LLM output, embeddings, semantic retrieval, or automatic failure-case creation.

## Next gate

The next bounded request gate should update or verify the live public issue body so issue #1 points reviewers to the uploaded-file parsed document persistence proof:

```text
external reviewer parsed-document persistence issue-body refresh v0
```
