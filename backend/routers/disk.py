from fastapi import APIRouter

from algorithms.disk_fcfs import disk_fcfs
from algorithms.disk_sstf import sstf
from algorithms.disk_scan import scan
from algorithms.disk_cscan import cscan

from schemas.disk import DiskRequest, ScanRequest, CScanRequest


router = APIRouter(
    tags=["Disk Scheduling"]
)


@router.post("/fcfs")
def run_disk_fcfs(data: DiskRequest):
    result = disk_fcfs(data.requests, data.head)

    return result


@router.post("/sstf")
def run_sstf(data: DiskRequest):
    result = sstf(data.requests, data.head)

    return result


@router.post("/scan")
def run_scan(data: ScanRequest):
    result = scan(
        data.requests,
        data.head,
        data.disk_size,
        data.direction,
        data.count_zero,
        data.professor_version,
        data.time_per_track
    )

    return result




@router.post("/cscan")
def run_cscan(data: CScanRequest):
    result = cscan(
        data.requests,
        data.head,
        data.disk_size,
        data.direction,
        data.count_zero,
        data.professor_version,
        data.time_per_track
    )
    return result