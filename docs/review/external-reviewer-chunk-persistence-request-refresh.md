# External Reviewer Chunk Persistence Request Refresh

Phase marker: external reviewer chunk persistence request refresh v0.

## Purpose

This gate updates the external reviewer request path so a reviewer can inspect the uploaded-file chunk persistence proof without reading the full phase history.

It is request infrastructure only.

It does not add runtime behavior.

It does not edit the live public issue body.

## Uploaded-file chunk persistence proof

Reviewer-facing surfaces now point to:

- `docs/review/uploaded-file-chunk-persistence-runtime-smoke.md`
- `docs/review/uploaded-file-chunk-persistence-application-refresh.md`

The proof is narrow:

```text
The service can manually persist and list derived chunk text for an explicit document id through POST /documents/{document_id}/chunks and GET /documents/{document_id}/chunks. It keeps persistence_boundary = chunk_text_only_no_raw_file_storage, while upload chunk preview remains preview_only_not_persisted.
```

## Updated request surfaces

- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/external-review-feedback.md`
- `docs/review/external-review-request.md`
- `docs/review/external-reader-proof-path.md`
- `docs/review/external-reviewer-brief.md`
- `docs/review/external-reviewer-link-map.md`
- `docs/application/portfolio-index.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/review/readme-proof-marker-archive.md`

## Boundaries

This is not external reviewer feedback.

This is not automatic persistence from upload preview.

This is not hosted deployment evidence.

It is not customer validation, Braincrew acceptance, production readiness, raw file storage, full parsed text persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, LLM output, embeddings, semantic retrieval, or automatic failure-case creation.

## Next gate

The next bounded request gate should update or verify the live public issue body so issue #1 points reviewers to the uploaded-file chunk persistence proof:

```text
external reviewer chunk persistence issue-body refresh v0
```
