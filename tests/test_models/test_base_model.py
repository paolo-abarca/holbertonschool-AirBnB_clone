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

    def test_update_base_model(self):
        """
        method 2 that tests BaseModel update
        """
        my_model_2 = BaseModel()
        my_model_2.name = "My Second Model"
        my_model_2.my_number = 90
        hour_1 = my_model_2.updated_at
        my_model_2.save()
        my_model_2_json = my_model_2.to_dict()

        my_model_2.name = "My Second Model 2.0"
        my_model_2.my_number = 95
        hour_2 = my_model_2.updated_at
        my_model_2.save()
        my_model_2_json_2 = my_model_2.to_dict()

        self.assertNotEqual(hour_1, hour_2)
        self.assertNotEqual(my_model_2_json, my_model_2_json_2)


if __name__ == "__main__":
    unittest.main()
