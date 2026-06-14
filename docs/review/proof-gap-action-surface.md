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

For `semantic_retrieval_quality`, the action surface keeps the gap open. After
Phase 866, the gap has a local representative fixture covering all current
NoiseProof information roles and source types, plus an owner-runtime packet and
validator for a future live embedding-backed domain qrels run. The current
accepted evidence still does not include live embedding generation and does not
prove production semantic retrieval quality:

```text
status -> unproven
claim_boundary -> representative_local_fixture_and_caller_provided_vectors_do_not_prove_production_semantic_retrieval_quality
acceptable_evidence -> run a live embedding-backed domain qrels quality evaluation beyond caller-provided fixture vectors
blocked_claims -> semantic retrieval quality is proven
recommended_next_gate -> owner_runtime_live_embedding_domain_qrels_eval_v0
proof_routes -> docs/review/live-embedding-domain-qrels-owner-runtime-eval-packet.md; docs/evaluation/representative-live-semantic-quality-report.md; docs/evaluation/live-semantic-qrels-baseline-report.md; docs/evaluation/live-lexical-qrels-baseline-report.md; docs/evaluation/qrels-backed-semantic-quality-report.md
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
next actual gap-reduction gate selected from this action surface. The most
direct next product gate after Phase 864 is:

```text
owner_runtime_live_embedding_domain_qrels_eval_v0
```
