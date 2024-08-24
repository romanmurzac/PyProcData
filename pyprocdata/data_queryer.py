import polars as pl

from ppd_constants import PPD_DEFINITIONS_PATH


class QueryReader:

    def __init__(self, config, job_definition, raw_data) -> None:
        self.is_transformation = config["processes"]["transformation"]
        self.query_path = PPD_DEFINITIONS_PATH + job_definition + "/" + config["transformation"]
        self.raw_data = raw_data
    
    def _read_query(self):
        with open(self.query_path, "r", encoding="utf-8") as query_file:
            sql_query = query_file.read()
            return sql_query

    def run_query(self):
        if self.is_transformation:
            sql_query = self._read_query()
            with pl.SQLContext(register_globals=True, eager=True) as ctx:
                transformed_data = ctx.execute(sql_query)
                return transformed_data
        else:
            return self.raw_data


if __name__ == "__main__":
    query_reader = QueryReader("ppd_definitions/transformation.sql")
    print(query_reader.read_query())
    query_reader.run_query()