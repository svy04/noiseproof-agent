# Embedding Schema Runtime Verification

Status: local runtime evidence.

Phase marker: embedding schema runtime verification v0.

Docker runtime verification performed for the `chunk_embeddings` schema migration.

This verification used Docker because the schema claim depends on real PostgreSQL/pgvector behavior, not only static SQL text. The migration must be accepted by a database that has the `vector` extension available.

## Environment

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
Database image: pgvector/pgvector:pg16
Ephemeral container: noiseproof-agent-embedding-schema-db
Host port: 55433
```

An isolated Docker Compose project was attempted first, but `docker-compose.yml` sets a fixed `container_name: noiseproof-agent-db`, which conflicted with an existing local container. The verification then used a separate ephemeral `docker run` container name so the existing default DB container was not stopped or removed.

## Commands

```powershell
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55433/noiseproof'
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
docker exec noiseproof-agent-embedding-schema-db psql -U noiseproof -d noiseproof -c "SELECT column_name, data_type, udt_name FROM information_schema.columns WHERE table_name = 'chunk_embeddings' ORDER BY ordinal_position;"
docker exec noiseproof-agent-embedding-schema-db psql -U noiseproof -d noiseproof -c "SELECT filename FROM schema_migrations WHERE filename = '015_chunk_embeddings.sql';"
```

## Observed Migration Status

Before applying migrations:

```text
Applied migrations: 0
Pending migrations: 14
pending 015_chunk_embeddings.sql
```

After applying migrations:

```text
Applied migrations: 14
Pending migrations: 0
applied 015_chunk_embeddings.sql
```

## Observed Table Shape

```text
chunk_embeddings
id                   uuid
chunk_id             uuid
embedding_model      text
embedding_dimension  integer
embedding_text_hash  text
embedding_created_at timestamptz
distance_metric      text
embedding_status     text
embedding            vector
metadata_json        jsonb
created_at           timestamptz
```

The database reported `embedding` as `USER-DEFINED` with `udt_name = vector`, confirming that the pgvector type is active for the table.

Search marker: embedding vector.

## Observed Migration Row

```text
filename
015_chunk_embeddings.sql
```

## Current Non-claims

This is not embedding generation.

This is not semantic retrieval implementation.

This is not hosted deployment evidence.

This is not repository code.

This is not an API endpoint.

This is not HNSW or IVFFlat index evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not product-complete.

## Next Gate

```text
embedding repository review v0
```

The next gate should decide the smallest repository boundary for creating and listing `chunk_embeddings` metadata without generating embeddings or running semantic retrieval yet.
