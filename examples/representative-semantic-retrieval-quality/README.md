# Representative Semantic Retrieval Quality Fixture

Phase marker: representative semantic retrieval quality fixture v0.

This fixture is local and bounded. It expands the earlier tiny semantic retrieval quality fixture into a small representative slice of NoiseProof's own information roles and source types.

It contains:

- 6 queries
- 12 corpus chunks
- 24 qrels
- 6 negative qrels
- caller-provided 5-dimensional fixture vectors
- all information-role labels from `docs/research/meaningful-information-collection.md`
- source types: `csv`, `html`, `markdown`, `memo`, `pdf`

## Files

```text
manifest.json
corpus.json
queries.json
```

## Boundary

This is local fixture data only.

It is not live embedding generation.

It is not production semantic retrieval quality evidence.

It is not a public benchmark result.

It is not a model comparison.

It is not hosted deployment evidence.
