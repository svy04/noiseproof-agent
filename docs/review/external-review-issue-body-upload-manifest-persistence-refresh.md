# External Review Issue Body Upload-manifest Persistence Refresh

Phase marker: external reviewer upload-manifest persistence issue-body refresh v0.

## Purpose

This gate updates the live public issue #1 body so external reviewers can reach the uploaded-file intake manifest persistence proof directly from the feedback request.

Issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Observed issue body markers

The issue body now starts with codepoint `35` (`#`) and includes:

```text
uploaded-file intake manifest persistence proof
https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md
Boundary: manifest metadata only via POST /documents/upload-intake-manifests and GET /documents/upload-intake-manifests, persistence_boundary = manifest_only_no_raw_file_storage, not raw file storage, not hosted deployment evidence, and not external reviewer feedback.
```

It also includes the uploaded-file intake manifest persistence proof as item 7 in the suggested 5-minute path.

## Artifact Links

- `docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md`
- `docs/review/uploaded-file-intake-manifest-persistence-application-refresh.md`
- `docs/review/external-reviewer-upload-manifest-persistence-request-refresh.md`

## Boundary

This is an owner-authored issue edit.

It is not external reviewer feedback.

It is not raw file storage.

It is not hosted deployment evidence.

It is not customer validation, Braincrew acceptance, production readiness, document row creation, chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, LLM output, embeddings, semantic retrieval, or automatic failure-case creation.

## Next gate

The next evidence gate remains:

```text
external reviewer feedback v0
```
