#!/usr/bin/python3
"""This script defines the Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
"""This is the Review class which inherits the BaseModel"""
place_id = ""
user_id = ""
text = ""
