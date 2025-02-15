import polars as pl

from ppd_constants import SOURCE_FILE_PATH


class DataReader:
    """
    A class to read data from various file formats into a Polars DataFrame.\n
    Attributes:
        file_name (str): Full path to the source file.
    """

    def __init__(self, config: dict) -> None:
        """
        Initializes the DataReader with a configuration dictionary.\n
        Args:
            config (dict): A dictionary containing the source file path.
        """
        self.file_name = SOURCE_FILE_PATH + config["source_file"]

    def _identify_format(self) -> str:
        """
        Identifies the file format based on its extension.\n
        Returns:
            str: The file extension (e.g., 'csv', 'json', 'parquet').
        """
        file_format = self.file_name.split(".")[-1]
        return file_format

    def _read_file(self) -> pl.DataFrame:
        """
        Reads the file using the appropriate Polars function based on file format.\n
        Returns:
            pl.DataFrame: The loaded DataFrame.
        """
        format = self._identify_format()
        if format in ["xls", "xlsx"]:
            return eval(f"pl.read_excel('{self.file_name}')")
        return eval(f"pl.read_{format}('{self.file_name}')")

    def read_data(self) -> pl.DataFrame:
        """
        Reads the data and returns a Polars DataFrame.\n
        Returns:
            pl.DataFrame: The loaded DataFrame.
        """
        dataframe = self._read_file()
        return dataframe


# Run the code as a script.
if __name__ == "__main__":
    config = {"source_file": "data_query.csv"}
    data_reader = DataReader(config)
    print("File format:", data_reader._identify_format())
    df = data_reader.read_data()
    print(df)
