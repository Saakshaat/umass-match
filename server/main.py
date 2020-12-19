from fastapi import FastAPI

from resources.api import main_router

# creating the FastAPI app instance
app = FastAPI()

# Add top-level router and dependencies to the FastAPI app
app.include_router(main_router)
