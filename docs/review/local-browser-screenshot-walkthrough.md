# Local Browser Screenshot Walkthrough

Status: self-authored local browser screenshot gate.

Phase marker: local browser screenshot walkthrough v0.

Label: Local browser screenshot walkthrough.

This artifact records a local browser capture of the current operations dashboard after a deterministic workflow preview created persisted retrieval, evidence, gate, report, and workflow-run records.

Screenshot:

```text
docs/review/media/local-browser-dashboard-walkthrough.png
```

The goal is not to make a design claim. The goal is to show that a reviewer can visually inspect the local operations surface and follow a workflow run into its lineage read model.

## Capture Method

Runtime context:

```text
docker compose up -d db
python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
uv run uvicorn app.main:create_app --factory --host 127.0.0.1 --port 8000
```

Browser capture:

```text
GET /ops/dashboard
```

The browser screenshot was captured from the local FastAPI HTML dashboard at:

```text
http://127.0.0.1:8000/ops/dashboard
```

Before the screenshot, a deterministic workflow preview was created for:

```text
Which segment had enterprise demand growth and what evidence supports it?
```

Captured workflow id:

```text
69074111-d029-4970-abae-7edb75484165
```

Lineage route:

```text
GET /workflow-runs/{id}/lineage
```

Observed dashboard check:

```text
status_code: 200
contains_workflow_runs: true
contains_lineage_link: true
contains_workflow_id: true
```

The screenshot file size was above the documentation threshold used by `apps/api/tests/test_docs.py`, which guards against empty or placeholder image artifacts.

## What The Screenshot Shows

The captured dashboard includes:

- summary counts for documents, agent runs, failure cases, evidence ledger records, generated reports, and gate outcomes
- trace/filter links for evidence, gate, and report records
- recent agent runs
- failure cases
- workflow runs with `detail` and `lineage` links
- retrieval runs
- evidence ledger records
- Noise Gate records
- report records
- dashboard boundary text

This is useful because it gives a reviewer a single visual proof surface for the current local operating model:

```text
workflow run -> retrieval records -> evidence ledger records -> Noise Gate records -> report records -> lineage link
```

## Allowed Claim

NoiseProof Agent has a self-authored local browser screenshot walkthrough showing that the current local operations dashboard renders workflow runs and lineage links after a deterministic workflow preview.

## Boundary

This is local browser evidence only.

This is not hosted deployment evidence.

This is not customer validation.

This is not external reviewer feedback.

This is not production observability.

This is not design quality evidence.

This is not semantic retrieval evidence.

This is not LLM evidence.

This is not market prediction quality evidence.

This is not Braincrew acceptance.

## Next Gate

The next evidence gate should reduce self-authored proof and introduce outside judgment:

```text
external reviewer feedback v0
```
