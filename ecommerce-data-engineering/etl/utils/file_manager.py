from pathlib import Path

import pandas as pd

# Project directories
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = PROJECT_ROOT / "data" / "raw"
INTERMEDIATE_DIR = PROJECT_ROOT / "data" / "intermediate"

RAW_DIR.mkdir(parents=True, exist_ok=True)
INTERMEDIATE_DIR.mkdir(parents=True, exist_ok=True)


def raw_file(filename: str) -> Path:
    """
    Return the full path to a raw CSV file.
    """
    return RAW_DIR / filename


def intermediate_file(name: str) -> Path:
    """
    Return the full path to an intermediate parquet file.
    """
    return INTERMEDIATE_DIR / f"{name}.parquet"


def save_dataset(name: str, df: pd.DataFrame):
    """
    Save a dataframe as parquet.
    """
    df.to_parquet(intermediate_file(name), index=False)


def load_dataset(name: str):
    """
    Load a parquet dataset.
    """
    return pd.read_parquet(intermediate_file(name))


def save_all(datasets: dict):
    for name, df in datasets.items():
        save_dataset(name, df)


def load_all():
    datasets = {}

    for file in INTERMEDIATE_DIR.glob("*.parquet"):
        datasets[file.stem] = pd.read_parquet(file)

    return datasets
