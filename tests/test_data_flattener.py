import pytest
import polars as pl
from pyprocdata.data_flattener import DataFlattener


@pytest.fixture
def mock_config():
    return {"processes": {"flattening": True}}


@pytest.mark.parametrize(
    "input_data,expected_columns",
    [
        ([{"a": 1, "b": 2}, {"a": 3, "b": 4}], ["nested_a", "nested_b"]),
        ([{"x": 10, "y": 20}], ["nested_x", "nested_y"]),
    ],
)
def test_flatten_data(mock_config, input_data, expected_columns):
    dataframe = pl.DataFrame({"nested": input_data})
    flattener = DataFlattener(mock_config, dataframe)
    result = flattener.flatten_data()

    assert all(col in result.columns for col in expected_columns)
