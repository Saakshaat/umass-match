from sqlalchemy import Column, Integer, ForeignKey, Enum, Boolean

from .base import Model, IDMixin
from .enums import UMassResidence, Club, Major, VideoGame, Music
from .types import ArrayOfEnum


class Profile(Model, IDMixin):
    __tablename__ = 'profile'

    user_id = Column(Integer, ForeignKey('user.id'))

    umass_residences = Column(ArrayOfEnum(Enum(UMassResidence)))
    clubs = Column(ArrayOfEnum(Enum(Club)))

    majors = Column(ArrayOfEnum(Enum(Major)), nullable=False)
    grad_year = Column(Integer, nullable=False)

    video_games = Column(ArrayOfEnum(Enum(VideoGame)))
    music = Column(ArrayOfEnum(Enum(Music)))
    movies = Column(Boolean, nullable=True)  # shift to ArrayOfEnum for what kind of movies
