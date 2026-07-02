from unittest.mock import patch

from etl.pipeline import run_pipeline


@patch("etl.pipeline.run_quality_checks")
@patch("etl.pipeline.build_analytics")
@patch("etl.pipeline.build_warehouse")
@patch("etl.pipeline.load_data")
@patch("etl.pipeline.transform_data")
@patch("etl.pipeline.validate_data")
@patch("etl.pipeline.extract_data")
def test_pipeline_calls_all_steps(
    mock_extract,
    mock_validate,
    mock_transform,
    mock_load,
    mock_warehouse,
    mock_analytics,
    mock_quality,
):
    run_pipeline()

    mock_extract.assert_called_once()
    mock_validate.assert_called_once()
    mock_transform.assert_called_once()
    mock_load.assert_called_once()
    mock_warehouse.assert_called_once()
    mock_analytics.assert_called_once()
    mock_quality.assert_called_once()


@patch("etl.pipeline.run_quality_checks")
@patch("etl.pipeline.build_analytics")
@patch("etl.pipeline.build_warehouse")
@patch("etl.pipeline.load_data")
@patch("etl.pipeline.transform_data")
@patch("etl.pipeline.validate_data")
@patch("etl.pipeline.extract_data")
def test_pipeline_execution_order(
    mock_extract,
    mock_validate,
    mock_transform,
    mock_load,
    mock_warehouse,
    mock_analytics,
    mock_quality,
):
    order = []

    mock_extract.side_effect = lambda: order.append("extract")
    mock_validate.side_effect = lambda: order.append("validate")
    mock_transform.side_effect = lambda: order.append("transform")
    mock_load.side_effect = lambda: order.append("load")
    mock_warehouse.side_effect = lambda: order.append("warehouse")
    mock_analytics.side_effect = lambda: order.append("analytics")
    mock_quality.side_effect = lambda: order.append("quality")

    run_pipeline()

    assert order == [
        "extract",
        "validate",
        "transform",
        "load",
        "warehouse",
        "analytics",
        "quality",
    ]
