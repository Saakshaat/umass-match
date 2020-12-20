from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base()


class IDMixin:
    id = Column(Integer(), autoincrement=True,
                primary_key=True)  # replace column type with how OAuth provider identifies
