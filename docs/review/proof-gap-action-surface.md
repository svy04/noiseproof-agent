# Proof Gap Action Surface

Phase 858 adds proof gap action surface v0.

Phase `proof_gap_action_surface_current_state_refresh_v0` refreshes the same
surface after `proof_gap_priority_matrix_v0`.

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

## Current-state Refresh

After `proof_gap_priority_matrix_v0`, the action surface now separates:

```text
highest-trust evidence gate -> external_reviewer_feedback_v0
next local implementation gate -> proof_gap_action_surface_current_state_refresh_v0
next robust PDF local product gate -> real_world_table_extraction_evidence_gate_v0
```

For `robust_pdf_extraction`, the action surface no longer points at
`multi_real_world_pdf_parse_observation_matrix_remote_verification_v0` as the
next gate, because that remote workflow verification is already represented in
the current GOAL ledger and proof routes. It is now part of current evidence and
proof routing:

```text
current_evidence -> ...plus_multi_real_world_pdf_parse_observation_matrix_remote_verification_v0
proof_routes -> docs/review/multi-real-world-pdf-parse-observation-remote-verification.md
recommended_next_gate -> real_world_table_extraction_evidence_gate_v0
```

This refresh does not close the robust PDF gap.

After `robust_pdf_extraction_next_real_world_quality_gate_v0`, the action
surface includes:

```text
current_evidence -> ...plus_robust_pdf_extraction_next_real_world_quality_gate_v0
proof_routes -> docs/review/robust-pdf-extraction-next-real-world-quality-gate.md
proof_routes -> docs/evaluation/robust-pdf-real-world-quality-gate-report.md
recommended_next_gate -> cross_publisher_real_world_pdf_fixture_gate_v0
```

The robust-PDF quality gate is blocked because the current real-world matrix has
one publisher family only and no table extraction, OCR, or layout fidelity
evidence.

After `cross_publisher_real_world_pdf_fixture_gate_v0`, the action surface
includes:

```text
current_evidence -> ...plus_cross_publisher_real_world_pdf_fixture_gate_v0
proof_routes -> docs/review/cross-publisher-real-world-pdf-fixture-gate.md
proof_routes -> docs/evaluation/cross-publisher-real-world-pdf-fixture-gate-report.md
recommended_next_gate -> real_world_table_extraction_evidence_gate_v0
```

The cross-publisher fixture gate reduces the publisher-family blocker, but the
robust-PDF gap remains open because table extraction, OCR, and layout fidelity
evidence are still missing.

## Semantic Retrieval Quality Example

For `semantic_retrieval_quality`, the action surface keeps the gap open. After
Phase 866, the gap has a local representative fixture covering all current
NoiseProof information roles and source types, plus an owner-runtime packet,
runner, and validator for a future live embedding-backed domain qrels run. The current
accepted evidence still does not include live embedding generation and does not
prove production semantic retrieval quality:

```text
status -> unproven
claim_boundary -> representative_local_fixture_and_caller_provided_vectors_do_not_prove_production_semantic_retrieval_quality
acceptable_evidence -> run a live embedding-backed domain qrels quality evaluation beyond caller-provided fixture vectors
blocked_claims -> semantic retrieval quality is proven
recommended_next_gate -> owner_runtime_live_embedding_domain_qrels_eval_v0
proof_routes -> docs/review/live-embedding-domain-qrels-owner-runtime-runner.md; docs/review/live-embedding-domain-qrels-owner-runtime-eval-packet.md; docs/evaluation/representative-live-semantic-quality-report.md; docs/evaluation/live-semantic-qrels-baseline-report.md; docs/evaluation/live-lexical-qrels-baseline-report.md; docs/evaluation/qrels-backed-semantic-quality-report.md
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

Next recommended local product gate after this current-state refresh:

```text
real_world_table_extraction_evidence_gate_v0
```

If real-world fixture inputs are unavailable, stop and record the planned path,
actual state, blocking mismatch, why it blocks, and the minimum action to
resume before selecting another gate.
