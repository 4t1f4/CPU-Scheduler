from pydantic import BaseModel


class Process(BaseModel):
    id: str
    arrival: int
    burst: int
    priority: int


class CPURequest(BaseModel):
    processes: list[Process]



class RoundRobinRequest(BaseModel):
    processes: list[Process]
    quantum: int