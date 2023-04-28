import json
import os

import boto3
import uvicorn
from fastapi import FastAPI, Response

from data_reader import DataReader

app = FastAPI()

reader_host = os.environ.get("READER_HOST", "localhost")
reader_port = os.environ.get("READER_PORT", "8000")

dynamodb = boto3.client(
    'dynamodb',
    region_name='local',
    endpoint_url=f"http://{reader_host}:{reader_port}",
    aws_access_key_id="X",
    aws_secret_access_key="X"
)

data_reader = DataReader(dynamodb)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/charge_point_live_status")
def get_statuses():
    data = data_reader.read("ChargePointLiveStatus")
    return Response(content=json.dumps(data), media_type="application/json")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)