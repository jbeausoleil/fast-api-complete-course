"""
Main FastAPI application for Todo API.

- Initializes FastAPI app instance and database tables.
- Provides a route to read all todo items from the database.
- Integrates SQLAlchemy ORM for data access.
- Uses Pydantic models for response validation.
"""
from http.client import HTTPException
from typing import Annotated, List

from fastapi import FastAPI, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

from database import engine, get_db
import models
from models import Todo
from schemas import TodoResponse

app = FastAPI()

# Create all database tables on startup (no-op if tables already exist).
models.Base.metadata.create_all(bind=engine)

# Create shorthand for api argument database dependency
db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/", response_model=List[TodoResponse], status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    """
    Retrieve all todo items.

    Returns a list of all todo items stored in the database, serialized using the Pydantic response model.

    Args:
        db (Session): SQLAlchemy database session provided by dependency injection.

    Returns:
        List[TodoResponse]: A list of all todo items in the database.
    """
    return db.query(Todo).all()

@app.get("/{todo_id}", response_model=TodoResponse, status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    """
    Retrieve a single todo item by its unique positive integer ID.

    Args:
        db (Session): SQLAlchemy database session provided by dependency injection.
        todo_id (int): The unique ID of the todo item. Must be greater than 0.

    Returns:
        TodoResponse: The requested todo item, serialized via the Pydantic response model.

    Raises:
        HTTPException: 404 error if the todo item with the specified ID is not found.
    """
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"todo with id {todo_id} not found")
    return todo
