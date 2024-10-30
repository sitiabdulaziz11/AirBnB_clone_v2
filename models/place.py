#!/usr/bin/python3
""" Place Module for HBNB project
"""
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
import models

from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay
    """
    __tablename__ = 'places'
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name= Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms= Column(Integer, )
        number_bathrooms= Column(Integer, default=0)
        max_guest= Column(Integer, default=0)
        price_by_night= Column(Integer, default=0)
        latitude= Column(Float)
        longitude= Column(Float)
        amenity_ids = []
        # amenity_ids = Column(String(1024), nullable=True)
        # reviews = relationship("Review", backref="place", cascade="all, delete")
        reviews = relationship("Review", backref="place", cascade="delete")
        
        amenities = relationship('Amenity', secondary="place_amenity", back_populates='place_amenities', viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        
        @property  # used to define methods in a class that can be accessed like attributes.
        def reviews(self):
            """Get a list of all linked Reviews.
            """

            review_list = []

            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)

            return review_list

        @property
        def amenities(self):
            """Get and Set linked Amenities.
            """

            amenity_list = []

            for amenity in models.storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)

            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Adding an Amenity.id to the amenity_ids
            """

            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
