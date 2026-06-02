# Semantic Retrieval Quality Report Regeneration Command

Phase marker: semantic retrieval quality report regeneration command v0.

This gate makes the toy semantic retrieval quality report reproducible from fixture files instead of relying on a hand-maintained markdown table.

It adds byte-for-byte regeneration for:

```text
docs/evaluation/semantic-retrieval-quality-report.md
```

## Command

Run from `apps/api`:

```bash
uv run python -m app.services.semantic_quality_report_command \
  --fixture ../../examples/semantic-retrieval-quality \
  --rankings ../../examples/semantic-retrieval-quality/rankings.json \
  --output ../../docs/evaluation/semantic-retrieval-quality-report.md \
  --k 2
```

## Inputs

- `examples/semantic-retrieval-quality/manifest.json`
- `examples/semantic-retrieval-quality/corpus.json`
- `examples/semantic-retrieval-quality/queries.json`
- `examples/semantic-retrieval-quality/rankings.json`

`rankings.json` is a caller-provided toy ranking fixture. Its boundary marker is:

```text
ranking_fixture_only_not_search_quality
```

## Code Path

- `app.services.semantic_quality_report_command`
- `packages/ingestion/retrieval/quality_fixture.py`
- `packages/ingestion/retrieval/quality_metrics.py`
- `packages/ingestion/retrieval/quality_report.py`

## Output Boundary

The generated report keeps:

- `toy_fixture_metric_only_not_search_quality`
- `q-what-missing`
- visible weak rankings
- visible semantic/lexical disagreement

## Claim Boundary

Allowed claim:

```text
The toy semantic retrieval quality report can be regenerated from explicit local fixture inputs.
```

Forbidden claims:

- not embedding generation
- not vector search quality evidence
- not benchmark result
- not model comparison
- not production semantic retrieval quality
- not hosted deployment evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance

This command is reproducibility plumbing, not retrieval quality proof.
