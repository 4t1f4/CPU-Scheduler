from fastapi import APIRouter

from algorithms.pr_fifo import fifo_page_replacement
from algorithms.pr_optimal import optimal_page_replacement
from algorithms.pr_lru import lru_page_replacement

from schemas.page_replacement import PageReplacementRequest


router = APIRouter(
    tags=["Page Replacement"]
)


@router.post("/fifo")
def run_fifo(data: PageReplacementRequest):

    result = fifo_page_replacement(
        data.pages,
        data.frame_count
    )

    return result


@router.post("/optimal")
def run_optimal(data: PageReplacementRequest):

    result = optimal_page_replacement(
        data.pages,
        data.frame_count
    )

    return result


@router.post("/lru")
def run_lru(data: PageReplacementRequest):

    result = lru_page_replacement(
        data.pages,
        data.frame_count
    )

    return result