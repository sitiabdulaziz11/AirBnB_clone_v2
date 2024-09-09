#!/usr/bin/python3
""" State Module for HBNB project
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """ Amenitys of the places
    """
    __tablename__ = 'amenities'
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        if getenv("HBNB_TYPE_STORAGE") == "db":
            place_amenity = Table("place_amenity", Base.metadata,
                        Column("place_id", String(60),
                                ForeignKey("places.id"),
                                primary_key=True, nullable=False),
                        Column("amenity_id", String(60),
                                ForeignKey("amenities.id"),
                                primary_key=True, nullable=False))

        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
        # place_amenities = relationship("Place", secondary=place_amenity, back_populates="amenities")
    else:
        name = ""
