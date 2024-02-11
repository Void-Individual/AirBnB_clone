#!/usr/bin/python3
from models.base_model import BaseModel

"""Module to handle the City class"""


class City(BaseModel):
    """Class to handle city instances"""

    state_id = ''
    name = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
