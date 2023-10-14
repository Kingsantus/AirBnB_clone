#!/usr/bin/python3
"""State Module handle the name of the state"""
import models
from models.base_model import BaseModel

class State(BaseModel):
    """State class that handle state name inherit frpm BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)

