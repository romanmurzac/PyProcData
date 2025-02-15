import html
import polars as pl


class HTMLUnescaper:
    """
    Unescape HTML-encoded strings in specified columns of a DataFrame.\n
    Attributes:
        columns_unescaping (list): List of column names to apply HTML unescaping.
        raw_data (pl.DataFrame): The input DataFrame containing the data to be processed.
    """

    def __init__(self, config: dict, raw_data: pl.DataFrame) -> None:
        """
        Initializes the HTMLUnescaper with configuration and raw data.\n
        Args:
            config (dict): A dictionary containing process configurations.
            raw_data (pl.DataFrame): The raw input data.
        """
        self.columns_unescaping = config["processes"]["html_unescape"]
        self.raw_data = raw_data

    def unescape_html(self) -> pl.DataFrame:
        """
        Applies HTML unescaping to specified columns in the DataFrame.\n
        Returns:
            pl.DataFrame: The updated DataFrame with unescaped HTML characters.
        """
        if self.columns_unescaping:
            for column in self.columns_unescaping:
                self.raw_data = self.raw_data.update(
                    self.raw_data.select(
                        pl.col(column).map_elements(
                            html.unescape, return_dtype=pl.String
                        )
                    )
                )
        return self.raw_data


# Run the code as a script.
if __name__ == "__main__":
    df = pl.DataFrame({"name": ["&amp;", "&lt;Hello&gt;"]})
    config = {"processes": {"html_unescape": ["name"]}}
    unescaper = HTMLUnescaper(config, df)
    cleaned_df = unescaper.unescape_html()
    print(cleaned_df)
