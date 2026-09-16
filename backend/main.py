from fastapi import FastAPI
from pydantic import BaseModel

from algorithms.fcfs import fcfs


app = FastAPI()


class Process(BaseModel):
    id: str
    arrival: int
    burst: int
    priority: int


class FCFSRequest(BaseModel):
    processes: list[Process]


@app.get("/")
def home():
    return {"message": "OS Algorithm Simulator Backend is Running!"}


@app.post("/api/cpu/fcfs")
def run_fcfs(data: FCFSRequest):

    # convert pydantic objects into dictionaries
    processes = [process.model_dump() for process in data.processes]

    # run FCFS algorithm
    result = fcfs(processes)

    return result