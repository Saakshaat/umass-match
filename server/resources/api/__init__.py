from fastapi import APIRouter

main_router = APIRouter()


@main_router.get("/", status_code=200)
async def root():
    return {"msg": "Welcome to UMass Match!"}
