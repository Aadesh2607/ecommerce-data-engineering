from sqlalchemy import inspect, text

from etl.database import engine
from etl.logger import logger
from etl.utils.parquet_manager import load_dataframe

TABLE_MAPPING = {
    "customers": ("stg_customers", "customer_id"),
    "products": ("stg_products", "product_id"),
    "orders": ("stg_orders", "order_id"),
    "payments": ("stg_payments", "payment_id"),
    "shipments": ("stg_shipments", "shipment_id"),
}


def load_data(datasets=None):
    """
    Incrementally load transformed parquet data into PostgreSQL staging tables.
    """

    logger.info("=" * 60)
    logger.info("LOAD PHASE STARTED")
    logger.info("=" * 60)

    inspector = inspect(engine)

    existing_tables = inspector.get_table_names(schema="staging")

    total_inserted = 0

    try:
        with engine.begin() as conn:
            for dataset, (table, pk) in TABLE_MAPPING.items():
                logger.info(f"Checking staging.{table}")

                if table not in existing_tables:
                    raise Exception(f"staging.{table} does not exist.")

                df = load_dataframe(dataset)

                if df.empty:
                    logger.warning(f"{dataset}.parquet is empty.")
                    continue

                existing_ids = set(conn.execute(text(f"""
                            SELECT {pk}
                            FROM staging.{table}
                            """)).scalars())

                new_rows = df[~df[pk].isin(existing_ids)]

                if new_rows.empty:
                    logger.info(f"[OK] {table}: No new records found.")
                    continue

                new_rows.to_sql(
                    table,
                    con=conn,
                    schema="staging",
                    if_exists="append",
                    index=False,
                    method="multi",
                    chunksize=5000,
                )

                total_inserted += len(new_rows)

                logger.info(
                    f"[OK] Inserted {len(new_rows):,} rows into staging.{table}"
                )

        logger.info("=" * 60)
        logger.info(
            f"Load completed successfully. Total rows inserted: {total_inserted:,}"
        )
        logger.info("=" * 60)

    except Exception:
        logger.exception("LOAD PHASE FAILED")
        raise
