#!/usr/bin/python3
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
