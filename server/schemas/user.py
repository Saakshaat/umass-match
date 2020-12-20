import re
from datetime import datetime
from typing import List

from pydantic import BaseModel, validator

from .contact import Contact
from .match import Match
from .profile import Profile


class UserGeneral(BaseModel):
    first_name: str
    last_name: str
    email: str
    contacts: Contact
    profile: Profile


class UserPost(UserGeneral):
    @validator('email')
    def validate_umass_email(cls, v):
        if not bool(re.match('^..*@umass\.edu', v)):
            raise ValueError('Email should belong to a UMass domain')

        return v


class UserGet(UserGeneral):
    id: int
    last_matched_time: datetime = None
    previous_matches: List[Match] = []

    class Config:
        orm_mode = True
