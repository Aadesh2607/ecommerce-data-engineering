from pathlib import Path

from sqlalchemy import text

from etl.database import engine
from etl.logger import logger

SQL_FILE = Path(__file__).parent / "sql" / "analytics.sql"


def build_analytics():

    logger.info("=" * 60)
    logger.info("BUILDING ANALYTICS VIEWS")
    logger.info("=" * 60)

    sql = SQL_FILE.read_text(encoding="utf-8")

    try:
        with engine.begin() as conn:
            conn.execute(text(sql))

        logger.info("[OK] Analytics Views Created")

    except Exception:
        logger.exception("ANALYTICS BUILD FAILED")

        raise


if __name__ == "__main__":
    build_analytics()
