#!/usr/bin/python3
"""
Unittest for class File Storage
"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import os


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
        self.assertEqual(type(storage).__name__, "FileStorage")
        self.assertEqual(type(FileStorage()), FileStorage)
        with self.assertRaises(TypeError):
            FileStorage(None)
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        self.assertEqual(type(storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
