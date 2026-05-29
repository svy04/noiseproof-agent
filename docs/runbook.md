# Runbook: NoiseProof Agent

## Current Status

Phase 22 adds an Evidence Ledger dashboard table: persisted evidence rows are now visible beside retrieval, gate, and report records in the plain operations dashboard.

Phase 22.5 adds a review-only cross-link decision: direct evidence -> gate -> report links are deferred until a single workflow parent exists.

Implemented:

- FastAPI app skeleton
- `GET /health`
- `GET /ops/summary`
- `POST /documents/profile`
- document metadata create/list endpoints
- agent run metadata create/list endpoints
- failure case create/list endpoints
- messy market data fixtures
- Document Profiler v0
- parser adapter stubs for markdown, CSV, HTML/URL, PDF text-only fallback, and unknown source types
- `POST /documents/parse-preview`
- chunk strategy experiment v0 for fixed-window, heading-aware, and row-aware strategies
- `POST /documents/chunk-preview`
- lexical retrieval v0 over generated chunks
- `POST /retrieval-runs`
- `GET /retrieval-runs`
- Collection Plan Preview v0
- `POST /collection-plans/preview`
- Evidence Ledger Preview v0
- `POST /evidence-ledgers/preview`
- Noise Gate Preview v0
- `POST /noise-gates/preview`
- Claim-bounded Report Preview v0
- `POST /reports/preview`
- Persisted Report Preview Records v0
- `POST /reports`
- `GET /reports`
- generated, blocked, and needs-revision report counts from persisted Report records
- Record Linkage v0
- `workflow_trace_id` on persisted Evidence Ledger, Noise Gate, and Report records
- matching `workflow_trace_id` in `agent_runs.trace_json` for persisted evidence/gate/report endpoints
- Trace-id Lookup v0
- `GET /traces/{workflow_trace_id}`
- Persisted Record Filtering v0
- `GET /evidence-ledgers?workflow_trace_id=...`
- `GET /evidence-ledgers?status=...`
- `GET /noise-gates?workflow_trace_id=...`
- `GET /noise-gates?decision=...`
- `GET /reports?workflow_trace_id=...`
- `GET /reports?status=...`
- Dashboard Trace/Filter Links v0
- trace lookup and record filter links in `GET /ops/dashboard`
- Agent-run Linkage Review v0
- `docs/review/agent-run-linkage-review.md`
- Agent-run Lifecycle v0
- `run_with_trace()` parent run creation before operation execution
- completion/failure updates on the same `agent_runs` row
- Persisted Child Record Agent-run Linkage v0
- `agent_run_id` on persisted Evidence Ledger, Noise Gate, and Report records
- `db/migrations/006_child_agent_run_ids.sql`
- Dashboard Parent/Child Provenance Links v0
- parent run links on Noise Gate rows in `GET /ops/dashboard`
- parent run links on Report rows in `GET /ops/dashboard`
- Evidence Ledger Dashboard Table v0
- persisted Evidence Ledger rows in `GET /ops/dashboard`
- trace, parent run, and status filter links on Evidence Ledger dashboard rows
- Evidence-to-gate/report Local Cross-links Review v0
- `docs/review/evidence-to-gate-report-cross-links-review.md`
- direct evidence -> gate -> report links remain unimplemented until a single workflow parent exists
- Operations Dashboard v0
- `GET /ops/dashboard`
- Evaluation/Application Package v0
- `docs/evaluation/*`
- `docs/application/*`
- Auto Trace Recording v0
- preview endpoints create `agent_runs.trace_json` metadata
- Persisted Evidence Ledger Records v0
- `POST /evidence-ledgers`
- `GET /evidence-ledgers`
- unsupported and contradiction counts from persisted ledger entries
- Persisted Noise Gate Records v0
- `POST /noise-gates`
- `GET /noise-gates`
- blocked and needs-revision gate counts from persisted Noise Gate records
- PostgreSQL schema init SQL
- GitHub Actions API smoke CI

Not implemented:

- file upload
- robust PDF extraction
- persisted parse records
- persisted chunks
- embeddings
- distributed tracing or hosted observability

## Local Database

From repo root:

```bash
cp .env.example .env
docker compose up -d db
```

The database init script is mounted from:

```text
db/init/001_schema.sql
```

It creates:

- `documents`
- `agent_runs`
- `failure_cases`
- `retrieval_runs`
- `evidence_ledger_entries`
- `noise_gate_records`
- `report_records`

It also enables:

- `pgcrypto`
- `vector`

If local port `5432` is already occupied by another Postgres process, keep the repo-local `.env` ignored and use:

```text
POSTGRES_PORT=55432
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
```

For an existing local database created before Phase 15, apply:

```powershell
Get-Content db/migrations/002_evidence_ledger_entries.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
Get-Content db/migrations/003_noise_gate_records.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
Get-Content db/migrations/004_report_records.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
Get-Content db/migrations/005_workflow_trace_ids.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
```

## API

From repo root:

```bash
cd apps/api
uv sync
uv run uvicorn app.main:app --reload
```

Expected local URL:

```text
http://localhost:8000
```

## Smoke Checks

```bash
curl http://localhost:8000/health
curl http://localhost:8000/ops/summary
curl http://localhost:8000/ops/dashboard
```

Expected `/health` shape:

```json
{
  "status": "ok",
  "service": "noiseproof-agent-api",
  "workflow_version": "phase22-evidence-dashboard-table"
}
```

Expected `/ops/summary` shape:

```json
{
  "status": "placeholder",
  "workflow_version": "phase22-evidence-dashboard-table",
  "document_count": 0,
  "agent_run_count": 0,
  "failure_case_count": 0,
  "noise_gate_record_count": 0,
  "blocked_gate_count": 0,
  "revision_gate_count": 0,
  "report_record_count": 0,
  "generated_report_count": 0,
  "blocked_report_count": 0,
  "revision_report_count": 0,
  "unsupported_claim_count": 0,
  "contradiction_count": 0,
  "average_latency_ms": null,
  "notes": [
    "Retrieval runs recorded: 0. Evidence Ledger persisted entries now drive unsupported and contradiction counts.",
    "Embeddings, semantic retrieval, distributed tracing, and final report generation beyond deterministic previews are still not implemented."
  ]
}
```

Profile fixture-like text:

```bash
curl -X POST http://localhost:8000/documents/profile \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"text\":\"# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.\"}"
```

Expected `/documents/profile` shape:

```json
{
  "source_type": "markdown",
  "character_count": 69,
  "line_count": 4,
  "approximate_token_count": 18,
  "has_tables": false,
  "has_urls": true,
  "has_dates": true,
  "has_numbers": true,
  "extraction_quality": "medium",
  "recommended_strategy": "heading-aware",
  "warnings": [
    "Very short text; profile may not represent a full document."
  ]
}
```

Preview parser output without saving it:

```bash
curl -X POST http://localhost:8000/documents/parse-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"content\":\"# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.\"}"
```

Expected `/documents/parse-preview` shape:

```json
{
  "source_type": "markdown",
  "parser": "markdown",
  "text": "# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.",
  "metadata": {
    "heading_count": 1,
    "link_count": 1,
    "bullet_count": 0
  },
  "warnings": [],
  "failure_case_candidate": null,
  "profile": {
    "source_type": "markdown",
    "character_count": 69,
    "line_count": 4,
    "approximate_token_count": 18,
    "has_tables": false,
    "has_urls": true,
    "has_dates": true,
    "has_numbers": true,
    "extraction_quality": "medium",
    "recommended_strategy": "heading-aware",
    "warnings": [
      "Very short text; profile may not represent a full document."
    ]
  }
}
```

PDF preview boundary:

```bash
curl -X POST http://localhost:8000/documents/parse-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"pdf\",\"content\":\"Extracted PDF text preview only.\"}"
```

The PDF parser is currently a text-only fallback. Robust PDF extraction is not claimed.

Preview chunk strategy comparison without saving chunks:

```bash
curl -X POST http://localhost:8000/documents/chunk-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"content\":\"# Market\nRevenue grew 12% in 2026.\n\n## Risks\nCosts rose 7%.\",\"max_characters\":80,\"overlap\":10}"
```

Expected `/documents/chunk-preview` shape:

```json
{
  "source_type": "markdown",
  "parser": "markdown",
  "profile": {},
  "parse_warnings": [],
  "failure_case_candidate": null,
  "strategies": [
    {
      "strategy": "fixed-window",
      "chunks": [
        {
          "strategy": "fixed-window",
          "chunk_index": 0,
          "text": "...",
          "character_count": 59,
          "approximate_token_count": 15,
          "metadata": {
            "start": 0,
            "end": 59
          }
        }
      ],
      "metrics": {
        "chunk_count": 1,
        "max_characters": 80,
        "overlap": 10
      },
      "warnings": []
    },
    {
      "strategy": "heading-aware",
      "chunks": [
        {
          "strategy": "heading-aware",
          "chunk_index": 0,
          "text": "...",
          "character_count": 34,
          "approximate_token_count": 9,
          "metadata": {
            "header_path": "Market",
            "heading_level": 1
          }
        }
      ],
      "metrics": {
        "chunk_count": 2,
        "boundary_count": 2
      },
      "warnings": []
    },
    {
      "strategy": "row-aware",
      "chunks": [
        {
          "strategy": "row-aware",
          "chunk_index": 0,
          "text": "...",
          "character_count": 8,
          "approximate_token_count": 2,
          "metadata": {
            "row_start": 1,
            "row_end": 1
          }
        }
      ],
      "metrics": {
        "chunk_count": 4,
        "boundary_count": 4
      },
      "warnings": [
        "Source type is not CSV; row-aware strategy used non-empty text lines as row boundaries."
      ]
    }
  ]
}
```

Run lexical retrieval v0 and record the run:

```bash
curl -X POST http://localhost:8000/retrieval-runs \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"strategy\":\"heading-aware\",\"sources\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"content\":\"# Demand\nEnterprise demand grew 12% in 2026.\"},{\"source_id\":\"doc-noise\",\"source_type\":\"markdown\",\"content\":\"# Weather\nRainfall was heavy in Seoul.\"}]}"
```

Expected `/retrieval-runs` response shape:

```json
{
  "id": "uuid",
  "question": "Which segment had enterprise demand growth?",
  "strategy": "heading-aware",
  "status": "completed",
  "latency_ms": 0,
  "result_count": 1,
  "hit_rate": 1.0,
  "citation_coverage": 1.0,
  "missing_evidence_count": 0,
  "metadata_json": {
    "source_count": 2,
    "top_k": 5,
    "max_characters": 500,
    "overlap": 0,
    "warning_count": 0
  },
  "created_at": "timestamp",
  "results": [
    {
      "source_id": "doc-demand",
      "source_type": "markdown",
      "chunk_strategy": "heading-aware",
      "chunk_index": 0,
      "text": "...",
      "score": 0.75,
      "matched_terms": ["demand", "enterprise", "growth"],
      "metadata": {}
    }
  ],
  "warnings": []
}
```

No-results retrieval is recorded with:

```json
{
  "status": "no_results",
  "result_count": 0,
  "missing_evidence_count": 1,
  "results": []
}
```

Create a Collection Plan Preview without saving or retrieving anything:

```bash
curl -X POST http://localhost:8000/collection-plans/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Did this company's AI narrative become materially stronger?\"}"
```

Expected `/collection-plans/preview` response shape:

```json
{
  "question": "Did this company's AI narrative become materially stronger?",
  "information_need": "Determine which role-diverse sources are needed before retrieval for: ...",
  "possible_claims": [
    "The available sources support a limited claim about: ...",
    "The available sources weaken or contradict a claim about: ...",
    "The current sources are insufficient to make a stronger claim about: ..."
  ],
  "required_roles": [
    "direct_support",
    "contradiction",
    "timeline_anchor",
    "missing_data_signal"
  ],
  "source_types_to_check": [
    "news",
    "financial_report",
    "company_statement",
    "analyst_note"
  ],
  "minimum_evidence_needed": "at least one direct support source; one contradiction or missing-data signal; one visible timeline anchor.",
  "known_risks": [
    "same-source repeated narrative may look like independent confirmation",
    "marketing narrative may outrun operational evidence"
  ],
  "stop_conditions": [
    "only same-source repeated narrative found",
    "no contradiction or missing-data signal found"
  ],
  "warnings": [
    "Collection Plan Preview does not judge truth or retrieve evidence.",
    "This plan only defines information roles needed before retrieval."
  ]
}
```

Buy/sell-style questions should include `user_intent_check` and a stop condition for buy/sell drift. This endpoint does not call an LLM, search external sources, expand retrieval, generate an Evidence Ledger, create a final report, build a dashboard, or persist records.

Create an Evidence Ledger Preview from retrieval candidates:

```bash
curl -X POST http://localhost:8000/evidence-ledgers/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"retrieval_results\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"chunk_strategy\":\"heading-aware\",\"chunk_index\":0,\"text\":\"Enterprise demand grew 12% in 2026.\",\"score\":0.75,\"matched_terms\":[\"demand\",\"enterprise\",\"growth\"],\"metadata\":{\"source_date\":\"2026-05-28\"}}]}"
```

Expected `/ops/dashboard` behavior:

```text
Returns text/html with Operations Dashboard v0, summary counts, recent agent runs, failure cases, and retrieval runs.
```

Expected `/evidence-ledgers/preview` response shape:

```json
{
  "question": "Which segment had enterprise demand growth?",
  "entries": [
    {
      "claim": "Which segment had enterprise demand growth",
      "source_id": "doc-demand",
      "source_type": "markdown",
      "source_date": "2026-05-28",
      "evidence_span": "Enterprise demand grew 12% in 2026.",
      "confidence": "medium",
      "limitation": "Supported by a lexical retrieval candidate; not yet validated by a Critic / Noise Gate.",
      "contradicting_source_ids": [],
      "status": "supported",
      "matched_terms": ["demand", "enterprise", "growth"],
      "role": "direct_support"
    }
  ],
  "summary": {
    "supported_count": 1,
    "weakly_supported_count": 0,
    "contradicted_count": 0,
    "unsupported_count": 0,
    "blocked_count": 0,
    "source_count": 1
  },
  "warnings": [
    "Evidence Ledger Preview does not judge final truth or generate a final report.",
    "Entries are derived from retrieval candidates and must still pass a future Critic / Noise Gate."
  ]
}
```

No-evidence and buy/sell-style questions produce `blocked` ledger entries. Contradiction language is surfaced as `contradicted`. The `/preview` endpoint does not call an LLM, search external sources, run a Critic / Noise Gate, create a final report, build a dashboard, or persist Evidence Ledger entries by itself.

Persist an Evidence Ledger v0 record set:

```bash
curl -X POST http://localhost:8000/evidence-ledgers \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Should I buy this company?\",\"retrieval_results\":[]}"
curl http://localhost:8000/evidence-ledgers
```

Expected persisted response shape:

```json
{
  "question": "Should I buy this company?",
  "entries": [
    {
      "id": "uuid",
      "question": "Should I buy this company?",
      "claim": "Should I buy this company",
      "status": "blocked",
      "role": "user_intent_check",
      "created_at": "timestamp"
    }
  ],
  "summary": {
    "blocked_count": 1
  },
  "stored_entry_count": 1
}
```

Evidence Ledger persistence is v0. It does not link entries to retrieval run ids, persist report records, call an LLM, or judge final truth. Noise Gate records are persisted separately by `POST /noise-gates`.

Preview whether current ledger entries can pass the Noise Gate:

```bash
curl -X POST http://localhost:8000/noise-gates/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
```

Expected `/noise-gates/preview` response shape:

```json
{
  "question": "Which segment had enterprise demand growth?",
  "decision": "pass",
  "final_response_allowed": true,
  "checks": [
    {
      "name": "every_strong_claim_has_evidence",
      "status": "pass",
      "message": "Every current ledger claim has source-linked evidence."
    }
  ],
  "blocked_claims": [],
  "downgraded_claims": [],
  "allowed_claims": ["Enterprise demand grew"],
  "required_revisions": [],
  "fallback_message": null,
  "warnings": [
    "Noise Gate Preview does not generate a report or call an LLM.",
    "It only checks whether current ledger evidence can pass into a future report stage."
  ]
}
```

Unsupported or blocked ledger entries return `decision: blocked`. Contradictions, missing source dates, missing limitations, high-confidence single-source claims, and overconfident draft language return `decision: needs_revision` unless trading-advice drift blocks the response. This endpoint does not call an LLM, persist gate records, create a final report, or build a dashboard.

Persist a Noise Gate v0 record:

```bash
curl -X POST http://localhost:8000/noise-gates \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Should I buy this company?\",\"evidence_entries\":[{\"claim\":\"Should I buy this company\",\"source_id\":null,\"source_type\":null,\"source_date\":null,\"evidence_span\":\"\",\"confidence\":\"none\",\"limitation\":\"Question drifts into buy/sell or financial-advice intent.\",\"contradicting_source_ids\":[],\"status\":\"blocked\",\"matched_terms\":[],\"role\":\"user_intent_check\"}],\"draft_claims\":[\"Should I buy this company?\"]}"
curl http://localhost:8000/noise-gates
```

Expected persisted response shape:

```json
{
  "id": "uuid",
  "question": "Should I buy this company?",
  "decision": "blocked",
  "final_response_allowed": false,
  "evidence_entry_count": 1,
  "draft_claim_count": 1,
  "created_at": "timestamp"
}
```

Current persistence is v0. It does not link gate records to an `agent_runs` id, persist report records, call an LLM, or judge final truth.

Preview a claim-bounded report after the Noise Gate:

```bash
curl -X POST http://localhost:8000/reports/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
```

Expected `/reports/preview` response shape:

```json
{
  "question": "Which segment had enterprise demand growth?",
  "status": "generated",
  "report": {
    "summary": "1 claim(s) can be stated with current evidence boundaries.",
    "claims": [
      {
        "claim": "Enterprise demand grew",
        "source_ids": ["doc-demand"],
        "evidence_spans": ["Enterprise demand grew 12% in 2026."],
        "confidence": "medium",
        "limitations": ["Supported by one retrieved source."],
        "contradictions": []
      }
    ],
    "limitations": ["Supported by one retrieved source."],
    "contradictions": [],
    "next_data_needed": [
      "Add an independent second source for claim: Enterprise demand grew",
      "Check for contradicting sources for claim: Enterprise demand grew"
    ]
  },
  "gate": {},
  "fallback_message": null,
  "required_revisions": [],
  "warnings": [
    "Report Preview is deterministic and does not use an LLM.",
    "It only formats claims that passed the Noise Gate; it does not create new claims."
  ]
}
```

If the Noise Gate returns `blocked` or `needs_revision`, `report` is `null` and the response includes `fallback_message` plus `required_revisions`. This endpoint does not call an LLM, persist report records, create a dashboard, or create claims outside the allowed gate output.

Persist a deterministic Report Preview v0 record:

```bash
curl -X POST http://localhost:8000/reports \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl http://localhost:8000/reports
```

Expected persisted response shape:

```json
{
  "id": "uuid",
  "question": "Which segment had enterprise demand growth?",
  "status": "generated",
  "workflow_trace_id": "uuid",
  "agent_run_id": "uuid",
  "gate_decision": "pass",
  "claim_count": 1,
  "evidence_entry_count": 1,
  "draft_claim_count": 1,
  "created_at": "timestamp"
}
```

Current report persistence is v0. It stores deterministic preview output only; it does not call an LLM or create a free-form final report.
Persisted evidence, gate, and report records include both `workflow_trace_id` and `agent_run_id`. The same `workflow_trace_id` is written to the matching `agent_runs.trace_json` entry for the persistence endpoint. This is local parent/child linkage, not full distributed tracing.
Use `GET /traces/{workflow_trace_id}` to inspect records and agent-run traces that share that id.
Use the persisted record list filters to narrow evidence, gate, and report records without adding search or ranking:

```bash
curl "http://localhost:8000/evidence-ledgers?workflow_trace_id=<uuid>"
curl "http://localhost:8000/evidence-ledgers?status=blocked"
curl "http://localhost:8000/noise-gates?workflow_trace_id=<uuid>"
curl "http://localhost:8000/noise-gates?decision=blocked"
curl "http://localhost:8000/reports?workflow_trace_id=<uuid>"
curl "http://localhost:8000/reports?status=generated"
curl "http://localhost:8000/traces/<uuid>"
```

Open the dashboard to use the same trace lookup and filter endpoints from a browser-readable surface:

```bash
curl http://localhost:8000/ops/dashboard
```

The dashboard links are navigation aids over existing records. Evidence Ledger, Noise Gate, and Report rows also expose parent run links through `GET /traces/{workflow_trace_id}`. They do not add ranking, search, LLM calls, distributed tracing, hosted observability, or UI polish.

Inspect auto-created preview traces:

```bash
curl http://localhost:8000/agent-runs
```

Expected trace boundary:

```json
[
  {
    "workflow_version": "phase22-evidence-dashboard-table",
    "status": "completed",
    "trace_json": {
      "endpoint": "POST /reports/preview",
      "phase": "phase22-evidence-dashboard-table",
      "workflow_trace_id": "uuid",
      "report_status": "generated"
    }
  }
]
```

The trace is metadata for inspectability. It is not distributed tracing or hosted observability.

## Metadata Examples

Create a document metadata record:

```bash
curl -X POST http://localhost:8000/documents \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"pdf\",\"source_uri\":\"sample://market-report-001.pdf\",\"title\":\"Sample market report\",\"source_date\":\"2026-05-28\",\"extraction_quality\":\"unknown\",\"status\":\"registered\"}"
```

Create an agent run metadata record:

```bash
curl -X POST http://localhost:8000/agent-runs \
  -H "Content-Type: application/json" \
  -d "{\"user_question\":\"Which sources conflict on demand growth?\"}"
```

Create a failure case metadata record:

```bash
curl -X POST http://localhost:8000/failure-cases \
  -H "Content-Type: application/json" \
  -d "{\"failure_type\":\"unsupported_claim\",\"description\":\"Draft stated demand growth without source evidence.\",\"next_action\":\"Require source id before report generation.\"}"
```

## Verification Without Docker

If Docker is unavailable, run the API compile and smoke tests:

```bash
cd apps/api
uv sync
uv run python -m compileall app ../../packages/ingestion
uv run pytest -q
```

These tests use an in-memory repository override. They do not prove PostgreSQL runtime connectivity.

## Evaluation And Application Package

Review these Phase 10-14 artifacts before making application claims:

```text
docs/evaluation/eval-plan.md
docs/evaluation/retrieval-eval-report.md
docs/evaluation/failure-cases.md
docs/application/braincrew-role-map.md
docs/application/cover-message.md
docs/application/portfolio-index.md
docs/review/application-ready-review.md
```

## Boundary

Do not claim persisted chunks, embeddings, DB persistence for collection plans, direct evidence -> gate -> report cross-links, distributed tracing, hosted observability, or free-form answer generation exists until those stages are implemented and verified with examples. The current dashboard is a plain operations view over existing metadata, not a polished product UI. Direct `agent_run_id` child-record linkage exists for persisted Evidence Ledger, Noise Gate, and Report records, but it remains local service provenance rather than distributed tracing.
