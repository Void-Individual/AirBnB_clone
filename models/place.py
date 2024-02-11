#!/usr/bin/python3
from models.base_model import BaseModel

"""Module to handle the place class"""


class Place(BaseModel):
    """Class to handle place instances"""

    name = ''
    city_id = ''
    user_id = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
