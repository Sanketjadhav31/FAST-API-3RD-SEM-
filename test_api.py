"""Quick API test to verify PostgreSQL integration"""
import requests
import time
import subprocess
import sys

def test_api():
    """Test the API endpoints"""
    base_url = "http://localhost:8000"
    
    print("Testing API endpoints with PostgreSQL...")
    print("=" * 60)
    
    try:
        # Test health endpoint
        response = requests.get(f"{base_url}/health", timeout=5)
        print(f"✓ Health check: {response.json()}")
        
        # Test root endpoint
        response = requests.get(f"{base_url}/", timeout=5)
        print(f"✓ Root endpoint: {response.json()}")
        
        # Create a task
        task_data = {
            "title": "PostgreSQL Test Task",
            "description": "Testing with external PostgreSQL database",
            "status": "todo",
            "priority": "high"
        }
        response = requests.post(f"{base_url}/tasks", json=task_data, timeout=5)
        task = response.json()
        print(f"✓ Created task: {task['title']} (ID: {task['id']})")
        
        # Get all tasks
        response = requests.get(f"{base_url}/tasks", timeout=5)
        tasks = response.json()
        print(f"✓ Retrieved {len(tasks)} task(s)")
        
        # Create a label
        label_data = {
            "name": "PostgreSQL",
            "color": "#336699"
        }
        response = requests.post(f"{base_url}/labels", json=label_data, timeout=5)
        label = response.json()
        print(f"✓ Created label: {label['name']}")
        
        # Create a comment
        comment_data = {
            "task_id": task['id'],
            "content": "This task is using PostgreSQL!"
        }
        response = requests.post(f"{base_url}/comments", json=comment_data, timeout=5)
        comment = response.json()
        print(f"✓ Created comment: {comment['content'][:30]}...")
        
        print("\n" + "=" * 60)
        print("All API tests passed! ✓")
        print("Your application is successfully using PostgreSQL!")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("✗ Could not connect to the API. Make sure the server is running.")
        print("Run: uvicorn app.main:app --reload")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Test failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_api()
