import pytest
import polars as pl
from unittest.mock import patch
from pyprocdata.data_writer import DataWriter


@pytest.fixture
def mock_dataframe():
    return pl.DataFrame({"col1": [1, 2, 3]})


@pytest.fixture
def mock_config_csv():
    return {"target_file": "output.csv"}


@pytest.fixture
def mock_config_json():
    return {"target_file": "output.json"}


@patch("polars.DataFrame.write_csv")
def test_write_csv(mock_write_csv, mock_dataframe, mock_config_csv):
    writer = DataWriter(mock_dataframe, mock_config_csv)
    writer.write_data()
    mock_write_csv.assert_called_once()


@patch("polars.DataFrame.write_json")
def test_write_json(mock_write_json, mock_dataframe, mock_config_json):
    writer = DataWriter(mock_dataframe, mock_config_json)
    writer.write_data()
    mock_write_json.assert_called_once()
