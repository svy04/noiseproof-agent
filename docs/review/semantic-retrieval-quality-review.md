# Semantic Retrieval Quality Review

Phase marker: semantic retrieval quality review v0.

Status: review-only.

## Purpose

Decide the smallest safe quality-evaluation boundary before claiming that semantic retrieval is good.

Do not claim semantic retrieval quality from the runtime smoke. The Phase 228 smoke proves that persisted semantic retrieval runs can execute locally. It does not prove that the retrieved chunks are useful, complete, or better than lexical retrieval.

## Primary Sources Checked

TREC / NIST retrieval evaluation:

```text
https://trec.nist.gov/
https://trec.nist.gov/trec_eval/
```

Relevant observation:

- Retrieval evaluation normally needs query topics, judged relevant documents, and a scoring method such as MAP or other ranked-retrieval metrics.

BEIR:

```text
https://arxiv.org/abs/2104.08663
https://github.com/beir-cellar/beir
```

Relevant observation:

- BEIR treats retrieval evaluation as benchmarked search over datasets with relevance judgments.
- The common pattern is not a single successful example; it is repeated query/corpus/qrels evaluation with metrics such as nDCG, Recall, and Precision at cutoffs.

Sentence Transformers InformationRetrievalEvaluator:

```text
https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator
```

Relevant observation:

- `InformationRetrievalEvaluator` reports ranked-retrieval metrics such as MRR, nDCG, Accuracy, Precision, Recall, and MAP.

Local NoiseProof collection-planning note:

```text
docs/research/meaningful-information-collection.md
```

Relevant observation:

- NoiseProof should evaluate whether retrieval returns role-diverse information, not only semantically similar text.
- Required roles include direct support, contradiction, quantitative anchor, timeline anchor, definition anchor, source quality check, missing data signal, scope boundary, and user intent check.

## Current State

NoiseProof currently has:

```text
chunk_embeddings table
caller-provided chunk embedding endpoint
semantic retrieval preview endpoint
semantic retrieval persistence endpoint
local runtime smoke for semantic retrieval persistence
```

Current semantic retrieval runtime proof:

```text
docs/review/semantic-retrieval-persistence-runtime-smoke.md
```

That proof records:

```text
POST /documents/{document_id}/semantic-retrieval-runs -> 201
GET /retrieval-runs -> 200
retrieval_run_count_after = retrieval_run_count_before + 1
dimension mismatch -> 400
evidence_ledger_count_unchanged -> true
```

This is runtime behavior, not retrieval quality evidence.

## Decision

The next gate should be:

```text
semantic retrieval quality fixture v0
```

Before implementing quality scoring against arbitrary data, create a small local fixture with:

```text
queries
corpus chunks
caller-provided embeddings
qrels / relevant chunk ids
negative chunks
missing embedding cases
information-role labels
```

The fixture should support both lexical and semantic retrieval comparison, but it should not introduce embedding generation.

## Candidate Metrics

Use only small, inspectable metrics at first:

```text
Hit@k
Recall@k
MRR@k
nDCG@k
missing_embedding_rate
semantic_vs_lexical_disagreement
role_coverage_at_k
```

Metric intent:

| Metric | Why it matters |
|---|---|
| Hit@k | verifies at least one labeled relevant chunk appears in the candidate set |
| Recall@k | checks how many labeled relevant chunks were retrieved |
| MRR@k | rewards ranking a relevant chunk early |
| nDCG@k | supports graded relevance later, if the fixture adds grades |
| missing_embedding_rate | keeps missing vector coverage visible |
| semantic_vs_lexical_disagreement | reveals when semantic and lexical candidates diverge |
| role_coverage_at_k | checks whether direct support, contradiction, quantitative anchors, and boundary signals are represented |

## Quality Claim Rule

Allowed after this review:

```text
NoiseProof has selected a bounded quality-evaluation plan for semantic retrieval.
```

Not allowed:

```text
NoiseProof has proven semantic retrieval quality.
```

Not allowed:

```text
Semantic retrieval is better than lexical retrieval.
```

## Boundary

This is not embedding generation.

This is not vector search quality evidence.

This is not a benchmark result.

This is not a model comparison.

This is not a retrieval tuning change.

This is not Evidence Ledger generation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not Braincrew acceptance.

This is not product-complete.

## Next Gate

```text
next product gate: semantic retrieval quality fixture v0
```
