#!/usr/bin/python3
"""This script defines the Amenity Class"""

import models
from models.base_model import BaseModel

class Amenity(BaseModel):
    """This is the Amenity class which inherits the BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
