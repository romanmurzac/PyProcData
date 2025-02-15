import json

from ppd_constants import JOB_DEFINITIONS_NAME


class DefinitionReader:
    """
    Read and parse job definitions from a JSON file.
    """

    def read_definition(self) -> list:
        """
        Reads job definitions from a JSON file and extracts job names.\n
        Returns:
            list: A list of job names.
        """
        with open(JOB_DEFINITIONS_NAME, "r") as file:
            job_definitions = json.load(file)
            job_names = [job["job_name"] for job in job_definitions]
            return job_names


# Run the code as a script.
if __name__ == "__main__":
    definition_reader = DefinitionReader()
    job_definitions = definition_reader.read_definition()
    print(job_definitions)
