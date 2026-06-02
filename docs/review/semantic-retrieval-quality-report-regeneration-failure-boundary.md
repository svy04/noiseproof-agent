# Semantic Retrieval Quality Report Regeneration Failure Boundary

Phase marker: semantic retrieval quality report regeneration failure boundary v0.

This gate makes the semantic retrieval quality report regeneration command fail inspectably when the malformed rankings fixture is supplied.

## Behavior

Malformed rankings fixture example:

```json
{"lexical_rankings": {}}
```

Expected command behavior:

```text
exit code 2
semantic_quality_report_regeneration_failed
semantic_rankings
not vector search quality evidence
```

The command should produce no traceback for this user-facing validation failure.

## Why This Matters

The regeneration command is part of the proof surface. If it fails with a raw traceback, it becomes harder for a reviewer to inspect what happened and whether the failure changes the claim boundary.

This failure boundary keeps the command aligned with the project thesis:

```text
unsupported or malformed inputs should fail visibly before they become stronger claims
```

## Claim Boundary

This is command failure handling only.

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
