# Semantic Retrieval Quality Report

Phase marker: semantic retrieval quality report v0.

This report records toy fixture metric output for semantic retrieval evaluation plumbing.

It is not vector search quality evidence.

## Fixture

- fixture: `semantic-retrieval-quality-fixture-v0`
- queries: 4
- corpus chunks: 6
- qrels: 8
- claim boundary: `toy_fixture_metric_only_not_search_quality`

## Aggregate Metrics

| Metric | Value |
|---|---:|
| Hit@k | 0.75 |
| Recall@k | 0.375 |
| MRR@k | 0.375 |
| nDCG@k | 0.198 |
| missing_embedding_rate | 0.1667 |
| semantic_vs_lexical_disagreement | 0.9167 |
| role_coverage_at_k | 0.625 |

## Per-query Metrics

| Query | Hit@k | Recall@k | MRR@k | nDCG@k | role_coverage_at_k |
|---|---:|---:|---:|---:|---:|
| q-demand-growth | 1 | 0.5 | 0.5 | 0.4966 | 1 |
| q-risk-contradiction | 1 | 0.5 | 0.5 | 0.0827 | 0.5 |
| q-source-quality | 1 | 0.5 | 0.5 | 0.2128 | 1 |
| q-what-missing | 0 | 0 | 0 | 0 | 0 |

## Diagnostic Matrix

This matrix explains fixture misses; it does not prove semantic retrieval quality.

| Query | Semantic top-k | Missed relevant | Missing roles | Lexical rescue | Warnings |
|---|---|---|---|---|---|
| q-demand-growth | chunk-scope-boundary, chunk-demand-growth | chunk-revenue-growth | none | chunk-revenue-growth | lexical_retrieved_relevant_not_in_semantic_top_k |
| q-risk-contradiction | chunk-demand-growth, chunk-source-quality | chunk-contradictory-channel | contradiction | chunk-contradictory-channel | missing_required_information_roles_at_k, lexical_retrieved_relevant_not_in_semantic_top_k |
| q-source-quality | chunk-demand-growth, chunk-missing-source | chunk-source-quality | none | chunk-source-quality | relevant_chunk_missing_embedding, lexical_retrieved_relevant_not_in_semantic_top_k |
| q-what-missing | none | chunk-missing-source, chunk-scope-boundary | missing_data_signal, scope_boundary, user_intent_check | chunk-missing-source | no_semantic_candidates_at_k, no_relevant_semantic_candidate_at_k, missing_required_information_roles_at_k, relevant_chunk_missing_embedding, lexical_retrieved_relevant_not_in_semantic_top_k |

## Interpretation

This report intentionally uses a weak semantic ranking fixture so misses and disagreements remain visible.

`q-what-missing` retrieves no relevant semantic candidate in this fixture. That is useful because it proves the evaluator can surface a missing-data failure instead of turning every semantic retrieval run into a success story.

`semantic_vs_lexical_disagreement = 0.9167` means the toy semantic ranking and toy lexical ranking diverge strongly in this fixture. This is a warning signal, not a quality claim.

## Boundary

This is not embedding generation.

This is not vector search quality evidence.

This is not a benchmark result.

This is not a model comparison.

This is not Evidence Ledger generation.

This is not hosted deployment evidence.
