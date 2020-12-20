import datetime

from models.user import User


def get_all_matchable_users(user_data, db):
    """
    A `matchable` user is someone who has not been matched with the current user before and has not been
    matched themself in the past 7 days.

    :param user_data: the data of the current user
    :param db: database session
    :return: list of `User` object of all matchable users
    """

    current_time = datetime.datetime.now()
    seven_days_ago = current_time - datetime.timedelta(minutes=1)

    past_matched_ids_list = [match.id for match in user_data.previous_matches]

    # an active user is someone who has not been matched in the past 7 days and
    matchable_users = db.query(User).filter(
        User.last_matched_time > seven_days_ago and User.id not in past_matched_ids_list).all()

    return matchable_users


def match_user(user_id: int, db):
    user_data = db.query(User).get(user_id)

    matchable_users = get_all_matchable_users(user_data, db)

    return matchable_users
