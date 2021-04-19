from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.services.database import (
    add_book,
    delete_book,
    retrieve_book_details,
    retrieve_all_books,
    update_book_details,
    retrieve_books_limit,
    book_searching,
)
from app.services.models.book_data_model import (
    ErrorResponseModel,
    ResponseModel,
    BookSchema,
    UpdateBookModel,
)

router = APIRouter()


@router.post("/addbook/", response_description="Book data added into the database")
async def add_book_data(bk: BookSchema = Body(...)):
    resp = jsonable_encoder(bk)
    result = await add_book(resp)
    return ResponseModel(result, "Book added successfully.")


@router.get("/getallbooks/", response_description="Book retrieved")
async def get_all_books():
    get_resp = await retrieve_all_books()
    if get_resp:
        return ResponseModel(get_resp, "Book data retrieved successfully")
    return ResponseModel(get_resp, "Books data not available ")

@router.get("/{limit}", response_description="Book retrieved")
async def get_books_with_custom_count(limit):
    get_resp = await retrieve_books_limit(int(limit))
    if get_resp:
        return ResponseModel(get_resp, " {} Book data retrieved successfully".format(limit))
    return ResponseModel(get_resp, "Books data not available ")


@router.get("/bookdetails/{id}", response_description="Book data retrieved")
async def get_book_data(id):
    get_resp = await retrieve_book_details(id)
    if get_resp:
        return ResponseModel(get_resp, "Book data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")


@router.put("/updatebook/{id}")
async def update_book_data(id: str, req: UpdateBookModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_resp = await update_book_details(id, req)
    if update_resp:
        return ResponseModel(
            "Book with ID: {} name update is successful".format(id),
            "Book name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the book data.",
    )


@router.delete("/remove/{id}", response_description="Book data deleted from the database")
async def delete_book_data(id: str):
    delete_resp = await delete_book(id)
    if delete_resp:
        return ResponseModel(
            "Book with ID: {} deleted ".format(id), "Book deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Book with id {0} doesn't exist".format(id)
    )

@router.get("/page/{limit}", response_description="Book retrieved")
async def get_books_with_custom_count(limit):
    limit_resp = await retrieve_books_limit(int(limit))
    if limit_resp:
        return ResponseModel(limit_resp, "Book data retrieved successfully")
    return ResponseModel(limit_resp, "Books data not available ")

@router.get("/search/{search}", response_description="Book retrieved")
async def search_books(search):
    search_resp = await book_searching(search)
    if search_resp:
        return ResponseModel(search_resp, "Book data retrieved successfully")
    return ResponseModel(search_resp, "Books data not available ")
