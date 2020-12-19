from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship

from .base import Model, IDMixin
from .enums import Major
from .types import ArrayOfEnum


class User(Model, IDMixin):
    __tablename__ = 'user'
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)

    email = Column(String, nullable=False)
    contacts = relationship("Contact", uselist=False)

    majors = Column(ArrayOfEnum(Enum(Major)), nullable=False)
    preferences = relationship("Profile", uselist=False)
    # matches: self-referential (https://docs.sqlalchemy.org/en/14/orm/self_referential.html)
