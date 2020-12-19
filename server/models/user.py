from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import Model, IDMixin


class User(Model, IDMixin):
    __tablename__ = 'user'
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    email = Column(String, nullable=False)
    contacts = relationship("Contact", uselist=False)

    profile = relationship("Profile", uselist=False)
    # matches: self-referential (https://docs.sqlalchemy.org/en/14/orm/self_referential.html)
