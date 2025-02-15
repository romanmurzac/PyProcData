import pytest
import polars as pl
from unittest.mock import patch, mock_open
from pyprocdata.data_queryer import QueryReader

MOCK_SQL = "SELECT * FROM df"


@pytest.fixture
def mock_dataframe():
    return pl.DataFrame({"col1": [1, 2, 3]})


@pytest.fixture
def mock_config():
    return {"processes": {"transformation": True}, "transformation": "query.sql"}


@patch("builtins.open", new_callable=mock_open, read_data=MOCK_SQL)
@patch("polars.SQLContext.execute")
def test_run_query(mock_execute, mock_open, mock_config, mock_dataframe):
    mock_execute.return_value = mock_dataframe

    query_reader = QueryReader(mock_config, "job1", mock_dataframe)
    result = query_reader.run_query()

    assert result.equals(mock_dataframe)
    mock_execute.assert_called_once()
