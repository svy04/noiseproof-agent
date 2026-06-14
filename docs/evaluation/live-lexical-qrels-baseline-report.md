# Live Lexical Qrels Baseline Eval

Phase marker: live lexical qrels baseline v0.

This report evaluates the existing local lexical retriever output against the tiny qrels fixture.

This is not semantic retrieval quality evidence.

## Run Source

- run_source: `live_lexical_retrieve_candidates`
- retrieval_strategy: `fixed-window`
- qrels_boundary: `qrels_backed_toy_eval_not_semantic_quality_evidence`
- boundary: `live_lexical_qrels_baseline_not_semantic_quality_evidence`

## Aggregate Metrics

| Metric | Value |
|---|---:|
| Hit@k | 1 |
| Recall@k | 0.5 |
| MRR@k | 0.75 |
| nDCG@k | 0.5825 |
| judged_coverage_at_k | 0.5714 |
| retrieved_count_at_k | 7 |
| unjudged_retrieved_count_at_k | 3 |
| judged_relevant_count | 8 |

## Live Run

| Query | Retrieved by live lexical retriever | Missed relevant | Unjudged retrieved | Warnings |
|---|---|---|---|---|
| q-demand-growth | chunk-contradictory-channel, chunk-demand-growth | chunk-revenue-growth | chunk-contradictory-channel | missed_relevant_documents_at_k, unjudged_retrieved_documents |
| q-risk-contradiction | chunk-demand-growth, chunk-contradictory-channel | chunk-source-quality | chunk-demand-growth | missed_relevant_documents_at_k, unjudged_retrieved_documents |
| q-source-quality | chunk-missing-source, chunk-scope-boundary | chunk-source-quality | chunk-scope-boundary | missed_relevant_documents_at_k, unjudged_retrieved_documents |
| q-what-missing | chunk-missing-source | chunk-scope-boundary | none | missed_relevant_documents_at_k |

## Quality Claim Gate

This gate blocks the live lexical baseline from being cited as semantic retrieval quality evidence.

- status: `blocked`
- can_claim_semantic_quality: `false`
- summary: `live_lexical_qrels_baseline_quality_claim_blocked`
- blocker_codes: `toy_qrels_fixture_boundary, unjudged_retrieved_documents, incomplete_judged_coverage, missed_relevant_documents, live_lexical_baseline_boundary`

## Boundary

This is a live lexical baseline over a tiny local fixture.

This is not semantic retrieval quality evidence.

This is not embedding generation.

This is not representative retrieval evaluation.

This is not a benchmark result.

This is not hosted deployment evidence.
