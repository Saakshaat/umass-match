from typing import List

from fastapi import APIRouter

from models import user as user_model
from resources.crud import create, read
from schemas import user as user_schemas, contact as contact_model
from . import session_dep

user_router = APIRouter()


@user_router.post("/user/", response_model=user_schemas.UserGet, status_code=201)
async def create_single_user(user_data: user_schemas.UserPost, db=session_dep):
    contacts = create.create_single_resource(model=contact_model.Contact, data=user_data.contacts, db=db)
    user = create.create_single_resource(model=user_model.User, data=user_data, db=db)
    user.contacts = contacts
    db.commit()

    return user


@user_router.get("/user/{user_id}/", response_model=user_schemas.UserGet, status_code=200)
async def get_single_user(user_id: int, db=session_dep):
    return read.read_single_resource(model=user_model.User, identifier='id', value=user_id, db=db)


@user_router.get("/users/", response_model=List[user_schemas.UserGet], status_code=200)
async def get_all_users(db=session_dep):
    return read.read_multiple_resources(model=user_model.User, db=db)
