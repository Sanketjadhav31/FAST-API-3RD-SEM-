from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database import create_db_and_tables
from app.routers import tasks, comments, labels

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events"""
    # Startup: Initialize database
    create_db_and_tables()
    yield
    # Shutdown: Cleanup if needed

app = FastAPI(
    title="Task Management API",
    description="A modern RESTful API for task management with comments, labels, and activity logging",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tasks.router)
app.include_router(comments.router)
app.include_router(labels.router)

@app.get("/", tags=["Root"])
def read_root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to Task Management API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
