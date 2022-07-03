#!/usr/bin/python3
"""
Unittest for class File Storage
"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class TestFileStorage(unittest.TestCase):
    """
    basic tests for FileStorage
    """
    def test_filestorage(self):
        """
        method that tests FileStorage
        """
        filestorage = FileStorage()
        all_objs = filestorage.all()

        self.assertEqual(type(all_objs), dict)

    def test_filestorage_2(self):
        """
        method 2 that tests Filestorage
        """
        for all_objs in storage.all().values():
            string = all_objs

        self.assertTrue(string is all_objs)

    def test_filestorage_3(self):
        """
        method 3 that tests FileStorage
        """
        os.remove("file.json")
        self.assertFalse(os.path.exists("file.json"))
        user = User()
        user.save()

        self.assertTrue(os.path.exists("file.json"))

    def test_filestorage_4(self):
        """
        method 4 that tests FileStorage
        """
        os.remove("file.json")
        basemodel_2 = BaseModel()
        basemodel_2.save()
        with open("file.json", "r") as f:
            string_2 = f.read()

            self.assertIn(type(basemodel_2).__name__ +
                          "." + basemodel_2.id, string_2)

    def test_filestorage_5(self):
        """
        method 5 that tests FileStorage
        """
        self.assertEqual(storage.reload(), None)
        storage.save()
        storage.reload()
        self.new = BaseModel()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]

        self.assertEqual(self.new.to_dict()['id'], obj.to_dict()['id'])
        self.assertTrue(os.path.exists('file.json'))


if __name__ == "__main__":
    unittest.main()
