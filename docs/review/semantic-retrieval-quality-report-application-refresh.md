# Semantic Retrieval Quality Report Application Refresh

Phase marker: semantic retrieval quality report application refresh v0.

Status: documentation-only application surface refresh.

## Purpose

Surface the toy semantic retrieval quality report in reviewer-facing application docs without converting the report into a quality claim.

This refresh exists because the repo now has a small labeled fixture, a deterministic evaluator, and a static report that records toy fixture metric output, visible misses, and semantic/lexical disagreement.

## Updated Surfaces

```text
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
docs/application/braincrew-role-map.md
docs/review/application-ready-review.md
docs/review/external-reader-proof-path.md
docs/review/readme-proof-marker-archive.md
```

Primary report artifact:

```text
docs/evaluation/semantic-retrieval-quality-report.md
```

## Surfaced Report

```text
fixture_id: semantic-retrieval-quality-fixture-v0
Hit@k: 0.75
Recall@k: 0.375
MRR@k: 0.375
nDCG@k: 0.198
semantic_vs_lexical_disagreement: 0.9167
visible failure: q-what-missing
```

The surfaced report is toy fixture metric output only. It keeps `q-what-missing` visible because the point is inspectability, not a success narrative.

## Claim Update

Allowed claim:

```text
NoiseProof has a bounded toy fixture report for semantic retrieval quality metrics, including visible failures and disagreement with lexical ranking.
```

Forbidden claim:

```text
NoiseProof does not prove vector search quality, does not claim a benchmark result, does not compare models, and does not prove production semantic retrieval quality.
```

## Boundary

This is not embedding generation.

This is not vector search quality evidence.

This is not a benchmark result.

Boundary marker: not benchmark result.

This is not a model comparison.

This is not Evidence Ledger generation.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not Braincrew acceptance.

This is not product-complete.

## Next Gate

```text
next product gate: semantic retrieval quality report reviewer request refresh v0
```
