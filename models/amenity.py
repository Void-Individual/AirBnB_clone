#!/usr/bin/python3
from models.base_model import BaseModel

"""Module to handle the amenity class"""


class Amenity(BaseModel):
    """Class to handle amenity instances"""

    name = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
