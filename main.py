from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

books = {}

app = FastAPI()


class Book(BaseModel):
  title: str
  author: str
  isbn: str


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
  return {"message": f"Hello {name}"}


@app.get("/hello/{name}/age/{age}")
async def say_hello(name: str, age: int):
  return {"message": f"Hello {name}, you are {age} years old"}


@app.post("/books")
async def create_book(book: Book):
  books[book.isbn] = book
  return {"message": f"Book {book.title} has been created"}


@app.get("/books/{isbn}")
async def get_books(isbn: str):

  book = books[isbn]
  if book:
    return {"message": book}
  else:
    return {"message": "Book not found"}


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=80)
