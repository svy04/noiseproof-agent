# Semantic Quality Claim Gate

Status: implemented.

Phase marker: semantic quality claim gate v0.

Purpose: prevent the toy semantic retrieval quality fixture from being cited as semantic retrieval or vector-search quality evidence.

## Implemented Artifacts

```text
packages/ingestion/retrieval/quality_metrics.py
packages/ingestion/retrieval/quality_report.py
docs/evaluation/semantic-retrieval-quality-report.md
apps/api/tests/test_semantic_quality_report.py
apps/api/tests/test_docs.py
```

## Gate Output

The committed toy fixture currently produces:

```text
status: blocked
can_claim_semantic_quality: false
summary: semantic_quality_claim_blocked
boundary: claim_gate_only_not_vector_search_quality_evidence
```

Current blocker codes:

```text
toy_fixture_boundary
no_embedding_generation
missing_embeddings
no_semantic_candidates_at_k
no_relevant_semantic_candidate_at_k
missing_required_information_roles_at_k
missing_relevant_chunk_embeddings
lexical_rescue_needed
```

## Reviewer Reading

The gate is intentionally negative.

It makes the report easier to inspect by naming exactly why the fixture cannot be promoted into a quality claim:

- the fixture is synthetic and local
- embeddings are caller-provided fixture values
- at least one relevant chunk has no embedding
- one query has no semantic candidates at top-k
- some relevant chunks are only recovered by the lexical ranking
- some required information roles are missing at top-k

## Boundary

This is claim blocking only.

This is not vector search quality evidence.

This is not embedding generation.

This is not benchmark evidence.

This is not retrieval tuning.

This is not a model comparison.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.
