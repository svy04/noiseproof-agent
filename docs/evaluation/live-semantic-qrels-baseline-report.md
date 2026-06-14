# Live Semantic Qrels Baseline Eval

Phase marker: live semantic qrels baseline v0.

This report evaluates caller-provided fixture vectors through the same exact cosine boundary used by the semantic retrieval preview/run path.

This is not semantic retrieval quality evidence.

## Run Source

- run_source: `caller_provided_live_semantic_cosine`
- retrieval_strategy: `semantic-cosine`
- ranking_boundary: `exact_cosine_caller_provided_query_vector`
- qrels_boundary: `qrels_backed_toy_eval_not_semantic_quality_evidence`
- boundary: `caller_provided_live_semantic_qrels_baseline_not_quality_evidence`

## Aggregate Metrics

| Metric | Value |
|---|---:|
| Hit@k | 1 |
| Recall@k | 0.75 |
| MRR@k | 1 |
| nDCG@k | 0.7296 |
| judged_coverage_at_k | 0.75 |
| retrieved_count_at_k | 8 |
| unjudged_retrieved_count_at_k | 2 |
| judged_relevant_count | 8 |

## Live Run

| Query | Retrieved by caller-provided cosine | Missed relevant | Unjudged retrieved | Warnings |
|---|---|---|---|---|
| q-demand-growth | chunk-demand-growth, chunk-revenue-growth | none | none | none |
| q-risk-contradiction | chunk-contradictory-channel, chunk-source-quality | none | none | none |
| q-source-quality | chunk-source-quality, chunk-contradictory-channel | chunk-missing-source | chunk-contradictory-channel | missed_relevant_documents_at_k, unjudged_retrieved_documents |
| q-what-missing | chunk-scope-boundary, chunk-source-quality | chunk-missing-source | chunk-source-quality | missed_relevant_documents_at_k, unjudged_retrieved_documents |

## Missing Embeddings

- missing_embedding_chunk_ids: `chunk-missing-source`

## Quality Claim Gate

This gate blocks this caller-provided vector baseline from being cited as semantic retrieval quality evidence.

- status: `blocked`
- can_claim_semantic_quality: `false`
- summary: `live_semantic_qrels_baseline_quality_claim_blocked`
- blocker_codes: `toy_qrels_fixture_boundary, unjudged_retrieved_documents, incomplete_judged_coverage, missed_relevant_documents, caller_provided_embedding_boundary, no_live_embedding_generation, tiny_fixture_boundary, missing_chunk_embeddings`

## Boundary

This is a live semantic baseline over a tiny local fixture with caller-provided vectors.

This is not semantic retrieval quality evidence.

This is not live embedding generation.

This is not representative retrieval evaluation.

This is not a benchmark result.

This is not hosted deployment evidence.
