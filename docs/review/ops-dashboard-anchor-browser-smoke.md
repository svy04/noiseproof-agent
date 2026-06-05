# Ops Dashboard Anchor Browser Smoke

Status: local browser automation smoke evidence.

Phase marker: ops dashboard anchor browser smoke v0.

## Purpose

Record local Playwright browser automation evidence that `GET /ops/dashboard` renders clickable inspection anchors with `data-method="GET"` while the POST-only failure-case draft preview remains a visible method cue rather than a clickable anchor.

Screenshot:

```text
docs/review/media/ops-dashboard-anchor-browser-smoke.png
```

## Runtime Setup

Commands:

```text
$env:POSTGRES_PORT='55436'
docker compose -p noiseproof-phase526 up -d db
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55436/noiseproof'
uv run uvicorn app.main:app --host 127.0.0.1 --port 8102
```

Seeded records:

```text
POST /workflow-runs/execute-preview -> 201
POST /failure-cases -> 201
POST /workflow-runs -> 201
GET /ops/dashboard -> 200
```

The additional failed workflow was intentionally left without a linked failure case so the dashboard would show the POST-only draft-preview cue.

## Browser Automation

Tooling:

```text
Playwright browser automation
```

The local Playwright CLI opened:

```text
http://127.0.0.1:8102/ops/dashboard
```

The final browser smoke used a temporary npm workspace outside the repository:

```text
%TEMP%/noiseproof-phase526-playwright
```

This kept runtime helper dependencies out of the repository and captured the browser screenshot into `docs/review/media/ops-dashboard-anchor-browser-smoke.png`.

## Observed Browser Result

```json
{
  "title": "NoiseProof Operations Dashboard v0",
  "dashboard_status_code": 200,
  "browser_anchor_count": 27,
  "browser_get_anchor_count": 27,
  "browser_post_anchor_count": 0,
  "post_only_draft_preview_anchor_count": 0,
  "post_only_draft_preview_cue_visible": true,
  "all_browser_get_anchors_marked_get": true
}
```

Representative hrefs observed from the browser DOM:

```text
/evidence-ledgers?status=unsupported
/evidence-ledgers?status=contradicted
/noise-gates?decision=blocked
/noise-gates?decision=needs_revision
/noise-gates?decision=pass
```

## Allowed Claim

NoiseProof Agent has local browser automation evidence that the current operations dashboard renders GET-marked inspection anchors and does not expose the POST-only draft-preview route as a clickable anchor.

## Boundary

This is local browser automation evidence only.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not design quality evidence.

It is not production observability.

It is not semantic retrieval quality evidence.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
