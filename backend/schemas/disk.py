from typing import Literal
from pydantic import BaseModel


class DiskRequest(BaseModel):
    requests: list[int]
    head: int


class ScanRequest(BaseModel):
    requests: list[int]
    head: int
    disk_size: int
    direction: Literal["left", "right"] = "left"
    count_zero: bool = True
    professor_version: bool = False
    time_per_track: float = 1


class CScanRequest(BaseModel):
    requests: list[int]
    head: int
    disk_size: int
    direction: Literal["left", "right"] = "right"
    count_zero: bool = True
    professor_version: bool = False
    time_per_track: float = 1