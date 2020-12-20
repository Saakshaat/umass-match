from datetime import datetime
from operator import attrgetter
from typing import List

from fastapi import APIRouter, HTTPException

from models import user as user_model, match
from resources.crud import read, create, custom
from schemas import user as user_schemas
from schemas.match import Match, FilterParams
from . import session_dep

matching_router = APIRouter()


@matching_router.post('/user/{user_id}/match/{other_user_id}', response_model=List[user_schemas.UserGet],
                      status_code=201)
async def add_new_match(user_id: int, other_user_id: int, filter_params: FilterParams, db=session_dep):
    matched_user = custom.match_user(user_id=user_id, filter_params=filter_params, ldb=db)
    user_data = read.read_single_resource(model=user_model.User, identifier='id', value=user_id, db=db)
    other_user_data = read.read_single_resource(model=user_model.User, identifier='id', value=other_user_id, db=db)

    current_match_data = Match(current_user_id=user_id, other_user_id=other_user_id)
    other_match_data = Match(current_user_id=other_user_id, other_user_id=user_id)

    current_match = create.create_single_isolated_resource(model=match.Match, data=current_match_data, db=db)
    other_match = create.create_single_isolated_resource(model=match.Match, data=other_match_data, db=db)

    user_data.last_matched_time = datetime.now()
    other_user_data.last_matched_time = datetime.now()

    db.add(current_match)
    db.add(other_match)

    db.commit()

    db.refresh(user_data)

    return matched_user


@matching_router.get("/user/{user_id}/match/latest/", response_model=user_schemas.UserGet, status_code=200)
async def get_latest_match(user_id: int, db=session_dep):
    user_data = read.read_single_resource(model=user_model.User, identifier='id', value=user_id, db=db)

    if user_data is None or user_data.previous_matches == []:
        raise HTTPException(status_code=404, detail='No matches made yet!')

    latest_match = max(user_data.previous_matches, key=attrgetter('matched_at'))

    return read.read_single_resource(model=user_model.User, identifier='id', value=latest_match.other_user_id, db=db)
