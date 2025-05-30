# AI Services Authentication API

A REST API service built with FastAPI that supports JWT authentication for AI service discovery and access.

## Features

- AI Services Discovery: Endpoint that lists available AI services with details
- JWT-based Authentication: Secure access to services with JSON Web Tokens
- Service Session Creation: Create sessions for AI services with appropriate access controls

## Project Structure

```
├── app/
│   ├── api/
│   │   ├── auth.py       # Authentication API endpoints
│   │   └── services.py   # Services API endpoints
│   ├── auth/
│   │   └── jwt.py        # JWT token handling
│   ├── db/
│   │   └── database.py   # Mock database
│   └── models/
│       └── schemas.py    # Pydantic models
├── config.py             # Application configuration
├── main.py               # FastAPI application entry point
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Requirements

- Python 3.8+
- FastAPI
- PyJWT
- Uvicorn
- Python-dotenv

## Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
uvicorn main:app --reload
```

## API Endpoints

### Service Discovery

- `GET /services/discovery`: List all available AI services

### Authentication

- `POST /auth/token`: Get an access token for a specific service
  - Required parameters: `id_service` (UUID), `password` (string)

### Service Session

- `POST /services/session`: Create a session for an authenticated service
  - Required header: `Authorization: Bearer <token>`
  - Required body: Service-specific data as JSON

## Example Usage

1. Discover available services:
   ```
   GET /services/discovery
   ```

2. Request a token for a service:
   ```
   POST /auth/token
   {
     "id_service": "3f91e6c2-1d43-4a77-9c17-6ab872a4b2db",
     "password": "test_password"
   }
   ```

3. Create a service session:
   ```
   POST /services/session
   Authorization: Bearer <token>
   {
     "data": {
       "questions": [
         {"question": "Tell me about yourself"}
       ]
     }
   }
   ```