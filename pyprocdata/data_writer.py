import polars as pl

from ppd_constants import TARGET_FILE_PATH


class DataWriter:
    """
    A class to write a Polars DataFrame to various file formats.\n
    Attributes:
        dataframe (pl.DataFrame): The DataFrame to be written.
        file_name (str): Full path to the target file.
    """

    def __init__(self, dataframe: pl.DataFrame, config: dict) -> None:
        """
        Initializes the DataWriter with a DataFrame and configuration.\n
        Args:
            dataframe (pl.DataFrame): The data to be written.
            config (dict): A dictionary containing the target file path.
        """
        self.dataframe = dataframe
        self.file_name = TARGET_FILE_PATH + config["target_file"]

    def _identify_format(self) -> str:
        """
        Identifies the file format based on the file extension.\n
        Returns:
            str: The file extension in lowercase.
        """
        file_format = self.file_name.split(".")[-1].lower()
        return file_format

    def write_data(self) -> None:
        """
        Writes the DataFrame to the target file based on its format.
        """
        format = self._identify_format()
        match format:
            case "xls", "xlsx":
                self.dataframe.write_excel(self.file_name)
            case "csv":
                self.dataframe.write_csv(self.file_name)
            case "json":
                self.dataframe.write_json(self.file_name)
            case "avro":
                self.dataframe.write_avro(self.file_name)
            case "parquet":
                self.dataframe.write_parquet(self.file_name)
            case _:
                raise ValueError(f"Unsupported file format: {format}")


# Run the code as a script.
if __name__ == "__main__":
    df = pl.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
    config = {"target_file": "output_data.csv"}
    writer = DataWriter(df, config)
    writer.write_data()
