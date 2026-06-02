# Semantic Retrieval Quality Fixture

Phase marker: semantic retrieval quality fixture v0.

This fixture creates a tiny labeled corpus for the next semantic retrieval quality-evaluation gate.

It is intentionally small:

- 4 queries
- 6 corpus chunks
- 8 qrels
- caller-provided 3-dimensional toy vectors
- one chunk with a missing embedding
- information-role labels from `docs/research/meaningful-information-collection.md`

## Files

```text
manifest.json
corpus.json
queries.json
```

## Boundary

This is fixture data only.

It is not embedding generation.

It is not vector search quality evidence.

It is not a benchmark result.

It is not a model comparison.

It is not Evidence Ledger generation.
