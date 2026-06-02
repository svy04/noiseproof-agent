# External Review Issue Body Retrieval Persistence Refresh

Phase marker: external reviewer retrieval persistence issue-body refresh v0.

## Purpose

This gate updates the live public issue #1 body so external reviewers can reach the uploaded-file retrieval persistence proof directly from the feedback request.

Issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Observed issue body markers

Observed after owner-authored issue edit:

```text
updatedAt: 2026-06-02T04:14:29Z
first_codepoint: 35
startsWith: ## Request
comment_count: 1
owner_comment_count: 1
```

The issue body now includes:

```text
uploaded-file retrieval persistence proof
https://github.com/svy04/noiseproof-agent/blob/main/docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md
Boundary: explicit POST /documents/{document_id}/retrieval-runs, metadata_json.candidate_chunk_ids, metadata_source_table = document_chunks, no Evidence Ledger generation, not hosted deployment evidence, and not external reviewer feedback.
```

It also includes the uploaded-file retrieval persistence proof in the suggested 5-minute path.

## Artifact Links

- `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`
- `docs/review/external-reviewer-retrieval-persistence-request-refresh.md`

## Boundary

This is an owner-authored issue edit.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not customer validation, Braincrew acceptance, production readiness, Evidence Ledger generation, Noise Gate generation, report generation, raw uploaded byte storage, full parsed text persistence, LLM output, embeddings, semantic retrieval, financial advice, or automatic failure-case creation.

## Next gate

The next evidence gate remains:

```text
external reviewer feedback v0
```
