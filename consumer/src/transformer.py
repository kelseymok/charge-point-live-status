import base64
from typing import Dict

import json


class Transformer:

    def process(self, payload: str):
        data = json.loads(payload)
        result = self._status_notification_extractor(data)
        return result

    def _status_notification_extractor(self, data: Dict) -> bytes:
        flattened = {
            # "message_id": data["message_id"],
            "message_type": data["message_type"],
            "charge_point_id": data["charge_point_id"],
            "action": data["action"],
            # "write_timestamp": data["write_timestamp"],
            # "write_timestamp_epoch": data["write_timestamp_epoch"],
            "connector_id": data["body"]["connector_id"],
            "error_code": data["body"]["error_code"],
            "status": data["body"]["status"],
            "timestamp": data["body"]["timestamp"],
            "info": data["body"]["info"],
            "vendor_id": data["body"]["vendor_id"],
            "vendor_error_code": data["body"]["vendor_error_code"],
        }

        return flattened
