# Compose Project Isolation

Status: implemented.

Phase marker: compose project isolation v0.

## Purpose

Allow Docker Compose runtime smokes to use isolated project names without colliding on fixed container names.

This fixes a repeated local verification problem: runtime smokes can run with a command such as `docker compose -p noiseproof-phase595 ...`, but fixed `container_name` values forced every project to reuse names such as `noiseproof-agent-db`.

## Source Check

Primary references:

```text
https://docs.docker.com/reference/compose-file/services/#container_name
https://docs.docker.com/compose/how-tos/project-name/
```

Docker Compose uses a project name to isolate environments. The Compose service reference also documents `container_name` as an explicit custom container name, with the important scaling/project-isolation consequence that Compose cannot scale a service beyond one container when that service specifies `container_name`.

## Decision

Remove fixed `container_name` declarations from `docker-compose.yml` for:

```text
db
clamav
api
```

Let Compose derive project-scoped container names instead.

## Before

```text
db -> container_name: noiseproof-agent-db
clamav -> container_name: noiseproof-agent-clamav
api -> container_name: noiseproof-agent-api
```

Observed issue:

```text
fixed container_name collision
```

When another DB was already running with the default fixed name, an isolated smoke using a different project name still collided on the same container name.

## Runtime Verification

Commands:

```text
docker compose -p noiseproof-phase595 config
POSTGRES_PORT=55439 docker compose -p noiseproof-phase595 up -d db
docker compose -p noiseproof-phase595 ps
docker compose -p noiseproof-phase595 exec -T db pg_isready -U noiseproof -d noiseproof
docker compose -p noiseproof-phase595 down -v
```

Observed:

```text
project: noiseproof-phase595
published_port: 55439
container: noiseproof-phase595-db-1
container_name: /noiseproof-phase595-db-1
pg_isready: /var/run/postgresql:5432 - accepting connections
cleanup: docker compose -p noiseproof-phase595 down -v
phase595_cleanup: done
```

The service was still in Docker healthcheck `starting` state when inspected, but PostgreSQL accepted connections and the phase-specific project cleaned up its own container, network, and volume.

## Boundary

This is local Compose project isolation only.

It is not hosted deployment evidence.

It is not production orchestration.

It is not Kubernetes readiness.

It is not a database migration.

It is not API behavior.

It is not ClamAV production evidence.

It is not external reviewer feedback.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
