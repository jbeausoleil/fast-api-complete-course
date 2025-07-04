from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int


class BookRequest(BaseModel):
    """
    Schema for book creation requests.

    Attributes:
        title: Title of the book (min length: 3).
        author: Name of the author (min length: 1).
        description: Book summary (1-500 characters).
        rating: User rating from 0 to 5 (inclusive).
    """
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=500)
    rating: int = Field(ge=0, lt=6)

    model_config = {
        "extra": "forbid",
        "json_schema_extra": {
            "examples": [
                {
                    "title": "The Quantum Enigma",
                    "author": "Lena Torres",
                    "description": "A journey into the strange world of quantum physics, blending science with philosophical insights.",
                    "rating": 5
                }
            ]
        }
    }


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
async def get_books() -> list[Book]:
    return books


@app.post("/books", response_model=Book)
async def create_book(book: BookRequest) -> Book:
    """
    Create and store a new book.

    Args:
        book: The new book data (without ID).

    Returns:
        The newly created Book with a server-assigned ID.
    """
    next_id = get_next_book_id()
    new_book = Book(id=next_id, **book.model_dump())
    books.append(new_book)
    return new_book


def get_next_book_id() -> int:
    """
    Return the next available book ID.
    """
    next_id = max((b.id for b in books), default=0) + 1
    return next_id
