import polars as pl

from ppd_constants import SOURCE_FILE_PATH


class DataReader:

    def __init__(self, config) -> None:
        self.file_name = SOURCE_FILE_PATH + config["source_file"]
    
    def _identify_format(self):
        file_format = self.file_name.split(".")[-1]
        return file_format
    
    def _generate_function(self):
        format = self._identify_format()
        if format in ["xls", "xlsx"]:
            return eval(f"pl.read_excel('{self.file_name}')")
        return eval(f"pl.read_{format}('{self.file_name}')")

    def read_data(self):
        dataframe = self._generate_function()
        return dataframe


if __name__ == "__main__":
    data_reader = DataReader("./testing_data/nested_data.csv")
    print(data_reader.identify_format())
    print(data_reader.read_data())
