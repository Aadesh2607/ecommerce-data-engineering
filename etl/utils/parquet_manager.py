from pathlib import Path

import pandas as pd

# Base project directory
BASE_DIR = Path(__file__).resolve().parents[2]

# data/intermediate/
INTERMEDIATE_DIR = BASE_DIR / "data" / "intermediate"

INTERMEDIATE_DIR.mkdir(parents=True, exist_ok=True)


def save_dataframe(df: pd.DataFrame, filename: str) -> None:
    """
    Save DataFrame as parquet.
    """

    path = INTERMEDIATE_DIR / f"{filename}.parquet"

    df.to_parquet(
        path,
        index=False,
        engine="pyarrow",
    )


def load_dataframe(filename: str) -> pd.DataFrame:
    """
    Load parquet file.
    """

    path = INTERMEDIATE_DIR / f"{filename}.parquet"

    return pd.read_parquet(
        path,
        engine="pyarrow",
    )


def parquet_exists(filename: str) -> bool:
    """
    Check whether parquet exists.
    """

    path = INTERMEDIATE_DIR / f"{filename}.parquet"

    return path.exists()


def delete_parquet(filename: str) -> None:
    """
    Delete parquet file.
    """

    path = INTERMEDIATE_DIR / f"{filename}.parquet"

    if path.exists():
        path.unlink()


def clear_all_parquet() -> None:
    """
    Delete all intermediate parquet files.
    """

    for file in INTERMEDIATE_DIR.glob("*.parquet"):
        file.unlink()
