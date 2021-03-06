#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ

storage_type = environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade="all, delete", backref="user")
        reviews = relationship('Review', cascade="all, delete", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
