# External Reviewer Retrieval Persistence Request Refresh

Phase marker: external reviewer retrieval persistence request refresh v0.

## Purpose

This gate updates the external reviewer request path so a reviewer can inspect the uploaded-file retrieval persistence proof without reading the full phase history.

It is request infrastructure only.

It does not add runtime behavior.

It does not edit the live public issue body.

## Uploaded-file retrieval persistence proof

Reviewer-facing surfaces now point to:

- `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`

The proof is narrow:

```text
The service can read persisted document_chunks through POST /documents/{document_id}/retrieval-runs, create one retrieval_runs row, and preserve selected chunk ids in metadata_json.candidate_chunk_ids with metadata_source_table = document_chunks.
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

It is not customer validation, Braincrew acceptance, production readiness, Evidence Ledger generation, Noise Gate generation, report generation, raw uploaded byte storage, full parsed text persistence, LLM output, embeddings, semantic retrieval, financial advice, or automatic failure-case creation.

Explicit non-claims:

```text
no Evidence Ledger generation
no semantic retrieval
not financial advice
```

## Next gate

The next bounded request gate should update or verify the live public issue body so issue #1 points reviewers to the uploaded-file retrieval persistence proof:

```text
external reviewer retrieval persistence issue-body refresh v0
```
