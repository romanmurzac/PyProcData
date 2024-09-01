import polars as pl


class Flattener:

    def __init__(self, config, raw_data) -> None:
        self.is_flatten = config["processes"]["flattening"]
        self.raw_data = pl.DataFrame(raw_data)

    def _get_composed_columns(self, datatype):
        schema = self.raw_data.schema
        if datatype == "STRUCT":
            composed_columns = [col for col, datatype in schema.items() if isinstance(datatype, pl.datatypes.Struct)]
        elif datatype == "LIST":
            composed_columns = [col for col, datatype in schema.items() if isinstance(datatype, pl.datatypes.List)]
        return composed_columns
    
    def _get_subcolumns(self, column):
        columns = self.raw_data.select(pl.col(column).struct.field("*")).columns
        return columns
    
    def _rename_column(self, column, subcolumn):
        self.raw_data = self.raw_data.rename({subcolumn: f"{column}_{subcolumn}"})
        return self.raw_data
    
    def _flatten_level(self, datatype, column):
        if datatype == "STRUCT":
            self.raw_data = self.raw_data.unnest(column)
        elif datatype == "LIST":
            self.raw_data = self.raw_data.explode(column)
        return self.raw_data
    
    def flat_data(self):
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
  

if __name__ == "__main__":
    config = {"processes": {"flattening": True}}
    df = pl.DataFrame({"a": {"b": [1, 2, 3], "c": "text"}, "d": [{"e": "string", "f": "str"}, {"e": "int"}, {"f": "str"}]})
    flattener = Flattener(config, df)
    fully_flatten = flattener.flat_data()
    print(fully_flatten)
