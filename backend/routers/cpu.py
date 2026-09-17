from fastapi import APIRouter
from algorithms.fcfs import fcfs
from schemas.process import FCFSRequest

router = APIRouter()


@router.post("/fcfs")
def run_fcfs(data: FCFSRequest):

    # convert Pydantic objects into dictionaries
    processes = [process.model_dump() for process in data.processes]

    # run FCFS algorithm
    result = fcfs(processes)

    return result