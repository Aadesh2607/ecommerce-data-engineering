"""
Application configuration.

Loads environment variables and exposes them
through a single Settings object.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings:
    # -----------------------------
    # Database
    # -----------------------------
    DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
    DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))
    DB_NAME = os.getenv("POSTGRES_DB", "ecommerce_db")
    DB_USER = os.getenv("POSTGRES_USER", "postgres")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")

    DATABASE_URL = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # -----------------------------
    # Paths
    # -----------------------------
    DATA_DIR = BASE_DIR / "data"

    RAW_DATA = DATA_DIR / "raw"
    PROCESSED_DATA = DATA_DIR / "processed"
    REJECTED_DATA = DATA_DIR / "rejected"
    ARCHIVE_DATA = DATA_DIR / "archive"

    LOG_DIR = BASE_DIR / "logs"


settings = Settings()
