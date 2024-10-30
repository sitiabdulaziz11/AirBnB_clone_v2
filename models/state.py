#!/usr/bin/python3
""" State Module for HBNB project
"""
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    
    __tablename__ = "states"
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""
        
        @property
        def cities(self):
            """returns the list of City instances with state_id
            """
            from models import storage
            cities_list = []
            for city in storage.get_all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
