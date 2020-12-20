import datetime

from sqlalchemy import or_
from sqlalchemy.orm import Session

from models.profile import Profile
from models.user import User


def get_all_matchable_users(user_data, db: Session):
    """
    A `matchable` user is someone who has not been matched with the current user before and has not been
    matched themself in the past 7 days.

    :param user_data: the data of the current user
    :param db: database session
    :return: list of `User` object of all matchable users
    """

    current_time = datetime.datetime.now()
    seven_days_ago = current_time - datetime.timedelta(seconds=10)  # TODO: revert to days

    past_matched_ids_list = [match.other_user_id for match in user_data.previous_matches]
    # an active user is someone who has not been matched in the past 7 days and
    matchable_users = db.query(User).filter(User.id != user_data.id).filter(User.id.notin_(
        past_matched_ids_list)).filter(or_(User.last_matched_time is None,
                                           User.last_matched_time < seven_days_ago)).all()  # TODO: convert into subquery for builder pattern

    return matchable_users


def filter_users_by_profile(user_data, prev_subquery, db: Session):
    filtered_users = db.query(User, prev_subquery).join(User.profile).filter(
        bool(set(Profile.majors) & set(user_data.profile.majors))).subquery()

    if len(filtered_users) == 0:
        return db.query(User, prev_subquery).all()

    return filtered_users


def match_user(user_id: int, db: Session):
    user_data = db.query(User).get(user_id)

    matchable_users = get_all_matchable_users(user_data, db)

    return matchable_users
