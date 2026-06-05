# Workflow Proof Bundle Dashboard Link

Status: accepted.

Phase marker: workflow proof bundle dashboard link v0.

## Purpose

Expose the existing workflow proof bundle read model from the plain operations dashboard so a reviewer can move from a workflow row to the combined proof surface without manually constructing the URL.

This adds a dashboard navigation link only.

## Implemented Behavior

`GET /ops/dashboard` workflow rows now link to:

```text
GET /workflow-runs/{id}
GET /workflow-runs/{id}/lineage
GET /workflow-runs/{id}/proof-bundle
```

The rendered link shape is:

```text
href="/workflow-runs/{workflow_run_id}/proof-bundle">proof bundle</a>
```

The proof bundle endpoint itself remains the existing read model:

```text
GET /workflow-runs/{id}/proof-bundle
```

## Verification

Focused route test:

```text
uv run pytest -q tests/test_routes.py -k "proof_bundle_views"
```

Observed result:

```text
1 passed, 144 deselected
```

Route test:

```text
test_ops_dashboard_links_workflow_runs_to_detail_lineage_and_proof_bundle_views
```

## Boundary

This gate adds:

- no new endpoint
- no schema
- no migration
- no new lineage storage
- direct Evidence Ledger -> Noise Gate -> Report stage links are now represented by Phase 530 workflow-created link tables, while this dashboard-link gate remains navigation only
- no distributed tracing
- no hosted observability
- no LLM calls
- no embeddings
- no retrieval expansion
- no report generation
- no external reviewer feedback
- no hosted deployment evidence
- no product-complete claim

It makes an existing proof surface easier to inspect from the dashboard. It does not make the underlying proof stronger than the existing workflow detail, lineage, and trace lookup records.
