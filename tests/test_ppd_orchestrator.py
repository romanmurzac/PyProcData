import pytest
import polars as pl
from unittest.mock import patch
from pyprocdata.ppd_orchestrator import PPDOrchestrator


@pytest.fixture
def mock_job_definitions():
    return ["job1"]


@pytest.fixture
def mock_config_params():
    return [
        {
            "source_file": "data.csv",
            "target_file": "output.csv",
            "processes": {
                "flattening": True,
                "html_unescape": ["name"],
                "masking": ["name"],
                "transformation": "query.sql",
            },
        }
    ]


@pytest.fixture
def mock_dataframe():
    return pl.DataFrame({"name": ["Alice &amp; Bob"], "age": [25]})


@pytest.fixture
def mock_transformed_dataframe():
    return pl.DataFrame({"name": ["Alice & Bob"], "age": [25]})


@pytest.fixture
def mock_masked_dataframe():
    return pl.DataFrame({"name": ["*****MASKED*****"], "age": [25]})


@pytest.fixture
def mock_flattened_dataframe():
    return pl.DataFrame(
        {"name": ["*****MASKED*****"], "age": [25]}
    )  # Assuming flattening doesn’t change these fields


@patch("pyprocdata.ppd_orchestrator.DefinitionReader")
@patch("pyprocdata.ppd_orchestrator.ConfigReader")
@patch("pyprocdata.ppd_orchestrator.DataReader")
@patch("pyprocdata.ppd_orchestrator.HTMLUnescaper")
@patch("pyprocdata.ppd_orchestrator.QueryReader")
@patch("pyprocdata.ppd_orchestrator.DataMasker")
@patch("pyprocdata.ppd_orchestrator.DataFlattener")
@patch("pyprocdata.ppd_orchestrator.DataWriter")
@patch("pyprocdata.ppd_orchestrator.logger")
def test_pipeline_run(
    mock_logger,
    mock_data_writer,
    mock_data_flattener,
    mock_data_masker,
    mock_query_reader,
    mock_html_unescaper,
    mock_data_reader,
    mock_config_reader,
    mock_definition_reader,
    mock_job_definitions,
    mock_config_params,
    mock_dataframe,
    mock_transformed_dataframe,
    mock_masked_dataframe,
    mock_flattened_dataframe,
):
    # Mock the behavior of each component in the pipeline.
    mock_definition_reader.return_value.read_definition.return_value = (
        mock_job_definitions
    )
    mock_config_reader.return_value.read_config.return_value = mock_config_params

    # Mock data reader.
    mock_data_reader.return_value.read_data.return_value = mock_dataframe

    # Mock HTML Unescape.
    mock_html_unescaper.return_value.unescape_html.return_value = (
        mock_transformed_dataframe
    )

    # Mock SQL Query transformation.
    mock_query_reader.return_value.run_query.return_value = mock_transformed_dataframe

    # Mock data masking.
    mock_data_masker.return_value.mask_data.return_value = mock_masked_dataframe

    # Mock flattening.
    mock_data_flattener.return_value.flatten_data.return_value = (
        mock_flattened_dataframe
    )

    # Mock DataWriter (ensure it's called).
    mock_data_writer.return_value.write_data.return_value = None

    # Run orchestrator.
    orchestrator = PPDOrchestrator()
    orchestrator.pipeline_run()

    # Assertions to ensure each step is executed in order.
    mock_definition_reader.return_value.read_definition.assert_called_once()
    mock_config_reader.return_value.read_config.assert_called_once()

    mock_data_reader.return_value.read_data.assert_called_once()
    mock_html_unescaper.return_value.unescape_html.assert_called_once()
    mock_query_reader.return_value.run_query.assert_called_once()
    mock_data_masker.return_value.mask_data.assert_called_once()
    mock_data_flattener.return_value.flatten_data.assert_called_once()
    mock_data_writer.return_value.write_data.assert_called_once()

    # Ensure logs are created.
    mock_logger.info.assert_called()
