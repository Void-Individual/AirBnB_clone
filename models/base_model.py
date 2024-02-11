#!/usr/bin/python3
"""Module for BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Return string representation of BaseModel instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updating instance attribute 'updated_at' with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
