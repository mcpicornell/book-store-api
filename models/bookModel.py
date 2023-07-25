from pydantic import BaseModel, Field
from bson import ObjectId  
from typing import Optional
import uuid


class Book(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    title: str
    author: str
    publication_year: int
    description: str


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publication_year: Optional[int] = None
    description: Optional[str] = None
    class Config:
        arbitrary_types_allowed = True