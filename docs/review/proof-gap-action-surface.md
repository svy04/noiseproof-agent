# Proof Gap Action Surface

Phase 858 adds proof gap action surface v0.

## What Changed

NoiseProof already exposed a read-only proof gap registry through:

```text
GET /ops/summary
GET /ops/dashboard
```

This phase adds two narrower ops endpoints:

```text
GET /ops/proof-gaps
GET /ops/proof-gaps/{gap_id}
```

These endpoints return the current proof gaps plus action metadata:

```text
acceptable_evidence
blocked_claims
proof_routes
recommended_next_gate
action_boundary
```

## Current Gap Coverage

The surface covers:

```text
robust_pdf_extraction
actual_embedding_generation
semantic_retrieval_quality
distributed_tracing
hosted_observability
hosted_deployment
external_reviewer_feedback
```

## Semantic Retrieval Quality Example

For `semantic_retrieval_quality`, the action surface keeps the gap open:

```text
status -> unproven
claim_boundary -> caller_provided_vector_runs_are_operational_counts_not_quality_evidence
acceptable_evidence -> run a qrels-backed retrieval quality evaluation
blocked_claims -> semantic retrieval quality is proven
recommended_next_gate -> qrels_backed_semantic_retrieval_quality_eval_v0
proof_routes -> docs/review/semantic-retrieval-quality-diagnostic-matrix.md
```

## Boundary

This is `action_surface_only_not_new_proof_or_gap_closure`.

It is not robust PDF extraction evidence, not live embedding generation proof, not semantic retrieval quality evidence, not distributed tracing, not hosted observability, not hosted deployment evidence, not external reviewer feedback, not customer validation, not Braincrew acceptance, and not product-complete.

## Verification

Local focused tests:

```text
uv run pytest tests/test_routes.py::test_ops_proof_gap_action_surface_exposes_gap_details_without_closing_gap tests/test_routes.py::test_ops_proof_gap_action_surface_returns_404_for_unknown_gap -q
```

Observed result:

```text
2 passed
```

## Next Gate

Next recommended gate: either remote workflow verification after push, or the
first actual gap-reduction gate selected from this action surface. The most
direct next product gate is:

```text
qrels_backed_semantic_retrieval_quality_eval_v0
```
