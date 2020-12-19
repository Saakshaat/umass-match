import re

from pydantic import BaseModel, validator

from .contact import Contact
from .preference import Preference


class UserGeneral(BaseModel):
    first_name: str
    middle_name: str = None
    last_name: str
    email: str
    contacts: Contact
    preferences: Preference


class UserPost(UserGeneral):
    @validator('email')
    def validate_umass_email(cls, v):
        if not bool(re.match('^..*@umass\.edu', v)):
            raise ValueError('Email should belong to a UMass domain')

        return v


class UserGet(UserGeneral):
    id: int

    class Config:
        orm_mode = True
