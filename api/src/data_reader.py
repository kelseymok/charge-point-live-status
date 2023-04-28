from typing import Dict, List, Union

import boto3


class DataReader:
    def __init__(self, storage_client: boto3.client):
        self.storage_client = storage_client

    def read(self, table_name: str) -> List[Dict]:
        items = [self._unpack(x) for x in self.get_all(table_name)["Items"]]
        return items

    def _unpack(self, data: Dict):
        return {
            "charge_point_id": data["charge_point_id"]["S"],
            "event_timestamp": data["event_timestamp"]["S"],
            "error_code":  data["error_code"]["S"],
            "status":  data["status"]["S"],
            "vendor_error_code":  data["vendor_error_code"]["S"],
            "vendor_id": data["vendor_id"]["S"]
        }

    def get_all(self, table_name: str) -> Union[Dict, List]:
        response = self.storage_client.scan(
            TableName=table_name,
        )

        return response
