# Semantic Retrieval Quality Report Check Mode

Phase marker: semantic retrieval quality report check mode v0.

This gate adds a check-only mode for the semantic retrieval quality report regeneration command.

The goal is to let reviewers and CI-style checks verify that the committed report is still current without rewriting the report file.

## Command

Run from `apps/api`:

```bash
uv run python -m app.services.semantic_quality_report_command \
  --fixture ../../examples/semantic-retrieval-quality \
  --rankings ../../examples/semantic-retrieval-quality/rankings.json \
  --output ../../docs/evaluation/semantic-retrieval-quality-report.md \
  --k 2 \
  --check
```

## Current Report Result

When the committed report matches byte-for-byte regeneration, the command returns:

```text
exit code 0
semantic_quality_report_current
byte-for-byte regeneration
not vector search quality evidence
```

## Stale Report Result

When the committed report does not match byte-for-byte regeneration, the command returns:

```text
exit code 3
semantic_quality_report_stale
byte-for-byte regeneration mismatch
not vector search quality evidence
```

Check mode must not write the output file.

## Claim Boundary

This is staleness detection for a toy report only.

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
