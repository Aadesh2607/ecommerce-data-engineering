from etl.logger import logger
from etl.utils.parquet_manager import (
    load_dataframe,
    save_dataframe,
)


def transform_data():
    """
    Transform all validated datasets.
    """

    logger.info("=" * 60)
    logger.info("TRANSFORM PHASE STARTED")
    logger.info("=" * 60)

    # ----------------------------
    # Customers
    # ----------------------------

    customers = load_dataframe("customers")

    customers.columns = customers.columns.str.lower()

    customers["first_name"] = customers["first_name"].str.title()
    customers["last_name"] = customers["last_name"].str.title()
    customers["email"] = customers["email"].str.lower()

    save_dataframe(customers, "customers")

    # ----------------------------
    # Products
    # ----------------------------

    products = load_dataframe("products")

    products.columns = products.columns.str.lower()

    save_dataframe(products, "products")

    # ----------------------------
    # Orders
    # ----------------------------

    orders = load_dataframe("orders")

    orders.columns = orders.columns.str.lower()

    orders["order_date"] = orders["order_date"].astype("datetime64[ns]")

    save_dataframe(orders, "orders")

    # ----------------------------
    # Payments
    # ----------------------------

    payments = load_dataframe("payments")

    payments.columns = payments.columns.str.lower()

    save_dataframe(payments, "payments")

    # ----------------------------
    # Shipments
    # ----------------------------

    shipments = load_dataframe("shipments")

    shipments.columns = shipments.columns.str.lower()

    save_dataframe(shipments, "shipments")

    logger.info("Transformation completed successfully.\n")
