#!/usr/bin/python3
"""
importing the BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    initializing public class attribute
    """
    place_id = ""
    user_id = ""
    text = ""
