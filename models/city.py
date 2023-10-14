#!/usr/bin/python3
<<<<<<< HEAD
"""This script defines the City Class"""
=======
"""city module that process the city with state id"""
import models
>>>>>>> d82495985a52147f8ad7889ab7dd8a4599ebda06
from models.base_model import BaseModel


class City(BaseModel):
<<<<<<< HEAD
"""This is the city class which inherits the BaseModel"""
state_id = ""
name = ""
=======
    """class city to handle city info"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
>>>>>>> d82495985a52147f8ad7889ab7dd8a4599ebda06
