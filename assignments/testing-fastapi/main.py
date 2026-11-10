from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str


INITIAL_BOOKS = {
    1: {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    2: {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
}
books = {}
next_book_id = 3


def reset_books():
    global next_book_id
    books.clear()
    books.update({book_id: book.copy() for book_id, book in INITIAL_BOOKS.items()})
    next_book_id = 3


reset_books()


@app.get("/books")
def list_books():
    return list(books.values())


@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]


@app.post("/books", status_code=201)
def create_book(book: Book):
    global next_book_id
    new_book = {"id": next_book_id, **book.dict()}
    books[next_book_id] = new_book
    next_book_id += 1
    return new_book


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[book_id] = {"id": book_id, **book.dict()}
    return books[book_id]


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    del books[book_id]
    return {"message": "Book deleted"}