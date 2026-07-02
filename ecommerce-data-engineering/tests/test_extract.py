from etl.extract import FILES


def test_all_expected_csv_files_exist():
    """
    Verify all expected datasets are configured.
    """

    expected = {
        "customers",
        "products",
        "orders",
        "payments",
        "shipments",
    }

    assert set(FILES.keys()) == expected


def test_csv_filenames():

    for filename in FILES.values():
        assert filename.endswith(".csv")


def test_dataset_count():

    assert len(FILES) == 5
