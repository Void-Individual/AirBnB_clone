#!/usr/python3
from models.base_model import BaseModel

"""Module for the state class"""

class State(BaseModel):
    """Class to handle state instances"""

    name = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        