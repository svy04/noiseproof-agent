# Report Markdown Local Inspection Paths

Status: implemented.

Phase marker: report markdown local inspection paths v0.

## Purpose

Make persisted report markdown easier to inspect by rendering local GET surfaces that a reviewer can use after seeing the stage input ids.

Before this gate, `GET /reports/{report_record_id}/markdown` showed `Stage Input Links` and the raw `Stage Input Manifest`, but a reviewer still had to know which local read endpoints existed. This gate adds a deterministic `Local Inspection Paths` section with the current report markdown URL, the current report workflow-trace filter, the trace lookup path, and list surfaces for retrieval runs, Evidence Ledger entries, and Noise Gate records.

## Implemented Surface

Endpoint:

```text
GET /reports/{report_record_id}/markdown
```

New markdown section:

```text
## Local Inspection Paths

- Current report markdown: /reports/{report_record_id}/markdown
- Current report record: /reports?workflow_trace_id={report_workflow_trace_id}
- Current workflow trace: /traces/{report_workflow_trace_id}
- Retrieval runs: /retrieval-runs (match retrieval run id above)
- Evidence Ledger entries: /evidence-ledgers (match Evidence Ledger entry ids above)
- Noise Gate records: /noise-gates (match Noise Gate record id above)
```

## Code Path

```text
apps/api/app/services/report_markdown.py
_render_local_inspection_paths()
```

## Test Coverage

```text
uv run --project apps/api pytest apps/api/tests/test_routes.py::test_semantic_retrieval_run_noise_gate_and_report_preserve_source_retrieval_provenance -q
```

RED:

```text
AssertionError: assert '## Local Inspection Paths' in markdown_export.text
```

GREEN:

```text
1 passed
```

## Boundary

This is deterministic markdown read-surface inspectability only.

It is not new record creation.

It is not new retrieval behavior.

It does not create Evidence Ledger rows.

It does not create Noise Gate records.

It does not generate new reports.

It does not call an LLM.

It does not generate embeddings.

It is not semantic retrieval quality evidence.

It is not Evidence Ledger quality evidence.

It is not Noise Gate quality evidence.

It is not report quality evidence.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.

## Next Gate

```text
local Docker/FastAPI runtime smoke for report markdown local inspection paths if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
