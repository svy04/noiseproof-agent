# Qrels-backed Semantic Retrieval Quality Eval

Phase marker: qrels-backed semantic retrieval quality eval v0.

This report evaluates a tiny local retrieval run against explicit qrels.

This is not semantic retrieval quality evidence.

## Formats

- qrels: `trec_qrels_qid_iter_docno_relevance`
- run: `trec_run_qid_Q0_docno_rank_score_runid`
- boundary: `qrels_backed_toy_eval_not_semantic_quality_evidence`

## Aggregate Metrics

| Metric | Value |
|---|---:|
| Hit@k | 0.75 |
| Recall@k | 0.375 |
| MRR@k | 0.375 |
| nDCG@k | 0.198 |
| judged_coverage_at_k | 0.6667 |
| retrieved_count_at_k | 6 |
| unjudged_retrieved_count_at_k | 2 |
| judged_relevant_count | 8 |

## Per-query Diagnostics

| Query | Retrieved | Missed relevant | Unjudged retrieved | Warnings |
|---|---|---|---|---|
| q-demand-growth | chunk-scope-boundary, chunk-demand-growth | chunk-revenue-growth | chunk-scope-boundary | missed_relevant_documents_at_k, unjudged_retrieved_documents |
| q-risk-contradiction | chunk-demand-growth, chunk-source-quality | chunk-contradictory-channel | chunk-demand-growth | missed_relevant_documents_at_k, unjudged_retrieved_documents |
| q-source-quality | chunk-demand-growth, chunk-missing-source | chunk-source-quality | none | missed_relevant_documents_at_k |
| q-what-missing | none | chunk-missing-source, chunk-scope-boundary | none | no_run_results_at_k, no_relevant_documents_retrieved_at_k, missed_relevant_documents_at_k |

## Quality Claim Gate

This gate blocks this toy qrels-backed evaluation from being cited as semantic retrieval quality evidence.

- status: `blocked`
- can_claim_semantic_quality: `false`
- summary: `qrels_backed_semantic_quality_claim_blocked`
- blocker_codes: `toy_qrels_fixture_boundary, unjudged_retrieved_documents, incomplete_judged_coverage, missed_relevant_documents, missing_run_results`

## Boundary

This is qrels-backed toy fixture evaluation only.

This is not semantic retrieval quality evidence.

This is not embedding generation.

This is not a benchmark result.

This is not a model comparison.

This is not hosted deployment evidence.
