
class DataFlattener:

    def __init__(self, config, raw_data) -> None:
        self.is_flatten = config["processes"]["flattening"]
        self.raw_data = raw_data

    def flatten_data(self):
        if self.is_flatten:
            pass
        return self.raw_data
