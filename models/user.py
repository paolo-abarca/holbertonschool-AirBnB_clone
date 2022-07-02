#!/usr/bin/python3
"""
importing the BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    initializing public class attribute
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
