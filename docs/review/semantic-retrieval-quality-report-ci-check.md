# Semantic Retrieval Quality Report CI Check

Phase marker: semantic retrieval quality report ci check v0.

This gate wires the existing check-only semantic retrieval quality report command into GitHub Actions CI.

The goal is to prevent the committed toy semantic retrieval quality report from drifting away from byte-for-byte regeneration when fixture, ranking, metric, or formatting code changes.

## CI Step

The workflow step is named:

```text
Check semantic retrieval quality report staleness
```

It runs from `apps/api`:

```bash
uv run python -m app.services.semantic_quality_report_command \
  --fixture ../../examples/semantic-retrieval-quality \
  --rankings ../../examples/semantic-retrieval-quality/rankings.json \
  --output ../../docs/evaluation/semantic-retrieval-quality-report.md \
  --k 2 \
  --check
```

## Expected Current Marker

When the committed report is current, the command prints:

```text
semantic_quality_report_current
```

When the committed report is stale, the command exits non-zero and prints:

```text
semantic_quality_report_stale
```

## Claim Boundary

This is CI staleness protection for a toy fixture report only.

It is:

- not embedding generation
- not vector search quality evidence
- not benchmark result
- not model comparison
- not production semantic retrieval quality
- not hosted deployment evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance

It does not close external reviewer feedback v0.
