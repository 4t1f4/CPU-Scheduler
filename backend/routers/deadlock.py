from fastapi import APIRouter

from algorithms.bankers import bankers_algorithm
from algorithms.rag import check_deadlock

from schemas.deadlock import BankersRequest, RagRequest


router = APIRouter(
    tags=["Deadlock Detection"]
)


@router.post("/bankers")
def run_bankers(data: BankersRequest):

    result = bankers_algorithm(
        data.allocation,
        data.maximum,
        data.available
    )

    return result


@router.post("/rag")
def run_rag(data: RagRequest):

    result = check_deadlock(
        data.total_resources,
        data.allocation,
        data.requests
    )

    return result