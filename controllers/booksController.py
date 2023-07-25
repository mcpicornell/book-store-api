from models.bookModel import Book, BookUpdate
from database.database import booksCollection

def get_books():
    books = list(booksCollection.find({}))
    return [book_model_from_mongo(book) for book in books]

def get_book_by_id(book_id):
    book_id = str(book_id)
    book = booksCollection.find_one({"_id":book_id})
    return book

def create_book(book: Book):
    inserted_book = booksCollection.insert_one(book.mode_dump())
    return {"message": "Book created successfully", "inserted_id": str(inserted_book.inserted_id)}

def update_book(book_id, book: BookUpdate):
    book_id = str(book_id)
    book = {k: v for k, v in book.model_dump().items() if v is not None}
    updated_book = booksCollection.update_one({"_id": book_id}, {"$set": book})
    if updated_book.modified_count > 0:
        return {"message": "Book updated successfully"}
    else:
        return {"message": "Book not found or no changes were made"}
    
def delete_book(book_id):
    book_id = str(book_id)
    deleted_book = booksCollection.delete_one({"_id": book_id})
    if deleted_book.deleted_count > 0:
        return {"message": "Book deleted successfully"}
    else:
        return {"message": "Book not found"}
    
def book_model_from_mongo(data):
    book = Book(**data)
    book.id = str(data["_id"])  
    return book