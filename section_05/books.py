from dataclasses import Field
from pydoc import describe

from fastapi import Body, FastAPI, HTTPException, status
from fastapi.responses import Response
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

class BookRequest(BaseModel):
    title: str
    author: str
    description: str
    rating: int

    model_config = {"extra": "forbid"}

books: list[Book] = [
    Book(
        id=1,
        title="The Quantum Enigma",
        author="Lena Torres",
        description="A journey into the strange world of quantum physics, blending science with philosophical insights.",
        rating=5
    ),
    Book(
        id=2,
        title="Micro Habits for Massive Growth",
        author="Lena Torres",
        description="A practical guide to personal development through small, sustainable daily habits.",
        rating=4
    ),
    Book(
        id=3,
        title="Tales of the Forgotten Realm",
        author="Marcus Gray",
        description="Epic fantasy adventure in a world of lost kingdoms and ancient secrets.",
        rating=5
    ),
    Book(
        id=4,
        title="The Hidden City",
        author="Rahul Mehta",
        description="A gripping mystery uncovering the secrets buried beneath a bustling metropolis.",
        rating=4
    ),
    Book(
        id=5,
        title="Under the Red Sky",
        author="Claire Zhang",
        description="A poignant romance set against the backdrop of sweeping deserts and crimson sunsets.",
        rating=3
    ),
    Book(
        id=6,
        title="Deep Dive Into Data",
        author="Omar Alvarez",
        description="A beginner-friendly yet thorough exploration of data science principles and applications.",
        rating=5
    )
]


@app.get("/books")
async def get_books():
    return books


@app.post("/books", response_model=Book)
async def create_book(book: BookRequest):
    """
    Create a new book and add it to the collection.

    Args:
        book_request (BookRequest): The new book data (without ID).

    Returns:
        Book: The newly created book, with server-assigned ID.
        :param book:
    """
    next_id = max((b.id for b in books), default=0) + 1
    new_book = Book(id=next_id, **book.model_dump())
    books.append(new_book)
    return new_book