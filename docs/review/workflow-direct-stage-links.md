# Workflow Direct Stage Links

Status: implemented.

Phase marker: workflow direct stage links v0.

## Purpose

Make deterministic workflow-created Evidence Ledger, Noise Gate, and Report records easier to inspect as a local stage chain.

Before this gate, `GET /workflow-runs/{id}/lineage` resolved `stage_input_manifest` values as a derived read model. This gate adds direct workflow stage link rows for records created by `POST /workflow-runs/execute-preview`.

## Implemented Tables

```text
noise_gate_evidence_links
report_evidence_links
report_noise_gate_links
```

Migration:

```text
db/migrations/023_workflow_stage_links.sql
```

Fresh DB schema:

```text
db/init/001_schema.sql
```

## API Surface

`GET /workflow-runs/{id}/lineage` now includes:

```text
direct_stage_links
summary.direct_stage_link_count
warning_codes: direct_stage_link_table
```

For a one-evidence workflow preview, the expected direct stage link count is:

```text
direct_stage_link_count: 3
```

The shared persistence boundary is:

```text
workflow_created_records_only_not_standalone_payload_lineage
```

## Boundary

This is local deterministic workflow lineage only.

It covers workflow-created records from `POST /workflow-runs/execute-preview`.

Standalone gate/report endpoints remain payload-only unless they create explicit stage links.

It is not distributed tracing, hosted observability, autonomous workflow execution, LLM-backed report generation, evidence quality proof, hosted deployment evidence, external reviewer feedback, or product-complete.

## Verification

```text
uv run pytest -q tests/test_routes.py::test_workflow_lineage_exposes_direct_stage_links_for_workflow_created_records
uv run pytest -q tests/test_docs.py::test_workflow_direct_stage_links_docs_and_schema_are_inspectable
```

## Honest Claim

NoiseProof now records direct local stage-link rows for deterministic workflow-created records:

```text
Evidence Ledger row -> Noise Gate record
Evidence Ledger row -> Report record
Noise Gate record -> Report record
```

This improves inspectability of the local workflow proof path without claiming production RAG quality, distributed tracing, hosted deployment evidence, or autonomous agent behavior.
