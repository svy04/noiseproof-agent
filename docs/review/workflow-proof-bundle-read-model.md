# Workflow Proof Bundle Read Model

Status: Accepted

Phase marker: workflow proof bundle read model v0

## Context

NoiseProof already exposes separate inspection surfaces for a deterministic workflow preview:

- `GET /workflow-runs/{id}` for parent and child records
- `GET /workflow-runs/{id}/lineage` for derived stage input lineage
- `GET /traces/{workflow_trace_id}` for records that share a local trace id

Those routes are useful, but a reviewer has to know which three links to open. The next bounded product gate is a small proof-bundle read model that collects those existing surfaces without creating new storage.

## Decision

Add:

```text
GET /workflow-runs/{id}/proof-bundle
```

The endpoint returns the workflow parent, workflow trace id when present, existing workflow detail response, existing derived lineage response, existing trace lookup response when a trace id is present, proof surface links, and explicit boundary warnings.

## Implemented Behavior

`GET /workflow-runs/{id}/proof-bundle` returns:

```text
bundle_boundary: read_model_only_existing_records_no_new_storage
proof_surfaces:
  - /workflow-runs/{id}
  - /workflow-runs/{id}/lineage
  - /traces/{workflow_trace_id} when available
```

For metadata-only workflow rows without `trace_json.workflow_trace_id`, the endpoint still returns detail and lineage surfaces, but `workflow_trace_id` and `trace` are `null` and the warnings explain that trace lookup is omitted.

## Verification

Focused route tests:

```text
uv run pytest -q tests/test_routes.py -k "proof_bundle"
```

Observed result:

```text
2 passed, 143 deselected
```

## Boundaries

This gate adds:

- no database table
- no migration
- no new persisted lineage fact
- no direct Evidence Ledger -> Noise Gate -> Report foreign-key links
- no distributed tracing
- no hosted observability
- no LLM calls
- no embeddings
- no retrieval expansion
- no report generation
- no external reviewer feedback
- no hosted deployment evidence
- no product-complete claim

The endpoint is a convenience read model over existing local records. It makes the current proof easier to inspect; it does not make the proof stronger than the underlying records.
