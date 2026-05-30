# Migration runner review

Status: review-only gate

## Question

Phase 43 proved that an existing Docker volume can keep stale executable schema defaults until a forward migration is applied. Should NoiseProof add a migration runner now, keep manual `psql` commands only, or adopt a heavier migration framework?

## Current evidence

- Fresh database initialization uses `db/init/001_schema.sql`.
- Existing volumes do not replay files from `db/init` after the first initialization.
- Existing forward migrations live in `db/migrations/*.sql`.
- The current runbook applies migrations by runbook-only psql piping.
- Phase 43 required piping `db/migrations/010_workflow_version_defaults.sql` into the running DB to bring schema defaults current.
- There is no `schema_migrations` table or migration tracking surface.

## Alternatives considered

### 1. Keep runbook-only psql piping

Pros:

- Lowest implementation cost.
- Keeps migration behavior explicit and visible.
- No new code path to maintain.

Cons:

- No applied-migration tracking.
- Easy to skip a migration on an existing volume.
- Repeated manual commands are hard to audit.
- Future agents may not know whether a local DB is current.

### 2. Adopt Alembic now

Pros:

- Established Python migration ecosystem.
- Tracks revisions and ordering.
- Suitable for larger schema evolution.

Cons:

- Introduces a second migration format next to the existing SQL files.
- Requires config, revision scripts, and migration conventions that are larger than the current project needs.
- Risks turning an inspectability gate into migration-framework work.

### 3. Add a lightweight SQL migration runner

Pros:

- Reuses the existing SQL migration files.
- Can create a small `schema_migrations` table.
- Can apply only pending migrations in filename order.
- Fits the current Docker/PostgreSQL/local-portfolio scope.
- Keeps the implementation small enough to inspect.

Cons:

- Needs careful baseline behavior for databases that already contain old migrations but no tracking table.
- Must not pretend to be a production migration platform.
- Must surface failures instead of silently continuing.

## Decision

Add a lightweight SQL migration runner next.

Do not implement the runner in this review gate.

The next implementation should add the smallest runner that can:

- connect using `DATABASE_URL`
- create `schema_migrations` if absent
- list `db/migrations/*.sql` in sorted order
- support an explicit baseline mode for already-current local databases
- apply pending SQL files one at a time
- record applied filename, checksum or byte count, and applied timestamp
- fail loudly on SQL errors

## Boundary

This review adds no runtime behavior, migration runner, schema tables, columns, endpoints, dashboard rendering, LLM calls, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

## Next direction

lightweight SQL migration runner v0
