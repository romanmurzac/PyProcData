import polars as pl

from ppd_constants import TARGET_FILE_PATH


class DataWriter:
    
    def __init__(self, dataframe, config) -> None:
        self.dataframe = dataframe
        self.file_name = TARGET_FILE_PATH + config["target_file"]
    
    def _identify_format(self):
        file_format = self.file_name.split(".")[-1]
        return file_format

    def write_data(self):
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
