# Representative Live Semantic Quality Eval

Phase 864 adds representative live semantic quality eval v0.

Phase marker: representative live semantic quality eval v0.

## Source-first Anchor

This phase keeps the qrels-backed evaluation discipline, but replaces the tiny
semantic fixture with a local representative fixture for NoiseProof's own
market-intelligence information roles and source types.

Primary references retained for the metric and qrels boundary:

- NIST TREC qrels format: `https://trec.nist.gov/data/qrels_eng/`
- NIST `trec_eval`: `https://github.com/usnistgov/trec_eval`
- nDCG reference path: `https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html`

## What Changed

New fixture:

```text
examples/representative-semantic-retrieval-quality/
```

New evaluator and command:

```text
packages/ingestion/retrieval/representative_semantic_quality.py
apps/api/app/services/representative_live_semantic_quality_command.py
app.services.representative_live_semantic_quality_command
```

New report:

```text
docs/evaluation/representative-live-semantic-quality-report.md
```

CI now checks the report is byte-for-byte current with:

```text
Check representative live semantic quality report staleness
```

## Fixture Coverage

The representative fixture records:

```text
coverage_status -> passed
role_coverage_ratio -> 1.0
source_type_coverage_ratio -> 1.0
query_count -> 6
chunk_count -> 12
qrel_count -> 24
negative_qrel_count -> 6
required_source_types -> csv, html, markdown, memo, pdf
missing_information_roles -> none
missing_source_types -> none
missing_embedding_chunk_ids -> none
```

The required information roles come from `docs/research/meaningful-information-collection.md`:

```text
direct_support
contradiction
quantitative_anchor
timeline_anchor
definition_anchor
source_quality_check
missing_data_signal
scope_boundary
user_intent_check
```

## Observed Local Fixture Result

The committed representative report records:

```text
run_source -> representative_caller_provided_live_semantic_cosine
retrieval_strategy -> semantic-cosine
ranking_boundary -> exact_cosine_caller_provided_query_vector
Hit@k -> 1.0
Recall@k -> 1.0
MRR@k -> 1.0
nDCG@k -> 0.9954
judged_coverage_at_k -> 1.0
retrieved_count_at_k -> 18
unjudged_retrieved_count_at_k -> 0
judged_relevant_count -> 18
```

The quality claim gate remains blocked:

```text
status -> blocked
can_claim_semantic_quality -> false
summary -> representative_live_semantic_quality_claim_blocked
```

Blocking evidence includes:

```text
toy_qrels_fixture_boundary
caller_provided_embedding_boundary
no_live_embedding_generation
local_fixture_boundary
not_production_benchmark
```

## Proof Gap Update

`semantic_retrieval_quality` remains `unproven`.

The current evidence is now:

```text
representative_local_semantic_quality_eval_with_caller_provided_vectors
```

The claim boundary is:

```text
representative_local_fixture_and_caller_provided_vectors_do_not_prove_production_semantic_retrieval_quality
```

The next recommended gate is:

```text
live_embedding_backed_domain_qrels_quality_eval_v0
```

## Boundary

This is a local representative fixture for NoiseProof information roles and source types.

It is not production semantic retrieval quality evidence, not live embedding generation, not a public benchmark result, not a model comparison, not hosted deployment evidence, not external reviewer feedback, not customer validation, not Braincrew acceptance, and not product-complete.

## Verification

Local focused tests:

```text
uv run pytest tests/test_representative_live_semantic_quality.py -q
```

Observed result:

```text
4 passed
```

## Next Gate

Next recommended gate:

```text
live_embedding_backed_domain_qrels_quality_eval_v0
```
