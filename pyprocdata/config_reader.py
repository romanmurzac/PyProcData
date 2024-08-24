import json

from ppd_constants import PPD_DEFINITIONS_PATH, CONFIG_FILE_NAME
from definition_reader import DefinitionReader


class ConfigReader:

    def __init__(self, job_definition) -> None:
        self.job_definition = job_definition
    
    def read_config(self) -> dict:
        with open(f"{PPD_DEFINITIONS_PATH}{self.job_definition}/{CONFIG_FILE_NAME}", "r") as file:
            config_file = json.load(file)
        return config_file


if __name__ == "__main__":
    definition_reader = DefinitionReader()
    definitions = definition_reader.read_definition()
    print(definitions)
    config_reader = ConfigReader(definitions)
    configs = config_reader.read_config()
    print(configs)
