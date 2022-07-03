#!/usr/bin/python3
"""
Unittest for class Base Model
"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase_model(unittest.TestCase):
    """
    basic tests for BaseModel
    """
    def test_base_model(self):
        """
        method that tests BaseModel
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        my_model_json = my_model.to_dict()

        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(type(my_model.__dict__), dict)


if __name__ == "__main__":
    unittest.main()
