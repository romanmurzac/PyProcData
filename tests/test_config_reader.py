import pytest
import json

from src.config_reader import ConfigReader


class TestConfigReader:

    @pytest.fixture
    def valid_json_file(self, tmp_path):
        data = {"key1": "value1", "key2": "value2"}
        file_path = tmp_path / "valid_config.json"
        with open(file_path, 'w') as file:
            json.dump(data, file)
        return file_path

    @pytest.fixture
    def invalid_json_file(self, tmp_path):
        file_path = tmp_path / "invalid_config.json"
        with open(file_path, 'w') as file:
            file.write("{key1: value1, key2: value2")
        return file_path

    @pytest.fixture
    def empty_json_file(self, tmp_path):
        file_path = tmp_path / "empty_config.json"
        with open(file_path, 'w') as file:
            file.write("{}")
        return file_path

    @pytest.mark.parametrize("fixture_name, expected_output, expected_exception", [
        ("valid_json_file", {"key1": "value1", "key2": "value2"}, None),
        ("invalid_json_file", None, json.JSONDecodeError),
        ("empty_json_file", {}, None),
    ])
    def test_read_config(self, request, fixture_name, expected_output, expected_exception):
        """
        Parametrized test for reading JSON configuration files.
        
        This test verifies that the read_config method correctly handles various JSON files
        including valid, invalid, and empty JSON files.
        
        :param request: The pytest request object to access fixtures dynamically.
        :param fixture_name: The name of the fixture to be used.
        :param expected_output: The expected output dictionary.
        :param expected_exception: The expected exception, if any.
        """
        file_path = request.getfixturevalue(fixture_name)
        config_reader = ConfigReader(file_path)

        if expected_exception:
            with pytest.raises(expected_exception):
                config_reader.read_config()
        else:
            config = config_reader.read_config()
            assert config == expected_output

    def test_read_nonexistent_file(self):
        """
        Test reading a nonexistent JSON configuration file.
        
        This test verifies that the read_config method raises a FileNotFoundError
        when attempting to read a nonexistent JSON configuration file.
        """
        config_reader = ConfigReader("nonexistent_config.json")
        with pytest.raises(FileNotFoundError):
            config_reader.read_config()
