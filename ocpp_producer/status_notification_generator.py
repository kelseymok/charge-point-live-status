import json
import uuid

from dateutil import parser
from datetime import datetime, timezone, timedelta
from typing import Callable, Dict
from freezegun import freeze_time

from ocpp.v16 import call, call_result
from ocpp.v16.enums import ChargePointErrorCode, ChargePointStatus
import pandas as pd
from pandas import to_datetime


class GenerateStatusNotifications:
    def pulse(self, starting_time: str, ending_time: str, freq=60):
        collect = []
        with freeze_time(starting_time) as frozen_datetime:
            while (now := datetime.now(timezone.utc)) < parser.parse(ending_time):
                result = self._status_notification_payload(timestamp=now.isoformat())
                collect.append(result)
                frozen_datetime.tick(freq)
        return collect

    def _status_notification_payload(self, timestamp):
        return call.StatusNotificationPayload(
            connector_id=1,
            error_code=ChargePointErrorCode.no_error,
            status=ChargePointStatus.finishing,
            timestamp=timestamp
        ).__dict__

    def decorate(self, charge_point_id: uuid, data: Dict):
        return {
            "charge_point_id": str(charge_point_id),
            "action": "StatusNotification",
            "body": json.dumps(data),
            "timestamp": data["timestamp"]
        }

    def generate(self):
        num_chargers = 10
        collect = []
        for n in range(num_chargers):
           charge_point_id = uuid.uuid4()
           collect = collect + [ self.decorate(charge_point_id, x) for x in self.pulse("2023-01-01T09:00:00+00:00", "2023-01-01T18:00:00+00:00") ]
        df = pd.DataFrame(collect)
        df["timestamp"] = to_datetime(df["timestamp"]).sort_values()
        df.drop(["timestamp"], axis=1, inplace=True)
        now = int(datetime.now(timezone.utc).timestamp())
        df.to_json(f"./data/{now}.json", orient="records")

GenerateStatusNotifications().generate()