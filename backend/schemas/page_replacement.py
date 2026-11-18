from pydantic import BaseModel, Field


class PageReplacementRequest(BaseModel):
    pages: list[int] = Field(min_length=1)
    frame_count: int = Field(gt=0)