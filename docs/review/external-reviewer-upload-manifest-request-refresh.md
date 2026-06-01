# External Reviewer Upload-manifest Request Refresh

Phase marker: external reviewer upload-manifest request refresh v0.

## Purpose

This gate updates the external reviewer request path so a reviewer can inspect the uploaded-file intake manifest proof without reading the full phase history.

It is request infrastructure only.

It does not add runtime behavior.

## Uploaded-file intake manifest proof

Reviewer-facing surfaces now point to:

- `docs/review/uploaded-file-intake-manifest-preview.md`
- `docs/review/uploaded-file-intake-manifest-runtime-smoke.md`
- `docs/review/uploaded-file-intake-manifest-application-refresh.md`

The proof is narrow:

```text
The service can return a preview-only upload intake manifest with content_sha256, parser/profile summary, storage_decision = do_not_persist_raw_upload_yet, replayable = false, and persistence_boundary = preview_only_not_persisted.
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

It is not customer validation, Braincrew acceptance, production readiness, document row creation, chunk persistence, retrieval persistence, Evidence Ledger persistence, Noise Gate persistence, report persistence, workflow persistence, LLM output, embeddings, semantic retrieval, or automatic failure-case creation.

## Next gate

The next bounded gate should update or verify the live public issue body so issue #1 points reviewers to the uploaded-file intake manifest proof:

```text
external reviewer upload-manifest issue-body refresh v0
```
