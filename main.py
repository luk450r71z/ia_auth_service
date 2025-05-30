from fastapi import FastAPI

from app.api import auth, services
from config import API_TITLE, API_DESCRIPTION, API_VERSION

# Create FastAPI application
app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION
)

# Include routers
app.include_router(auth.router)
app.include_router(services.router)


@app.get("/", tags=["Root"])
async def read_root():
    """
    Root endpoint
    """
    return {"message": "Welcome to AI Services Authentication API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 