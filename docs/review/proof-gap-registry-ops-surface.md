# Proof Gap Registry Ops Surface

Status: implemented.

Phase marker: proof gap registry ops surface v0.

## Purpose

Make the current unproven claims inspectable from the runtime operations surface instead of leaving them only in prose.

This adds a read-only proof gap registry to:

```text
GET /ops/summary
GET /ops/dashboard
```

The registry lists current gaps only; not new proof.

## Runtime Surface

`GET /ops/summary` now includes `proof_gap_registry` entries for:

```text
robust_pdf_extraction
actual_embedding_generation
semantic_retrieval_quality
distributed_tracing
hosted_observability
hosted_deployment
external_reviewer_feedback
```

Each row includes:

```text
gap_id
status
current_evidence
claim_boundary
next_evidence_needed
```

Important current markers:

```text
external_reviewer_feedback.status -> pending
external_reviewer_feedback.current_evidence -> owner_authored_issue_only
external_reviewer_feedback.next_evidence_needed -> qualifying outside reviewer comment
semantic_retrieval_quality.claim_boundary -> caller_provided_vector_runs_are_operational_counts_not_quality_evidence
```

`GET /ops/dashboard` now renders a `Proof Gap Registry` table with the same gaps and the marker:

```text
current gaps only; not new proof
```

## Files Changed

```text
apps/api/app/schemas.py
apps/api/app/services/proof_gap_registry.py
apps/api/app/routes/ops.py
apps/api/app/services/ops_dashboard.py
apps/api/tests/test_routes.py
apps/api/tests/test_docs.py
README.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
docs/review/application-ready-review.md
```

## Boundary

This is an ops read-model surface only.

This is not robust PDF extraction evidence.

This is not live embedding generation proof.

This is not semantic retrieval quality evidence.

This is not distributed tracing.

This is not hosted observability.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.
