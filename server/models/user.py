from sqlalchemy import Column, String

from .base import Model, IDMixin


class User(Model, IDMixin):
    __tablename__ = 'user'
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
