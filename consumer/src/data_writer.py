from typing import Dict


class DataWriter:
    def __init__(self, client):
        self.client = client

    def write(self, data: Dict):
        self._status_notification_request(data)

    def _status_notification_request(self, data: Dict):
        item = {
            "charge_point_id": {
                "S": str(data["charge_point_id"] or "")
            },
            "event_timestamp": {
                "S": str(data["timestamp"] or ""),
            },
            "error_code": {
                "S": str(data["error_code"] or "")
            },
            "status": {
                "S": str(data["status"] or "")
            },
            "vendor_error_code": {
                "S": str(data["vendor_error_code"] or "")
            },
            "vendor_id": {
                "S": str(data["vendor_id"] or "")
            }
        }
        self.client.put_item(TableName="ChargePointLiveStatus", Item=item)

