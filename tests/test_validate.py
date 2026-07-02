from unittest.mock import patch

import pandas as pd

from etl.validate import validate_data


@patch("etl.validate.save_dataframe")
@patch("etl.validate.load_dataframe")
def test_validate_removes_duplicates(
    mock_load,
    mock_save,
):
    """
    Duplicate rows should be removed.
    """

    df = pd.DataFrame(
        {
            "customer_id": [1, 1, 2],
            "name": [
                "John",
                "John",
                "Jane",
            ],
        }
    )

    mock_load.return_value = df

    validate_data()

    saved_df = mock_save.call_args[0][0]

    assert len(saved_df) == 2


@patch("etl.validate.save_dataframe")
@patch("etl.validate.load_dataframe")
def test_validate_removes_empty_rows(
    mock_load,
    mock_save,
):
    """
    Empty rows should be removed.
    """

    df = pd.DataFrame(
        {
            "customer_id": [1, None],
            "name": [
                "John",
                None,
            ],
        }
    )

    mock_load.return_value = df

    validate_data()

    saved_df = mock_save.call_args[0][0]

    assert len(saved_df) == 1


@patch("etl.validate.save_dataframe")
@patch("etl.validate.load_dataframe")
def test_validate_resets_index(
    mock_load,
    mock_save,
):
    """
    Index should be reset after cleaning.
    """

    df = pd.DataFrame(
        {
            "customer_id": [1, 1, 2],
            "name": [
                "John",
                "John",
                "Jane",
            ],
        }
    )

    df = df.drop_duplicates()

    df.index = [5, 8]

    mock_load.return_value = df

    validate_data()

    saved_df = mock_save.call_args[0][0]

    assert list(saved_df.index) == [0, 1]
