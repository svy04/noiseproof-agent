# Failure-case workflow parent linkage schema review

## Status

Accepted.

This is a review-only gate. It adds no schema, migration, runtime behavior, API behavior, dashboard rendering, or automatic failure-case creation.

## Question

If a reviewer confirms a failure-case draft produced from a failed workflow parent, should the durable `failure_cases` row be able to retain the originating workflow parent id?

## Decision

Yes, but only through an explicit schema gate.

The selected schema direction is:

```text
nullable workflow_run_id on failure_cases
```

The intended database shape is:

```sql
workflow_run_id UUID REFERENCES workflow_runs(id) ON DELETE SET NULL
```

The column must be nullable because existing failure cases can come from parser, ingestion, retrieval, manual review, or agent-run failures without a deterministic workflow parent.

## Alternatives considered

### Option A - Keep only agent_run_id on failure_cases

Rejected as the final shape.

`agent_run_id` is useful for operation-level linkage, but the current deterministic workflow parent is `workflow_runs`. A failure case produced from a failed workflow should be able to point to the workflow parent without overloading agent-run metadata.

### Option B - Add nullable workflow_run_id on failure_cases

Selected.

This keeps the relationship inspectable while preserving old and non-workflow failure cases. It also matches the project pattern already used for workflow-created retrieval, evidence, gate, and report child records.

### Option C - Use a generic source_id/source_type pair

Rejected for now.

A generic polymorphic reference would be flexible, but weaker for inspection and harder to validate with simple SQL and API tests.

### Option D - Auto-create failure cases with workflow_run_id during workflow failure

Rejected for this gate.

automatic failure-case creation remains deferred until a human-confirmed creation path has been proven through API and database tests.

## Required future migration shape

The next implementation gate should add:

```sql
ALTER TABLE failure_cases
  ADD COLUMN IF NOT EXISTS workflow_run_id UUID REFERENCES workflow_runs(id) ON DELETE SET NULL;

CREATE INDEX IF NOT EXISTS idx_failure_cases_workflow_run_id
  ON failure_cases(workflow_run_id);
```

The fresh init schema and migration set must stay aligned.

## Required API boundary

The future API update should allow manual failure-case creation with an optional `workflow_run_id`.

It must not automatically create failure cases from workflow failures.

It must not imply that `workflow_run_id` proves complete workflow failure causality. It proves only that the failure-case record has an explicit workflow-parent reference supplied through a supported persistence path.

## Claim boundary

Allowed claim after this review:

```text
The selected schema direction is a nullable workflow_run_id on failure_cases, but no migration is added in this review gate.
```

Forbidden claims after this review:

```text
failure_cases already have workflow_run_id.
workflow failures automatically create failure cases.
workflow_run_id proves complete workflow failure causality.
the project has production incident classification.
```

## Next bounded gate

The next bounded gate should be:

```text
failure-case workflow parent linkage schema v0
```

That gate should add the nullable column, update init SQL and migrations, update schemas/repository persistence, and test manual creation/listing with workflow parent linkage.
