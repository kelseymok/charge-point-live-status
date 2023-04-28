import boto3
from botocore.stub import Stubber
from data_reader import DataReader


class TestDataReader:
    def test_read_status(self):
        client = boto3.client("dynamodb", region_name="eu-central-1")

        request = {
            'TableName': 'ChargePointLiveStatus'
        }

        response = {
            'Items': [
                {
                    "charge_point_id": {
                        "S": "f4bbf74b-8a62-454b-b8aa-54e7f9592323"
                    },
                    "event_timestamp": {
                        "S": "2023-01-01T09:00:00+00:00"
                    },
                    "error_code": {
                        "S": "NoError"
                    },
                    "status": {
                        "S": "Charging"
                    },
                    "vendor_error_code": {
                        "S": ""
                    },
                    "vendor_id": {
                        "S": ""
                    }
                },

            ],
            'Count': 1,
            'ScannedCount': 1,
            'ResponseMetadata': {
                'RequestId': 'a0568385-1c84-4b6b-8fb4-479f8b15f7fb',
                'HTTPStatusCode': 200,
            }
        }


        with Stubber(client) as stubber:
            stubber.add_response('scan', response, request)
            data_reader = DataReader(client)
            result = data_reader.read(table_name="ChargePointLiveStatus")
            assert result == [
                {
                    'charge_point_id': 'f4bbf74b-8a62-454b-b8aa-54e7f9592323',
                     'error_code': 'NoError',
                     'event_timestamp': '2023-01-01T09:00:00+00:00',
                     'status': 'Charging',
                     'vendor_error_code': '',
                     'vendor_id': ''
                },
            ]
