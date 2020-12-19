from sqlalchemy import Column, Integer, String, ForeignKey

from .base import Model, IDMixin


class Contact(Model, IDMixin):
    __tablename__ = 'contact'
    
    user_id = Column(Integer, ForeignKey('user.id'))
    discord = Column(String, nullable=True)
    phone = Column(Integer, nullable=True)
    snapchat = Column(String, nullable=True)
    instagram = Column(String, nullable=True)
