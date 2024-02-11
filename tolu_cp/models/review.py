#!/usr/bin/python3
from models.base_model import BaseModel

"""Module to handle the review class"""


class Review(BaseModel):
    """Class to handle review instances"""

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
