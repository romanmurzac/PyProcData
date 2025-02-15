import pytest
import polars as pl
from pyprocdata.data_html_unescaper import HTMLUnescaper


class TestHTMLUnescaper:
    TEST_STATES = "actual_result, expected_result"
    test_cases = [
        (["Hello &amp; World"], ["Hello & World"]),
        (["1 &lt; 2 &amp; 3 &gt; 2"], ["1 < 2 & 3 > 2"]),
        (["&lt;div&gt;"], ["<div>"]),
        (["&quot;Quotes&quot;"], ['"Quotes"']),
        (["&apos;Apostrophe&apos;"], ["'Apostrophe'"]),
        (["No special characters"], ["No special characters"]),
        ([""], [""]),
    ]

    @pytest.mark.parametrize(TEST_STATES, test_cases)
    def test_data_unescape_html(self, actual_result, expected_result):
        # Create a Polars DataFrame with the test data
        df = pl.DataFrame({"test_column": actual_result})

        # Define the config to target the column for unescaping.
        config = {"processes": {"html_unescape": ["test_column"]}}

        # Initialize and process with HTMLUnescaper.
        html_unescaper = HTMLUnescaper(config=config, raw_data=df)
        output_df = html_unescaper.unescape_html()

        # Extract processed data and compare.
        result_list = output_df["test_column"].to_list()
        assert result_list == expected_result
