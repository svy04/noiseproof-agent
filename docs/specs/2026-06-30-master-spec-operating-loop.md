# Master Spec Operating Loop v0

Status: implemented in this branch.
Date: 2026-06-30
Target gate: `master_spec_operating_loop_v0`

## Current Repo State

The repository already has a large `docs/GOAL.md`, a proof-bounded README,
application and review artifacts, API/runtime tests, and many phase-specific
proof notes.

The missing operating surface is a stable master spec that future agents must
read before choosing and implementing the next gate.

## Sources To Absorb

| Source | Local use |
|---|---|
| W3C PROV-DM | Keep evidence and workflow lineage modeled as provenance records. |
| SLSA Provenance | Treat run inputs, dependencies, byproducts, and verification metadata as first-class proof. |
| OpenTelemetry | Keep traces, logs, metrics, and context propagation conceptually separated. |
| RAGAS, ALCE, BEIR, trec_eval | Keep retrieval, citation, and answer support metrics separated. |
| Model Cards and Datasheets for Datasets | Keep capability claims and dataset/fixture claims bounded. |
| Docling, Unstructured, PyMuPDF/OCR tooling | Keep document parsing capability boundaries split by modality. |
| Patent scans around RAG provenance and proof-of-provenance systems | Borrow general provenance/linkage/audit patterns only, without copying claims or implementations. |

## Non-goals

- no API behavior change
- no retrieval expansion
- no embeddings
- no Evidence Ledger behavior change
- no Critic / Noise Gate behavior change
- no final report behavior change
- no dashboard work
- no production-readiness claim

## Implementation Scope

Create:

```text
docs/MASTER-SPEC.md
docs/specs/README.md
docs/specs/2026-06-30-master-spec-operating-loop.md
apps/api/tests/test_master_spec_operating_loop.py
```

Update:

```text
README.md
docs/GOAL.md
docs/runbook.md
```

## Data Or API Contract

No data model or API contract changes.

## Tests

Run:

```powershell
cd apps/api
uv run pytest tests/test_master_spec_operating_loop.py -q
uv run python -m compileall app ../../packages/ingestion
```

If the full suite is feasible, run:

```powershell
uv run pytest -q
```

## Docs To Update

- README: add a short Master Spec Operating Loop pointer.
- GOAL: add read order that points to `docs/MASTER-SPEC.md`.
- Runbook: add the gate-start checklist.

## Stop Conditions

Stop if:

- `docs/GOAL.md` contradicts the master spec read-order rule
- a required source cannot be linked as a primary source
- tests show existing proof-surface expectations are broken
- this gate starts changing runtime behavior

## Claim Boundaries

Implemented:

- master spec operating loop documentation
- short-term spec folder and template rule
- test that checks the operating loop files and markers

Not implemented:

- new product capability
- new runtime proof
- new external validation
- new hosted deployment proof

Can claim:

- Future gates now have a documented master-spec-first loop.

Cannot claim:

- Product behavior improved.
- External reviewers accepted the proof packet.
- The system is production-ready.

## Next Gate If Passed

Return to `docs/GOAL.md` and choose the next highest-value implementation or
evidence gate. The current proof surface still points toward external reviewer
feedback and stronger robust-PDF/semantic-retrieval evidence gates; this
operating loop does not close those gaps.
