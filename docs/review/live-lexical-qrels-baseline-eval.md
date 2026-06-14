# Live Lexical Qrels Baseline Eval

Phase 860 adds live lexical qrels baseline eval v0.

Phase marker: live lexical qrels baseline v0.

## Source-first Anchor

This phase keeps the Phase 859 TREC-style qrels/run shape, but changes the run
source from a hand-authored fixture file to the existing local lexical retriever:

- qrels file shape: `TOPIC ITERATION DOCUMENT# RELEVANCY`
- run shape: `query_id -> ranked document ids`
- run source: `live_lexical_retrieve_candidates`
- retrieval strategy: `fixed-window`
- metrics: `Hit@k`, `Recall@k`, `MRR@k`, `nDCG@k`, and `judged_coverage_at_k`

Primary references retained for the naming and file-shape boundary:

- NIST TREC qrels format: `https://trec.nist.gov/data/qrels_eng/`
- NIST `trec_eval`: `https://github.com/usnistgov/trec_eval`
- nDCG reference path: `https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html`

## What Changed

New evaluator and command:

```text
packages/ingestion/retrieval/live_lexical_qrels.py
apps/api/app/services/live_lexical_qrels_baseline_command.py
app.services.live_lexical_qrels_baseline_command
```

New report:

```text
docs/evaluation/live-lexical-qrels-baseline-report.md
```

The command loads:

```text
examples/semantic-retrieval-quality/
```

Then it converts each fixture corpus chunk into a `RetrievalSource`, calls the
existing `retrieve_candidates()` path, builds a per-query ranked run, and sends
that run into the qrels evaluator.

CI now checks the report is byte-for-byte current with:

```text
Check live lexical qrels baseline report staleness
```

## Observed Local Fixture Result

The committed live lexical baseline report records:

```text
Hit@k -> 1.0
Recall@k -> 0.5
MRR@k -> 0.75
nDCG@k -> 0.5825
judged_coverage_at_k -> 0.5714
retrieved_count_at_k -> 7
unjudged_retrieved_count_at_k -> 3
judged_relevant_count -> 8
```

The quality claim gate remains blocked:

```text
status -> blocked
can_claim_semantic_quality -> false
summary -> live_lexical_qrels_baseline_quality_claim_blocked
```

Blocking evidence includes:

```text
toy_qrels_fixture_boundary
unjudged_retrieved_documents
incomplete_judged_coverage
missed_relevant_documents
live_lexical_baseline_boundary
```

## Proof Gap Update

`semantic_retrieval_quality` remains `unproven`.

The current evidence is now:

```text
toy_live_lexical_qrels_baseline_toy_qrels_backed_eval_and_caller_provided_vector_runs
```

The claim boundary is:

```text
live_lexical_baseline_and_toy_qrels_do_not_prove_semantic_retrieval_quality
```

The next recommended gate is:

```text
representative_live_semantic_retrieval_quality_eval_v0
```

## Boundary

This is a live lexical baseline over a tiny local fixture.

It is not semantic retrieval quality evidence, not embedding generation, not representative retrieval evaluation, not a benchmark result, not a model comparison, not hosted deployment evidence, not external reviewer feedback, not customer validation, not Braincrew acceptance, and not product-complete.

## Verification

Local focused tests:

```text
uv run pytest tests/test_live_lexical_qrels_baseline.py -q
uv run pytest tests/test_routes.py::test_ops_summary_and_dashboard_surface_current_proof_gap_registry tests/test_routes.py::test_ops_proof_gap_action_surface_exposes_gap_details_without_closing_gap -q
```

Observed result:

```text
4 passed
2 passed
```

## Next Gate

Next recommended gate:

```text
representative_live_semantic_retrieval_quality_eval_v0
```
