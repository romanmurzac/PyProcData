import json
import pytest
from unittest.mock import mock_open, patch
from pyprocdata.definition_reader import DefinitionReader


@pytest.fixture
def mock_json():
    return '[{"job_name": "job1"}, {"job_name": "job2"}]'


@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_read_definition_empty(mock_file):
    reader = DefinitionReader()
    result = reader.read_definition()
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data='[{"job_name": "job1"}]')
def test_read_definition_single(mock_file):
    reader = DefinitionReader()
    result = reader.read_definition()
    assert result == ["job1"]


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"job_name": "job1"}, {"job_name": "job2"}]',
)
def test_read_definition_multiple(mock_file):
    reader = DefinitionReader()
    result = reader.read_definition()
    assert result == ["job1", "job2"]
