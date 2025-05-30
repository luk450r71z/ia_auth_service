from typing import List
from uuid import uuid4, UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.auth.jwt import verify_token
from app.db.database import get_all_services, get_service_by_id, create_session
from app.models.schemas import AIService, ServiceRequest, ServiceSession

router = APIRouter(prefix="/services", tags=["Services"])


@router.get("/discovery", response_model=List[AIService])
async def discover_services():
    """
    Endpoint to discover available AI services
    """
    return get_all_services()


@router.post("/session", response_model=ServiceSession)
async def create_service_session(service_request: ServiceRequest, token_data: dict = Depends(verify_token)):
    """
    Create a session for an AI service using the access token
    """
    service_id = token_data.get("service_id")
    client_id = token_data.get("sub")
    
    # Check if service exists - convert string to UUID
    service = get_service_by_id(UUID(service_id))
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Service with ID {service_id} not found",
        )
    
    # In a real application, validate the data against the service requirements
    
    # Generate session
    session_id = uuid4()
    
    # Create a resource URI for the service
    if service["name_service"] == "chatbot-interview":
        resource_uri = f"https://api.example.com/chatbot/{session_id}"
    else:
        resource_uri = f"https://api.example.com/services/{service_id}/{session_id}"
    
    # Create and store the session
    session = create_session(
        session_id=session_id,
        service_id=UUID(service_id),
        client_id=client_id,
        resource_uri=resource_uri
    )
    
    return session 