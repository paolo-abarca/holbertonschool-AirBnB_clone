#!/usr/bin/python3
"""
Unittest for class City
"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestCity(unittest.TestCase):
    """
    basic tests for City
    """
    def test_city(self):
        """
        method that tests City
        """
        my_city = City()
        my_city.name = "Lima"
        my_city.my_number = 30
        my_city.save()
        my_city_json = my_city.to_dict()

        self.assertEqual(type(my_city).__name__, "City")
        self.assertEqual(my_city.name, "Lima")
        self.assertEqual(my_city.my_number, 30)
        self.assertEqual(type(my_city.__dict__), dict)

    def test_update_city(self):
        """
        method 2 that tests City
        """
        my_city_2 = City()
        my_city_2.name = "Lima_2"
        my_city_2.my_number = 50
        hour_1 = my_city_2.updated_at
        my_city_2.save()
        my_city_2_json = my_city_2.to_dict()

        my_city_2.name = "Lima_2.0"
        my_city_2.my_number = 55
        hour_2 = my_city_2.updated_at
        my_city_2.save()
        my_city_2_json_2 = my_city_2.to_dict()

        self.assertNotEqual(hour_1, hour_2)
        self.assertNotEqual(my_city_2_json, my_city_2_json_2)

    def test_city_init(self):
        """
        method 3 that tests City init
        """
        my_city_3 = City()
        self.assertIsInstance(my_city_3, BaseModel)
        self.assertIsInstance(my_city_3.created_at, datetime)
        self.assertIsInstance(my_city_3.updated_at, datetime)
        self.assertNotIsInstance(my_city_3.id, uuid.UUID)
        self.assertIsInstance(my_city_3.id, str)
        self.assertIsInstance(my_city_3.state_id, str)
        self.assertIsInstance(my_city_3.name, str)


if __name__ == "__main__":
    unittest.main()
