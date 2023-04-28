
from datetime import datetime, timezone
from time import sleep

import boto3
import os

delay = os.environ.get("DELAY_START_SECONDS", 240)
sleep(int(delay))

storage_host = os.environ.get("STORAGE_HOST")
storage_port = os.environ.get("STORAGE_PORT")

dynamodb = boto3.client('dynamodb', region_name='local', endpoint_url=f"http://{storage_host}:{storage_port}", aws_access_key_id="X",
    aws_secret_access_key="X")


def delete_table(table_name: str):
    response = dynamodb.delete_table(
        TableName=table_name
    )
def create_table(table_name: str):
    dynamodb.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'charge_point_id',
                'AttributeType': 'S'
            }
        ],
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'charge_point_id',
                'KeyType': 'HASH'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )

def datetime_now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def scan(table_name: str):
    response = dynamodb.scan(
        TableName=table_name,
    )
    return response


response = dynamodb.list_tables()
print(response)
create_table("ChargePointLiveStatus")
response = dynamodb.list_tables()
print(response)