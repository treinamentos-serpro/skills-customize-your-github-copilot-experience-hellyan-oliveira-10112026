from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str


books = {
    1: {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    2: {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
}
next_book_id = 3


@app.get("/books")
def list_books():
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return the requested book, or raise HTTPException with status 404.
    pass


@app.post("/books", status_code=201)
def create_book(book: Book):
    global next_book_id
    # TODO: Save the validated book with a unique ID and return it.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    # TODO: Replace the book's details, or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Delete the requested book, or raise HTTPException with status 404.
    pass