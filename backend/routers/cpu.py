from fastapi import APIRouter

from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.srtf import srtf
from algorithms.priority import priority_scheduling
from algorithms.round_robin import round_robin

from schemas.process import FCFSRequest, RoundRobinRequest

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


#this srtf ka endpoint
@router.post("/srtf")
def run_srtf(data: FCFSRequest):

    # convert Pydantic objects into dictionaries
    processes = [process.model_dump() for process in data.processes]

    # run SRTF algorithm
    result = srtf(processes)

    return result


#this priority ka endpoint
@router.post("/priority")
def run_priority(data: FCFSRequest):

    # convert Pydantic objects into dictionaries
    processes = [process.model_dump() for process in data.processes]

    # run Priority scheduling algorithm
    result = priority_scheduling(processes)

    return result


#this is round robin ka endpoint
@router.post("/round-robin")
def run_round_robin(data: RoundRobinRequest):
    processes = [process.model_dump() for process in data.processes]

    result = round_robin(processes, data.quantum)

    return result