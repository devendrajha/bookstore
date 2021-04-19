from fastapi import FastAPI

from app.services.routes.book import router as BookStore

app = FastAPI()

app.include_router(BookStore, tags=["BookStoreServices"], prefix="/bookstore")

@app.get("/", tags=["Root"])
async def read_root():
    return {
        "message": "Welcome book store app!",
        "1. Get bookdetails ":"http://127.0.0.1:8000/bookstore/bookdetails/{id},   (example-   http://127.0.0.1:8000/bookstore/bookdetails/607c61cfeeaccff87b517330)",
        "2. Get all books in db ":"http://127.0.0.1:8000/bookstore/getallbooks/",
        "3. Get books based on count ":"http://127.0.0.1:8000/bookstore/page/{limit} ,  (example:- http://127.0.0.1:8000/bookstore/page/4)",
        "4. Add new book entry in db ":"http://127.0.0.1:8000/bookstore/addbook/",
        "5. Update books from ":"http://127.0.0.1:8000/bookstore/updatebook/{id} and add json in post body",
        "6. search books from ":"http://127.0.0.1:8000/bookstore/search/{search},   (example:- http://127.0.0.1:8000/bookstore/search/google)",
        "7. Delete books from ":"http://127.0.0.1:8000/bookstore/remove/{id}",

    }
