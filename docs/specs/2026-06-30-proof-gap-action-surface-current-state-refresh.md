# Proof Gap Action Surface Current-state Refresh Spec

title: Proof gap action surface current-state refresh

status: implemented

date: 2026-06-30

target_gate: `proof_gap_action_surface_current_state_refresh_v0`

## current_repo_state

`proof_gap_priority_matrix_v0` is now the current prioritization gate. It keeps
`external_reviewer_feedback_v0` as the highest-trust evidence gap, but selects
`proof_gap_action_surface_current_state_refresh_v0` as the next local
implementation gate because external reviewer feedback cannot be self-completed.

The current `GET /ops/proof-gaps` action surface is useful, but
`robust_pdf_extraction.recommended_next_gate` still points at
`multi_real_world_pdf_parse_observation_matrix_remote_verification_v0`. That
remote verification is already represented in the current GOAL ledger and
reviewer route. The action surface should now point to the next local
gap-reduction gate instead of a completed remote-verification step.

## sources_to_absorb

Use the already-assimilated source cards in
`docs/research/source-assimilation-registry.md` and the ranking decision in
`docs/research/proof-gap-priority-matrix.md`.

No new source card is required because this gate is a current-state refresh over
existing proof-gap action metadata.

Relevant source patterns:

- Model Cards: keep public capability status, caveats, and next evidence visible.
- Datasheets for Datasets: keep real-world fixture source policy and omissions
  visible before stronger PDF claims.
- Docling and Unstructured: keep PDF digital text, tables, OCR, layout, and
  typed-element quality separate.
- SLSA Provenance: proof routes should point at the current subject, observed
  artifacts, and verification result.
- Diataxis: reviewer-facing paths, API references, and runbook notes should not
  drift apart.

## non_goals

- Do not implement PDF parsing, OCR, table extraction, embeddings, retrieval,
  Evidence Ledger behavior, Critic / Noise Gate behavior, reports, dashboard, or
  hosted deployment.
- Do not claim robust PDF extraction.
- Do not claim semantic retrieval quality.
- Do not claim external reviewer feedback.
- Do not edit GitHub issue bodies.
- Do not run external provider calls or require secrets.

## implementation_scope

Update:

- `apps/api/app/services/proof_gap_registry.py`
- `apps/api/tests/test_routes.py`
- `apps/api/tests/test_docs.py`
- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/review/proof-gap-action-surface.md`

Create:

- `docs/review/proof-gap-action-surface-current-state-refresh.md`
- `apps/api/tests/test_proof_gap_action_surface_current_state_refresh.py`

## data_or_api_contract

No schema or endpoint changes.

Keep:

```text
GET /ops/proof-gaps
GET /ops/proof-gaps/{gap_id}
surface_boundary -> action_surface_only_not_new_proof_or_gap_closure
gap_count -> 7
```

Refresh:

```text
robust_pdf_extraction.current_evidence includes multi_real_world_pdf_parse_observation_matrix_remote_verification_v0
robust_pdf_extraction.proof_routes includes docs/review/multi-real-world-pdf-parse-observation-remote-verification.md
robust_pdf_extraction.recommended_next_gate -> robust_pdf_extraction_next_real_world_quality_gate_v0
robust_pdf_extraction.next_evidence_needed -> robust_pdf_extraction_next_real_world_quality_gate_v0
```

Keep external state blocked:

```text
external_reviewer_feedback.recommended_next_gate -> external_reviewer_feedback_v0
external_reviewer_feedback.status -> pending
```

## tests

Write a RED test first that proves the current action surface is stale:

```text
uv run pytest tests/test_proof_gap_action_surface_current_state_refresh.py -q
```

Expected before implementation:

```text
FAIL because robust_pdf_extraction still points to multi_real_world_pdf_parse_observation_matrix_remote_verification_v0
```

Then update implementation and docs until the focused test and existing route
tests pass.

## docs_to_update

Update the action-surface review doc and top-level navigation surfaces so future
agents see this as a metadata/current-state refresh only.

## stop_conditions

Stop if:

- the current GOAL ledger contradicts the priority matrix about the next local
  gate;
- a claimed next gate would require external reviewer feedback, owner API
  secrets, or a hosted target;
- the change would make robust PDF extraction, semantic retrieval quality,
  hosted deployment, hosted observability, or external validation sound closed.

If stopped, report:

```text
planned_path:
actual_state:
blocking_mismatch:
why_this_blocks_the_gate:
minimum_action_to_resume:
```

## claim_boundaries

This gate is action-surface current-state metadata only.

It is not new runtime evidence, not robust PDF extraction evidence, not live
embedding generation proof, not semantic retrieval quality evidence, not hosted
deployment evidence, not hosted observability evidence, not distributed tracing
evidence, not external reviewer feedback, not customer validation, not
Braincrew acceptance, and not product-complete.

## next_gate_if_passed

Next local product gate candidate:

```text
robust_pdf_extraction_next_real_world_quality_gate_v0
```

If the required real-world fixture inputs are unavailable, stop and record the
blocking mismatch before selecting a different local gate.
