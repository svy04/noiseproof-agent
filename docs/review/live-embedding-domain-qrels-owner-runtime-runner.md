# Live embedding-backed domain qrels owner-runtime runner v0

Phase 868 adds the owner-runtime runner for the next semantic retrieval quality
gate.

## Purpose

The runner turns the Phase 866 packet into an executable owner-runtime command:

```text
uv run python -m app.services.live_embedding_domain_qrels_harness --run-owner-runtime-eval --output <runtime-report-path-outside-repo>
```

This prepares `owner_runtime_live_embedding_domain_qrels_eval_v0` without
committing secrets, calling providers in CI, or claiming semantic retrieval
quality before the owner supplies runtime evidence.

## Implemented Behavior

```text
phase_marker -> live embedding-backed domain qrels owner-runtime runner v0
command -> --run-owner-runtime-eval
fixture_root -> examples/representative-semantic-retrieval-quality
run_source -> owner_runtime_openai_embedding_domain_qrels
provider_call_count -> 18
query_count -> 6
chunk_count -> 12
qrel_count -> 24
```

The runner:

- rejects output paths inside the repository before provider calls
- checks `OPENAI_API_KEY`, `NOISEPROOF_ENABLE_OPENAI_PROVIDER`, and `CI`
- calls the provider only after owner-runtime input is ready
- writes a metadata-only report outside the repository
- keeps the full run details and provider raw responses out of the committed report
- reuses `--validate-owner-runtime-eval-report` for post-run validation

## Missing-input CI Check

The CI check intentionally runs without `OPENAI_API_KEY`.

Expected result:

```text
run_status -> input_not_ready
owner_runtime_input_status -> missing_openai_api_key
api_calls_attempted -> false
openai_api_key_printed -> false
```

## Output Path Guard

Repository paths are rejected before provider calls:

```text
output_path_allowed -> false
required_location -> outside_repository
api_calls_attempted -> false
```

## Still Pending

The next gate remains:

```text
owner_runtime_live_embedding_domain_qrels_eval_v0
```

That gate requires the owner to configure `OPENAI_API_KEY` outside the
repository, set `NOISEPROOF_ENABLE_OPENAI_PROVIDER=true`, run outside CI, and
store the runtime report outside the repository before validation.

## Boundary

This is an owner-runtime runner and missing-input CI guard only.

It is not live embedding generation proof, not production semantic retrieval quality evidence,
not a public benchmark result, not hosted deployment evidence, not external reviewer feedback,
not customer validation, not Braincrew acceptance, and not product-complete.
