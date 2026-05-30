# Workflow lineage warning code documentation review

Status: Phase 36.5 review-only gate.

This review decides how the newly exposed lineage `warning_codes` should be documented before adding more runtime behavior, dashboard rendering, or schema.

## Current evidence

Phase 36 added response-level `warning_codes` to:

```text
GET /workflow-runs/{id}/lineage
```

The endpoint still returns human-readable `warnings`. That is intentional: `warning_codes` are for machine-readable grouping, while human-readable warnings remain canonical for readers.

## Documentation boundary

The documentation should explain only the current response shape:

- `warning_codes`
- `warnings`
- `lineage_boundary`
- no persisted warning-code storage
- no strict relational evidence -> gate -> report lineage

The current warning codes are:

| code | meaning |
| --- | --- |
| `derived_read_model_boundary` | The lineage endpoint is a derived read model over existing workflow child records and `stage_input_manifest`. |
| `missing_manifest_reference` | One or more manifest ids could not be resolved inside the current workflow run. |
| `invalid_manifest_shape` | A known manifest field has an invalid shape, such as `input_evidence_ledger_entry_ids` not being a list. |
| `local_workflow_scope` | Resolution is intentionally scoped to records attached to the current workflow run. |

## Decision

Do not add runtime behavior in this review gate.

Specifically:

- no migrations
- no columns
- no join tables
- no warning-code persistence
- no warning-code enum table
- no dashboard rendering change
- no mutation endpoint
- no repair endpoint
- no direct evidence -> gate -> report foreign keys
- no LLM calls
- no embeddings or retrieval changes

The safest next step is to add a runbook example that shows both `warnings` and `warning_codes` in one lineage response shape.

## Recommended next gate

```text
workflow lineage warning code runbook example v0
```

Acceptance criteria:

- runbook includes a small `GET /workflow-runs/{id}/lineage` response shape
- example includes both `warnings` and `warning_codes`
- example includes at least `derived_read_model_boundary` and `local_workflow_scope`
- example states that warning codes are response-level taxonomy only
- no migrations
- no columns
- no join tables
- no dashboard polish

## Claim boundary

Allowed claim:

```text
NoiseProof has reviewed how lineage warning codes should be documented before expanding runtime behavior.
```

Forbidden claim:

```text
NoiseProof has persisted warning-code analytics, dashboard warning-code rendering, production diagnostics, lineage repair, or strict relational evidence -> gate -> report lineage.
```
