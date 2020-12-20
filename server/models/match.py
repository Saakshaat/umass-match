from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func

from .base import Model, IDMixin


class Match(Model, IDMixin):
    __tablename__ = 'match'
    current_user_id = Column(Integer, ForeignKey('user.id'))

    other_user_id = Column(Integer, ForeignKey('user.id'))
    other_user_name = Column(String, nullable=False)

    matched_at = Column(DateTime, server_default=func.now())
