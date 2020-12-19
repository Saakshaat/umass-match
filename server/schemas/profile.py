from typing import List

from pydantic import BaseModel

from models.enums import UMassResidence, Clubs


class Profile(BaseModel):
    user_id: int = None
    umass_residences: List[UMassResidence] = []
    clubs: List[Clubs] = []

    class Config:
        orm_mode = True
