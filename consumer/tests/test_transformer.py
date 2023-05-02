import base64

from transformer import Transformer
import json


class TestTransformer:

    def test_process(self):

        payload = '{"message_id": "fede980d-2f2f-4dc0-93bc-ad64b375caa0", "message_type": 2, "charge_point_id": "94073806-8222-430e-8ca4-fab78b58fb67", "action": "StatusNotification", "write_timestamp": "2023-01-01T10:43:13.900215+00:00", "body": {"connector_id": 2, "error_code": "NoError", "status": "Charging", "timestamp": "2023-01-01T10:43:13.900215+00:00", "info": null, "vendor_id": null, "vendor_error_code": null}, "write_timestamp_epoch": 1672569793900}'
        transformer = Transformer()
        data_bytes = transformer.process(payload)
        assert data_bytes == b'eyJtZXNzYWdlX2lkIjogImZlZGU5ODBkLTJmMmYtNGRjMC05M2JjLWFkNjRiMzc1Y2FhMCIsICJtZXNzYWdlX3R5cGUiOiAyLCAiY2hhcmdlX3BvaW50X2lkIjogIjk0MDczODA2LTgyMjItNDMwZS04Y2E0LWZhYjc4YjU4ZmI2NyIsICJhY3Rpb24iOiAiU3RhdHVzTm90aWZpY2F0aW9uIiwgIndyaXRlX3RpbWVzdGFtcCI6ICIyMDIzLTAxLTAxVDEwOjQzOjEzLjkwMDIxNSswMDowMCIsICJ3cml0ZV90aW1lc3RhbXBfZXBvY2giOiAxNjcyNTY5NzkzOTAwLCAiY29ubmVjdG9yX2lkIjogMiwgImVycm9yX2NvZGUiOiAiTm9FcnJvciIsICJzdGF0dXMiOiAiQ2hhcmdpbmciLCAidGltZXN0YW1wIjogIjIwMjMtMDEtMDFUMTA6NDM6MTMuOTAwMjE1KzAwOjAwIiwgImluZm8iOiBudWxsLCAidmVuZG9yX2lkIjogbnVsbCwgInZlbmRvcl9lcnJvcl9jb2RlIjogbnVsbH0='

    def test__status_notification_request_reshaper(self):
        data = {
            # "message_id": "338c112c-420c-4df4-8318-2160875eb532",
            "message_type": 2,
            "charge_point_id": "01a0f039-7685-4a7f-9ef6-8d262a7898fb",
            "action": "StatusNotification",
            # "write_timestamp": "2023-01-01T12:54:07.750286+00:00",
            "body": {
                "connector_id": 1,
                "error_code": "NoError",
                "status": "Preparing",
                "timestamp": "2023-01-01T12:54:07.750286+00:00",
                "info": None,
                "vendor_id": None,
                "vendor_error_code": None
            },
            # "write_timestamp_epoch":1672577647750
        }
        transformer = Transformer()
        result = transformer._status_notification_extractor(data)

        assert result == {
            # "message_id": "338c112c-420c-4df4-8318-2160875eb532",
            "message_type": 2,
            "charge_point_id": "01a0f039-7685-4a7f-9ef6-8d262a7898fb",
            "action": "StatusNotification",
            # "write_timestamp": "2023-01-01T12:54:07.750286+00:00",
            "connector_id": 1,
            "error_code": "NoError",
            "status": "Preparing",
            "timestamp": "2023-01-01T12:54:07.750286+00:00",
            "info": None,
            "vendor_id": None,
            "vendor_error_code": None,
            # "write_timestamp_epoch": 1672577647750
        }
