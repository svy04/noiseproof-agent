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
- `POST /workflow-runs/execute-preview`
- `GET /workflow-runs/{id}`
- `GET /workflow-runs/{id}/lineage`
- `POST /failure-cases`
- `GET /failure-cases`
- `GET /failure-cases/workflow-review-queue`

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
Phase 26 surfaces workflow-run metadata rows in the plain operations dashboard, labeled as metadata-only and not workflow execution.
Phase 28 adds a deterministic workflow execution preview that creates a workflow parent and runs retrieval -> evidence -> gate -> report preview steps, without child `workflow_run_id` columns.
Phase 29 adds nullable child `workflow_run_id` links for retrieval, evidence, gate, and report rows created by the deterministic workflow preview.
Phase 30 adds workflow-run detail lookup for inspecting child records attached to one workflow parent.
Phase 31 adds stage input manifests on deterministic workflow Noise Gate and Report records so downstream previews show persisted upstream ids they consumed.
Phase 32 adds a derived workflow lineage read model at `GET /workflow-runs/{id}/lineage`, built from existing workflow child records and `stage_input_manifest` values. It does not add new storage, migrations, direct foreign-key lineage, or join tables.
Phase 33 adds workflow row links in `GET /ops/dashboard` to both `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/lineage`. Phase 34 adds a targeted missing-reference fixture for the derived lineage read model. Phase 35 hardens manifest-shape handling for non-list evidence id values. Phase 35.5 reviews lineage warning taxonomy before adding structured warning fields. Phase 36 adds `warning_codes` to the lineage response while preserving human-readable warnings. Phase 36.5 reviews warning-code documentation before dashboard or persistence expansion. Phase 37 adds a runbook response-shape example for lineage warnings and warning codes. Phase 37.5 reviews dashboard surfacing before adding dashboard rendering. Phase 38 surfaces a compact warning-code legend in the plain dashboard. Phase 38.5 documents the expected dashboard legend in the runbook. Phase 39 reviews whether to rename the runtime `workflow_version` value. Phase 40 renames it to `phase40-lineage-warning-code-dashboard`. These phases do not add dashboard polish, a frontend framework, malformed-manifest mutation endpoint, or new lineage storage.

Not implemented yet:

- file upload
- robust PDF extraction
- persisted parse records
- persisted chunks
- persisted collection plans
- autonomous workflow execution endpoints
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
curl -X POST http://localhost:8000/workflow-runs/execute-preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"strategy\":\"fixed-window\",\"sources\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"content\":\"Enterprise segment demand growth was 12 percent in 2026.\"}],\"draft_claims\":[\"Enterprise segment demand growth was supported by current retrieved evidence.\"]}"
curl http://localhost:8000/workflow-runs/<uuid>
curl http://localhost:8000/workflow-runs/<uuid>/lineage
```

PDF upload preview can extract digital text with PyMuPDF from uploaded PDF bytes. PDF upload chunk and retrieval handoffs reuse PyMuPDF digital text extraction for `POST /documents/upload-chunk-preview`, `POST /documents/upload-chunks`, and `POST /documents/upload-retrieval-preview`. PDF-derived upload chunks preserve minimal parser provenance into document retrieval-run candidate metadata. JSON `parse-preview` can still accept already-extracted PDF text through the text-only fallback. OCR, table extraction, layout fidelity, and robust PDF extraction are not claimed.
Collection Plan Preview is deterministic and does not call LLMs, search external sources, expand retrieval, create an Evidence Ledger by itself, or persist records.
Evidence Ledger Preview is deterministic and does not call LLMs, search external sources, run a Critic / Noise Gate, or create a final report. `POST /evidence-ledgers` persists the generated preview entries as v0 ledger records.
Noise Gate Preview is deterministic and does not call LLMs, create a final report, or build a dashboard.
`POST /noise-gates` persists the deterministic gate decision as a v0 Noise Gate record with local parent `agent_run_id` provenance. It does not create a final report.
Report Preview is deterministic and does not call LLMs. `POST /reports` persists the deterministic preview output as a v0 Report record; it does not create a free-form final report.
Persisted evidence, gate, and report records include `workflow_trace_id`, which also appears in the matching `agent_runs.trace_json`; persisted evidence, gate, and report rows are linked back to their parent run from the dashboard.
Operations Dashboard v0 is a plain FastAPI HTML view over current metadata. It now links to trace lookup, record filters, parent run provenance, persisted Evidence Ledger rows, workflow detail rows, and derived workflow lineage rows, but it is still not a polished product UI.
Auto Trace Recording v0 is metadata tracing for preview endpoints, not distributed tracing or hosted observability.
WorkflowRun Metadata Persistence v0 is create/list metadata storage only. WorkflowRun Dashboard Table v0 renders those metadata rows in the plain dashboard.
Deterministic Workflow Execution Preview v0 creates and updates a parent workflow row, then runs deterministic retrieval -> evidence -> gate -> report preview steps. Phase 29 attaches those child records to the parent `workflow_run_id` while keeping `workflow_trace_id` for correlation. Phase 30 exposes `GET /workflow-runs/{id}` for inspecting those child records from the parent. Phase 31 adds `stage_input_manifest` on workflow-created Noise Gate and Report records so persisted upstream ids are visible without claiming direct foreign-key lineage. Phase 32 exposes `GET /workflow-runs/{id}/lineage` as a derived read model over those existing rows. Phase 33 links dashboard workflow rows to both inspection endpoints. Phase 34 tests missing manifest references in that derived read model. Phase 35 ignores non-list evidence id manifest values with a warning instead of iterating them as ids. Phase 35.5 reviews warning categories while keeping current warnings human-readable. Phase 36 exposes those categories as response-level `warning_codes`. Phase 36.5 reviews how those codes should be documented before adding dashboard rendering or persistence. Phase 37 documents a runbook example for that response shape. Phase 37.5 reviews whether to surface those codes in the plain dashboard before changing runtime behavior. Phase 38 surfaces the codes as a bounded dashboard legend. It still does not create direct evidence -> gate -> report foreign-key links, use semantic retrieval, compute embeddings, call LLMs, search external sources, or create a free-form final answer.
Failure-case Workflow Review Queue v0 adds `GET /failure-cases/workflow-review-queue`, a read model over failed, blocked, and needs-revision workflow parents plus existing `failure_cases.workflow_run_id` links. It does not create failure_cases and keeps the human confirmation boundary at `POST /failure-cases/draft-preview` plus manual persistence.
Failure-case Workflow Review Queue Dashboard Surfacing v0 adds the same read model to `GET /ops/dashboard` as the `Failure-case Workflow Review Queue` section. It shows queue counts, review statuses, stage/error metadata, linked failure-case ids, and a POST-only draft-preview cue without creating failure_cases. The draft preview now renders as a POST-only cue, not a clickable GET link.
Ops Dashboard GET-only Link Method Boundary v0 makes `GET /ops/dashboard` state: Dashboard links are GET-only inspection routes. POST-only actions render as method cues, not anchors.
Ops Dashboard Anchor Method Metadata v0 makes every clickable dashboard anchor carry `data-method="GET"` while POST-only actions remain method cues, not anchors.
