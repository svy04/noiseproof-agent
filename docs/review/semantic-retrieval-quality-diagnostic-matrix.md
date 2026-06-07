# Semantic Retrieval Quality Diagnostic Matrix

Phase marker: semantic retrieval quality diagnostic matrix v0.

Status: implemented.

## Purpose

Make the toy semantic retrieval quality report easier to inspect before anyone reads the aggregate metrics as a quality claim.

The implementation adds per-query diagnostics to `packages/ingestion/retrieval/quality_metrics.py` and renders them in `docs/evaluation/semantic-retrieval-quality-report.md`.

## What Changed

The evaluator now records, per query:

- semantic top-k candidate ids
- lexical top-k candidate ids
- retrieved relevant chunk ids
- missed relevant chunk ids
- covered information roles
- missing information roles
- relevant chunks that have no embedding
- lexical rescue chunk ids
- structured warnings

The report now includes a `Diagnostic Matrix` section.

## Observed Fixture Warnings

`q-what-missing` remains intentionally weak:

```text
semantic_top_k: []
missed_relevant_chunk_ids: chunk-missing-source, chunk-scope-boundary
missing_information_roles: missing_data_signal, scope_boundary, user_intent_check
relevant_missing_embedding_chunk_ids: chunk-missing-source
lexical_rescue_chunk_ids: chunk-missing-source
warnings:
  - no_semantic_candidates_at_k
  - no_relevant_semantic_candidate_at_k
  - missing_required_information_roles_at_k
  - relevant_chunk_missing_embedding
  - lexical_retrieved_relevant_not_in_semantic_top_k
```

This is a failure-exposure improvement, not a retrieval-quality improvement.

## Verification

Focused tests:

```text
uv run pytest tests/test_semantic_quality_evaluator.py -q
uv run pytest tests/test_semantic_quality_report.py -q
uv run pytest tests/test_docs.py -q -k semantic_retrieval_quality_diagnostic_matrix
```

Report regeneration command:

```text
uv run python -m app.services.semantic_quality_report_command --fixture ../../examples/semantic-retrieval-quality --rankings ../../examples/semantic-retrieval-quality/rankings.json --output ../../docs/evaluation/semantic-retrieval-quality-report.md --k 2
```

## Boundary

This is not embedding generation.

This is not vector search quality evidence.

This is not a benchmark result.

This is not a model comparison.

This is not a retrieval tuning change.

This is not Evidence Ledger generation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
