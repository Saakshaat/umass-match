import re

from pydantic import BaseModel, validator

from .contact import Contact
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

    class Config:
        orm_mode = True
