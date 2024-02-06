#!/usr/bin/python3
import uuid
import datetime

"""Module to for the base class of all hbnb objects"""


class BaseModel:
    """
    The base class to define all the methods and attributes
    to be used in sub classes
    """

    def __init__(self):
        """Instantiating the class with values for id,
        the time and day created and the last updates done
        in the class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Method to print details of the class"""

        class_name = self.__class__.__name__
        st = f"[{class_name}] ({self.id}) {self.__dict__}"
        return st

    def save(self):
        """Method to update the updated at value"""

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dict of the key/value pairs of the instance"""

        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return dic
