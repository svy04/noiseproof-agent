# Workflow Proof Bundle Reviewer Checklist

Phase marker: workflow proof bundle reviewer checklist v0.

## Purpose

Make `GET /workflow-runs/{workflow_run_id}/proof-bundle` easier for reviewers to inspect without adding storage, workflow behavior, LLM calls, retrieval behavior, or dashboard polish.

The proof bundle already collects workflow detail, derived lineage, optional trace lookup, proof surfaces, and warnings. This gate adds a small `reviewer_checklist` field that names what each reviewer should inspect and what each surface does not prove.

## Implemented Behavior

`GET /workflow-runs/{workflow_run_id}/proof-bundle` now returns `reviewer_checklist` items:

```text
detail_counts
lineage_links
trace_lookup
failure_case_handoff
```

Each item includes:

```text
check_id
proof_surface
status
inspection_goal
boundary
```

Expected statuses:

```text
available
not_available
not_applicable
```

For deterministic preview workflows with a `workflow_trace_id`, `trace_lookup` points to `/traces/{workflow_trace_id}` and has status `available`.

For metadata-only workflow rows without a `workflow_trace_id`, `trace_lookup` has status `not_available` and explicitly says the bundle does not claim trace-level proof.

For workflows without linked failure cases, `failure_case_handoff` has status `not_applicable`.

## Boundary

This is a read-only response-shape inspectability gate.

It is not distributed tracing, not hosted observability, not new storage, not a new lineage contract, not retry behavior, not root-cause automation, not semantic retrieval quality evidence, not embedding generation, not LLM output, not external reviewer feedback, and not product-complete.

## Verification

Route tests:

```text
test_workflow_run_proof_bundle_exposes_reviewer_checklist_without_new_storage
```

Documentation test:

```text
test_workflow_proof_bundle_reviewer_checklist_is_recorded
```

## Next Gate

External reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from the current repository state.
