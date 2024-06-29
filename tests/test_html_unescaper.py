import pytest

from src.html_unescaper import HTMLUnescaper


class TestHTMLUnescaper:

    TEST_STATES = "actual_result, expected_result"
    test_cases = [
        ("Hello &amp; World", "Hello & World"),
        ("1 &lt; 2 &amp; 3 &gt; 2", "1 < 2 & 3 > 2"),
        ("&lt;div&gt;", "<div>"),
        ("&quot;Quotes&quot;", "\"Quotes\""),
        ("&apos;Apostrophe&apos;", "'Apostrophe'"),
        ("No special characters", "No special characters"),
        ("","")
    ]
    
    @pytest.mark.parametrize(TEST_STATES, test_cases)
    def test_unescape_html(self, actual_result, expected_result):
        html_unescaper = HTMLUnescaper(actual_result)
        input_data = html_unescaper.unescape_html()
        assert input_data == expected_result
