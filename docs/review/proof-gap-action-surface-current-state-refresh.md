# Proof Gap Action Surface Current-state Refresh

Phase `proof_gap_action_surface_current_state_refresh_v0` refreshes the
existing proof gap action surface after `proof_gap_priority_matrix_v0`.

## What Changed

Updated:

- `apps/api/app/services/proof_gap_registry.py`
- `apps/api/tests/test_routes.py`
- `apps/api/tests/test_proof_gap_action_surface_current_state_refresh.py`
- `docs/review/proof-gap-action-surface.md`
- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`

## Decision

The priority matrix ranked `external_reviewer_feedback` first, but that gate
cannot be self-completed. The next local action was therefore to refresh the
action surface so the API no longer points at stale evidence gates.

For `robust_pdf_extraction`, the action surface now treats the multi real-world
PDF parse observation matrix remote verification as current routed evidence:

```text
current_evidence -> ...plus_multi_real_world_pdf_parse_observation_matrix_remote_verification_v0
proof_routes -> docs/review/multi-real-world-pdf-parse-observation-remote-verification.md
```

The next local product gate is now:

```text
robust_pdf_extraction_next_real_world_quality_gate_v0
```

## Boundary

This is action-surface current-state metadata only.

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

RED test before implementation:

```text
uv run pytest tests/test_proof_gap_action_surface_current_state_refresh.py -q
```

Observed result before implementation:

```text
2 failed
```

Focused tests after implementation:

```text
uv run pytest tests/test_proof_gap_action_surface_current_state_refresh.py -q
uv run pytest tests/test_routes.py::test_ops_proof_gap_action_surface_exposes_gap_details_without_closing_gap tests/test_routes.py::test_ops_proof_gap_action_surface_returns_404_for_unknown_gap tests/test_docs.py::test_proof_gap_action_surface_is_recorded_without_closing_gaps tests/test_proof_gap_priority_matrix.py tests/test_proof_gap_action_surface_current_state_refresh.py -q
```

Observed result after implementation:

```text
2 passed
6 passed
```

Full local verification:

```text
uv run python -m compileall app ../../packages/ingestion
uv run pytest -q
```

Observed result:

```text
compileall completed
1279 passed in 86.66s
```

## Next Gate

Next local product gate candidate:

```text
robust_pdf_extraction_next_real_world_quality_gate_v0
```

Do not use this refresh to claim robust PDF extraction.
