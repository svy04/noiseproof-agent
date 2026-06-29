# Source Assimilation Registry v0

Status: implemented in this branch.
Date: 2026-06-30
Target gate: `source_assimilation_registry_v0`

## Current Repo State

`docs/MASTER-SPEC.md` defines a source-first doctrine and a source-card shape,
but the repository does not yet have one registry where future agents can see
which primary sources, papers, standards, maintained projects, and patents have
already been absorbed into the product vision.

Without a registry, future gates can still cite impressive sources without
recording what is actually borrowed, what is rejected, and what cannot be
claimed.

## Sources To Absorb

| Source | Local use |
|---|---|
| W3C PROV-DM | provenance model for source/retrieval/claim/report lineage |
| SLSA Provenance | subject, materials, invocation, and byproduct metadata discipline |
| OpenTelemetry specification | traces/logs/metrics/context separation |
| RAGAS | multi-surface RAG evaluation framing |
| ALCE | citation quality as a separate evaluation surface |
| BEIR and trec_eval | qrels/run/metric-shaped retrieval evaluation |
| Model Cards | capability, limitation, intended-use, and metric disclosure pattern |
| Datasheets for Datasets | fixture/source collection transparency |
| Diataxis | reader path/reference/explanation separation |
| Docling and Unstructured | document element/parsing capability separation |
| US20260105079A1 | RAG transparency/source-span linkage pattern, patent boundary preserved |
| US10628389B2 | provenance verification around non-native systems, patent boundary preserved |

## Non-goals

- no runtime implementation
- no API behavior change
- no new benchmark claim
- no new external validation
- no patent implementation claim
- no product-complete claim

## Implementation Scope

Create:

```text
docs/research/source-assimilation-registry.md
docs/review/source-assimilation-registry.md
apps/api/tests/test_source_assimilation_registry.py
```

Update:

```text
docs/MASTER-SPEC.md
README.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
```

## Data Or API Contract

No data model, API, or runtime behavior changes.

## Tests

Run:

```powershell
cd apps/api
uv run pytest tests/test_source_assimilation_registry.py -q
uv run pytest tests/test_current_state_reconciliation_after_master_spec.py tests/test_master_spec_operating_loop.py -q
uv run python -m compileall app ../../packages/ingestion
```

If time allows:

```powershell
uv run pytest -q
```

## Docs To Update

- MASTER-SPEC: point future gates to the source assimilation registry.
- README: expose the registry as a current operating surface.
- GOAL: include the registry in the read order.
- Runbook: include the registry in the gate-start checklist.
- Portfolio index: expose the registry for reviewers.

## Stop Conditions

Stop if:

- the registry implies source adoption proves implementation maturity
- the patent cards read like permission to copy protected claims
- tests show the registry is not reachable from master spec/read path surfaces
- the gate starts changing runtime behavior

## Claim Boundaries

Implemented:

- a source assimilation registry with structured source cards
- a review artifact for the registry gate
- tests that keep the registry linked from master spec/read path surfaces

Not implemented:

- any new runtime capability
- any new source adapter
- any new benchmark
- any patent-derived implementation
- any external validation

Can claim:

- Future gates now have a documented source-card registry for primary-source assimilation.

Cannot claim:

- NoiseProof implements every referenced paper, standard, or patent.
- NoiseProof is benchmarked against RAGAS, ALCE, BEIR, or trec_eval.
- NoiseProof has legal clearance to implement patent claims.
- NoiseProof is product-complete.

## Next Gate If Passed

Return to the reconciled current-state sources and choose the next evidence
gate. A strong next candidate is a proof-gap priority spec that uses the source
registry to rank external reviewer feedback, robust PDF extraction evidence,
production semantic retrieval quality, hosted deployment, and hosted
observability.
