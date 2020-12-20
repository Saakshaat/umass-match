import datetime

from sqlalchemy import or_
from sqlalchemy.orm import Session

from models.user import User
from schemas.match import FilterParams


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


class Filter:
    """
    This class implements a Filter object which has filter methods working on the Builder design pattern.

    ~~~~~~~
    Thank you Prof Marius
    ~~~~~~~
    """

    def __init__(self, user_data, matchable_users):
        self.user_data = user_data
        self.matchable_users = matchable_users

    def filter_users_by_majors(self):
        filtered_users = []
        for user in self.matchable_users:
            if bool(set(user.profile.majors) & set(self.user_data.profile.majors)):
                filtered_users.append(user)

        if len(filtered_users) == 0:
            return self

        self.matchable_users = filtered_users
        return self

    def filter_users_by_clubs(self):
        filtered_users = []
        for user in self.matchable_users:
            if bool(set(user.profile.clubs) & set(self.user_data.profile.clubs)):
                filtered_users.append(user)

        if len(filtered_users) == 0:
            return self

        self.matchable_users = filtered_users
        return self

    def filter_users_by_residences(self):
        filtered_users = []
        for user in self.matchable_users:
            if bool(set(user.profile.umass_residences) & set(self.user_data.profile.umass_residences)):
                filtered_users.append(user)

        if len(filtered_users) == 0:
            return self

        self.matchable_users = filtered_users
        return self

    def filter_by_grad_year(self):
        filtered_users = []
        for user in self.matchable_users:
            if user.profile.grad_year == self.user_data.profile.grad_year:
                filtered_users.append(user)

        if len(filtered_users) == 0:
            return self

        self.matchable_users = filtered_users
        return self

    def filter_by_video_games(self):
        filtered_users = []
        for user in self.matchable_users:
            if user.profile.video_games and self.user_data.profile.video_games:
                filtered_users.append(user)

        if len(filtered_users) == 0:
            return self

        self.matchable_users = filtered_users
        return self

    def filter_by_music(self):
        filtered_users = []
        for user in self.matchable_users:
            if user.profile.music and self.user_data.profile.music:
                filtered_users.append(user)

        if len(filtered_users) == 0:
            return self

        self.matchable_users = filtered_users
        return self

    def filter_by_movies(self):
        filtered_users = []
        for user in self.matchable_users:
            if user.profile.movies and self.user_data.profile.movies:
                filtered_users.append(user)

        if len(filtered_users) == 0:
            return self

        self.matchable_users = filtered_users
        return self


def match_user(user_id: int, filter_params: FilterParams, db: Session):
    user_data = db.query(User).get(user_id)

    matchable_users = get_all_matchable_users(user_data, db)

    filtered = Filter(user_data=user_data,
                      matchable_users=matchable_users)
    if filter_params.majors:
        filtered = filtered.filter_users_by_majors()

    if filter_params.clubs:
        filtered = filtered.filter_users_by_clubs()

    if filter_params.residences:
        filtered = filtered.filter_users_by_residences()

    if filter_params.grad_year:
        filtered = filtered.filter_by_grad_year()

    if filter_params.video_games:
        filtered = filtered.filter_by_video_games()

    if filter_params.music:
        filtered = filtered.filter_by_music()

    if filter_params.movies:
        filtered = filtered.filter_by_movies()

    filtered_users = filtered.matchable_users

    return filtered_users
