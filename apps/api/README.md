# NoiseProof Agent API

Day 2 FastAPI skeleton for NoiseProof Agent.

Implemented in this package:

- `GET /health`
- `GET /ops/summary`
- `POST /documents`
- `GET /documents`
- `POST /documents/profile`
- `POST /agent-runs`
- `GET /agent-runs`
- `POST /failure-cases`
- `GET /failure-cases`

Not implemented yet:

- file upload
- parsing
- chunking
- embeddings
- retrieval
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
```
