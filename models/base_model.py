#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone
"""

import uuid
from os import getenv
from dateutil import parser
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object
    

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
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = kwargs.get('created_at', datetime.now())
            self.updated_at = kwargs.get('updated_at', datetime.now())

            for key, value in kwargs.items():
                if key in ['updated_at', 'created_at', 'id', '__class__']:
                    continue
                setattr(self, key, value)
            # if 'id' in kwargs:
            #     self.id = kwargs['id']
                
            # # if 'created_at' in kwargs:
            # #     self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%d %H:%M:%S.%f')
            
            # if 'created_at' in kwargs:
            #     if isinstance(kwargs['created_at'], str):
            #         # self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%d %H:%M:%S.%f')
            #         self.created_at = parser.parse(kwargs['created_at'])
            #     elif isinstance(kwargs['created_at'], datetime):
            #         self.created_at = kwargs['created_at']
            #     else:
            #         self.created_at = datetime.now()  # Default to current time if neither
            # else:
            #     self.created_at = datetime.now()
                        
            # # if 'updated_at' in kwargs:
            # #     self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%d %H:%M:%S.%f')
            
            # if 'updated_at' in kwargs:
            #     if isinstance(kwargs['updated_at'], str):
            #         self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%d %H:%M:%S.%f')
            #     elif isinstance(kwargs['updated_at'], datetime):
            #         self.updated_at = kwargs['updated_at']
            #     else:
            #         self.updated_at = datetime.now()  # Default to current time if neither
            # else:
            #     self.updated_at = datetime.now()

            # # Iterate over kwargs to set instance attribute
            # for key, value in kwargs.items():
            #     if key == 'updated_at' or key == 'created_at':
            #         if isinstance(value, str):
            #             value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
            #         elif isinstance(value, datetime):
            #             pass  # Value is already a datetime, no need to convert
            #         else:
            #             value = datetime.now()  # Handle if value is neither a string nor a datetime
            #         setattr(self, key, value)  # Set the attribute for 'created_at' or 'updated_at'
            #     else:
            #         setattr(self, key, value)  # For other keys, directly assign the value
                    
            #         # Use hasattr to check if attribute already exists
            #     if not hasattr(self, key) and key != '__class__':
            #         setattr(self, key, value)
                
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
        
        # Remove _sa_instance_state if it exists
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
    
    def delete(self):
        """ Delete the current instance from the storage
        """
        from models import storage
        storage.delete(self)
        # storage.save()
