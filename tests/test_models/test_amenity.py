#!/usr/bin/python3
"""
Unittest for class Amenity
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestAmenity(unittest.TestCase):
    """
    basic tests for Amenity
    """
    def test_amenity(self):
        """
        method that tests Amenity
        """
        my_amenity = Amenity()
        my_amenity.name = "Holberton"
        my_amenity.my_number = 40
        my_amenity.save()
        my_amenity_json = my_amenity.to_dict()

        self.assertEqual(type(my_amenity).__name__, "Amenity")
        self.assertEqual(my_amenity.name, "Holberton")
        self.assertEqual(my_amenity.my_number, 40)
        self.assertEqual(type(my_amenity.__dict__), dict)

    def test_update_amenity(self):
        """
        method 2 that tests Amenity update
        """
        my_amenity_2 = Amenity()
        my_amenity_2.name = "Holberton_2"
        my_amenity_2.my_number = 50
        hour_1 = my_amenity_2.updated_at
        my_amenity_2.save()
        my_amenity_2_json = my_amenity_2.to_dict()

        my_amenity_2.name = "Holberton_2.0"
        my_amenity_2.my_number = 55
        hour_2 = my_amenity_2.updated_at
        my_amenity_2.save()
        my_amenity_2_json_2 = my_amenity_2.to_dict()

        self.assertNotEqual(hour_1, hour_2)
        self.assertNotEqual(my_amenity_2_json, my_amenity_2_json_2)

    def test_amenity_init(self):
        """
        method 3 that tests Amenity init
        """
        my_amenity_3 = Amenity()
        self.assertIsInstance(my_amenity_3, BaseModel)
        self.assertIsInstance(my_amenity_3.created_at, datetime)
        self.assertIsInstance(my_amenity_3.updated_at, datetime)
        self.assertNotIsInstance(my_amenity_3.id, uuid.UUID)
        self.assertIsInstance(my_amenity_3.id, str)
        self.assertIsInstance(my_amenity_3.name, str)


if __name__ == "__main__":
    unittest.main()
