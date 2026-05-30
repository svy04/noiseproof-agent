ALTER TABLE agent_runs
  ALTER COLUMN workflow_version SET DEFAULT 'phase40-lineage-warning-code-dashboard';

ALTER TABLE workflow_runs
  ALTER COLUMN workflow_version SET DEFAULT 'phase40-lineage-warning-code-dashboard';
