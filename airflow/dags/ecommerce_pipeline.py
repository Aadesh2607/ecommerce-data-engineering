# isort: skip_file
# ruff: noqa

from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    "owner": "Aadesh",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="ecommerce_etl_pipeline",
    description="Production Ecommerce ETL Pipeline",
    start_date=datetime(2026, 7, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    tags=["etl", "postgres", "warehouse"],
) as dag:
    run_pipeline = BashOperator(
        task_id="run_etl_pipeline",
        cwd="/opt/project",
        bash_command="python -m etl.pipeline",
    )

    run_pipeline
