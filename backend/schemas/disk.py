from pydantic import BaseModel


class DiskRequest(BaseModel):
    requests: list[int]
    head: int