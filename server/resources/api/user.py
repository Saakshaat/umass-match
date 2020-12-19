from fastapi import APIRouter, HTTPException

from models import user as user_model
from resources.crud import create
from schemas import user as user_schemas
from . import session_dep

user_router = APIRouter()


@user_router.post("/user/", response_model=user_schemas.UserGet, status_code=201)
async def create_single_user(user_data: user_schemas.UserPost, db=session_dep):
    return create.create_single_resource(model=user_model.User, data=user_data, db=db)


@user_router.get("/user/{user_id}/", response_model=user_schemas.UserGet, status_code=200)
async def get_single_user(user_id: int, db=session_dep):
    user = db.query(user_model.User).get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f'No user with id={user_id} found')

    return user
