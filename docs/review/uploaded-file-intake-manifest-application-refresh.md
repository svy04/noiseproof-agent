# Uploaded File Intake Manifest Application Refresh

Phase marker: uploaded file intake manifest application refresh v0.

## Purpose

This gate surfaces the upload intake manifest endpoint and its local runtime smoke in application-facing documents.

It is application-facing documents only.

It does not add runtime behavior.

## What changed

The application package now points reviewers to:

- `POST /documents/upload-intake-manifest-preview`
- `docs/review/uploaded-file-intake-manifest-preview.md`
- `docs/review/uploaded-file-intake-manifest-runtime-smoke.md`

The updated application claim is narrow:

```text
NoiseProof can expose a preview-only uploaded-file intake manifest with content hash, parser/profile summary, and explicit storage boundary before opening raw file persistence.
```

## Application-facing surfaces

Updated surfaces:

- `docs/application/portfolio-index.md`
- `docs/application/braincrew-role-map.md`
- `docs/review/application-ready-review.md`
- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`

## Boundaries

This is not hosted deployment evidence.

It is not raw file storage.

It is not retrieval persistence.

It is not external reviewer feedback, customer validation, Braincrew acceptance, production readiness, document row creation, chunk persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, LLM output, embeddings, semantic retrieval, or automatic failure-case creation.

## Next gate

The next bounded gate should update the external review request path so a future reviewer sees the uploaded-file intake manifest proof without mistaking it for storage:

```text
external reviewer upload-manifest request refresh v0
```
