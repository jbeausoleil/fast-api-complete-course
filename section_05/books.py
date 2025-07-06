from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from starlette import status
from starlette.status import HTTP_201_CREATED
from typing import Optional

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


class BookUpdate(BaseModel):
    """
    Schema for updating a book.

    All fields are optional. Only the fields provided will be updated.

    Attributes:
        title: Updated title of the book (min length: 3).
        author: Updated author name (min length: 1).
        description: Updated book summary (1-500 characters).
        rating: Updated user rating from 0 to 5 (inclusive).
    """
    title: Optional[str] = Field(None, min_length=3)
    author: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = Field(None, min_length=1, max_length=500)
    rating: Optional[int] = Field(None, ge=0, lt=6)

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


def get_next_book_id() -> int:
    """
    Return the next available book ID.
    """
    next_id = max((b.id for b in books), default=0) + 1
    return next_id


@app.get("/books", response_model=list[Book])
async def get_books() -> list[Book]:
    return books


@app.get("/books/{book_id}", response_model=Book, responses={404: {"description": "Book not found."}})
async def get_book_by_id(book_id: int = Path(gt=0)) -> Book:
    try:
        return next(book for book in books if book.id == book_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Book not found.")


@app.get("/books/", response_model=list[Book])
async def get_book_by_rating(book_rating: int) -> list[Book]:
    """
    Return all books with the given rating.
    Raises 404 if no books match.
    """
    """
    Return all books with the given rating. Returns an empty list if no books match.
    """
    return [book for book in books if book.rating == book_rating]


@app.post("/books", response_model=Book, status_code=HTTP_201_CREATED)
async def create_book(book: BookRequest) -> Book:
    """
    Create and store a new book.

    Args:
        book: The new book data (without ID).

    Returns:
        The newly created Book with a server-assigned ID.
    """
    if any(book.title == book.title for book in books):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Book with this title already exists."
        )
    next_id = get_next_book_id()
    new_book = Book(id=next_id, **book.model_dump())
    books.append(new_book)
    return new_book


@app.put("/books/{book_id}", response_model=Book)
async def update_book(update: BookUpdate, book_id: int = Path(gt=0)) -> Book:
    """
    Update the details of an existing book.

    Applies partial updates to the fields provided.

    Raises:
        HTTPException: If no book with the given ID is found.
    """
    try:
        index = next(i for i, b in enumerate(books) if b.id == book_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found.")
    existing_book = books[index]
    existing_book = existing_book.model_dump()
    existing_book.update(update.model_dump(exclude_unset=True))
    updated_book = Book(**existing_book)
    books[index] = updated_book
    return updated_book


@app.delete("/books/{book_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)) -> None:
    """
    Delete a book by its ID.

    Removes the book with the given ID from the collection.

    Raises:
        HTTPException: If no book with the given ID is found.
    """
    try:
        index = next(i for i, b in enumerate(books) if b.id == book_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found.")
    del books[index]
    return
