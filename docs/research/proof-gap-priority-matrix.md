# Proof Gap Priority Matrix

Status: active prioritization policy.

Phase marker: `proof_gap_priority_matrix_v0`.

Canonical path: `docs/research/proof-gap-priority-matrix.md`.

This matrix ranks the current NoiseProof proof gaps before the next product or
evidence gate is selected. It does not close any gap. It exists because the
repository now has many proof surfaces, and the next gate should be chosen by
source-backed risk reduction instead of momentum.

## Source Basis

This matrix reuses the current source cards in
`docs/research/source-assimilation-registry.md`:

- W3C PROV-DM: prioritize gaps that make lineage between source, run, claim,
  and report more inspectable.
- SLSA Provenance: prefer proof packets that name subject, inputs, parameters,
  byproducts, and verification result.
- OpenTelemetry: keep local traces, distributed tracing, and hosted
  observability separate.
- RAGAS, ALCE, BEIR, and trec_eval: keep retrieval quality, citation support,
  answer support, and judged-query metrics separate.
- Model Cards and Datasheets for Datasets: public claims and fixture packs need
  intended use, caveats, source policy, and non-claims.
- Diataxis: separate reviewer route, runbook, explanation, and reference jobs.
- Docling and Unstructured: split PDF/document parsing into digital text,
  tables, OCR, layout, and typed-element quality.
- US20260105079A1 and US10628389B2: borrow the general pattern of source-span
  traceability and added provenance around systems that were not born with it;
  do not treat patent text as implementation permission.

## Scoring Rule

Scores use a 1-5 scale:

```text
reviewer_value: how much a serious reviewer would care
product_risk_reduction: how much the gap blocks the product thesis
source_basis_strength: how directly the source registry supports the next move
local_feasibility: how much can be advanced without external state
```

External-dependency gates can rank highest while still not being the next local
implementation gate. Do not fake, simulate, or self-author external evidence to
make them look complete.

## Current Matrix

| Rank | Gap | Current status | Reviewer value | Product risk reduction | Source basis strength | Local feasibility | Dependency | Priority call |
|---|---|---|---:|---:|---:|---:|---|---|
| 1 | `external_reviewer_feedback` | pending | 5 | 4 | 3 | 1 | qualifying outside reviewer comment | Highest trust gap, but cannot be self-completed. Keep request surfaces current; do not claim closure until a non-owner comment qualifies. |
| 2 | `robust_pdf_extraction` | unproven | 5 | 5 | 5 | 4 | broader real-world fixtures and parser-quality evidence | Highest local product-risk gap after feedback. Keep digital text, tables, OCR, layout, encrypted/no-text failures, and real-world source policy separate. |
| 3 | `semantic_retrieval_quality` | unproven | 5 | 5 | 5 | 3 | owner-runtime embeddings or representative judged runs | Core RAG quality gap. Advance only with qrels, run files, missed relevant chunks, unjudged retrieved count, and embedding provenance. |
| 4 | `actual_embedding_generation` | unproven | 4 | 4 | 4 | 2 | owner-provided provider secret | Needed before stronger semantic retrieval claims, but cannot require secrets in default CI. |
| 5 | `hosted_deployment` | not implemented | 4 | 3 | 3 | 3 | selected hosted target and secret boundary | Useful for reviewer access, but local runtime proof does not become hosted proof. |
| 6 | `hosted_observability` | not implemented | 4 | 3 | 4 | 2 | hosted runtime first | Logs, metrics, and traces matter after a hosted target exists. |
| 7 | `distributed_tracing` | not claimed | 3 | 2 | 4 | 2 | second service or external collector | Defer until there is a real cross-service boundary. Local spans are not distributed tracing. |

## Selection Result

Current highest-trust evidence gate:

```text
external_reviewer_feedback_v0
```

This remains pending until a qualifying outside reviewer comment exists.
Specifically, owner comments, issue-body edits, workflow screens, and
self-authored route refreshes do not close it.

Current next local implementation gate:

```text
proof_gap_action_surface_current_state_refresh_v0
```

Reason:

```text
The current proof gap action surface is useful, but its recommended next gates
can drift behind the GOAL ledger and portfolio surfaces. Before adding another
product proof, refresh the action surface so each gap's recommended next gate
matches the latest accepted state and this priority matrix.
```

After that refresh, the next local product gate should usually be one of:

```text
robust_pdf_extraction_next_real_world_quality_gate_v0
semantic_retrieval_quality_next_live_qrels_gate_v0
```

The final choice depends on which gate has executable inputs in the current
environment. If a gate requires external state that is unavailable, stop and
record the planned path, actual state, blocking mismatch, why it blocks, and the
minimum action to resume.

## Boundaries

This matrix is not new runtime evidence.

Boundaries:

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
