#!/usr/bin/python3
<<<<<<< HEAD
"""This script defines Place Class"""

from models.base_model import BaseModel


class Place(BaseModel):
"""This is the Place class which inherits the BaseModel"""
city_id = ""
user_id = ""
name = ""
description = ""
number_rooms = 0
number_bathrooms = 0
max_guest = 0
price_by_night = 0
latitude = 0.0
longitude = 0.0
amenity_ids = []
=======
"""place module handle info of the place"""
import models
from models.base_model import BaseModel

class Place(BaseModel):
    """place class that handle info inheriting from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
>>>>>>> d82495985a52147f8ad7889ab7dd8a4599ebda06
