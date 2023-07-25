from fastapi import FastAPI
from models.bookModel import BookUpdate, Book
from fastapi import HTTPException
from controllers.booksController import create_book, get_books, get_book_by_id, update_book, delete_book, book_model_from_mongo

app = FastAPI()

@app.get("/api/books")
def read_books():
    return get_books();

@app.get("/api/books/{book_id}")
def read_book_by_id(book_id):
    return get_book_by_id(book_id);

@app.post("/api/books", status_code=201)
def create_new_book(book: Book):
    return create_book(book);

@app.put("/api/books/{book_id}")
def update_book_by_id(book_id, book: BookUpdate):
    return update_book(book_id, book)

@app.delete("/api/books/{book_id}", status_code=204)
def delete_book_by_id(book_id):
    return delete_book(book_id)