from fastapi import FastAPI
from routers.cpu import router as cpu_router
from routers.disk import router as disk_router

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