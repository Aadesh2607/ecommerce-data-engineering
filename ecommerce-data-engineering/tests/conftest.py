import pandas as pd
import pytest


@pytest.fixture
def sample_customers():
    return pd.DataFrame(
        {
            "customer_id": [1, 2, 3],
            "first_name": ["John", "Jane", "Bob"],
            "last_name": ["Doe", "Smith", "Brown"],
            "email": [
                "john@test.com",
                "jane@test.com",
                "bob@test.com",
            ],
            "city": [
                "New York",
                "London",
                "Paris",
            ],
            "country": [
                "USA",
                "UK",
                "France",
            ],
            "signup_date": [
                "2025-01-01",
                "2025-01-02",
                "2025-01-03",
            ],
        }
    )


@pytest.fixture
def sample_products():
    return pd.DataFrame(
        {
            "product_id": [101, 102],
            "product_name": ["Laptop", "Mouse"],
            "category": [
                "Electronics",
                "Accessories",
            ],
            "price": [800.0, 20.0],
        }
    )


@pytest.fixture
def sample_orders():
    return pd.DataFrame(
        {
            "order_id": [1, 2],
            "customer_id": [1, 2],
            "product_id": [101, 102],
            "quantity": [2, 1],
            "unit_price": [800.0, 20.0],
            "total_amount": [1600.0, 20.0],
            "order_date": [
                "2025-01-10",
                "2025-01-11",
            ],
        }
    )
