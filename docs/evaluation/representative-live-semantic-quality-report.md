# Representative Live Semantic Quality Eval

Phase marker: representative live semantic quality eval v0.

This report evaluates a local representative fixture for NoiseProof information roles and source types using caller-provided vectors.

This is not production semantic retrieval quality evidence.

## Run Source

- run_source: `representative_caller_provided_live_semantic_cosine`
- retrieval_strategy: `semantic-cosine`
- ranking_boundary: `exact_cosine_caller_provided_query_vector`
- qrels_boundary: `qrels_backed_toy_eval_not_semantic_quality_evidence`
- boundary: `representative_local_fixture_not_production_semantic_quality_evidence`

## Fixture Coverage

- coverage_status: `passed`
- role_coverage_ratio: `1`
- source_type_coverage_ratio: `1`
- query_count: `6`
- chunk_count: `12`
- qrel_count: `24`
- negative_qrel_count: `6`
- required_information_roles: `direct_support, contradiction, quantitative_anchor, timeline_anchor, definition_anchor, source_quality_check, missing_data_signal, scope_boundary, user_intent_check`
- required_source_types: `csv, html, markdown, memo, pdf`
- missing_information_roles: `none`
- missing_source_types: `none`
- missing_embedding_chunk_ids: `none`

## Aggregate Metrics

| Metric | Value |
|---|---:|
| Hit@k | 1 |
| Recall@k | 1 |
| MRR@k | 1 |
| nDCG@k | 0.9954 |
| judged_coverage_at_k | 1 |
| retrieved_count_at_k | 18 |
| unjudged_retrieved_count_at_k | 0 |
| judged_relevant_count | 18 |

## Per-query Diagnostics

| Query | Retrieved | Missed relevant | Unjudged retrieved | Warnings |
|---|---|---|---|---|
| q-buy-sell-boundary | chunk-buy-sell-risk, chunk-scope-boundary, chunk-missing-renewal | none | none | none |
| q-contradiction-risk | chunk-promo-html, chunk-distributor-memo, chunk-source-quality | none | none | none |
| q-definition-timeline | chunk-timeline-filing, chunk-definition-note, chunk-source-quality | none | none | none |
| q-demand-evidence | chunk-demand-note, chunk-demand-csv, chunk-demand-pdf | none | none | none |
| q-missing-before-claim | chunk-missing-renewal, chunk-scope-boundary, chunk-buy-sell-risk | none | none | none |
| q-source-quality | chunk-source-quality, chunk-promo-html, chunk-distributor-memo | none | none | none |

## Quality Claim Gate

This gate blocks this local representative fixture from being cited as production semantic retrieval quality evidence.

- status: `blocked`
- can_claim_semantic_quality: `false`
- summary: `representative_live_semantic_quality_claim_blocked`
- blocker_codes: `toy_qrels_fixture_boundary, caller_provided_embedding_boundary, no_live_embedding_generation, local_fixture_boundary, not_production_benchmark`

## Boundary

This is a local representative fixture for NoiseProof information roles and source types.

This is not production semantic retrieval quality evidence.

This is not live embedding generation.

This is not a public benchmark result.

This is not hosted deployment evidence.
