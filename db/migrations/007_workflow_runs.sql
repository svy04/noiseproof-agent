CREATE TABLE IF NOT EXISTS workflow_runs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  question TEXT NOT NULL,
  workflow_version TEXT NOT NULL DEFAULT 'phase24-workflow-run-schema',
  status TEXT NOT NULL DEFAULT 'created' CHECK (
    status IN (
      'created',
      'running',
      'completed',
      'failed',
      'blocked',
      'needs_revision'
    )
  ),
  trace_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  started_at TIMESTAMPTZ,
  ended_at TIMESTAMPTZ,
  latency_ms INTEGER,
  error_message TEXT
);
