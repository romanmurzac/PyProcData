import polars as pl


class DataFlattener:
    """
    Flatten nested structures (Struct and Array) within a DataFrame.\n
    Attributes:
        is_flatten (bool): Determines whether the flattening process should be applied.
        raw_data (pl.DataFrame): The input data to be flattened.
    """

    def __init__(self, config: dict, raw_data: pl.DataFrame) -> None:
        """
        Initializes the DataFlattener with configuration and raw data.\n
        Args:
            config (dict): A configuration dictionary containing flattening settings.
            raw_data (dict or pl.DataFrame): The raw input data.
        """
        self.is_flatten = config["processes"]["flattening"]
        self.raw_data = pl.DataFrame(raw_data)

    def _get_composed_columns(self, datatype: str) -> list:
        """
        Identifies and retrieves column names that contain nested structures.\n
        Args:
            datatype (str): The type of nested structure ("STRUCT" or "LIST").
        Returns:
            list: A list of column names that match the specified nested structure.
        """
        schema = self.raw_data.schema
        if datatype == "STRUCT":
            composed_columns = [
                col
                for col, datatype in schema.items()
                if isinstance(datatype, pl.datatypes.Struct)
            ]
        elif datatype == "LIST":
            composed_columns = [
                col
                for col, datatype in schema.items()
                if isinstance(datatype, pl.datatypes.List)
            ]
        return composed_columns

    def _get_subcolumns(self, column: str) -> list:
        """
        Retrieves the subcolumn names of a STRUCT column.\n
        Args:
            column (str): The column name containing a STRUCT.
        Returns:
            list: A list of subcolumn names.
        """
        columns = self.raw_data.select(pl.col(column).struct.field("*")).columns
        return columns

    def _rename_column(self, column: str, subcolumn: str) -> pl.DataFrame:
        """
        Renames subcolumns after unnesting to maintain uniqueness.\n
        Args:
            column (str): The original parent column.
            subcolumn (str): The extracted subcolumn.
        Returns:
            pl.DataFrame: The updated DataFrame with renamed columns.
        """
        self.raw_data = self.raw_data.rename({subcolumn: f"{column}_{subcolumn}"})
        return self.raw_data

    def _flatten_level(self, datatype: str, column: str) -> pl.DataFrame:
        """
        Flattens a specific column based on its nested structure type.\n
        Args:
            datatype (str): The type of structure to flatten ("STRUCT" or "LIST").
            column (str): The column to be flattened.
        Returns:
            pl.DataFrame: The updated DataFrame after flattening.
        """
        if datatype == "STRUCT":
            self.raw_data = self.raw_data.unnest(column)
        elif datatype == "LIST":
            self.raw_data = self.raw_data.explode(column)
        return self.raw_data

    def flatten_data(self) -> pl.DataFrame:
        """
        Recursively flattens all nested STRUCT and LIST columns in the DataFrame.\n
        Returns:
            pl.DataFrame: A fully flattened DataFrame.
        """
        if self.is_flatten:

            is_nested = True
            while is_nested:

                struct_columns = self._get_composed_columns("STRUCT")
                for column in struct_columns:
                    nested_columns = self._get_subcolumns(column)
                    self.raw_data = self._flatten_level("STRUCT", column)

                    for subcolumn in nested_columns:
                        self.raw_data = self._rename_column(column, subcolumn)

                list_columns = self._get_composed_columns("LIST")
                for column in list_columns:
                    self.raw_data = self._flatten_level("LIST", column)

                if not struct_columns and not list_columns:
                    is_nested = False

            return self.raw_data

        else:
            return self.raw_data


# Run the code as a script.
if __name__ == "__main__":
    config = {"processes": {"flattening": True}}
    df = pl.DataFrame(
        {
            "a": {"b": [1, 2, 3], "c": "text"},
            "d": [{"e": "string", "f": "str"}, {"e": "int"}, {"f": "str"}],
        }
    )
    flattener = DataFlattener(config, df)
    fully_flatten = flattener.flatten_data()
    print(fully_flatten)
