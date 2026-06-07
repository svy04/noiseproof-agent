# External-reader Proof Path Semantic Retrieval Quality Diagnostic Matrix Route Refresh

Phase marker: external-reader proof path semantic retrieval quality diagnostic matrix route refresh v0.

Status: implemented.

## Purpose

Route first-pass reviewers to the semantic retrieval diagnostic matrix proof chain so they can inspect retrieval misses before reading aggregate toy metrics.

This is reviewer navigation only. It does not create new retrieval behavior.

## Updated Surfaces

- `docs/review/external-reader-proof-path.md`
- `docs/review/external-reviewer-link-map.md`
- `docs/review/external-reviewer-shortlist.md`
- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`

## Routed Proof Chain

```text
docs/review/semantic-retrieval-quality-diagnostic-matrix.md
docs/review/semantic-retrieval-quality-diagnostic-matrix-remote-verification.md
docs/evaluation/semantic-retrieval-quality-report.md
```

Route markers:

```text
q-what-missing
no_semantic_candidates_at_k
no_relevant_semantic_candidate_at_k
missing_required_information_roles_at_k
relevant_chunk_missing_embedding
lexical_retrieved_relevant_not_in_semantic_top_k
CI run `27079764317`
External Feedback Screen run `27079764318`
```

## Boundary

This is route hygiene only.

It is not new runtime evidence.

It is not vector search quality evidence.

It is not embedding generation.

It is not a benchmark result.

It is not a model comparison.

It is not retrieval tuning.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.
