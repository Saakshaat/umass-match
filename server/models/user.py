from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship

from .base import Model, IDMixin
from .match import Match


class User(Model, IDMixin):
    __tablename__ = 'user'
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)
    contacts = relationship("Contact", uselist=False)

    profile = relationship("Profile", uselist=False)

    last_matched_time = Column(DateTime, nullable=True, default=None)
    previous_matches = relationship('Match', foreign_keys=[Match.current_user_id], uselist=True)
