#!/usr/bin/python3
"""
importing the BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    initializing public class attribute
    """
    state_id = ""
    name = ""
