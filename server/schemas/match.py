from datetime import datetime

from pydantic import BaseModel


class Match(BaseModel):
    id: int = None
    current_user_id: int = None
    other_user_id: int
    matched_at: datetime = None

    class Config:
        orm_mode = True


class FilterParams(BaseModel):
    majors: bool = False
    clubs: bool = False
    residences: bool = False
    grad_year: bool = False
    video_games: bool = False
    music: bool = False
    movies: bool = False
