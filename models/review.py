#!/usr/bin/python3
"""This script defines the Review Class"""

import models
from models.base_model import BaseModel

class Review(BaseModel):
    """This is the review class shich controls feedback  inheriting from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
