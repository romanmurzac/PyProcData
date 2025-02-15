import pytest
import polars as pl
from unittest.mock import patch
from pyprocdata.data_reader import DataReader


@pytest.fixture
def mock_config_csv():
    return {"source_file": "data.csv"}


@pytest.fixture
def mock_config_json():
    return {"source_file": "data.json"}


@patch("polars.read_csv")
def test_read_data_csv(mock_read_csv, mock_config_csv):
    mock_df = pl.DataFrame({"col1": [1, 2, 3]})
    mock_read_csv.return_value = mock_df

    reader = DataReader(mock_config_csv)
    result = reader.read_data()

    assert result.equals(mock_df)
    mock_read_csv.assert_called_once()


@patch("polars.read_json")
def test_read_data_json(mock_read_json, mock_config_json):
    mock_df = pl.DataFrame({"col1": [4, 5, 6]})
    mock_read_json.return_value = mock_df

    reader = DataReader(mock_config_json)
    result = reader.read_data()

    assert result.equals(mock_df)
    mock_read_json.assert_called_once()
