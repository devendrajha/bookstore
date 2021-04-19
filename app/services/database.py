import motor.motor_asyncio
from bson.objectid import ObjectId

AZURE_DATABASE_CONNECTION_STRING = "mongodb://com-devendra:3IjuoWA1r84AIQD1yV7PdWjfU0ms2vlcpnIRTMdZMI17OdU2RPzdhSY5W9YlV3GDuVrLnUsY5Xt6Gyclb4XX0w==@com-devendra.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@com-devendra@"
AZURE_DATABASE_CONNECTION_STRING='mongodb://localhost:27017'
client = motor.motor_asyncio.AsyncIOMotorClient(AZURE_DATABASE_CONNECTION_STRING)

database = client.storedb

book_collection = database.get_collection("book_collection")


def book_details(book) -> dict:
    return {
        "title": str(book["title"]),
        "author": book["author"],
        "book_description": book["book_description"],
        "cost": book["cost"],
        "create_time": book["create_time"],
    }


# crud operations

# Retrieve all books present in the database
async def retrieve_all_books():
    books = []
    async for b in book_collection.find():
        books.append(book_details(b))
    return books

# Retrieve books based on custom no.
async def retrieve_books_limit(lt =0):
    books = []
    async for b in book_collection.find({},limit=lt):
        books.append(book_details(b))
    return books


# Add a new book into to the database
async def add_book(book_data: dict) -> dict:
    res = await book_collection.insert_one(book_data)
    new_book = await book_collection.find_one({"_id": res.inserted_id})
    return book_details(new_book)


# Retrieve a book with a matching ID
async def retrieve_book_details(id: str) -> dict:
    res = await book_collection.find_one({"_id": ObjectId(id)})
    if res:
        return book_details(res)


# Update a book with a matching ID
async def update_book_details(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    res = await book_collection.find_one({"_id": ObjectId(id)})
    if res:
        resp = await book_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if resp:
            return True
        return False


# Delete a book from the database
async def delete_book(id: str):
    resp = await book_collection.find_one({"_id": ObjectId(id)})
    if resp:
        await book_collection.delete_one({"_id": ObjectId(id)})
        return True

"""
searching books based on title and author
create index in mongodb:-   db.book_collection.createIndex( { title: "text", author: "text"} )
After some search, I found out that MongoDB provided on Azure (DOCUMENTDB...) does not support it.
https://docs.microsoft.com/en-us/azure/documentdb/documentdb-indexing-policies
Note Search API works fine with locale mongodb

"""
async def book_searching(search):
    books = []
    async for b in book_collection.find({"$text": {"$search":search}}):
        books.append(book_details(b))
    return books

