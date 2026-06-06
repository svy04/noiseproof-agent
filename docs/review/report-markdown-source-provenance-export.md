# Report Markdown Source Provenance Export

Status: implemented.

Phase marker: report markdown source provenance export v0.

## Purpose

Make persisted Report markdown exports show source retrieval provenance as a first-class review section.

Before this gate, `GET /reports/{report_record_id}/markdown` rendered the raw `Stage Input Manifest`, but a reviewer had to inspect implementation details to notice whether a report was downstream of a semantic persisted retrieval run. This gate keeps the deterministic export boundary and makes that provenance obvious.

## Implemented Surface

Endpoint:

```text
GET /reports/{report_record_id}/markdown
```

New markdown section:

```text
## Source Retrieval Provenance

- Source retrieval mode: semantic_persisted
- Source query vector source: caller_provided_vector
- Source is semantic retrieval run: true
- Source retrieval persistence boundary: semantic_retrieval_run_only_no_evidence_ledger
- Handoff performs semantic retrieval: false
```

## Evidence

Route-level test coverage now verifies the full local handoff:

```text
POST /documents/{document_id}/semantic-retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
POST /retrieval-runs/{retrieval_run_id}/noise-gate
POST /retrieval-runs/{retrieval_run_id}/report
GET /reports/{report_record_id}/markdown
```

The markdown export renders provenance from the persisted Report record's `stage_input_manifest`.

## Boundary

This is a deterministic read-surface improvement only.

This is not a new report-generation path.

This is not free-form report generation.

This is not an LLM call.

This is not retrieval execution.

This is not semantic retrieval quality evidence.

This is not embedding generation.

This is not Evidence Ledger quality evidence.

This is not Noise Gate quality evidence.

This is not report quality evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

## Next Gate

```text
local Docker/FastAPI runtime smoke for report markdown source provenance export if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
