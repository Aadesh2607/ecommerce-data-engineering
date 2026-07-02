from etl.warehouse_loader import SQL_FILE


def test_warehouse_sql_file_exists():
    assert SQL_FILE.exists()


def test_warehouse_sql_not_empty():
    sql = SQL_FILE.read_text(encoding="utf-8")

    assert len(sql.strip()) > 0


def test_warehouse_sql_contains_truncate():
    sql = SQL_FILE.read_text(encoding="utf-8").lower()

    assert "truncate table" in sql


def test_warehouse_sql_contains_fact_table():
    sql = SQL_FILE.read_text(encoding="utf-8").lower()

    assert "fact_sales" in sql


def test_warehouse_sql_contains_dimension_tables():
    sql = SQL_FILE.read_text(encoding="utf-8").lower()

    assert "dim_customers" in sql
    assert "dim_products" in sql
    assert "dim_date" in sql
