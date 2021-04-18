from fastapi import FastAPI

from app.services.routes.book import router as BookStore

app = FastAPI()

app.include_router(BookStore, tags=["BookStore"], prefix="/bookstore")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome book store app!"}
