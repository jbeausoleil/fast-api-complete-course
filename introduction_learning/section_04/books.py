from fastapi import Body, FastAPI, HTTPException, status
from fastapi.responses import Response
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "The Quantum Enigma", "author": "Lena Torres", "category": "science"},
    {"id": 2, "title": "Micro Habits for Massive Growth", "author": "Lena Torres", "category": "self-help"},
    {"id": 3, "title": "Tales of the Forgotten Realm", "author": "Marcus Gray", "category": "fantasy"},
    {"id": 4, "title": "The Hidden City", "author": "Rahul Mehta", "category": "mystery"},
    {"id": 5, "title": "Under the Red Sky", "author": "Claire Zhang", "category": "romance"},
    {"id": 6, "title": "Deep Dive Into Data", "author": "Omar Alvarez", "category": "technology"},
    {"id": 7, "title": "Echoes of the Forgotten Code", "author": "Nadia Bell", "category": "technology"}
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    category: str

class BookUpdate(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None

@app.get("/books")
async def get_books():
    """
    Retrieve the full list of books.

    Returns:
        list: All books in the collection.
    """
    return books

@app.get("/books/{id}", response_model=Book)
async def get_book(id: int):
    """
    Retrieve a book by its unique ID.

    Args:
        id (int): The ID of the book.

    Returns:
        Book: The matching book, if found.

    Raises:
        HTTPException: If the book is not found.
    """
    for book in books:
        if book.get('id') == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found.")

@app.get("/books/")
async def get_book_by_category(category: str):
    """
    Retrieve all books matching the specified category (case-insensitive).

    Args:
        category (str): The book category.

    Returns:
        list: Books that match the category.
    """
    return [
        book for book in books
        if book.get('category').casefold() == category.casefold()
    ]

@app.get("/books/{author_name}/", response_model=Book)
async def get_book_by_author(author_name: Optional[str] = None, category: Optional[str] = None):
    """
    Retrieve all books by a given author, optionally filtered by category.

    Args:
        author_name (str): The author's name.
        category (str, optional): The book category.

    Returns:
        list: Books by the specified author (and category, if provided).
    """
    return [
        book for book in books
        if book.get('author').casefold() == author_name.casefold()
           and (category is None or book.get('category').casefold() == category.casefold())
    ]

@app.post("/books", response_model=Book)
async def create_book(book: Book):
    """
    Create a new book and add it to the collection.

    Args:
        book (Book): The book to add.

    Returns:
        Book: The newly created book.
    """
    books.append(book.model_dump())
    return book

@app.put("/books", response_model=Book)
async def update_book(id: int, book: BookUpdate):
    """
    Update an existing book by its ID.

    Args:
        id (int): The ID of the book to update.
        book (BookUpdate): Fields to update.

    Returns:
        Book: The updated book.

    Raises:
        HTTPException: If the ID is changed or the book is not found.
    """
    if book.id is not None and book.id != id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Changing the book ID is not allowed.")

    index = next((i for i, book in enumerate(books) if book['id'] == id), None)
    if index is not None:
        updated_book = book.model_dump(exclude_unset=True)
        updated_book['id'] = id  # preserve original id
        books[index] = {**books[index], **updated_book}
        return books[index]

    raise HTTPException(status_code=404, detail="Book not found.")

@app.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int):
    """
    Delete a book by its ID.

    Args:
        id (int): The ID of the book to delete.

    Returns:
        Response: 204 No Content on successful deletion.

    Raises:
        HTTPException: If the book is not found.
    """
    index = next((i for i, book in enumerate(books) if book['id'] == id), None)
    if index is not None:
        del books[index]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail="Book not found.")