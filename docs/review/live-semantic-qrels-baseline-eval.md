# Live Semantic Qrels Baseline Eval

Phase 862 adds live semantic qrels baseline eval v0.

Phase marker: live semantic qrels baseline v0.

## Source-first Anchor

This phase keeps the Phase 859 TREC-style qrels/run shape and the Phase 860
live-run discipline, but changes the run source to the same exact cosine
caller-provided vector boundary used by the semantic retrieval preview/run path:

- qrels file shape: `TOPIC ITERATION DOCUMENT# RELEVANCY`
- run shape: `query_id -> ranked document ids`
- run source: `caller_provided_live_semantic_cosine`
- retrieval strategy: `semantic-cosine`
- ranking boundary: `exact_cosine_caller_provided_query_vector`
- metrics: `Hit@k`, `Recall@k`, `MRR@k`, `nDCG@k`, and `judged_coverage_at_k`

Primary references retained for the naming and file-shape boundary:

- NIST TREC qrels format: `https://trec.nist.gov/data/qrels_eng/`
- NIST `trec_eval`: `https://github.com/usnistgov/trec_eval`
- nDCG reference path: `https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html`

## What Changed

New evaluator and command:

```text
packages/ingestion/retrieval/live_semantic_qrels.py
apps/api/app/services/live_semantic_qrels_baseline_command.py
app.services.live_semantic_qrels_baseline_command
```

New report:

```text
docs/evaluation/live-semantic-qrels-baseline-report.md
```

The command loads:

```text
examples/semantic-retrieval-quality/
```

Then it ranks each query against fixture chunks with caller-provided embeddings,
skips chunks without embeddings, builds a per-query ranked run, and sends that
run into the qrels evaluator.

CI now checks the report is byte-for-byte current with:

```text
Check live semantic qrels baseline report staleness
```

## Observed Local Fixture Result

The committed live semantic baseline report records:

```text
run_source -> caller_provided_live_semantic_cosine
retrieval_strategy -> semantic-cosine
ranking_boundary -> exact_cosine_caller_provided_query_vector
Hit@k -> 1.0
Recall@k -> 0.75
MRR@k -> 1.0
nDCG@k -> 0.7296
judged_coverage_at_k -> 0.75
retrieved_count_at_k -> 8
unjudged_retrieved_count_at_k -> 2
judged_relevant_count -> 8
missing_embedding_chunk_ids -> chunk-missing-source
```

The quality claim gate remains blocked:

```text
status -> blocked
can_claim_semantic_quality -> false
summary -> live_semantic_qrels_baseline_quality_claim_blocked
```

Blocking evidence includes:

```text
toy_qrels_fixture_boundary
unjudged_retrieved_documents
incomplete_judged_coverage
missed_relevant_documents
caller_provided_embedding_boundary
no_live_embedding_generation
tiny_fixture_boundary
missing_chunk_embeddings
```

## Proof Gap Update

`semantic_retrieval_quality` remains `unproven`.

The current evidence is now:

```text
toy_live_semantic_qrels_baseline_toy_live_lexical_qrels_baseline_toy_qrels_backed_eval_and_caller_provided_vector_runs
```

The claim boundary is:

```text
caller_provided_live_semantic_baseline_and_toy_qrels_do_not_prove_semantic_retrieval_quality
```

The next recommended gate is:

```text
representative_live_semantic_retrieval_quality_eval_v0
```

## Boundary

This is a live semantic baseline over a tiny local fixture with caller-provided vectors.

It is not semantic retrieval quality evidence, not live embedding generation, not representative retrieval evaluation, not a benchmark result, not a model comparison, not hosted deployment evidence, not external reviewer feedback, not customer validation, not Braincrew acceptance, and not product-complete.

## Verification

Local focused tests:

```text
uv run pytest tests/test_live_semantic_qrels_baseline.py -q
```

Observed result:

```text
4 passed
```

## Next Gate

Next recommended gate:

```text
representative_live_semantic_retrieval_quality_eval_v0
```
