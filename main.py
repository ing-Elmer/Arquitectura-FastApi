from fastapi import FastAPI
from Config.config import engine, Base
from Routes.router import router

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router, prefix="/user", tags=["User"])
