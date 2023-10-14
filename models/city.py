#!/usr/bin/python3
"""city module that process the city with state id"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """class city to handle city info"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
