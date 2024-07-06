import polars as pl


class DataMasker:

    def __init__(self, config, raw_data) -> None:
        self.columns = config["processes"]["masking"]
        self.raw_data = raw_data

    def _mask_element(self, element):
        element = "*****MASKED*****"
        return element
    
    def mask_data(self):
        if self.columns:
            for column in self.columns:
                self.raw_data = self.raw_data.with_columns(pl.when(True).then(pl.lit('*****MASKED*****')).otherwise(pl.col(column)).alias(column))
        return self.raw_data
