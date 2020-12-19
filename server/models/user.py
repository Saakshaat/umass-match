from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import Model, IDMixin


class User(Model, IDMixin):
    __tablename__ = 'user'
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    # major = enum
    contacts = relationship("Contact", uselist=False)
    preferences = relationship("Preference", uselist=False)
    # matches: self-referential (https://docs.sqlalchemy.org/en/14/orm/self_referential.html)
