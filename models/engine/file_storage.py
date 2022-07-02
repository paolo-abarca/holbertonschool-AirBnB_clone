#!/usr/bin/python3
"""
importing all necessary classes
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    initializing private class attributes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        method that returns all objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)

                for key, value in obj_dict.items():
                    name_class = eval(value["__class__"])(**value)
                    self.__objects[key] = name_class

        except FileNotFoundError:
            return

    def classes(self):
        """
        returns a full dictionary of all classes
        and their references
        """
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}

        return classes
