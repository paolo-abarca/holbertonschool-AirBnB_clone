#!/usr/bin/python3
"""
Unittest for class Review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestReview(unittest.TestCase):
    """
    basic tests for Review
    """
    def test_review(self):
        """
        method that tests Review
        """
        my_review = Review()
        my_review.name = "review"
        my_review.my_number = 70
        my_review.save()
        my_review_json = my_review.to_dict()

        self.assertEqual(type(my_review).__name__, "Review")
        self.assertEqual(my_review.name, "review")
        self.assertEqual(my_review.my_number, 70)
        self.assertEqual(type(my_review.__dict__), dict)

    def test_update_review(self):
        """
        method 2 that tests Review update
        """
        my_review_2 = Review()
        my_review_2.name = "review_2"
        my_review_2.my_number = 50
        hour_1 = my_review_2.updated_at
        my_review_2.save()
        my_review_2_json = my_review_2.to_dict()

        my_review_2.name = "review_2.0"
        my_review_2.my_number = 55
        hour_2 = my_review_2.updated_at
        my_review_2.save()
        my_review_2_json_2 = my_review_2.to_dict()

        self.assertNotEqual(hour_1, hour_2)
        self.assertNotEqual(my_review_2_json, my_review_2_json_2)

    def test_review_init(self):
        """
        method 3 that tests Review init
        """
        my_review_3 = Review()
        self.assertIsInstance(my_review_3, BaseModel)
        self.assertIsInstance(my_review_3.created_at, datetime)
        self.assertIsInstance(my_review_3.updated_at, datetime)
        self.assertNotIsInstance(my_review_3.id, uuid.UUID)
        self.assertIsInstance(my_review_3.id, str)
        self.assertIsInstance(my_review_3.place_id, str)
        self.assertIsInstance(my_review_3.text, str)
        self.assertIsInstance(my_review_3.user_id, str)


if __name__ == "__main__":
    unittest.main()
