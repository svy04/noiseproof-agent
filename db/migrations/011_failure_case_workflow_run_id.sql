ALTER TABLE failure_cases
  ADD COLUMN IF NOT EXISTS workflow_run_id UUID REFERENCES workflow_runs(id) ON DELETE SET NULL;

CREATE INDEX IF NOT EXISTS idx_failure_cases_workflow_run_id
  ON failure_cases(workflow_run_id);
