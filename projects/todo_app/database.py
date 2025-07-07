"""
Database setup for FastAPI app using SQLAlchemy and SQLite.

- Configures the database engine and session factory.
- Provides a Base class for SQLAlchemy ORM models.
- Defines a FastAPI-compatible dependency function for creating and closing DB sessions.

Usage:
    - Import `Base` to define SQLAlchemy models.
    - Use `get_db` as a dependency in FastAPI routes to access the database session.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite (local file named .todos.db)
SQLALCHEMY_DATABASE_URL = 'sqlite:///.todos.db'

# Create the database engine.
# For SQLite, 'check_same_thread=False' allows usage in multithreaded FastAPI apps.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create a configured "Session" class (for database sessions/transactions).
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions (all models will inherit from this).
Base = declarative_base()

def get_db():
    """
    Dependency generator that provides a SQLAlchemy database session.

    Yields:
        Session: A SQLAlchemy Session instance to interact with the database.

    Ensures:
        The session is properly closed after use, regardless of request outcome.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()