from sqlalchemy import Column, Integer, ForeignKey, DateTime, func

from .base import Model, IDMixin


class Match(Model, IDMixin):
    __tablename__ = 'match'
    # username1, username2
    current_user_id = Column(Integer, ForeignKey('user.id'))

    other_user_id = Column(Integer, ForeignKey('user.id'))

    matched_at = Column(DateTime, server_default=func.now())
