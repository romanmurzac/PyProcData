import pytest
import polars as pl
from pyprocdata.data_masker import DataMasker


@pytest.fixture
def mock_config():
    return {"processes": {"masking": ["name"]}}


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        (["Alice", "Bob"], ["*****MASKED*****", "*****MASKED*****"]),
        (["John", "Doe"], ["*****MASKED*****", "*****MASKED*****"]),
        ([], []),
    ],
)
def test_mask_data(mock_config, input_data, expected_output):
    dataframe = pl.DataFrame({"name": input_data})
    masker = DataMasker(mock_config, dataframe)
    result = masker.mask_data()

    assert result["name"].to_list() == expected_output
