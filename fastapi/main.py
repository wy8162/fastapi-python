from fastapi import FastAPI
from pydantic import BaseModel
import requests
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


@app.get("/ping")
async def ping():
  return {"message": "ok"}


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


@app.get("/gcp/metadata")
async def get_gcp_metadata():
  url = "http://metadata.google.internal/computeMetadata/v1/instance" \
        "/attributes/?recursive=true "
  headers = {"Metadata-Flavor": "Google"}
  response = requests.get(url, headers=headers)
  return {"message": response.json()}


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=80)
