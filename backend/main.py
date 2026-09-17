from fastapi import FastAPI
from routers.cpu import router as cpu_router

app = FastAPI()


@app.get("/")
def home():
    return {"message": "OS Algorithm Simulator Backend is Running!"}


app.include_router(
    cpu_router,
    prefix="/api/cpu"
)