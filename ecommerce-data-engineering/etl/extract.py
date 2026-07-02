import pandas as pd

from etl.logger import logger
from etl.utils.file_manager import raw_file
from etl.utils.parquet_manager import save_dataframe

FILES = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "payments": "payments.csv",
    "shipments": "shipments.csv",
}


def extract_data():
    """
    Extract CSV files and save them as parquet.
    """

    logger.info("=" * 60)
    logger.info("EXTRACT PHASE STARTED")
    logger.info("=" * 60)

    for dataset, filename in FILES.items():
        path = raw_file(filename)

        df = pd.read_csv(path)

        logger.info(f"Loaded {filename:<20} Rows: {len(df):>8,}")

        save_dataframe(df, dataset)

    logger.info("Extraction completed successfully.\n")
