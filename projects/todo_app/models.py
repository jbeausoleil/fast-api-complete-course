from database import Base
from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint

class Todo(Base):
    """
    SQLAlchemy ORM model for a todo item.

    Represents a task with a title, optional description, priority level, and completion status.

    Table Name:
        todos

    Columns:
        id (int): Primary key, unique identifier for the todo item.
        title (str): Short title or summary of the todo (required, max 100 chars).
        description (str, optional): Detailed description of the todo (max 100 chars).
        priority (int): Priority level of the todo item (0–10, inclusive).
        completed (bool): Completion status; True if the todo is done, False otherwise.

    Constraints:
        check_priority: Ensures the priority value is between 0 and 10 (inclusive).
    """
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=True)
    priority = Column(Integer, nullable=False, index=True)
    completed = Column(Boolean, default=False, index=True)

    __table_args__ = (
        CheckConstraint("priority >= 0 AND priority <= 10", name="check_priority"),
    )