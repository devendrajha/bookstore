from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    title: str = Field(...)
    author: str = Field(...)
    book_description: Optional[str] = Field(...)
    cost: float = Field(...)
    create_time: datetime = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources engineering",
                "year": 2,
                "gpa": "3.0",
            }
        }


class UpdateBookModel(BaseModel):
    title: str = Field(...)
    author: str = Field(...)
    book_description: str = Field(...)
    cost: int = Field(...)
    create_time: datetime = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
