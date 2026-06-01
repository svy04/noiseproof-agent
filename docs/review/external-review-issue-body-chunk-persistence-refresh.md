# External Review Issue Body Chunk Persistence Refresh

Phase marker: external reviewer chunk persistence issue-body refresh v0.

## Purpose

This gate updates the live public issue #1 body so external reviewers can reach the uploaded-file chunk persistence proof directly from the feedback request.

Issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Observed issue body markers

The issue body now starts with codepoint `35` (`#`) and includes:

```text
uploaded-file chunk persistence proof
https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-chunk-persistence-runtime-smoke.md
Boundary: manual chunk text persistence via POST /documents/{document_id}/chunks and GET /documents/{document_id}/chunks, persistence_boundary = chunk_text_only_no_raw_file_storage, preview remains preview_only_not_persisted, not automatic persistence from upload preview, not hosted deployment evidence, and not external reviewer feedback.
```

It also includes the uploaded-file chunk persistence proof as item 9 in the suggested 5-minute path.

## Artifact Links

- `docs/review/uploaded-file-chunk-persistence-runtime-smoke.md`
- `docs/review/uploaded-file-chunk-persistence-application-refresh.md`
- `docs/review/external-reviewer-chunk-persistence-request-refresh.md`

## Boundary

This is an owner-authored issue edit.

It is not external reviewer feedback.

It is not automatic persistence from upload preview.

It is not hosted deployment evidence.

It is not customer validation, Braincrew acceptance, production readiness, raw file storage, full parsed text persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, LLM output, embeddings, semantic retrieval, or automatic failure-case creation.

## Next gate

The next evidence gate remains:

```text
external reviewer feedback v0
```
