from __future__ import annotations

import argparse
import hashlib
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

import psycopg
from psycopg.rows import dict_row


SCHEMA_MIGRATIONS_SQL = """
CREATE TABLE IF NOT EXISTS schema_migrations (
  filename TEXT PRIMARY KEY,
  checksum TEXT NOT NULL,
  byte_count INTEGER NOT NULL,
  applied_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
"""


class MigrationError(RuntimeError):
    pass


@dataclass(frozen=True)
class MigrationFile:
    filename: str
    path: Path
    checksum: str
    byte_count: int
    sql: str


@dataclass(frozen=True)
class AppliedMigration:
    filename: str
    checksum: str
    byte_count: int


@dataclass(frozen=True)
class MigrationPlan:
    applied: list[MigrationFile]
    pending: list[MigrationFile]


def default_migrations_dir() -> Path:
    return Path(__file__).resolve().parents[3] / "db" / "migrations"


def discover_migrations(migrations_dir: Path) -> list[MigrationFile]:
    if not migrations_dir.exists():
        raise MigrationError(f"Migration directory does not exist: {migrations_dir}")

    migrations: list[MigrationFile] = []
    for path in sorted(migrations_dir.glob("*.sql")):
        sql = path.read_text(encoding="utf-8")
        raw = sql.encode("utf-8")
        migrations.append(
            MigrationFile(
                filename=path.name,
                path=path,
                checksum=hashlib.sha256(raw).hexdigest(),
                byte_count=len(raw),
                sql=sql,
            )
        )
    return migrations


def plan_migrations(
    migrations: list[MigrationFile],
    applied: Mapping[str, AppliedMigration],
) -> MigrationPlan:
    applied_items: list[MigrationFile] = []
    pending_items: list[MigrationFile] = []

    for migration in migrations:
        applied_migration = applied.get(migration.filename)
        if applied_migration is None:
            pending_items.append(migration)
            continue

        if applied_migration.checksum != migration.checksum:
            raise MigrationError(f"Migration checksum drift: {migration.filename}")
        if applied_migration.byte_count != migration.byte_count:
            raise MigrationError(f"Migration byte count drift: {migration.filename}")
        applied_items.append(migration)

    return MigrationPlan(applied=applied_items, pending=pending_items)


def _connect(database_url: str):
    return psycopg.connect(database_url, row_factory=dict_row)


def ensure_schema_migrations(conn) -> None:
    conn.execute(SCHEMA_MIGRATIONS_SQL)


def fetch_applied_migrations(conn) -> dict[str, AppliedMigration]:
    rows = conn.execute(
        """
        SELECT filename, checksum, byte_count
        FROM schema_migrations
        ORDER BY filename
        """
    ).fetchall()
    return {
        row["filename"]: AppliedMigration(
            filename=row["filename"],
            checksum=row["checksum"],
            byte_count=row["byte_count"],
        )
        for row in rows
    }


def record_migration(conn, migration: MigrationFile) -> None:
    conn.execute(
        """
        INSERT INTO schema_migrations (filename, checksum, byte_count)
        VALUES (%s, %s, %s)
        """,
        (migration.filename, migration.checksum, migration.byte_count),
    )


def baseline_migrations(conn, pending: list[MigrationFile]) -> None:
    for migration in pending:
        record_migration(conn, migration)


def apply_migrations(conn, pending: list[MigrationFile]) -> None:
    for migration in pending:
        with conn.transaction():
            conn.execute(migration.sql)
            record_migration(conn, migration)


def run(
    *,
    database_url: str,
    migrations_dir: Path,
    baseline: bool = False,
    status_only: bool = False,
) -> MigrationPlan:
    migrations = discover_migrations(migrations_dir)
    with _connect(database_url) as conn:
        ensure_schema_migrations(conn)
        applied = fetch_applied_migrations(conn)
        plan = plan_migrations(migrations, applied)

        if status_only:
            conn.commit()
            return plan

        if baseline:
            baseline_migrations(conn, plan.pending)
        else:
            apply_migrations(conn, plan.pending)
        conn.commit()
        return plan


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Apply NoiseProof SQL migrations.")
    parser.add_argument(
        "--database-url",
        default=os.getenv("DATABASE_URL"),
        help="PostgreSQL connection string. Defaults to DATABASE_URL.",
    )
    parser.add_argument(
        "--migrations-dir",
        type=Path,
        default=default_migrations_dir(),
        help="Directory containing ordered .sql migration files.",
    )
    parser.add_argument(
        "--baseline",
        action="store_true",
        help="Mark pending migrations as applied without executing SQL.",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Show applied/pending counts without applying migrations.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.database_url:
        raise MigrationError("DATABASE_URL is required")

    plan = run(
        database_url=args.database_url,
        migrations_dir=args.migrations_dir,
        baseline=args.baseline,
        status_only=args.status,
    )
    print(f"Applied migrations: {len(plan.applied)}")
    print(f"Pending migrations: {len(plan.pending)}")
    if args.status:
        for migration in plan.pending:
            print(f"pending {migration.filename}")
    elif args.baseline:
        for migration in plan.pending:
            print(f"baselined {migration.filename}")
    else:
        for migration in plan.pending:
            print(f"applied {migration.filename}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
