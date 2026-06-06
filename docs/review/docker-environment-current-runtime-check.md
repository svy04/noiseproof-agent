# Docker Environment Current Runtime Check

Status: verified.

Phase marker: docker environment current runtime check v0.

Purpose: record that the local Docker environment is available and currently running the NoiseProof API, PostgreSQL/pgvector database, and ClamAV service.

## Why Docker Is Needed

Docker is needed to make PostgreSQL/pgvector, the API container, and auxiliary services reproducible without depending on the host machine's global Python, PostgreSQL, or service configuration.

For NoiseProof, Docker matters because the portfolio proof is not only code. It must show that the service can stand up with its database, health endpoint, operations surface, and scanner-adjacent service boundary in an inspectable local environment.

## Observed Docker Installation

```text
Docker version 29.4.3, build 055a478
```

## Observed Containers

```text
noiseproof-agent-api-1 -> Up 22 hours
noiseproof-agent-db-1 -> Up 22 hours
db -> healthy
noiseproof-agent-clamav -> Up 3 days
clamav -> healthy
```

## HTTP Smoke Evidence

```text
GET /health -> 200
{
  "status": "ok",
  "service": "noiseproof-agent-api",
  "workflow_version": "phase40-lineage-warning-code-dashboard"
}
```

```text
GET /ops/summary -> 200
{
  "status": "placeholder",
  "document_count": 28,
  "agent_run_count": 89,
  "failure_case_count": 11,
  "noise_gate_record_count": 22,
  "raw_file_scan_result_count": 29,
  "contradiction_count": 6
}
```

## Boundary

This is local runtime environment evidence only.

It is not new product functionality.

It is not a fresh database migration.

It is not hosted deployment evidence.

It is not production readiness.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

Next gate: external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from current repository state.
