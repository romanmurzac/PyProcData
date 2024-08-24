import json

from ppd_constants import JOB_DEFINITIONS_NAME


class DefinitionReader:

    def read_definition(self) -> list:
        with open(JOB_DEFINITIONS_NAME, "r") as file:
            job_definitions = json.load(file)
            job_names = [job["job_name"] for job in job_definitions]
            return job_names


if __name__ == "__main__":
    definition_reader = DefinitionReader()
    print(definition_reader.read_definition())
    