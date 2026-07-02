from sqlalchemy import text

from etl.database import engine


def get_existing_ids(table_name: str, id_column: str):
    """
    Fetch all existing primary keys from a staging table.
    """

    query = text(f"""
        SELECT {id_column}
        FROM staging.{table_name}
        """)

    with engine.begin() as conn:
        rows = conn.execute(query).fetchall()

    return {row[0] for row in rows}
