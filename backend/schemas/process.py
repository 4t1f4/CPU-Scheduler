from pydantic import BaseModel


class Process(BaseModel):
    id: str
    arrival: int
    burst: int
    priority: int


class FCFSRequest(BaseModel):
    processes: list[Process]