# NoiseProof Agent API

Day 2 FastAPI skeleton for NoiseProof Agent.

Implemented in this package:

- `GET /health`
- `GET /ops/summary`
- `POST /documents`
- `GET /documents`
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
```
