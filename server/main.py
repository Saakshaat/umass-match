from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from resources.api import main_router


# creating the FastAPI app instance
app = FastAPI()

# Add CORS permissions
app.add_middleware(
	CORSMiddleware,
	allows_origins=["https://umatch.space", "http://umatch.space", "http://localhost", "http://localhost:8080"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)

# Add top-level router and dependencies to the FastAPI app
app.include_router(main_router)
