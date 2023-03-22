import requests
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

books = {}

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Book(BaseModel):
    title: str
    author: str
    isbn: str


routes = APIRouter()


@routes.get("/")
async def root():
    return {"message": "Hello World"}


@routes.get("/ping")
async def ping():
    return {"message": "ok"}


@routes.post("/books")
async def create_book(book: Book):
    books[book.isbn] = book
    return {"message": f"Book {book.title} has been created"}


@routes.get("/books/{isbn}")
async def get_books(isbn: str):
    book = books[isbn]
    if book:
        return {"message": book}
    else:
        return {"message": "Book not found"}


@routes.get("/gcp/metadata")
async def get_gcp_metadata():
    url = "http://metadata.google.internal/computeMetadata/v1/instance" \
          "/attributes/?recursive=true "
    headers = {"Metadata-Flavor": "Google"}
    response = requests.get(url, headers=headers)
    return {"message": response.json()}
