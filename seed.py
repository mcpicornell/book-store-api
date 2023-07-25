from faker import Faker
from models.bookModel import Book
from database.database import booksCollection
from main import app
from bson import ObjectId  
import uuid
from bson.binary import Binary


@app.post("/api/books")
def create_fake_book():
    fake = Faker()
    title = fake.sentence(nb_words=4)
    author = fake.name()
    publication_year = fake.random_int(min=1800, max=2023)
    description = fake.paragraph()
    book_id = str(uuid.uuid4())
    book_id_binary = Binary(book_id.encode("utf-8"), 4)
    book = Book(id=book_id_binary, title=title, author=author, publication_year=publication_year, description=description)
    booksCollection.insert_one(book.model_dump(by_alias=True))

    return {"message": "Fake book created successfully"}

def createBooks():
    for _ in range(0, 30):
        create_fake_book();

def drop_books_collection():
    booksCollection.drop()

drop_books_collection()
createBooks()