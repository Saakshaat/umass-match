from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from resources.api import main_router
from resources.auth import auth_dependency

# creating the FastAPI app instance
app = FastAPI()

# Add CORS permissions
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # shift to authenticated domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Add top-level router and dependencies to the FastAPI app
app.include_router(main_router, dependencies=[auth_dependency])
