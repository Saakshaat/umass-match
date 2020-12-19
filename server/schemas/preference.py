from typing import List

from pydantic import BaseModel

from models.enums import UMassResidence


class Preference(BaseModel):
    user_id: int = None
    umass_residences: List[UMassResidence] = []

    class Config:
        orm_mode = True
