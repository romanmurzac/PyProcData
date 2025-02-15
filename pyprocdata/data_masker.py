import polars as pl


class DataMasker:
    """
    Mask sensitive data in specified columns of a Polars DataFrame.\n
    Attributes:
        columns (list): List of column names to be masked.
        raw_data (pl.DataFrame): The input DataFrame containing the data to be processed.
    """

    def __init__(self, config: dict, raw_data: pl.DataFrame) -> None:
        """
        Initializes the DataMasker with configuration and raw data.\n
        Args:
            config (dict): A dictionary containing process configurations.
            raw_data (pl.DataFrame): The raw input data.
        """
        self.columns = config["processes"]["masking"]
        self.raw_data = raw_data

    def _mask_element(self, element) -> str:
        """
        Masks a given element with a predefined masked value.\n
        Args:
            element: The original data element.
        Returns:
            str: The masked string.
        """
        element = "*****MASKED*****"
        return element

    def mask_data(self) -> pl.DataFrame:
        """
        Masks the specified columns in the DataFrame by replacing all values with a masked string.\n
        Returns:
            pl.DataFrame: The updated DataFrame with masked data.
        """
        if self.columns:
            for column in self.columns:
                self.raw_data = self.raw_data.with_columns(
                    pl.when(True)
                    .then(pl.lit("*****MASKED*****"))
                    .otherwise(pl.col(column))
                    .alias(column)
                )
        return self.raw_data


# Run the code as a script.
if __name__ == "__main__":
    df = pl.DataFrame({"name": ["Alice", "Bob"], "ssn": ["123-45-6789", "987-65-4321"]})
    config = {"processes": {"masking": ["ssn"]}}
    masker = DataMasker(config, df)
    masked_df = masker.mask_data()
    print(masked_df)
