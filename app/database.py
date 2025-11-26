from sqlmodel import SQLModel, create_engine, Session
from typing import Generator

# Database URL - SQLite for development
DATABASE_URL = "sqlite:///./task_management.db"

# Create engine
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Set to False in production
    connect_args={"check_same_thread": False}  # Needed for SQLite
)

def create_db_and_tables():
    """Create all database tables"""
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """Dependency for getting database sessions"""
    with Session(engine) as session:
        yield session
