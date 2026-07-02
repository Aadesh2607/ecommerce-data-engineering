from etl.logger import logger
from etl.utils.parquet_manager import (
    load_dataframe,
    save_dataframe,
)

DATASETS = [
    "customers",
    "products",
    "orders",
    "payments",
    "shipments",
]


def validate_data():
    """
    Validate all extracted datasets.
    """

    logger.info("=" * 60)
    logger.info("VALIDATION PHASE STARTED")
    logger.info("=" * 60)

    for dataset in DATASETS:
        logger.info(f"Validating {dataset.title()}...")

        df = load_dataframe(dataset)

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove completely empty rows
        df = df.dropna(how="all")

        # Reset index
        df = df.reset_index(drop=True)

        save_dataframe(df, dataset)

        logger.info(f"{dataset.title()} valid: {len(df):,}")

    logger.info("Validation completed successfully.\n")
