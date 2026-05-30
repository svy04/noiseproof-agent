ALTER TABLE noise_gate_records
  ADD COLUMN IF NOT EXISTS stage_input_manifest JSONB NOT NULL DEFAULT '{}'::jsonb;

ALTER TABLE report_records
  ADD COLUMN IF NOT EXISTS stage_input_manifest JSONB NOT NULL DEFAULT '{}'::jsonb;
