"""
Seed script to populate the database with sample data
Run with: python seed.py
"""
from sqlmodel import Session
from datetime import datetime, timedelta, timezone
from app.database import engine, create_db_and_tables
from app.models import Task, Comment, Label, TaskLabel, ActivityLog
from app.models.task import TaskStatus, TaskPriority

def seed_database():
    """Populate database with sample data"""
    print("🌱 Starting database seeding...")
    
    # Create tables
    create_db_and_tables()
    print("✅ Database tables created")
    
    with Session(engine) as session:
        # Create Labels
        labels_data = [
            {"name": "Bug", "color": "#FF0000"},
            {"name": "Feature", "color": "#00FF00"},
            {"name": "Enhancement", "color": "#0000FF"},
            {"name": "Documentation", "color": "#FFA500"},
            {"name": "Urgent", "color": "#FF1493"},
        ]
        
        labels = []
        for label_data in labels_data:
            label = Label(**label_data)
            session.add(label)
            labels.append(label)
        
        session.commit()
        print(f"✅ Created {len(labels)} labels")
        
        # Create Tasks
        tasks_data = [
            {
                "title": "Fix login authentication bug",
                "description": "Users are unable to login with correct credentials",
                "status": TaskStatus.IN_PROGRESS,
                "priority": TaskPriority.HIGH,
                "due_date": datetime.now(timezone.utc) + timedelta(days=2),
            },
            {
                "title": "Implement user profile page",
                "description": "Create a page where users can view and edit their profile information",
                "status": TaskStatus.TODO,
                "priority": TaskPriority.MEDIUM,
                "due_date": datetime.now(timezone.utc) + timedelta(days=7),
            },
            {
                "title": "Write API documentation",
                "description": "Document all REST API endpoints with examples",
                "status": TaskStatus.TODO,
                "priority": TaskPriority.LOW,
                "due_date": datetime.now(timezone.utc) + timedelta(days=14),
            },
            {
                "title": "Optimize database queries",
                "description": "Improve performance of slow queries in the dashboard",
                "status": TaskStatus.DONE,
                "priority": TaskPriority.HIGH,
                "due_date": datetime.now(timezone.utc) - timedelta(days=1),
            },
            {
                "title": "Add email notifications",
                "description": "Send email notifications for task assignments and updates",
                "status": TaskStatus.TODO,
                "priority": TaskPriority.MEDIUM,
                "due_date": datetime.now(timezone.utc) + timedelta(days=10),
            },
        ]
        
        tasks = []
        for task_data in tasks_data:
            task = Task(**task_data)
            session.add(task)
            tasks.append(task)
        
        session.commit()
        print(f"✅ Created {len(tasks)} tasks")
        
        # Assign labels to tasks
        task_label_assignments = [
            (0, [0, 4]),  # Task 0: Bug, Urgent
            (1, [1]),     # Task 1: Feature
            (2, [3]),     # Task 2: Documentation
            (3, [2]),     # Task 3: Enhancement
            (4, [1, 2]),  # Task 4: Feature, Enhancement
        ]
        
        for task_idx, label_indices in task_label_assignments:
            for label_idx in label_indices:
                task_label = TaskLabel(
                    task_id=tasks[task_idx].id,
                    label_id=labels[label_idx].id
                )
                session.add(task_label)
        
        session.commit()
        print("✅ Assigned labels to tasks")
        
        # Create Comments
        comments_data = [
            {
                "content": "I've started investigating this issue. It seems to be related to session management.",
                "author": "Alice Johnson",
                "task_id": tasks[0].id,
            },
            {
                "content": "Found the root cause - the JWT token expiration logic is incorrect.",
                "author": "Alice Johnson",
                "task_id": tasks[0].id,
            },
            {
                "content": "Should we include social media links in the profile?",
                "author": "Bob Smith",
                "task_id": tasks[1].id,
            },
            {
                "content": "Yes, let's add LinkedIn and GitHub links.",
                "author": "Carol Davis",
                "task_id": tasks[1].id,
            },
            {
                "content": "I can help with this. I'll use Swagger for the documentation.",
                "author": "David Wilson",
                "task_id": tasks[2].id,
            },
            {
                "content": "Great work! The dashboard is much faster now.",
                "author": "Eve Martinez",
                "task_id": tasks[3].id,
            },
            {
                "content": "Query time reduced from 2.5s to 0.3s. Added proper indexes.",
                "author": "Frank Brown",
                "task_id": tasks[3].id,
            },
        ]
        
        comments = []
        for comment_data in comments_data:
            comment = Comment(**comment_data)
            session.add(comment)
            comments.append(comment)
        
        session.commit()
        print(f"✅ Created {len(comments)} comments")
        
        # Create Activity Logs
        activity_logs_data = [
            {
                "task_id": tasks[0].id,
                "action": "created",
                "description": "Task 'Fix login authentication bug' created",
                "performed_by": "Alice Johnson",
            },
            {
                "task_id": tasks[0].id,
                "action": "status_changed",
                "description": "Status changed from TODO to IN_PROGRESS",
                "performed_by": "Alice Johnson",
            },
            {
                "task_id": tasks[1].id,
                "action": "created",
                "description": "Task 'Implement user profile page' created",
                "performed_by": "Bob Smith",
            },
            {
                "task_id": tasks[3].id,
                "action": "created",
                "description": "Task 'Optimize database queries' created",
                "performed_by": "Frank Brown",
            },
            {
                "task_id": tasks[3].id,
                "action": "status_changed",
                "description": "Status changed from IN_PROGRESS to DONE",
                "performed_by": "Frank Brown",
            },
        ]
        
        activity_logs = []
        for log_data in activity_logs_data:
            log = ActivityLog(**log_data)
            session.add(log)
            activity_logs.append(log)
        
        session.commit()
        print(f"✅ Created {len(activity_logs)} activity logs")
        
        print("\n🎉 Database seeding completed successfully!")
        print("\n📊 Summary:")
        print(f"   - Labels: {len(labels)}")
        print(f"   - Tasks: {len(tasks)}")
        print(f"   - Comments: {len(comments)}")
        print(f"   - Activity Logs: {len(activity_logs)}")
        print("\n🚀 You can now start the API server with: uvicorn app.main:app --reload")

if __name__ == "__main__":
    seed_database()
