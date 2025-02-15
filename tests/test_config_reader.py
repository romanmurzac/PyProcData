import pytest
from unittest.mock import patch, mock_open
from pyprocdata.config_reader import ConfigReader


@pytest.mark.parametrize(
    "mock_data,expected_flattening,expected_masking",
    [
        ('{"processes": {"flattening": true, "masking": ["name"]}}', True, ["name"]),
        ('{"processes": {"flattening": false, "masking": []}}', False, []),
        ('{"processes": {}}', None, None),
    ],
)
@patch("builtins.open", new_callable=mock_open)
def test_read_config(mock_file, mock_data, expected_flattening, expected_masking):
    mock_file.return_value.read.return_value = mock_data

    reader = ConfigReader("job1")
    result = reader.read_config()

    assert result["processes"].get("flattening") == expected_flattening
    assert result["processes"].get("masking") == expected_masking
