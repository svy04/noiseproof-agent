# Portfolio Index

Status: Phase 10 application artifact.

This page maps the repository into a reviewer-readable path.

## Start Here

1. `README.md`
2. `docs/product-brief.md`
3. `docs/architecture.md`
4. `docs/runbook.md`
5. `docs/application/braincrew-role-map.md`

## Implementation Artifacts

| Area | Artifact | Status |
|---|---|---|
| API service | `apps/api/app/main.py` | implemented |
| Metadata persistence | `apps/api/app/db.py` and `db/init/001_schema.sql` | implemented |
| Profiler | `packages/ingestion/profiler.py` | implemented |
| Parser boundaries | `packages/ingestion/parsers/*` | implemented |
| Chunking | `packages/ingestion/chunking/experiment.py` | implemented |
| Retrieval | `packages/ingestion/retrieval/lexical.py` | implemented |
| Collection plan | `packages/ingestion/collection/planner.py` | implemented |
| Evidence Ledger preview | `packages/ingestion/evidence/ledger.py` | implemented |
| Noise Gate preview | `packages/ingestion/noise_gate/gate.py` | implemented |
| Report preview | `packages/ingestion/reports/report.py` | implemented |
| Operations dashboard | `GET /ops/dashboard` | implemented |

## Verification Artifacts

| Artifact | Purpose |
|---|---|
| `apps/api/tests/test_routes.py` | API and workflow boundary tests |
| `apps/api/tests/test_docs.py` | Phase 10 documentation artifact tests |
| `.github/workflows/ci.yml` | CI smoke and tests |
| `docs/evaluation/eval-plan.md` | evaluation plan |
| `docs/evaluation/retrieval-eval-report.md` | current retrieval boundary report |
| `docs/evaluation/failure-cases.md` | failure case ledger |

## What Not To Claim

- production RAG quality
- robust PDF extraction
- semantic retrieval
- external customer validation
- financial prediction quality
- trading advice
- Product Engineer-level production ownership

## Current Best Claim

NoiseProof Agent is a small, inspectable data-agent portfolio project that shows how unsupported claims can be blocked before report output.
