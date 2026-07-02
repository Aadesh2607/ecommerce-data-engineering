from pathlib import Path

from sqlalchemy import text

from etl.database import engine
from etl.logger import logger

SQL_FILE = Path(__file__).parent / "sql" / "warehouse.sql"


def build_warehouse():
    """
    Build the warehouse by executing warehouse.sql.
    """

    logger.info("=" * 60)
    logger.info("BUILDING DATA WAREHOUSE")
    logger.info("=" * 60)

    sql = SQL_FILE.read_text(encoding="utf-8")

    try:
        with engine.begin() as conn:
            conn.execute(text(sql))

        logger.info("[OK] Warehouse built successfully.")

    except Exception:
        logger.exception("WAREHOUSE BUILD FAILED")

        raise


if __name__ == "__main__":
    build_warehouse()
