import html
import polars as pl


class HTMLUnescaper:
    def __init__(self, config, raw_data):
        self.columns_unescaping = config["processes"]["html_unescape"]
        self.raw_data = raw_data

    def unescape_html(self):
        if self.columns_unescaping:
            for column in self.columns_unescaping:
                self.raw_data = self.raw_data.update(self.raw_data.select(pl.col(column).map_elements(html.unescape, return_dtype=pl.String)))
        return self.raw_data


if __name__ == "__main__":

    df = pl.DataFrame({"name": "&amp;"})
    column = "name"
    df.update(df.select(pl.col(column).map_elements(html.unescape, return_dtype=pl.String)))
    print(df)
