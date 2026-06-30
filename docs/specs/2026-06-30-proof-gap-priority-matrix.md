# Proof Gap Priority Matrix Spec

title: Proof gap priority matrix

status: implemented

date: 2026-06-30

target_gate: `proof_gap_priority_matrix_v0`

## current_repo_state

NoiseProof now has:

- `docs/MASTER-SPEC.md` as the source-first operating constitution.
- `docs/research/source-assimilation-registry.md` as the current source-card
  registry.
- `GET /ops/proof-gaps` and `GET /ops/proof-gaps/{gap_id}` as proof gap action
  surfaces.
- many proof routes for PDF quality, semantic retrieval, local OTel spans,
  external-reader routing, and current issue-state screening.

The remaining high-level gaps still include `external_reviewer_feedback`,
`robust_pdf_extraction`, `semantic_retrieval_quality`,
`actual_embedding_generation`, `hosted_deployment`, `hosted_observability`, and
`distributed_tracing`.

## sources_to_absorb

Use the existing cards in `docs/research/source-assimilation-registry.md`:

- W3C PROV-DM
- SLSA Provenance
- OpenTelemetry
- RAGAS
- ALCE
- BEIR and trec_eval
- Model Cards
- Datasheets for Datasets
- Diataxis
- Docling and Unstructured
- US20260105079A1
- US10628389B2

No new source card is required for this gate because the work is a bounded
prioritization layer over the already-assimilated source registry.

## non_goals

- Do not implement retrieval.
- Do not implement embeddings.
- Do not implement Evidence Ledger changes.
- Do not implement Critic, Noise Gate, report generation, dashboard, or hosted
  deployment behavior.
- Do not claim external reviewer feedback.
- Do not claim robust PDF extraction or semantic retrieval quality.
- Do not edit public issue bodies.

## implementation_scope

Create:

- `docs/research/proof-gap-priority-matrix.md`
- `docs/review/proof-gap-priority-matrix.md`
- `apps/api/tests/test_proof_gap_priority_matrix.py`

Update:

- `docs/MASTER-SPEC.md`
- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`

## data_or_api_contract

No data model, API, or runtime behavior changes.

The matrix is a documentation contract with these required fields:

```text
phase_marker
source_basis
scoring_rule
current_matrix
selection_result
boundaries
```

The selection result must distinguish:

```text
highest-trust evidence gate: external_reviewer_feedback_v0
next local implementation gate: proof_gap_action_surface_current_state_refresh_v0
```

## tests

Add a documentation regression test that checks:

- the matrix, spec, review artifact, master spec, README, GOAL, runbook, and
  portfolio index all reference `proof_gap_priority_matrix_v0`;
- the canonical matrix path is linked;
- all current proof gap ids are listed;
- the source basis includes the current source-registry families;
- boundaries block product-complete, external-reviewer, hosted, robust-PDF, and
  semantic-quality claims;
- the next local gate is
  `proof_gap_action_surface_current_state_refresh_v0`.

## docs_to_update

Update the master operating loop and reviewer/application navigation so future
agents read this priority matrix before choosing another proof-reduction gate.

## stop_conditions

Stop before implementing runtime code if:

- the current proof gap registry and GOAL ledger disagree about the latest
  accepted gate;
- a selected gate requires external state such as a non-owner reviewer comment,
  owner API secrets, or a hosted target;
- the next step would imply robust extraction, semantic retrieval quality,
  hosted deployment, or external validation without evidence.

If stopped, report:

```text
planned_path:
actual_state:
blocking_mismatch:
why_this_blocks_the_gate:
minimum_action_to_resume:
```

## claim_boundaries

This gate is prioritization only. It is not new runtime evidence, not robust PDF
extraction evidence, not semantic retrieval quality evidence, not hosted
deployment evidence, not hosted observability evidence, not external reviewer
feedback, not customer validation, not Braincrew acceptance, and not
product-complete.

## next_gate_if_passed

Next recommended local gate:

```text
proof_gap_action_surface_current_state_refresh_v0
```

This next gate should refresh `apps/api/app/services/proof_gap_registry.py` and
the proof-gap action docs so the API's `recommended_next_gate` values match the
latest GOAL ledger and this matrix.
