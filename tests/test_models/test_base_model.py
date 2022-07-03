#!/usr/bin/python3
"""
Unittest for class Base Model
"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


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

    def test_base_model_2(self):
        """
        method 2 that tests BaseModel
        """
        dict_1 = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                  'created_at': '2017-09-28T21:03:54.052298',
                  '__class__': 'BaseModel',
                  'my_number': 89,
                  'updated_at': '2017-09-28T21:03:54.052302',
                  'name': 'My_First_Model'}

        my_model_3 = BaseModel(**dict_1)
        name = type(my_model_3).__name__
        format_date = '\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}'
        self.assertEqual(name, "BaseModel")
        self.assertEqual(len(my_model_3.id), 36)
        self.assertNotEqual(my_model_3.id, None)
        self.assertIsInstance(my_model_3.id, str)
        self.assertIsInstance(my_model_3.created_at, datetime)
        self.assertIsInstance(my_model_3.updated_at, datetime)
        self.assertRegex(str(my_model_3.created_at), format_date)
        self.assertRegex(str(my_model_3.updated_at), format_date)
        self.assertEqual(my_model_3.name, 'My_First_Model')
        self.assertEqual(my_model_3.my_number, 89)


if __name__ == "__main__":
    unittest.main()
