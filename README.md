# FastAPI Project

This is a basic FastAPI project setup.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, use:
```bash
uvicorn main:app --reload
```

The application will be available at:
- http://localhost:8000
- API documentation at http://localhost:8000/docs
- Alternative API documentation at http://localhost:8000/redoc

## Endpoints

- GET `/`: Returns a welcome message
- GET `/health`: Health check endpoint 