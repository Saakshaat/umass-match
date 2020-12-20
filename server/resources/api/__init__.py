from fastapi import APIRouter

main_router = APIRouter()

from resources.db import session_dependency

session_dep = session_dependency()


@main_router.get("/", status_code=200)
async def root():
    return {"msg": "Welcome to UMass Match!"}


from .user import user_router
from .match import match_router

# add individual routers to top-level router
main_router.include_router(user_router)
main_router.include_router(match_router)
