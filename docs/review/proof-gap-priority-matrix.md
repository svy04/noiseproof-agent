# Proof Gap Priority Matrix Review

Phase `proof_gap_priority_matrix_v0` adds a source-backed priority matrix for
choosing the next NoiseProof proof gate.

## What Changed

Added:

- `docs/research/proof-gap-priority-matrix.md`
- `docs/specs/2026-06-30-proof-gap-priority-matrix.md`
- `apps/api/tests/test_proof_gap_priority_matrix.py`

Updated navigation surfaces:

- `docs/MASTER-SPEC.md`
- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`

## Decision

The matrix separates two questions:

```text
What evidence would most increase trust?
What can be advanced locally without pretending external state exists?
```

Current highest-trust evidence gate:

```text
external_reviewer_feedback_v0
```

Current next local implementation gate:

```text
proof_gap_action_surface_current_state_refresh_v0
```

The local gate comes next because the action surface can drift behind the GOAL
ledger and portfolio surfaces. Before adding another product proof, the API and
docs should agree on each gap's recommended next evidence.

## Current Priority Order

```text
1. external_reviewer_feedback
2. robust_pdf_extraction
3. semantic_retrieval_quality
4. actual_embedding_generation
5. hosted_deployment
6. hosted_observability
7. distributed_tracing
```

External reviewer feedback ranks first, but it cannot be self-authored.

## Boundary

This is a prioritization and documentation gate only.

Boundaries:

- not new runtime evidence
- not robust PDF extraction evidence
- not live embedding generation proof
- not semantic retrieval quality evidence
- not hosted deployment evidence
- not hosted observability evidence
- not distributed tracing evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance
- not product-complete

## Verification

Local focused tests:

```text
uv run pytest tests/test_proof_gap_priority_matrix.py -q
```

Observed result:

```text
1 passed
```

Regression tests:

```text
uv run pytest tests/test_source_assimilation_registry.py tests/test_current_state_reconciliation_after_master_spec.py tests/test_master_spec_operating_loop.py tests/test_proof_gap_priority_matrix.py -q
```

Observed result:

```text
4 passed
```

Full local verification:

```text
uv run python -m compileall app ../../packages/ingestion
uv run pytest -q
```

Observed result:

```text
compileall completed
1277 passed in 105.74s
```

## Next Gate

Next recommended local gate:

```text
proof_gap_action_surface_current_state_refresh_v0
```

Do not use this matrix to claim that any proof gap is closed.
