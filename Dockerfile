FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
# Use PORT environment variable for cloud deployments (Render, Heroku, etc.)
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
