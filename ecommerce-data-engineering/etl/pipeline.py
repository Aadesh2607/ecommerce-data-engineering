import time

from etl.analytics_loader import build_analytics
from etl.extract import extract_data
from etl.load import load_data
from etl.logger import logger
from etl.quality_checker import run_quality_checks
from etl.transform import transform_data
from etl.validate import validate_data
from etl.warehouse_loader import build_warehouse


def run_pipeline():

    start_time = time.time()

    try:
        extract_data()

        validate_data()

        transform_data()

        load_data()

        build_warehouse()

        build_analytics()

        run_quality_checks()

        elapsed = round(time.time() - start_time, 2)

        logger.info("=" * 60)
        logger.info("PIPELINE COMPLETED SUCCESSFULLY")
        logger.info(f"Execution Time : {elapsed} seconds")
        logger.info("=" * 60)

    except Exception:
        logger.exception("PIPELINE FAILED")
        raise


if __name__ == "__main__":
    run_pipeline()
