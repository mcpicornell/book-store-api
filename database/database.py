from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()
def get_books_collection():
    mongo_url= os.getenv("MONGO_URL")
    booksCollection= os.getenv("COLLECTION")
    db= os.getenv("DATABASE")
    client = MongoClient(mongo_url)
    db = client[db]
    return db[booksCollection];

booksCollection = get_books_collection();