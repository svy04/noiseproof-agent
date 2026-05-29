# NoiseProof Agent API

FastAPI skeleton for NoiseProof Agent.

Implemented in this package:

- `GET /health`
- `GET /ops/summary`
- `POST /documents`
- `GET /documents`
- `POST /documents/profile`
- `POST /documents/parse-preview`
- `POST /documents/chunk-preview`
- `POST /collection-plans/preview`
- `POST /retrieval-runs`
- `GET /retrieval-runs`
- `POST /evidence-ledgers/preview`
- `POST /evidence-ledgers`
- `GET /evidence-ledgers`
- `POST /noise-gates/preview`
- `POST /noise-gates`
- `GET /noise-gates`
- `POST /reports/preview`
- `POST /reports`
- `GET /reports`
- `GET /traces/{workflow_trace_id}`
- `POST /agent-runs`
- `GET /agent-runs`
- `POST /workflow-runs`
- `GET /workflow-runs`
- `POST /failure-cases`
- `GET /failure-cases`

Phase 11 auto-records `agent_runs.trace_json` metadata for the document/profile, parse, chunk, collection-plan, evidence-ledger, noise-gate, and report preview endpoints.
Phase 15 adds `workflow_trace_id` linkage for persisted evidence, gate, and report endpoints.
Phase 16 adds direct trace-id lookup for persisted records and matching agent-run traces.
Phase 17 adds read-only query filters for persisted evidence, gate, and report lists.
Phase 18 adds trace lookup and filter links to the plain operations dashboard.
Phase 19 changes preview/persistence tracing to create a parent `agent_runs` row before operation execution, then update the same row to completed or failed.
Phase 20 stores the parent `agent_run_id` on persisted Evidence Ledger, Noise Gate, and Report records.
Phase 21 exposes parent run links for persisted Noise Gate and Report records in the plain operations dashboard.
Phase 22 exposes persisted Evidence Ledger rows in the plain operations dashboard.
Phase 25 adds create/list metadata persistence for `workflow_runs`, without workflow orchestration or child `workflow_run_id` links.

Not implemented yet:

- file upload
- robust PDF extraction
- persisted parse records
- persisted chunks
- persisted collection plans
- workflow execution endpoints
- child workflow_run_id links
- embeddings
- distributed tracing or hosted observability

## Local Run

From repo root:

```bash
docker compose up -d db
cd apps/api
uv sync
uv run uvicorn app.main:app --reload
```

Smoke checks:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/ops/summary
curl -X POST http://localhost:8000/documents/profile \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"text\":\"# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.\"}"
curl -X POST http://localhost:8000/documents/parse-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"pdf\",\"content\":\"Extracted PDF text preview only.\"}"
curl -X POST http://localhost:8000/documents/chunk-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"csv\",\"content\":\"date,segment,growth\n2026-05-28,enterprise,12%\n2026-05-29,smb,7%\",\"max_characters\":60}"
curl -X POST http://localhost:8000/retrieval-runs \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"strategy\":\"heading-aware\",\"sources\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"content\":\"# Demand\nEnterprise demand grew 12% in 2026.\"}]}"
curl -X POST http://localhost:8000/collection-plans/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Did this company's AI narrative become materially stronger?\"}"
curl -X POST http://localhost:8000/evidence-ledgers/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"retrieval_results\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"chunk_strategy\":\"heading-aware\",\"chunk_index\":0,\"text\":\"Enterprise demand grew 12% in 2026.\",\"score\":0.75,\"matched_terms\":[\"demand\",\"enterprise\",\"growth\"],\"metadata\":{\"source_date\":\"2026-05-28\"}}]}"
curl -X POST http://localhost:8000/noise-gates/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl -X POST http://localhost:8000/reports/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl -X POST http://localhost:8000/reports \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl http://localhost:8000/reports
curl http://localhost:8000/ops/dashboard
curl "http://localhost:8000/evidence-ledgers?workflow_trace_id=<uuid>"
curl "http://localhost:8000/evidence-ledgers?status=blocked"
curl "http://localhost:8000/noise-gates?workflow_trace_id=<uuid>"
curl "http://localhost:8000/noise-gates?decision=blocked"
curl "http://localhost:8000/reports?workflow_trace_id=<uuid>"
curl "http://localhost:8000/reports?status=generated"
curl "http://localhost:8000/traces/<uuid>"
curl -X POST http://localhost:8000/workflow-runs \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which sources disagree about memory demand?\",\"trace_json\":{\"phase\":\"metadata-only\"}}"
curl http://localhost:8000/workflow-runs
```

The PDF parser is currently a text-only fallback. Robust PDF extraction is not claimed.
Collection Plan Preview is deterministic and does not call LLMs, search external sources, expand retrieval, create an Evidence Ledger by itself, or persist records.
Evidence Ledger Preview is deterministic and does not call LLMs, search external sources, run a Critic / Noise Gate, or create a final report. `POST /evidence-ledgers` persists the generated preview entries as v0 ledger records.
Noise Gate Preview is deterministic and does not call LLMs, create a final report, or build a dashboard.
`POST /noise-gates` persists the deterministic gate decision as a v0 Noise Gate record with local parent `agent_run_id` provenance. It does not create a final report.
Report Preview is deterministic and does not call LLMs. `POST /reports` persists the deterministic preview output as a v0 Report record; it does not create a free-form final report.
Persisted evidence, gate, and report records include `workflow_trace_id`, which also appears in the matching `agent_runs.trace_json`; persisted evidence, gate, and report rows are linked back to their parent run from the dashboard.
Operations Dashboard v0 is a plain FastAPI HTML view over current metadata. It now links to trace lookup, record filters, parent run provenance, and persisted Evidence Ledger rows, but it is still not a polished product UI.
Auto Trace Recording v0 is metadata tracing for preview endpoints, not distributed tracing or hosted observability.
WorkflowRun Metadata Persistence v0 is create/list metadata storage only. It does not execute a workflow, attach child records to `workflow_run_id`, or create evidence -> gate -> report cross-links.
