import re

from pydantic import BaseModel, validator


class Contact(BaseModel):
    id: int = None
    user_id: int = None
    discord: str = None
    phone: str = None
    snapchat: str = None
    instagram: str = None

    @validator('discord')
    def validate_discord_username(cls, v):
        if not None and not bool(re.match('[a-zA-Z].*#[0-9]{4}$', v)):
            raise ValueError('Discord Username should be valid and follow NameString#1234')
        return v

    @validator('phone')
    def validate_phone(cls, v):
        if not None and not bool(re.match('[0-9]{10}$', v)):
            raise ValueError('Phone Number must be valid 10 digit number')
        return v

    class Config:
        orm_mode = True
