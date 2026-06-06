# Workflow Proof Bundle Reviewer Checklist Dashboard Discovery

Phase marker: workflow proof bundle reviewer checklist dashboard discovery v0.

## Purpose

Make the `reviewer_checklist` added to `GET /workflow-runs/{workflow_run_id}/proof-bundle` easier to discover from `GET /ops/dashboard`.

The dashboard already links workflow rows to detail, lineage, and proof bundle routes. This gate adds a visible `reviewer checklist` link label that points to the existing proof bundle endpoint, plus a short boundary note in the Workflow Runs section.

## Implemented Behavior

`GET /ops/dashboard` workflow rows now expose:

```text
detail
lineage
proof bundle
reviewer checklist
```

The `reviewer checklist` link points to:

```text
GET /workflow-runs/{id}/proof-bundle
```

The dashboard also states that the proof bundle includes a read-only `reviewer_checklist` for:

```text
detail counts
lineage links
trace lookup
failure-case handoff
```

## Boundary

This is dashboard discovery only.

It does not add storage, schema, migrations, or new lineage facts.

It is not distributed tracing, not hosted observability, not retry behavior, not root-cause automation, not external reviewer feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not LLM output, and not product-complete proof.

## Verification

Route test:

```text
test_ops_dashboard_surfaces_workflow_proof_bundle_reviewer_checklist_discovery
```

Documentation test:

```text
test_workflow_proof_bundle_reviewer_checklist_dashboard_discovery_is_recorded
```

## Next Gate

External reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from the current repository state.
