# External Review Issue Body Parsed-document Persistence Refresh

Phase marker: external reviewer parsed-document persistence issue-body refresh v0.

## Purpose

This gate updates the live public issue #1 body so external reviewers can reach the uploaded-file parsed document persistence proof directly from the feedback request.

Issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Observed issue body markers

The issue body now starts with codepoint `35` (`#`) and includes:

```text
uploaded-file parsed document persistence proof
https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md
Boundary: document metadata/profile only via POST /documents/upload-parsed-documents and GET /documents, persistence_boundary = document_metadata_and_profile_only_no_raw_file_storage, not raw file storage, not hosted deployment evidence, and not external reviewer feedback.
```

It also includes the uploaded-file parsed document persistence proof as item 8 in the suggested 5-minute path.

## Artifact Links

- `docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md`
- `docs/review/uploaded-file-parsed-document-persistence-application-refresh.md`
- `docs/review/external-reviewer-parsed-document-persistence-request-refresh.md`

## Boundary

This is an owner-authored issue edit.

It is not external reviewer feedback.

It is not raw file storage.

It is not hosted deployment evidence.

It is not customer validation, Braincrew acceptance, production readiness, robust PDF extraction, parsed text persistence, chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, LLM output, embeddings, semantic retrieval, or automatic failure-case creation.

## Next gate

The next evidence gate remains:

```text
external reviewer feedback v0
```
