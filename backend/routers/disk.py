from fastapi import APIRouter

from algorithms.disk_fcfs import disk_fcfs
from schemas.disk import DiskRequest


router = APIRouter(
    tags=["Disk Scheduling"]
)


@router.post("/fcfs")
def run_disk_fcfs(data: DiskRequest):
    result = disk_fcfs(data.requests, data.head)

    return result