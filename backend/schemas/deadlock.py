from pydantic import BaseModel, Field


class BankersRequest(BaseModel):
    allocation: list[list[int]]
    maximum: list[list[int]]
    available: list[int] = Field(min_length=1)


class RagRequest(BaseModel):
    total_resources: list[int] = Field(min_length=1)
    allocation: list[list[int]]
    requests: list[list[int]]