#!/usr/bin/python3
<<<<<<< HEAD
"""This script defines the Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
"""This is the Review class which inherits the BaseModel"""
place_id = ""
user_id = ""
text = ""
=======
"""Review module handle all feedback info about the place"""
import models
from models.base_model import BaseModel

class Review(BaseModel):
    """review class inherit from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
>>>>>>> d82495985a52147f8ad7889ab7dd8a4599ebda06
