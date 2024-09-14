#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone
"""

import uuid
from os import getenv
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


# if getenv("HBNB_TYPE_STORAGE") == "db":
Base = declarative_base()
# else:
    # Base = object
    

class BaseModel:
    """A base class for all hbnb models
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self) # moved to save
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            else:
                self.id = str(uuid.uuid4())
                
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()

            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.now()

            # Iterate over kwargs to set instance attribute
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    
                    # Use hasattr to check if attribute already exists
                if not hasattr(self, key) and key != '__class__':
                    setattr(self, key, value)
                
        # kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
        #                                 '%Y-%m-%dT%H:%M:%S.%f')
        # kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
        #                                 '%Y-%m-%dT%H:%M:%S.%f')
        # del kwargs['__class__']
        # self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
