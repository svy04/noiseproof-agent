from pathlib import Path

import pytest

from app import migration_runner


def write_migration(path: Path, sql: str) -> Path:
    path.write_text(sql, encoding="utf-8")
    return path


def test_discover_migrations_returns_sorted_files_with_checksums(tmp_path):
    write_migration(tmp_path / "010_second.sql", "SELECT 2;\n")
    write_migration(tmp_path / "002_first.sql", "SELECT 1;\n")

    migrations = migration_runner.discover_migrations(tmp_path)

    assert [migration.filename for migration in migrations] == [
        "002_first.sql",
        "010_second.sql",
    ]
    assert migrations[0].byte_count == len("SELECT 1;\n".encode("utf-8"))
    assert len(migrations[0].checksum) == 64
    assert migrations[0].sql == "SELECT 1;\n"


def test_plan_migrations_detects_pending_and_applied_items(tmp_path):
    first = write_migration(tmp_path / "002_first.sql", "SELECT 1;\n")
    second = write_migration(tmp_path / "003_second.sql", "SELECT 2;\n")
    migrations = migration_runner.discover_migrations(tmp_path)
    applied = {
        first.name: migration_runner.AppliedMigration(
            filename=first.name,
            checksum=migrations[0].checksum,
            byte_count=migrations[0].byte_count,
        )
    }

    plan = migration_runner.plan_migrations(migrations, applied)

    assert [migration.filename for migration in plan.applied] == [first.name]
    assert [migration.filename for migration in plan.pending] == [second.name]


def test_plan_migrations_rejects_checksum_drift(tmp_path):
    path = write_migration(tmp_path / "002_first.sql", "SELECT 1;\n")
    migrations = migration_runner.discover_migrations(tmp_path)
    applied = {
        path.name: migration_runner.AppliedMigration(
            filename=path.name,
            checksum="x" * 64,
            byte_count=migrations[0].byte_count,
        )
    }

    with pytest.raises(migration_runner.MigrationError, match="checksum drift"):
        migration_runner.plan_migrations(migrations, applied)


def test_runner_exposes_schema_migrations_table_sql():
    assert "CREATE TABLE IF NOT EXISTS schema_migrations" in migration_runner.SCHEMA_MIGRATIONS_SQL
    assert "filename TEXT PRIMARY KEY" in migration_runner.SCHEMA_MIGRATIONS_SQL
    assert "checksum TEXT NOT NULL" in migration_runner.SCHEMA_MIGRATIONS_SQL
    assert "byte_count INTEGER NOT NULL" in migration_runner.SCHEMA_MIGRATIONS_SQL
    assert "applied_at TIMESTAMPTZ NOT NULL DEFAULT now()" in migration_runner.SCHEMA_MIGRATIONS_SQL
