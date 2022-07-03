#!/usr/bin/python3
"""
Unittest for class Place
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestPlace(unittest.TestCase):
    """
    basic tests for Place
    """
    def test_place(self):
        """
        method that tests Place
        """
        my_place = Place()
        my_place.name = "Peru"
        my_place.my_number = 60
        my_place.save()
        my_place_json = my_place.to_dict()

        self.assertEqual(type(my_place).__name__, "Place")
        self.assertEqual(my_place.name, "Peru")
        self.assertEqual(my_place.my_number, 60)
        self.assertEqual(type(my_place.__dict__), dict)

    def test_update_place(self):
        """
        method 2 that tests Place update
        """
        my_place_2 = Place()
        my_place_2.name = "Peru_2"
        my_place_2.my_number = 50
        hour_1 = my_place_2.updated_at
        my_place_2.save()
        my_place_2_json = my_place_2.to_dict()

        my_place_2.name = "Peru_2.0"
        my_place_2.my_number = 55
        hour_2 = my_place_2.updated_at
        my_place_2.save()
        my_place_2_json_2 = my_place_2.to_dict()

        self.assertNotEqual(hour_1, hour_2)
        self.assertNotEqual(my_place_2_json, my_place_2_json_2)

    def test_place_init(self):
        """
        method 3 that tests Place init
        """
        my_place_3 = Place()
        self.assertIsInstance(my_place_3, BaseModel)
        self.assertIsInstance(my_place_3.created_at, datetime)
        self.assertIsInstance(my_place_3.updated_at, datetime)
        self.assertNotIsInstance(my_place_3.id, uuid.UUID)
        self.assertIsInstance(my_place_3.id, str)
        self.assertIsInstance(my_place_3.city_id, str)
        self.assertIsInstance(my_place_3.name, str)
        self.assertIsInstance(my_place_3.user_id, str)
        self.assertIsInstance(my_place_3.description, str)
        self.assertIsInstance(my_place_3.number_rooms, int)
        self.assertIsInstance(my_place_3.number_bathrooms, int)
        self.assertIsInstance(my_place_3.max_guest, int)
        self.assertIsInstance(my_place_3.price_by_night, int)
        self.assertIsInstance(my_place_3.latitude, float)
        self.assertIsInstance(my_place_3.longitude, float)
        self.assertIsInstance(my_place_3.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
