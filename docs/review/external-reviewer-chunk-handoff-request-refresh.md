# External Reviewer Chunk Handoff Request Refresh

Phase marker: external reviewer chunk handoff request refresh v0.

## Purpose

This gate updates the external reviewer request path so a reviewer can inspect the uploaded-file chunk handoff proof without reading the full phase history.

It is request infrastructure only.

It does not add runtime behavior.

It does not edit the live public issue body.

## Uploaded-file chunk handoff proof

Reviewer-facing surfaces now point to:

- `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md`

The proof is narrow:

```text
The service can create document metadata plus derived chunk rows from uploaded content through POST /documents/upload-chunks. It keeps handoff_boundary = explicit_upload_to_chunks_no_raw_file_storage and chunk persistence_boundary = chunk_text_only_no_raw_file_storage.
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

This is not hosted deployment evidence.

It is not customer validation, Braincrew acceptance, production readiness, raw uploaded byte storage, full parsed text persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, LLM output, embeddings, semantic retrieval, or automatic failure-case creation.

## Next gate

The next bounded request gate should update or verify the live public issue body so issue #1 points reviewers to the uploaded-file chunk handoff proof:

```text
external reviewer chunk handoff issue-body refresh v0
```
