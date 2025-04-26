from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import comments, users, routes, destinations

app = FastAPI(title="FastAPI Project")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(comments.router)
app.include_router(users.router)
app.include_router(routes.router)
app.include_router(destinations.router)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 