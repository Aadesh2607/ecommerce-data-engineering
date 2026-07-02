import random
from pathlib import Path

import pandas as pd
from faker import Faker

fake = Faker()

# ==========================================
# Configuration
# ==========================================

RAW_DATA_PATH = Path("data/raw")
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

NUM_CUSTOMERS = 10_000
NUM_PRODUCTS = 500
NUM_ORDERS = 100_000

CATEGORIES = [
    "Electronics",
    "Clothing",
    "Home",
    "Sports",
    "Books",
    "Beauty",
    "Toys",
    "Automotive",
    "Grocery",
    "Furniture",
]

PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking",
    "Wallet",
]

PAYMENT_STATUS = [
    "Completed",
    "Pending",
    "Failed",
]

SHIPMENT_STATUS = [
    "Delivered",
    "In Transit",
    "Processing",
    "Cancelled",
]


# ==========================================
# Customers
# ==========================================


def generate_customers():
    customers = []

    for customer_id in range(1, NUM_CUSTOMERS + 1):
        customers.append(
            {
                "customer_id": customer_id,
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.unique.email(),
                "city": fake.city(),
                "country": fake.country(),
                "signup_date": fake.date_between(
                    start_date="-3y",
                    end_date="today",
                ),
            }
        )

    df = pd.DataFrame(customers)
    df.to_csv(RAW_DATA_PATH / "customers.csv", index=False)

    print(f"✅ Customers Generated : {len(df)}")


# ==========================================
# Products
# ==========================================


def generate_products():
    products = []

    for product_id in range(1, NUM_PRODUCTS + 1):
        products.append(
            {
                "product_id": product_id,
                "product_name": fake.word().title() + " " + fake.word().title(),
                "category": random.choice(CATEGORIES),
                "price": round(random.uniform(10, 5000), 2),
            }
        )

    df = pd.DataFrame(products)
    df.to_csv(RAW_DATA_PATH / "products.csv", index=False)

    print(f"✅ Products Generated  : {len(df)}")


# ==========================================
# Orders
# ==========================================


def generate_orders():
    orders = []

    for order_id in range(1, NUM_ORDERS + 1):
        quantity = random.randint(1, 5)
        unit_price = round(random.uniform(10, 5000), 2)

        orders.append(
            {
                "order_id": order_id,
                "customer_id": random.randint(1, NUM_CUSTOMERS),
                "product_id": random.randint(1, NUM_PRODUCTS),
                "quantity": quantity,
                "unit_price": unit_price,
                "total_amount": round(quantity * unit_price, 2),
                "order_date": fake.date_between(
                    start_date="-2y",
                    end_date="today",
                ),
            }
        )

    df = pd.DataFrame(orders)
    df.to_csv(RAW_DATA_PATH / "orders.csv", index=False)

    print(f"✅ Orders Generated    : {len(df)}")


# ==========================================
# Payments
# ==========================================


def generate_payments():
    payments = []

    for payment_id in range(1, NUM_ORDERS + 1):
        payments.append(
            {
                "payment_id": payment_id,
                "order_id": payment_id,
                "payment_method": random.choice(PAYMENT_METHODS),
                "payment_status": random.choices(
                    PAYMENT_STATUS,
                    weights=[90, 7, 3],
                    k=1,
                )[0],
                "payment_date": fake.date_between(
                    start_date="-2y",
                    end_date="today",
                ),
            }
        )

    df = pd.DataFrame(payments)
    df.to_csv(RAW_DATA_PATH / "payments.csv", index=False)

    print(f"✅ Payments Generated : {len(df)}")


# ==========================================
# Shipments
# ==========================================


def generate_shipments():
    shipments = []

    for shipment_id in range(1, NUM_ORDERS + 1):
        shipments.append(
            {
                "shipment_id": shipment_id,
                "order_id": shipment_id,
                "shipment_status": random.choices(
                    SHIPMENT_STATUS,
                    weights=[80, 10, 8, 2],
                    k=1,
                )[0],
                "shipment_date": fake.date_between(
                    start_date="-2y",
                    end_date="today",
                ),
            }
        )

    df = pd.DataFrame(shipments)
    df.to_csv(RAW_DATA_PATH / "shipments.csv", index=False)

    print(f"✅ Shipments Generated: {len(df)}")


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":
    print("\n🚀 Generating Ecommerce Dataset...\n")

    generate_customers()
    generate_products()
    generate_orders()
    generate_payments()
    generate_shipments()

    print("\n🎉 Dataset generation completed successfully!")
