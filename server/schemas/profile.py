from typing import List

from pydantic import BaseModel

from models.enums import UMassResidence, Club, Major


class Profile(BaseModel):
    user_id: int = None
    umass_residences: List[UMassResidence] = []
    clubs: List[Club] = []
    majors: List[Major] = []
    grad_year: int
    video_games: bool = False
    music: bool = False
    movies: bool = False

    class Config:
        orm_mode = True