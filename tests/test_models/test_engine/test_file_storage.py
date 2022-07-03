#!/usr/bin/python3
"""
Unittest for class File Storage
"""
import unittest
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    basic tests for FileStorage
    """
    def test_filestorage(self):
        """
        method that tests FileStorage
        """
        all_objs = storage.all()

        self.assertEqual(type(all_objs), dict)


if __name__ == "__main__":
    unittest.main()
