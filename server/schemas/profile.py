from typing import List

from pydantic import BaseModel

from models.enums import (
    UMassResidence,
    Club,
    Major,
    VideoGame,
    Music,
    Movie
)


class Profile(BaseModel):
    user_id: int = None
    umass_residences: List[UMassResidence] = []
    clubs: List[Club] = []
    majors: List[Major] = []
    grad_year: int
    video_games: List[VideoGame] = []
    music: List[Music] = []
    movies: List[Movie] = []

    class Config:
        orm_mode = True
