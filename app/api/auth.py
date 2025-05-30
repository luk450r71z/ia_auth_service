from uuid import uuid4
import logging

from fastapi import APIRouter, HTTPException, status

from app.auth.jwt import create_access_token
from app.db.database import get_service_by_id
from app.models.schemas import AuthRequest, AuthResponse

# Configure logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/token", response_model=AuthResponse)
async def authenticate_service(auth_request: AuthRequest):
    """
    Authenticate a client to use a specific AI service
    """
    logger.info(f"Auth request for service ID: {auth_request.id_service}")
    
    # In a real application, validate the user against a database
    # For this example, we're using a hardcoded password
    if auth_request.password != "test_password":
        logger.warning("Invalid password provided")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    
    # Check if service exists
    service = get_service_by_id(auth_request.id_service)
    if not service:
        logger.warning(f"Service with ID {auth_request.id_service} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Service with ID {auth_request.id_service} not found",
        )
    
    # Generate a client ID (in a real app, this would be from your auth system)
    client_id = f"client_{uuid4()}"
    logger.info(f"Generated client ID: {client_id}")
    
    # Create access token with service permissions
    token_data = {
        "sub": client_id,
        "service_id": str(auth_request.id_service),
        "permissions": ["access"]
    }
    
    logger.info(f"Creating token with data: {token_data}")
    access_token, expire = create_access_token(token_data)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_at": expire
    } 