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


def setUpModule():
    """setup module """
    pass


def tearDownModule():
    """teardown module """
    pass


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


class TestModels(unittest.TestCase):

    def setUp(self):
        """ Set a variable """
        self.my_model = BaseModel()
        self.fisto = FileStorage()
        print("setUp")

    def tearDown(self):
        """ End variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set a Class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Del a Class"""
        print("tearDownClass")

    def test_file_storage_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_fiel_storage_exist(self):
        """ Check if methods exists """
        self.assertTrue(hasattr(self.fisto, "__init__"))
        self.assertTrue(hasattr(self.fisto, "all"))
        self.assertTrue(hasattr(self.fisto, "new"))
        self.assertTrue(hasattr(self.fisto, "save"))
        self.assertTrue(hasattr(self.fisto, "reload"))

    def test_models_save(self):
        """ Check if the save function works """
        self.my_model.name = "Halo"
        self.my_model.save()
        storage.reload()
        storage.all()
        self.assertTrue(storage.all(), "Halo")
        self.assertTrue(hasattr(self.my_model, 'save'))
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model.updated_at)


if __name__ == "__main__":
    unittest.main()
