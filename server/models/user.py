from sqlalchemy import Column, String

from .base import Model, IDMixin


class User(Model, IDMixin):
    __tablename__ = 'user'
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    # contact (phone, discord, snapchat, instagram) = another model
    # preferences = another model
    # matches: self-referential (https://docs.sqlalchemy.org/en/14/orm/self_referential.html)
