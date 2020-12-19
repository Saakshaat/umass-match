from sqlalchemy import Column, Integer, ForeignKey, Enum

from .base import Model, IDMixin
from .enums import UMassResidence, Club
from .types import ArrayOfEnum


class Profile(Model, IDMixin):
    __tablename__ = 'profile'

    user_id = Column(Integer, ForeignKey('user.id'))
    umass_residences = Column(ArrayOfEnum(Enum(UMassResidence)))
    clubs = Column(ArrayOfEnum(Enum(Club)))

