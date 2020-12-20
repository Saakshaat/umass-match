import datetime
from operator import attrgetter

from fastapi import APIRouter, HTTPException

from models import user as user_model, match
from resources.crud import read, create, custom
from schemas import user as user_schemas
from schemas.match import Match, FilterParams
from . import session_dep

match_router = APIRouter()


@match_router.post('/user/{user_id}/match/', response_model=user_schemas.UserGet, status_code=201)
async def add_new_match(user_id: int, filter_params: FilterParams, db=session_dep):
    user_data = read.read_single_resource(model=user_model.User, identifier='id', value=user_id, db=db)

    # check if user has already matched in the past 3 days
    if user_data.last_matched_time:
        three_days_after_match = user_data.last_matched_time + datetime.timedelta(days=3)
        current_time = datetime.datetime.now()

        if current_time < three_days_after_match:
            next_valid_date = datetime.date(day=three_days_after_match.day, month=three_days_after_match.month,
                                            year=three_days_after_match.year).strftime('%A %d %B %Y')
            raise HTTPException(status_code=403,
                                detail=f"You've already matched within the past 3 days. Wait till {next_valid_date}")

    # run matching algorithm
    matched_user = custom.match_user(user_id=user_id, filter_params=filter_params, db=db)

    # create Match Pydantic models
    current_match_data = Match(current_user_id=user_id, other_user_id=matched_user.id,
                               other_user_name=f"{matched_user.first_name} {matched_user.last_name}")
    other_match_data = Match(current_user_id=matched_user.id, other_user_id=user_id,
                             other_user_name=f"{user_data.first_name} {user_data.last_name}")

    # create match objects in the database
    current_match = create.create_single_isolated_resource(model=match.Match, data=current_match_data, db=db)
    other_match = create.create_single_isolated_resource(model=match.Match, data=other_match_data, db=db)

    # update last_matched_time for each user
    user_data.last_matched_time = datetime.datetime.now()
    matched_user.last_matched_time = datetime.datetime.now()

    # commit all changes in the database
    db.add(current_match)
    db.add(other_match)

    db.commit()

    db.refresh(user_data)

    return matched_user


@match_router.get("/user/{user_id}/match/latest/", response_model=user_schemas.UserGet, status_code=200)
async def get_latest_match(user_id: int, db=session_dep):
    user_data = read.read_single_resource(model=user_model.User, identifier='id', value=user_id, db=db)

    if user_data is None or user_data.previous_matches == []:
        raise HTTPException(status_code=404, detail='No matches made yet!')

    latest_match = max(user_data.previous_matches, key=attrgetter('matched_at'))

    return read.read_single_resource(model=user_model.User, identifier='id', value=latest_match.other_user_id, db=db)
