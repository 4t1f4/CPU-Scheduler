from fastapi import FastAPI

from routers.cpu import router as cpu_router
from routers.disk import router as disk_router
from routers.page_replacement import router as page_router
from routers.deadlock import router as deadlock_router


app = FastAPI()


@app.get("/")
def home():
    return {"message": "OS Algorithm Simulator Backend is Running!"}


app.include_router(
    cpu_router,
    prefix="/api/cpu"
)

app.include_router(
    disk_router,
    prefix="/api/disk"
)

app.include_router(
    page_router,
    prefix="/api/page-replacement"
)

app.include_router(
    deadlock_router,
    prefix="/api/deadlock"
)