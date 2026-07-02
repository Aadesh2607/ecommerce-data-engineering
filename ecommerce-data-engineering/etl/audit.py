from datetime import datetime

from sqlalchemy import text

from etl.database import engine


def start_audit(pipeline_name: str):

    with engine.begin() as conn:
        result = conn.execute(
            text("""
                INSERT INTO metadata.etl_audit
                (
                    pipeline_name,
                    start_time,
                    status
                )

                VALUES
                (
                    :pipeline_name,
                    :start_time,
                    'RUNNING'
                )

                RETURNING run_id;
            """),
            {"pipeline_name": pipeline_name, "start_time": datetime.now()},
        )

        return result.scalar()


def finish_audit(
    run_id: int, extracted: int, loaded: int, status: str, error_message=None
):

    end_time = datetime.now()

    with engine.begin() as conn:
        start_time = conn.execute(
            text("""
                SELECT start_time
                FROM metadata.etl_audit
                WHERE run_id=:run_id
            """),
            {"run_id": run_id},
        ).scalar()

        duration = (end_time - start_time).total_seconds()

        conn.execute(
            text("""
                UPDATE metadata.etl_audit

                SET

                end_time=:end_time,

                duration_seconds=:duration,

                status=:status,

                records_extracted=:extracted,

                records_loaded=:loaded,

                error_message=:error

                WHERE run_id=:run_id
            """),
            {
                "run_id": run_id,
                "end_time": end_time,
                "duration": duration,
                "status": status,
                "extracted": extracted,
                "loaded": loaded,
                "error": error_message,
            },
        )
