from etl.quality_checker import SQL_FILE


def test_quality_sql_file_exists():
    assert SQL_FILE.exists()


def test_quality_sql_not_empty():
    sql = SQL_FILE.read_text(encoding="utf-8")

    assert len(sql.strip()) > 0


def test_quality_sql_contains_select():
    sql = SQL_FILE.read_text(encoding="utf-8").lower()

    assert "select" in sql


def test_quality_sql_contains_staging_tables():
    sql = SQL_FILE.read_text(encoding="utf-8").lower()

    assert "stg_customers" in sql
    assert "stg_products" in sql
    assert "stg_orders" in sql
    assert "stg_payments" in sql
    assert "stg_shipments" in sql
