from etl.database import engine

try:
    with engine.connect() as conn:
        version = conn.exec_driver_sql("SELECT version();").scalar()
        print(version)
except Exception as e:
    print(e)
