from etl.load import TABLE_MAPPING


def test_table_mapping_contains_all_datasets():
    expected = {
        "customers",
        "products",
        "orders",
        "payments",
        "shipments",
    }

    assert set(TABLE_MAPPING.keys()) == expected


def test_table_mapping_table_names():
    assert TABLE_MAPPING["customers"][0] == "stg_customers"
    assert TABLE_MAPPING["products"][0] == "stg_products"
    assert TABLE_MAPPING["orders"][0] == "stg_orders"
    assert TABLE_MAPPING["payments"][0] == "stg_payments"
    assert TABLE_MAPPING["shipments"][0] == "stg_shipments"


def test_table_mapping_primary_keys():
    assert TABLE_MAPPING["customers"][1] == "customer_id"
    assert TABLE_MAPPING["products"][1] == "product_id"
    assert TABLE_MAPPING["orders"][1] == "order_id"
    assert TABLE_MAPPING["payments"][1] == "payment_id"
    assert TABLE_MAPPING["shipments"][1] == "shipment_id"
