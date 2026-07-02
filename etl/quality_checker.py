from pathlib import Path

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from etl.database import engine
from etl.logger import logger

SQL_FILE = Path(__file__).parent / "sql" / "quality_checks.sql"


def parse_sql_file():
    """
    Parse SQL file into named checks.

    Returns:
        List of tuples: (check_name, sql_statement)
    """

    lines = SQL_FILE.read_text(encoding="utf-8").splitlines()

    checks = []

    current_name = None
    current_sql = []

    for line in lines:
        if line.startswith("-- name:"):
            if current_name is not None:
                checks.append(
                    (
                        current_name,
                        "\n".join(current_sql).strip(),
                    )
                )

            current_name = line.replace("-- name:", "").strip()
            current_sql = []

        else:
            current_sql.append(line)

    if current_name is not None:
        checks.append(
            (
                current_name,
                "\n".join(current_sql).strip(),
            )
        )

    return checks


def validate_result(check_name, rows):

    if check_name == "staging_tables_not_empty":
        for table, count in rows:
            if count == 0:
                raise ValueError(f"{table} is empty.")

    elif check_name.startswith("duplicate_"):
        if rows:
            raise ValueError(f"{check_name}: duplicate records found.")

    elif check_name.startswith("null_"):
        if rows and rows[0][0] > 0:
            raise ValueError(f"{check_name}: NULL values found.")

    elif check_name == "orphan_orders":
        if rows and rows[0][0] > 0:
            raise ValueError("Orphan orders detected.")

    elif check_name == "orphan_products":
        if rows and rows[0][0] > 0:
            raise ValueError("Orders reference missing products.")

    elif check_name == "warehouse_row_counts":
        for value in rows[0]:
            if value == 0:
                raise ValueError("Warehouse contains empty tables.")


def run_quality_checks():

    logger.info("=" * 60)
    logger.info("RUNNING DATA QUALITY CHECKS")
    logger.info("=" * 60)

    checks = parse_sql_file()

    try:
        with engine.connect() as conn:
            for check_name, sql in checks:
                logger.info(f"Running: {check_name}")

                result = conn.execute(text(sql))

                if result.returns_rows:
                    rows = result.fetchall()

                    for row in rows:
                        logger.info(row)

                    validate_result(check_name, rows)

        logger.info("=" * 60)
        logger.info("ALL DATA QUALITY CHECKS PASSED")
        logger.info("=" * 60)

    except (ValueError, SQLAlchemyError) as e:
        logger.error("=" * 60)
        logger.error("DATA QUALITY CHECK FAILED")
        logger.error(str(e))
        logger.error("=" * 60)

        raise


if __name__ == "__main__":
    run_quality_checks()
