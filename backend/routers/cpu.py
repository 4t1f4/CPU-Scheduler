from fastapi import APIRouter

from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from schemas.process import FCFSRequest

router = APIRouter(
    tags=["CPU Scheduling"]
)


#this fcfs ka endpoint
@router.post("/fcfs")
def run_fcfs(data: FCFSRequest):

    # convert Pydantic objects into dictionaries
    processes = [process.model_dump() for process in data.processes]

    # run FCFS algorithm
    result = fcfs(processes)

    return result


#this sjf ka endpoint
@router.post("/sjf")
def run_sjf(data: FCFSRequest):

    # convert Pydantic objects into dictionaries
    processes = [process.model_dump() for process in data.processes]

    # run SJF algorithm
    result = sjf(processes)

    return result