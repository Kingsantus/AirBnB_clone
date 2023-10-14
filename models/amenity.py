#!/usr/bin/python3
"""Amenity model that handle the amenity info in room"""
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class amenity that inherit from baseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)

