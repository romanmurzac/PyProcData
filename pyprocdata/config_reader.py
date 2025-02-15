import json

from ppd_constants import PPD_DEFINITIONS_PATH, CONFIG_FILE_NAME
from definition_reader import DefinitionReader


class ConfigReader:
    """
    Reads and loads configuration files for all job definitions.
    The configuration files are expected to be in JSON format and stored in a predefined path.\n
    Attributes:
        job_definition (str): The name of the job definition whose configuration file needs to be read.
    """

    def __init__(self, job_definition: str) -> None:
        """
        Initializes the ConfigReader with a specific job definition.\n
        Args:
            job_definition (str): The name of the job definition.
        """
        self.job_definition = job_definition

    def read_config(self) -> dict:
        """
        Reads and loads the configuration file for the specified job definition.\n
        Returns:
            dict: A dictionary containing the parsed configuration data.
        """
        with open(
            f"{PPD_DEFINITIONS_PATH}{self.job_definition}/{CONFIG_FILE_NAME}", "r"
        ) as file:
            config_file = json.load(file)
        return config_file


# Run the code as a script.
if __name__ == "__main__":
    definitions = DefinitionReader().read_definition()
    for definition in definitions:
        config_reader = ConfigReader(definition)
        configs = config_reader.read_config()
        print(configs)
