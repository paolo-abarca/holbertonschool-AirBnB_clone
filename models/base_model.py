#!/usr/bin/python3
"""
importing all necessary classes and modules
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    module for the classes that contains the base
    class for the Airbnb console
    """
    def __init__(self, *args, **kwargs):
        """
        initializing attributes of public instances
        """
        if len(kwargs) != 0:
            del kwargs["__class__"]

            for key, value in kwargs.items():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")

                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")

                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        method that prints the information of an object
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        method that updates the updated_at attribute
        with the current date and time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        method that returns a new dictionary of an instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
