import polars as pl

from ppd_constants import PPD_DEFINITIONS_PATH


class QueryReader:
    """
    A class to read and execute SQL queries on a Polars DataFrame.\n
    Attributes:
        is_transformation (bool): Flag to determine if the transformation should be applied.
        query_path (str): Path to the SQL query file.
        raw_data (pl.DataFrame): The input DataFrame to be transformed.
    """

    def __init__(
        self, config: dict, job_definition: str, raw_data: pl.DataFrame
    ) -> None:
        """
        Initializes the QueryReader with configuration, job definition, and raw data.\n
        Args:
            config (dict): A dictionary containing process configurations.
            job_definition (str): The job definition name used to locate the SQL query.
            raw_data (pl.DataFrame): The raw input data to be transformed.
        """
        self.is_transformation = config["processes"]["transformation"]
        self.query_path = (
            PPD_DEFINITIONS_PATH + job_definition + "/" + config["transformation"]
        )
        self.raw_data = raw_data

    def _read_query(self) -> str:
        """
        Reads the SQL query from the specified file.\n
        Returns:
            str: The SQL query as a string.
        """
        with open(self.query_path, "r", encoding="utf-8") as query_file:
            sql_query = query_file.read()
            return sql_query

    def run_query(self) -> pl.DataFrame:
        """
        Executes the SQL query on the given Polars DataFrame.\n
        Returns:
            pl.DataFrame: The transformed DataFrame if transformation is enabled,
                          otherwise returns the raw DataFrame.
        """
        if self.is_transformation:
            sql_query = self._read_query()
            with pl.SQLContext(register_globals=True, eager=True) as ctx:
                transformed_data = ctx.execute(sql_query)
                return transformed_data
        else:
            return self.raw_data


# Run the code as a script.
if __name__ == "__main__":
    config = {
        "transformation": "transformation.sql",
        "processes": {"transformation": True},
    }
    dataframe = pl.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
    query_reader = QueryReader(config, "sample_2", dataframe)
    print(query_reader._read_query())
    transformed_df = query_reader.run_query()
    print(transformed_df)
