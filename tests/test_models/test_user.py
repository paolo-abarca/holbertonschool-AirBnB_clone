#!/usr/bin/python3
"""
Unittest for class User
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestUser(unittest.TestCase):
    """
    basic tests for User
    """
    def test_User(self):
        """
        method that tests User
        """
        my_user = User()
        my_user.name = "Paolo"
        my_user.my_number = 22
        my_user.save()
        my_user_json = my_user.to_dict()

        self.assertEqual(type(my_user).__name__, "User")
        self.assertEqual(my_user.name, "Paolo")
        self.assertEqual(my_user.my_number, 22)
        self.assertEqual(type(my_user.__dict__), dict)

    def test_update_user(self):
        """
        method 2 that tests User update
        """
        my_user_2 = User()
        my_user_2.name = "Paolo_2"
        my_user_2.my_number = 50
        hour_1 = my_user_2.updated_at
        my_user_2.save()
        my_user_2_json = my_user_2.to_dict()

        my_user_2.name = "Paolo_2.0"
        my_user_2.my_number = 55
        hour_2 = my_user_2.updated_at
        my_user_2.save()
        my_user_2_json_2 = my_user_2.to_dict()

        self.assertNotEqual(hour_1, hour_2)
        self.assertNotEqual(my_user_2_json, my_user_2_json_2)

    def test_user_init(self):
        """
        method 3 that tests User init
        """
        my_user_3 = User()
        self.assertIsInstance(my_user_3, BaseModel)
        self.assertIsInstance(my_user_3.created_at, datetime)
        self.assertIsInstance(my_user_3.updated_at, datetime)
        self.assertNotIsInstance(my_user_3.id, uuid.UUID)
        self.assertIsInstance(my_user_3.id, str)
        self.assertIsInstance(my_user_3.email, str)
        self.assertIsInstance(my_user_3.first_name, str)
        self.assertIsInstance(my_user_3.last_name, str)
        self.assertIsInstance(my_user_3.password, str)


if __name__ == "__main__":
    unittest.main()
