from pydantic import BaseModel

class TodoResponse(BaseModel):
    """
    Pydantic schema for serializing Todo items in API responses.

    Attributes:
        id (int): Unique identifier of the todo item.
        title (str): Title of the todo.
        description (str | None): Optional detailed description.
        priority (int): Priority level of the todo item.
        completed (bool): Completion status of the todo.
    """

    id: int
    title: str
    description: str | None = None
    priority: int
    completed: bool

    class Config:
        from_attributes = True  # Enables ORM mode for SQLAlchemy model compatibility.