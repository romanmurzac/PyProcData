import html


class HTMLUnescaper:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def unescape_html(self):
        return html.unescape(self.raw_data)
