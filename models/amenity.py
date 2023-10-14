#!/usr/bin/python3
<<<<<<< HEAD
"""This script defines the Amenity Class"""
=======
"""Amenity model that handle the amenity info in room"""
import models
>>>>>>> d82495985a52147f8ad7889ab7dd8a4599ebda06
from models.base_model import BaseModel


class Amenity(BaseModel):
<<<<<<< HEAD
"""This is the Amenity class which inherits the BaseModel"""
name = ""
=======
    """class amenity that inherit from baseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)

>>>>>>> d82495985a52147f8ad7889ab7dd8a4599ebda06
