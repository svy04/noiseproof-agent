CREATE TABLE IF NOT EXISTS noise_gate_evidence_links (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_run_id UUID NOT NULL REFERENCES workflow_runs(id) ON DELETE CASCADE,
  workflow_trace_id UUID NOT NULL,
  noise_gate_record_id UUID NOT NULL REFERENCES noise_gate_records(id) ON DELETE CASCADE,
  evidence_ledger_entry_id UUID NOT NULL REFERENCES evidence_ledger_entries(id) ON DELETE CASCADE,
  source_manifest_field TEXT NOT NULL DEFAULT 'noise_gate_records.stage_input_manifest.input_evidence_ledger_entry_ids',
  persistence_boundary TEXT NOT NULL DEFAULT 'workflow_created_records_only_not_standalone_payload_lineage',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (noise_gate_record_id, evidence_ledger_entry_id)
);

CREATE INDEX IF NOT EXISTS idx_noise_gate_evidence_links_workflow_run_id
  ON noise_gate_evidence_links(workflow_run_id);

CREATE INDEX IF NOT EXISTS idx_noise_gate_evidence_links_evidence_ledger_entry_id
  ON noise_gate_evidence_links(evidence_ledger_entry_id);

CREATE TABLE IF NOT EXISTS report_evidence_links (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_run_id UUID NOT NULL REFERENCES workflow_runs(id) ON DELETE CASCADE,
  workflow_trace_id UUID NOT NULL,
  report_record_id UUID NOT NULL REFERENCES report_records(id) ON DELETE CASCADE,
  evidence_ledger_entry_id UUID NOT NULL REFERENCES evidence_ledger_entries(id) ON DELETE CASCADE,
  source_manifest_field TEXT NOT NULL DEFAULT 'report_records.stage_input_manifest.input_evidence_ledger_entry_ids',
  persistence_boundary TEXT NOT NULL DEFAULT 'workflow_created_records_only_not_standalone_payload_lineage',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (report_record_id, evidence_ledger_entry_id)
);

CREATE INDEX IF NOT EXISTS idx_report_evidence_links_workflow_run_id
  ON report_evidence_links(workflow_run_id);

CREATE INDEX IF NOT EXISTS idx_report_evidence_links_evidence_ledger_entry_id
  ON report_evidence_links(evidence_ledger_entry_id);

CREATE TABLE IF NOT EXISTS report_noise_gate_links (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  workflow_run_id UUID NOT NULL REFERENCES workflow_runs(id) ON DELETE CASCADE,
  workflow_trace_id UUID NOT NULL,
  report_record_id UUID NOT NULL REFERENCES report_records(id) ON DELETE CASCADE,
  noise_gate_record_id UUID NOT NULL REFERENCES noise_gate_records(id) ON DELETE CASCADE,
  source_manifest_field TEXT NOT NULL DEFAULT 'report_records.stage_input_manifest.input_noise_gate_record_id',
  persistence_boundary TEXT NOT NULL DEFAULT 'workflow_created_records_only_not_standalone_payload_lineage',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (report_record_id, noise_gate_record_id)
);

CREATE INDEX IF NOT EXISTS idx_report_noise_gate_links_workflow_run_id
  ON report_noise_gate_links(workflow_run_id);

CREATE INDEX IF NOT EXISTS idx_report_noise_gate_links_noise_gate_record_id
  ON report_noise_gate_links(noise_gate_record_id);
