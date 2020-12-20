from datetime import datetime

from pydantic import BaseModel


class Match(BaseModel):
    id: int = None
    current_user_id: int = None
    other_user_id: int
    matched_at: datetime = None

    class Config:
        orm_mode = True
