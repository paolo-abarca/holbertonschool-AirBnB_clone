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
        self.assertEqual(storage.reload(), None)
        storage.save()
        storage.reload()
        self.new = BaseModel()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        self.assertEqual(self.new.to_dict()["id"], obj.to_dict()["id"])
        self.assertEqual(type(all_objs), dict)
        self.assertTrue(os.path.exists("file.json"))

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
        basemodel = BaseModel()
        storage.new(basemodel)
        user = User()
        storage.new(user)
        state = State()
        storage.new(state)
        place = Place()
        storage.new(place)
        city = City()
        storage.new(city)
        amenity = Amenity()
        storage.new(amenity)
        review = Review()
        storage.new(review)
        storage.save()
        text_save = ""
        with open("file.json", "r") as f:
            text_save = f.read()
            self.assertIn("BaseModel" + "." + basemodel.id, text_save)
            self.assertIn("User" + "." + user.id, text_save)
            self.assertIn("State" + "." + state.id, text_save)
            self.assertIn("Place" + "." + place.id, text_save)
            self.assertIn("City" + "." + city.id, text_save)
            self.assertIn("Amenity" + "." + amenity.id, text_save)
            self.assertIn("Review" + "." + review.id, text_save)

    def test_filestorage_5(self):
        """
        method 5 that tests FileStorage
        """
        filestorage = FileStorage()
        all_objs = filestorage.all()

        self.assertEqual(type(all_objs), dict)

    def test_filestorage_6(self):
        """
        method 6 that tests FileStorage
        """
        for all_objs in storage.all().values():
            string = all_objs

        self.assertTrue(string is all_objs)

    def test_filestorage_7(self):
        """
        method 7 that tests FileStorage
        """
        os.remove("file.json")
        self.assertFalse(os.path.exists("file.json"))
        user = User()
        user.save()

        self.assertTrue(os.path.exists("file.json"))

    def test_filestorage_8(self):
        """
        method 8 that tests FileStorage
        """
        os.remove("file.json")
        user_2 = User()
        user_2.save()
        with open("file.json", "r") as f:
            string_2 = f.read()

            self.assertIn(type(user_2).__name__ + "." + user_2.id, string_2)


if __name__ == "__main__":
    unittest.main()
