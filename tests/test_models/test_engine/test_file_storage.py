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
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        storage.new(bm)
        storage.new(us)
        storage.new(st)
        storage.new(pl)
        storage.new(cy)
        storage.new(am)
        storage.new(rv)
        self.assertIn("BaseModel." + bm.id, storage.all().keys())
        self.assertIn(bm, storage.all().values())
        self.assertIn("User." + us.id, storage.all().keys())
        self.assertIn(us, storage.all().values())
        self.assertIn("State." + st.id, storage.all().keys())
        self.assertIn(st, storage.all().values())
        self.assertIn("Place." + pl.id, storage.all().keys())
        self.assertIn(pl, storage.all().values())
        self.assertIn("City." + cy.id, storage.all().keys())
        self.assertIn(cy, storage.all().values())
        self.assertIn("Amenity." + am.id, storage.all().keys())
        self.assertIn(am, storage.all().values())
        self.assertIn("Review." + rv.id, storage.all().keys())
        self.assertIn(rv, storage.all().values())


if __name__ == "__main__":
    unittest.main()
