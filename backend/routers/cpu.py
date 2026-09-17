from fastapi import APIRouter
from algorithms.fcfs import fcfs

router = APIRouter()


@router.post("/fcfs")
def run_fcfs(data: dict):

    # get processes from request
    processes = data["processes"]

    # run FCFS algorithm
    result = fcfs(processes)

    return result