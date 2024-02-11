#!/usr/bin/python3
from models.base_model import BaseModel

"""Module to handle a user"""


class User(BaseModel):
    """Class to handle user instances"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
