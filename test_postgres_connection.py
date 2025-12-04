"""Test PostgreSQL connection and database setup"""
import os
from dotenv import load_dotenv
from sqlmodel import Session, select
from app.database import engine, create_db_and_tables
from app.models.task import Task
from app.models.label import Label
from app.models.comment import Comment
from app.models.activity_log import ActivityLog

# Load environment variables
load_dotenv()

def test_connection():
    """Test database connection"""
    print("Testing PostgreSQL connection...")
    print(f"Database URL: {os.getenv('DATABASE_URL')[:50]}...")
    
    try:
        # Test connection
        with Session(engine) as session:
            result = session.exec(select(1)).first()
            print("✓ Connection successful!")
            return True
    except Exception as e:
        print(f"✗ Connection failed: {e}")
        return False

def test_create_tables():
    """Create all database tables"""
    print("\nCreating database tables...")
    try:
        create_db_and_tables()
        print("✓ Tables created successfully!")
        return True
    except Exception as e:
        print(f"✗ Table creation failed: {e}")
        return False

def test_crud_operations():
    """Test basic CRUD operations"""
    print("\nTesting CRUD operations...")
    
    try:
        with Session(engine) as session:
            # Create a test task
            test_task = Task(
                title="Test Task",
                description="Testing PostgreSQL connection",
                status="todo",
                priority="medium"
            )
            session.add(test_task)
            session.commit()
            session.refresh(test_task)
            print(f"✓ Created task with ID: {test_task.id}")
            
            # Read the task
            task = session.get(Task, test_task.id)
            print(f"✓ Read task: {task.title}")
            
            # Update the task
            task.status = "in_progress"
            session.add(task)
            session.commit()
            print(f"✓ Updated task status to: {task.status}")
            
            # Delete the task
            session.delete(task)
            session.commit()
            print("✓ Deleted test task")
            
        return True
    except Exception as e:
        print(f"✗ CRUD operations failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("PostgreSQL Database Connection Test")
    print("=" * 60)
    
    # Test connection
    if not test_connection():
        return
    
    # Create tables
    if not test_create_tables():
        return
    
    # Test CRUD operations
    if not test_crud_operations():
        return
    
    print("\n" + "=" * 60)
    print("All tests passed! ✓")
    print("Your PostgreSQL database is ready to use.")
    print("=" * 60)

if __name__ == "__main__":
    main()
