from definition_reader import DefinitionReader
from config_reader import ConfigReader
from data_reader import DataReader
from data_writer import DataWriter
from data_queryer import QueryReader
from data_html_unescaper import HTMLUnescaper
from data_masker import DataMasker
from ppd_logger import logger


class PPDOrchestrator:
    
    def pipeline_run(self) -> None:

        # Initialize and get job definitions.
        definition_reader = DefinitionReader()
        job_definitions = definition_reader.read_definition()
        logger.info(f"job_definitions: {job_definitions}")

        # Process all jobs from definitions.
        for job_definition in job_definitions:

            # Initialize and get job configurations for each job.
            config_reader = ConfigReader(job_definition=job_definition)
            config_params = config_reader.read_config()
            logger.info(f"config: {config_params}")

            # Process all datasets from job configuration.
            for config in config_params:
                
                # Read data from source file.
                data_reader = DataReader(config=config)
                dataframe = data_reader.read_data()
                logger.info("Data was read from source file.")
                print(dataframe)

                # Apply HTML unescaping.
                data_unescaper = HTMLUnescaper(config=config, raw_data=dataframe)
                dataframe = data_unescaper.unescape_html()
                logger.info(f"Data was processed for HTML unescape.")
                print(dataframe)

                # Apply SQL transformation.
                data_transformer = QueryReader(config=config, job_definition=job_definition, raw_data=dataframe)
                dataframe = data_transformer.run_query()
                logger.info("Data was processed for SQL transformation.")
                print(dataframe)

                # Apply flattening.

                # Apply masking.
                data_masker = DataMasker(config=config, raw_data=dataframe)
                dataframe = data_masker.mask_data()
                print(dataframe)

                # Write processed dataframe to output file.
                data_writer = DataWriter(dataframe=dataframe, config=config)
                data_writer.write_data()
                logger.info(f"Data was written.")


if __name__ == "__main__":
    ppd_orchestrator = PPDOrchestrator()
    ppd_orchestrator.pipeline_run()
