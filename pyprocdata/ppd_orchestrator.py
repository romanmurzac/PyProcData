from definition_reader import DefinitionReader
from config_reader import ConfigReader
from data_reader import DataReader
from data_writer import DataWriter
from data_queryer import QueryReader
from data_html_unescaper import HTMLUnescaper
from data_masker import DataMasker
from data_flattener import DataFlattener
from ppd_logger import logger


class PPDOrchestrator:
    """
    Orchestrates the entire data processing pipeline.
    """

    def pipeline_run(self) -> None:
        """
        Runs the end-to-end pipeline for all job definitions.
        """
        try:
            # Initialize and get job definitions.
            definition_reader = DefinitionReader()
            job_definitions = definition_reader.read_definition()
            logger.info(f"Job Definitions Found: {job_definitions}")

            # Process all jobs from definitions.
            for job_definition in job_definitions:
                try:
                    logger.info(f"Processing Job: {job_definition}")

                    # Initialize and get job configurations for each job.
                    config_reader = ConfigReader(job_definition=job_definition)
                    config_params = config_reader.read_config()
                    logger.info(f"Config Loaded: {config_params}")

                    # Skip this job if config is empty.
                    if not config_params:
                        logger.warning(
                            f"No configuration found for job: {job_definition}. Skipping."
                        )
                        continue

                    # Process all datasets from job configuration.
                    for config in config_params:
                        try:
                            logger.info(
                                f"Processing Dataset: {config.get('source_file', 'UNKNOWN')}"
                            )

                            # Read data from source file.
                            data_reader = DataReader(config=config)
                            dataframe = data_reader.read_data()
                            logger.info(
                                f"Data Read Successfully ({dataframe.shape[0]} rows, {len(dataframe.columns)} columns)"
                            )

                            # Apply HTML unescaping.
                            if config["processes"].get("html_unescape"):
                                data_unescaper = HTMLUnescaper(
                                    config=config, raw_data=dataframe
                                )
                                dataframe = data_unescaper.unescape_html()
                                logger.info("Applied HTML Unescape.")

                            # Apply SQL transformation.
                            if config["processes"].get("transformation"):
                                data_transformer = QueryReader(
                                    config=config,
                                    job_definition=job_definition,
                                    raw_data=dataframe,
                                )
                                dataframe = data_transformer.run_query()
                                logger.info("SQL Transformation Applied.")

                            # Apply masking.
                            if config["processes"].get("masking"):
                                data_masker = DataMasker(
                                    config=config, raw_data=dataframe
                                )
                                dataframe = data_masker.mask_data()
                                logger.info("Data Masking Applied.")

                            # Apply flattening.
                            if config["processes"].get("flattening"):
                                data_flattener = DataFlattener(
                                    config=config, raw_data=dataframe
                                )
                                dataframe = data_flattener.flatten_data()
                                logger.info("Data Flattening Applied.")

                            # Write processed dataframe to output file.
                            data_writer = DataWriter(dataframe=dataframe, config=config)
                            data_writer.write_data()
                            logger.info(
                                f"Data Successfully Written to {config.get('target_file', 'UNKNOWN')}."
                            )

                        except Exception as e:
                            logger.error(
                                f"Error processing dataset {config.get('source_file', 'UNKNOWN')}: {e}",
                                exc_info=True,
                            )

                except Exception as e:
                    logger.error(
                        f"Error processing job {job_definition}: {e}", exc_info=True
                    )

        except Exception as e:
            logger.critical(
                f"Pipeline failed due to unexpected error: {e}", exc_info=True
            )


# Run the code as a script.
if __name__ == "__main__":
    ppd_orchestrator = PPDOrchestrator()
    ppd_orchestrator.pipeline_run()
