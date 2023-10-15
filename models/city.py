#!/usr/bin/python3
"""This script defines City Class"""

import models
from models.base_model import BaseModel

class City(BaseModel):
    """This is the city class which controls info inheriting from the BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
