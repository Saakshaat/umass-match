from fastapi import APIRouter

main_router = APIRouter()

from resources.db import session_dependency

session_dep = session_dependency()


@main_router.get("/", status_code=200)
async def root():
    return {"msg": "Welcome to UMass Match!"}
