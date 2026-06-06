# Report Markdown Stage Input Links

Status: implemented.

Phase marker: report markdown stage input links v0.

## Purpose

Make persisted report markdown easier to inspect by rendering the local stage input ids that connect a report back to its retrieval run, Evidence Ledger entries, and Noise Gate record.

Before this gate, the raw `Stage Input Manifest` was already present in the markdown export. This gate adds a smaller human-readable `Stage Input Links` section so a reviewer can see the upstream local ids without parsing JSON-like manifest output.

## Implemented Surface

```text
GET /reports/{report_record_id}/markdown
## Stage Input Links
- Retrieval run id: {retrieval_run_id}
- Evidence Ledger entry id: {input_evidence_ledger_entry_id}
- Noise Gate record id: {input_noise_gate_record_id}
```

## Code Path

```text
apps/api/app/services/report_markdown.py
_render_stage_input_links()
```

## Test Coverage

```text
uv run --project apps/api pytest -q apps/api/tests/test_routes.py::test_semantic_retrieval_run_noise_gate_and_report_preserve_source_retrieval_provenance
```

RED:

```text
AssertionError: assert '## Stage Input Links' in markdown_export.text
```

GREEN:

```text
1 passed
```

## Boundary

This is deterministic markdown read-surface inspectability only.

This is not new retrieval.

It does not create new retrieval runs.

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
local Docker/FastAPI runtime smoke for report markdown stage input links if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
