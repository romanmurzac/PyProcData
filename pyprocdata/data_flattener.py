import polars as pl


class DataFlattener:

    def __init__(self, config, raw_data) -> None:
        self.is_flatten = config["processes"]["flattening"]
        self.raw_data = raw_data.to_dict(as_series=False)
    
    def flatten_data(self):
        flattened_data = {}
        def flatten(nested_data, name=''):
            if isinstance(nested_data, dict):
                for column in nested_data:
                    flatten(nested_data[column], name + column + '_')
            elif isinstance(nested_data, list):
                for column in nested_data:
                    flatten(column, name)
            else:
                flattened_data[name[:-1]] = nested_data
        flatten(self.raw_data)
        return pl.DataFrame(flattened_data)


if __name__ == "__main__":
    config = {
        "processes": {
            "flattening": True
        }
    }
    data = pl.DataFrame({
    "count": 13,
    "virtualmachine": [
        {
            "id": "1082e2ed-ff66-40b1-a41b-26061afd4a0b",
            "name": "test-2",
            "displayname": "test-2",
            "securitygroup": [
                {
                    "id": "9e649fbc-3e64-4395-9629-5e1215b34e58",
                    "name": "test",
                    "tags": [{"tag": 1, "code": 123}, {"tag": 2, "code": 456}]
                }
            ],
            "nic": [
                {
                    "id": "79568b14-b377-4d4f-b024-87dc22492b8e",
                    "networkid": "05c0e278-7ab4-4a6d-aa9c-3158620b6471"
                },
                {
                    "id": "3d7f2818-1f19-46e7-aa98-956526c5b1ad",
                    "networkid": "b4648cfd-0795-43fc-9e50-6ee9ddefc5bd",
                    "traffictype": "Guest"
                }
            ],
            "hypervisor": "KVM",
            "affinitygroup": [],
            "isdynamicallyscalable": False
        }
    ]
})
    data_flattener = DataFlattener(config, data)
    print(data_flattener.flatten_data())