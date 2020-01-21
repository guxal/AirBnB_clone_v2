#!/usr/bin/python3
"""State Class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import environ
import models

storage_type = environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              cascade="all, delete-orphan", backref="state")
    else:
        name = ""

    if storage_type != 'db':
        @property
        def cities(self):
            """
            join cities with state_id
            """
            list_cities = []
            all_cities = models.storage.all(City)
            for key, city_obj in all_cities.items():
                if city_obj.state_id == self.id:
                    list_cities.append(city_obj)
            return list_cities
