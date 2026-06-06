# Workflow Proof Bundle Markdown Export

Status: implemented.

Phase marker: workflow proof bundle markdown export v0.

## Purpose

Add a reviewer-readable markdown rendering of the existing workflow proof bundle read model.

The JSON endpoint remains the source read model. The markdown endpoint is a read-only rendering for faster human inspection.

## Implemented Route

```text
GET /workflow-runs/{id}/proof-bundle/markdown
```

Response content type:

```text
text/markdown; charset=utf-8
```

The markdown export includes:

```text
# Workflow Proof Bundle
workflow_run_id
workflow_trace_id
bundle_boundary
## Summary Counts
## Proof Surfaces
## Reviewer Checklist
## Warnings
## Boundary
```

## Dashboard Discovery

`GET /ops/dashboard` workflow rows now include a GET-only `proof markdown` link next to `detail`, `lineage`, `proof bundle`, and `reviewer checklist`.

## Reviewer Checklist Surface

The markdown rendering exposes the same checklist items as the JSON proof bundle:

```text
detail_counts
lineage_links
trace_lookup
failure_case_handoff
```

## Boundary

This is a read-only rendering of the existing workflow proof bundle.

It creates no new storage.

It is not a new workflow execution path.

It is not distributed tracing.

It is not hosted observability.

It is not semantic retrieval quality evidence.

It is not embedding generation.

It is not Evidence Ledger quality evidence.

It is not Noise Gate quality evidence.

It is not report quality evidence.

It is not external reviewer feedback.

It is not product-complete.

## Test Evidence

```text
test_workflow_run_proof_bundle_markdown_export_is_readable_and_dashboard_linked
test_workflow_proof_bundle_markdown_export_is_recorded
```

## Next Gate

```text
local Docker/FastAPI runtime smoke for workflow proof bundle markdown export if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
