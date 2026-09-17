from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class SensorData(BaseModel):
    temperature: float
    humidity: float
    ion_concentration: float


@app.get("/")
def home():
    return {
        "message": "Battery Quality Control System is running"
    }


@app.post("/sensor-data")
def receive_sensor_data(data: SensorData):
    return {
        "status": "success",
        "data": data
    }