from unittest.mock import patch

import pandas as pd

from etl.transform import transform_data


@patch("etl.transform.save_dataframe")
@patch("etl.transform.load_dataframe")
def test_customer_names_are_title_case(
    mock_load,
    mock_save,
):
    customers = pd.DataFrame(
        {
            "FIRST_NAME": ["john"],
            "LAST_NAME": ["doe"],
            "EMAIL": ["JOHN@TEST.COM"],
        }
    )

    products = pd.DataFrame(
        {
            "PRODUCT_ID": [1],
            "PRODUCT_NAME": ["Laptop"],
            "CATEGORY": ["Electronics"],
            "PRICE": [1000],
        }
    )

    orders = pd.DataFrame(
        {
            "ORDER_DATE": ["2025-01-01"],
        }
    )

    payments = pd.DataFrame(
        {
            "PAYMENT_ID": [1],
            "ORDER_ID": [1],
            "PAYMENT_METHOD": ["Card"],
            "PAYMENT_STATUS": ["Paid"],
        }
    )

    shipments = pd.DataFrame(
        {
            "SHIPMENT_ID": [1],
            "ORDER_ID": [1],
            "SHIPMENT_STATUS": ["Delivered"],
        }
    )

    mock_load.side_effect = [
        customers,
        products,
        orders,
        payments,
        shipments,
    ]

    transform_data()

    transformed = mock_save.call_args_list[0][0][0]

    assert transformed["first_name"][0] == "John"
    assert transformed["last_name"][0] == "Doe"


@patch("etl.transform.save_dataframe")
@patch("etl.transform.load_dataframe")
def test_email_is_lowercase(
    mock_load,
    mock_save,
):
    customers = pd.DataFrame(
        {
            "FIRST_NAME": ["John"],
            "LAST_NAME": ["Doe"],
            "EMAIL": ["JOHN@TEST.COM"],
        }
    )

    products = pd.DataFrame(
        {
            "PRODUCT_ID": [1],
            "PRODUCT_NAME": ["Laptop"],
            "CATEGORY": ["Electronics"],
            "PRICE": [1000],
        }
    )

    orders = pd.DataFrame(
        {
            "ORDER_DATE": ["2025-01-01"],
        }
    )

    payments = pd.DataFrame(
        {
            "PAYMENT_ID": [1],
            "ORDER_ID": [1],
            "PAYMENT_METHOD": ["Card"],
            "PAYMENT_STATUS": ["Paid"],
        }
    )

    shipments = pd.DataFrame(
        {
            "SHIPMENT_ID": [1],
            "ORDER_ID": [1],
            "SHIPMENT_STATUS": ["Delivered"],
        }
    )

    mock_load.side_effect = [
        customers,
        products,
        orders,
        payments,
        shipments,
    ]

    transform_data()

    transformed = mock_save.call_args_list[0][0][0]

    assert transformed["email"][0] == "john@test.com"


@patch("etl.transform.save_dataframe")
@patch("etl.transform.load_dataframe")
def test_columns_are_lowercase(
    mock_load,
    mock_save,
):
    customers = pd.DataFrame(
        {
            "FIRST_NAME": ["John"],
            "LAST_NAME": ["Doe"],
            "EMAIL": ["john@test.com"],
        }
    )

    products = pd.DataFrame(
        {
            "PRODUCT_ID": [1],
            "PRODUCT_NAME": ["Laptop"],
            "CATEGORY": ["Electronics"],
            "PRICE": [1000],
        }
    )

    orders = pd.DataFrame(
        {
            "ORDER_DATE": ["2025-01-01"],
        }
    )

    payments = pd.DataFrame(
        {
            "PAYMENT_ID": [1],
            "ORDER_ID": [1],
            "PAYMENT_METHOD": ["Card"],
            "PAYMENT_STATUS": ["Paid"],
        }
    )

    shipments = pd.DataFrame(
        {
            "SHIPMENT_ID": [1],
            "ORDER_ID": [1],
            "SHIPMENT_STATUS": ["Delivered"],
        }
    )

    mock_load.side_effect = [
        customers,
        products,
        orders,
        payments,
        shipments,
    ]

    transform_data()

    transformed = mock_save.call_args_list[0][0][0]

    assert all(col == col.lower() for col in transformed.columns)


@patch("etl.transform.save_dataframe")
@patch("etl.transform.load_dataframe")
def test_order_date_is_datetime(
    mock_load,
    mock_save,
):
    customers = pd.DataFrame(
        {
            "FIRST_NAME": ["John"],
            "LAST_NAME": ["Doe"],
            "EMAIL": ["john@test.com"],
        }
    )

    products = pd.DataFrame(
        {
            "PRODUCT_ID": [1],
            "PRODUCT_NAME": ["Laptop"],
            "CATEGORY": ["Electronics"],
            "PRICE": [1000],
        }
    )

    orders = pd.DataFrame(
        {
            "ORDER_DATE": ["2025-01-01"],
        }
    )

    payments = pd.DataFrame(
        {
            "PAYMENT_ID": [1],
            "ORDER_ID": [1],
            "PAYMENT_METHOD": ["Card"],
            "PAYMENT_STATUS": ["Paid"],
        }
    )

    shipments = pd.DataFrame(
        {
            "SHIPMENT_ID": [1],
            "ORDER_ID": [1],
            "SHIPMENT_STATUS": ["Delivered"],
        }
    )

    mock_load.side_effect = [
        customers,
        products,
        orders,
        payments,
        shipments,
    ]

    transform_data()

    transformed_orders = mock_save.call_args_list[2][0][0]

    assert pd.api.types.is_datetime64_any_dtype(transformed_orders["order_date"])
