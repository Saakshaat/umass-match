from datetime import datetime

from fastapi import APIRouter

from models import user as user_model, match
from resources.crud import read, create
from schemas import user as user_schemas, match as match_schema
from . import session_dep

matching_router = APIRouter()


@matching_router.post('/user/{user_id}/match/', response_model=user_schemas.UserGet, status_code=201)
async def add_new_match(user_id: int, match_data: match_schema.Match, db=session_dep):
    other_user_id = match_data.other_user_id
    user_data = read.read_single_resource(model=user_model.User, identifier='id', value=user_id, db=db)

    current_match_data = match_schema.Match(current_user_id=user_id, other_user_id=other_user_id)
    other_match_data = match_schema.Match(current_user_id=other_user_id, other_user_id=user_id)

    current_match = create.create_single_isolated_resource(model=match.Match, data=current_match_data, db=db)
    other_match = create.create_single_isolated_resource(model=match.Match, data=other_match_data, db=db)

    user_data.last_matched_time = datetime.now()

    db.add(current_match)
    db.add(other_match)

    db.commit()

    db.refresh(user_data)

    print(vars(user_data))
    print(user_data.previous_matches)

    return user_data
