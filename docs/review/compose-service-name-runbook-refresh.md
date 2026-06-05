# Compose Service-name Runbook Refresh

Status: implemented.

Phase marker: compose service-name runbook refresh v0.

## Purpose

Phase 595 removed fixed Compose `container_name` declarations. This phase records the future-facing command pattern so new runtime smokes use Compose service names and project names instead of fixed container names.

historical smoke docs may still mention `noiseproof-agent-db`, because they record what was actually observed before Phase 595. Do not rewrite those historical proof records unless a specific evidence correction is needed.

## Source Check

Primary references:

```text
https://docs.docker.com/compose/how-tos/project-name/
https://docs.docker.com/reference/compose-file/services/#container_name
```

Docker Compose supports project names for isolating environments. A fixed `container_name` overrides Compose's generated name and weakens that project-scoped isolation pattern for local smoke runs.

## Future Smoke Pattern

Use service-scoped Compose commands:

```text
docker compose -p <project> ps db
docker compose -p <project> ps -q db
docker compose -p <project> exec -T db pg_isready -U noiseproof -d noiseproof
```

When container inspection is needed, resolve the project-scoped container id first:

```text
$container = docker compose -p <project> ps -q db
docker inspect -f '{{.Name}}' $container
docker inspect -f '{{.State.Health.Status}}' $container
```

## Do Not Use For New Smokes

do not write new smokes around `docker inspect noiseproof-agent-db`.

do not write new smokes around `docker exec noiseproof-agent-db`.

Do not assume the default Compose project name is available.

Do not stop or remove an existing default project when an isolated project name would be safer.

## Boundary

This is a runbook/documentation hygiene gate.

It is not a new runtime smoke.

It is not hosted deployment evidence.

It is not production orchestration.

It is not a database migration.

It is not API behavior.

It is not external reviewer feedback.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
