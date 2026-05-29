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
- `POST /retrieval-runs`
- `GET /retrieval-runs`
- `POST /agent-runs`
- `GET /agent-runs`
- `POST /failure-cases`
- `GET /failure-cases`

Not implemented yet:

- file upload
- robust PDF extraction
- persisted parse records
- persisted chunks
- embeddings
- Evidence Ledger generation
- Critic / Noise Gate
- final report generation

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
```

The PDF parser is currently a text-only fallback. Robust PDF extraction is not claimed.
