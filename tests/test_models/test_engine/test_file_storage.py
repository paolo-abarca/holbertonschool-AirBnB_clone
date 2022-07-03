#!/usr/bin/python3
"""
Unittest for class File Storage
"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


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

    def test_filestorage_2(self):
        """
        method 2 that tests Filestorage
        """
        my_filestorage = BaseModel()
        my_filestorage.name = "Paolo"
        my_filestorage.save()
        storage.reload()
        storage.all()
        self.assertTrue(storage.all(), "Paolo")
        self.assertTrue(hasattr(my_filestorage, 'save'))
        self.assertNotEqual(my_filestorage.created_at,
                            my_filestorage.updated_at)

    def test_filestorage_3(self):
        """
        method 3 that tests FileStorage
        """
        my_filestorage_2 = FileStorage()
        self.assertTrue(hasattr(my_filestorage_2, "__init__"))
        self.assertTrue(hasattr(my_filestorage_2, "all"))
        self.assertTrue(hasattr(my_filestorage_2, "new"))
        self.assertTrue(hasattr(my_filestorage_2, "save"))
        self.assertTrue(hasattr(my_filestorage_2, "reload"))


if __name__ == "__main__":
    unittest.main()
