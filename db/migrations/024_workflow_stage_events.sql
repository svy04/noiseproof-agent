CREATE TABLE IF NOT EXISTS workflow_stage_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_run_id UUID NOT NULL REFERENCES workflow_runs(id) ON DELETE CASCADE,
  workflow_trace_id UUID NOT NULL,
  stage_name TEXT NOT NULL,
  stage_order INTEGER NOT NULL CHECK (stage_order > 0),
  stage_status TEXT NOT NULL DEFAULT 'completed',
  started_at TIMESTAMPTZ NOT NULL,
  ended_at TIMESTAMPTZ,
  latency_ms INTEGER,
  input_summary_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  output_summary_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  event_boundary TEXT NOT NULL DEFAULT 'local_workflow_stage_event_log_not_distributed_tracing',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (workflow_run_id, stage_order, stage_name)
);

CREATE INDEX IF NOT EXISTS idx_workflow_stage_events_workflow_run_id
  ON workflow_stage_events(workflow_run_id, stage_order);

CREATE INDEX IF NOT EXISTS idx_workflow_stage_events_workflow_trace_id
  ON workflow_stage_events(workflow_trace_id);
