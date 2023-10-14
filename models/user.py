#!/usr/bin/python3
"""User Module Handle the User datas (create,show,update,delete)"""
import models
from models.base_model import BaseModel

class User(BaseModel):
    """User Class with CRUD"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
