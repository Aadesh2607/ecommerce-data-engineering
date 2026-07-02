# Ecommerce Data Engineering Pipeline

An end-to-end Data Engineering project that builds a modern ETL pipeline using Python, PostgreSQL, Docker, SQL, and Apache Airflow.

The pipeline extracts raw ecommerce data, validates it, transforms it, loads it into a staging database, builds a dimensional data warehouse, creates analytics views, and performs automated data quality checks.

---

## Tech Stack

- Python
- PostgreSQL
- SQLAlchemy
- Pandas
- Docker
- Apache Airflow
- SQL
- Pytest

---

## Project Architecture

```
CSV Files
     │
     ▼
Extract
     │
     ▼
Validate
     │
     ▼
Transform
     │
     ▼
Load (Staging)
     │
     ▼
Warehouse
     │
     ▼
Analytics Views
     │
     ▼
Data Quality Checks
```

---

## Project Structure

```
etl/
    extract.py
    validate.py
    transform.py
    load.py
    warehouse_loader.py
    analytics_loader.py
    quality_checker.py
    pipeline.py

sql/
    warehouse.sql
    analytics.sql
    quality_checks.sql

tests/
    ...

dashboard/

airflow/

docker/
```

---

## Features

- Automated ETL pipeline
- Data validation
- Duplicate removal
- Null handling
- Data transformation
- Incremental loading
- Star schema warehouse
- Analytics SQL views
- Automated data quality checks
- Logging
- Docker support
- Airflow orchestration
- Unit testing using Pytest

---

## Running the Pipeline

```bash
python -m etl.pipeline
```

---

## Running Quality Checks

```bash
python -m etl.quality_checker
```

---

## Running Tests

```bash
pytest
```

---

## Test Coverage

- Extract
- Validation
- Transform
- Load
- Warehouse
- Pipeline
- Data Quality

---

## Author

Aadesh Gaikwad