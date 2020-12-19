from typing import List

from pydantic import BaseModel

from models.enums import UMassResidence, Club


class Profile(BaseModel):
    user_id: int = None
    umass_residences: List[UMassResidence] = []
    clubs: List[Club] = []

    class Config:
        orm_mode = True
