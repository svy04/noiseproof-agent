# Workflow Lineage Warning Code Dashboard Review

Status: Accepted

Workflow lineage warning code dashboard review is a bounded review-only gate.

This is a review-only gate before any `GET /ops/dashboard` rendering change for lineage `warning_codes`.

## Context

Phase 36 added machine-readable `warning_codes` to `GET /workflow-runs/{id}/lineage` while preserving human-readable `warnings`.

Phase 36.5 reviewed how those codes should be documented.

Phase 37 added a runbook response-shape example that shows `warnings` and `warning_codes` together.

The next temptation is to show warning codes directly in the plain operations dashboard. That may be useful, but the dashboard currently acts as a navigation and inspection aid over existing records. It should not become an analytics surface or a second lineage renderer by accident.

## Decision

Do not add dashboard rendering in this review gate.

Keep `GET /ops/dashboard` unchanged for now. The dashboard already links workflow rows to `GET /workflow-runs/{id}/lineage`, where `warning_codes` are visible beside the human-readable warnings.

If warning codes are surfaced in the dashboard later, they should be shown as compact response-level taxonomy for the derived lineage read model, not as persisted warning-code records, aggregate metrics, or a strict relational lineage contract.

The first dashboard surfacing should be minimal:

- add a lineage warning-code hint near workflow lineage links
- show codes only when fetched from the existing lineage endpoint or clearly label them as lineage-response codes
- keep human-readable warnings canonical for readers
- keep the dashboard plain and inspection-oriented

## Warning Codes In Scope

The current lineage response can expose:

```text
derived_read_model_boundary
local_workflow_scope
missing_manifest_reference
invalid_manifest_shape
```

The dashboard should not redefine these. It should point readers back to the lineage endpoint and runbook explanation.

## Explicit Non-changes

This gate adds:

- no runtime behavior
- no dashboard rendering
- no dashboard analytics
- no migrations
- no columns
- no join tables
- no warning-code persistence
- no warning-code enum table
- no mutation endpoint
- no repair endpoint
- no direct evidence -> gate -> report foreign-key links

## Risks

Showing codes too early in the dashboard can make them look like durable stored facts instead of response-level taxonomy. It can also make the dashboard look more complete than the lineage model really is.

The safer next implementation is a very small dashboard surfacing gate that preserves the current boundaries.

## Next Gate

Recommended next gate:

```text
workflow lineage warning code dashboard surfacing v0
```

Acceptance for that gate should require:

- `GET /ops/dashboard` remains plain HTML
- workflow rows keep detail and lineage links
- warning-code display is bounded to existing lineage response semantics
- no migrations, columns, join tables, or warning-code persistence
- no LLM calls, embeddings, semantic retrieval, external search, autonomous workflow execution, or free-form final answer generation
