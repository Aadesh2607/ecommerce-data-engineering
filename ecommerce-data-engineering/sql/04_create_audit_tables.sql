CREATE SCHEMA IF NOT EXISTS metadata;

CREATE TABLE IF NOT EXISTS metadata.etl_audit
(
    run_id SERIAL PRIMARY KEY,

    pipeline_name VARCHAR(100),

    start_time TIMESTAMP,

    end_time TIMESTAMP,

    duration_seconds NUMERIC(10,2),

    status VARCHAR(20),

    records_extracted INTEGER,

    records_loaded INTEGER,

    error_message TEXT
);