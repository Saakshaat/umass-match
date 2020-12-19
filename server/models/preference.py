from sqlalchemy import Column, Integer, ForeignKey, Enum

from .base import Model, IDMixin
from .enums import UMassResidence
from .types import ArrayOfEnum


class Preference(Model, IDMixin):
    __tablename__ = 'preference'

    user_id = Column(Integer, ForeignKey('user.id'))
    umass_residences = Column(ArrayOfEnum(Enum(UMassResidence), default=UMassResidence.unknown))
