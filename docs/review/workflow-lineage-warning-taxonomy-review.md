# Workflow lineage warning taxonomy review

Status: Phase 35.5 review-only gate.

This review decides how to name the warning categories emitted by the derived workflow lineage read model before adding structured warning fields or schema.

## Current evidence

Phase 32 added:

```text
GET /workflow-runs/{id}/lineage
```

Phase 34 proved missing manifest references are surfaced without adding mutation paths. Phase 35 hardened malformed `input_evidence_ledger_entry_ids` shapes so non-list values are ignored as ids and reported with a warning.

The current response still returns `warnings` as human-readable strings. That is acceptable for the current read-model surface, but the project should not let unrelated warnings collapse into one vague bucket.

## Warning taxonomy

### derived_read_model_boundary

Meaning:

```text
The lineage response is derived from existing workflow child records and stage_input_manifest values.
```

This warning protects the boundary that the endpoint is not a strict relational lineage schema, not distributed tracing, and not a claim that evidence -> gate -> report foreign keys exist.

### missing_manifest_reference

Meaning:

```text
One or more manifest ids were present but could not be resolved inside the current workflow run.
```

This covers missing Evidence Ledger ids and missing Noise Gate ids. It should remain local to the current `workflow_run_id`; global lookup would imply stronger provenance than the deterministic preview currently proves.

### invalid_manifest_shape

Meaning:

```text
The manifest has a known field with an invalid shape, such as input_evidence_ledger_entry_ids not being a list.
```

This category is for malformed local manifest structure. It is not a repair claim, data migration claim, or guarantee that all malformed JSON shapes are normalized.

### local_workflow_scope

Meaning:

```text
Lineage resolution is intentionally scoped to records attached to the current workflow run.
```

This protects cross-workflow behavior: an id that exists in another workflow should still be reported as missing from the current workflow lineage response.

## Decision

Do not add warning code fields in this review gate.

Specifically:

- no migrations
- no columns
- no join tables
- no new warning enum column
- no new response schema field yet
- no dashboard polish
- no mutation endpoint
- no repair endpoint
- no LLM calls
- no embeddings or retrieval changes

For now, warning strings remain human-readable. The taxonomy above is a review artifact that names the categories before the API shape changes.

## Recommended next gate

```text
structured warning taxonomy v0
```

Acceptance criteria for that future gate:

- the lineage response can expose machine-readable warning categories
- existing human-readable warning strings remain available
- categories map to the taxonomy in this review
- no migrations
- no columns
- no join tables
- no direct evidence -> gate -> report foreign keys
- no dashboard polish

Follow-up implemented by Phase 36:

```text
structured warning taxonomy v0
```

Phase 36 exposes `warning_codes` on `GET /workflow-runs/{id}/lineage` while keeping the existing human-readable `warnings` field.

## Claim boundary

Allowed claim:

```text
NoiseProof has reviewed lineage warning categories before adding structured warning fields.
```

Forbidden claim:

```text
NoiseProof has production-grade provenance diagnostics, lineage repair, distributed tracing, or strict relational evidence -> gate -> report lineage.
```
