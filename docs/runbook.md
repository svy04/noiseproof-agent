# Runbook: NoiseProof Agent

## Current Status

Phase 5.5 is intended to prove that a question can produce a small role-based Collection Plan Preview before retrieval candidates are promoted toward Evidence Ledger work.

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
- PostgreSQL schema init SQL
- GitHub Actions API smoke CI

Not implemented:

- file upload
- robust PDF extraction
- persisted parse records
- persisted chunks
- embeddings
- Evidence Ledger generation
- Critic / Noise Gate
- final report generation
- web dashboard

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

It also enables:

- `pgcrypto`
- `vector`

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
```

Expected `/health` shape:

```json
{
  "status": "ok",
  "service": "noiseproof-agent-api",
  "workflow_version": "phase5.5-collection-plan-preview"
}
```

Expected `/ops/summary` shape:

```json
{
  "status": "placeholder",
  "workflow_version": "phase5.5-collection-plan-preview",
  "document_count": 0,
  "agent_run_count": 0,
  "failure_case_count": 0,
  "unsupported_claim_count": 0,
  "contradiction_count": 0,
  "average_latency_ms": null,
  "notes": [
    "Retrieval runs recorded: 0. Phase 5.5 adds Collection Plan Preview only; no Evidence Ledger, Critic, or dashboard implementation yet.",
    "Unsupported claim and contradiction counts remain placeholders until Evidence Ledger exists."
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

## Boundary

Do not claim persisted chunks, embeddings, Evidence Ledger, Critic / Noise Gate, report generation, dashboard, DB persistence for collection plans, or answer generation exists until those stages are implemented and verified with examples.
