# Qrels-backed Semantic Retrieval Quality Eval

Phase 859 adds qrels-backed semantic retrieval quality eval v0.

## Source-first Anchor

The implementation follows the small, local version of the TREC-style
evaluation shape:

- qrels file shape: `TOPIC ITERATION DOCUMENT# RELEVANCY`
- run file shape: `qid Q0 docno rank score runid`
- qrels format marker: `trec_qrels_qid_iter_docno_relevance`
- run format marker: `trec_run_qid_Q0_docno_rank_score_runid`
- metrics: `Hit@k`, `Recall@k`, `MRR@k`, `nDCG@k`, and `judged_coverage_at_k`

Primary references used for the naming and file-shape boundary:

- NIST TREC qrels format: `https://trec.nist.gov/data/qrels_eng/`
- NIST `trec_eval`: `https://github.com/usnistgov/trec_eval`
- nDCG reference path: `https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html`

## What Changed

New fixture files:

```text
examples/semantic-retrieval-quality/qrels.txt
examples/semantic-retrieval-quality/semantic-run.txt
```

New evaluator and command:

```text
packages/ingestion/retrieval/qrels_eval.py
apps/api/app/services/qrels_backed_semantic_quality_command.py
app.services.qrels_backed_semantic_quality_command
```

New report:

```text
docs/evaluation/qrels-backed-semantic-quality-report.md
```

CI now checks the report is byte-for-byte current with:

```text
Check qrels-backed semantic quality report staleness
```

## Observed Local Fixture Result

The committed toy qrels-backed report records:

```text
Hit@k -> 0.75
Recall@k -> 0.375
MRR@k -> 0.375
nDCG@k -> 0.198
judged_coverage_at_k -> 0.6667
retrieved_count_at_k -> 6
unjudged_retrieved_count_at_k -> 2
judged_relevant_count -> 8
```

The quality claim gate remains blocked:

```text
status -> blocked
can_claim_semantic_quality -> false
summary -> qrels_backed_semantic_quality_claim_blocked
```

Blocking evidence includes:

```text
toy_qrels_fixture_boundary
unjudged_retrieved_documents
incomplete_judged_coverage
missed_relevant_documents
missing_run_results
```

## Proof Gap Update

`semantic_retrieval_quality` remains `unproven`.

The current evidence is now:

```text
toy_qrels_backed_eval_and_caller_provided_vector_runs
```

The next recommended gate is:

```text
representative_qrels_and_live_retrieval_quality_eval_v0
```

## Boundary

This is qrels-backed toy fixture evaluation only.

It is not semantic retrieval quality evidence, not embedding generation, not a benchmark result, not a model comparison, not live vector search quality evidence, not hosted deployment evidence, not external reviewer feedback, not customer validation, not Braincrew acceptance, and not product-complete.

## Verification

Local focused tests:

```text
uv run pytest tests/test_semantic_quality_qrels_eval.py -q
```

Observed result:

```text
4 passed
```

## Next Gate

Next recommended gate:

```text
representative_qrels_and_live_retrieval_quality_eval_v0
```
