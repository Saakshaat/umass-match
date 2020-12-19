from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base()


class IDMixin:
    id = Column(Integer(), primary_key=True)
