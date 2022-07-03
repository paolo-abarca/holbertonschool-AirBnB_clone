#!/usr/bin/python3
"""
Unittest for class Base Model
"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBase_model(unittest.TestCase):
    """
    basic tests for BaseModel
    """
    def test_base_model(self):
        """
        method that tests BaseModel
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        my_model_json = my_model.to_dict()

        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(type(my_model.__dict__), dict)

    def test_update_base_model(self):
        """
        method 2 that tests BaseModel update
        """
        my_model_2 = BaseModel()
        my_model_2.name = "My Second Model"
        my_model_2.my_number = 90
        hour_1 = my_model_2.updated_at
        my_model_2.save()
        my_model_2_json = my_model_2.to_dict()

        my_model_2.name = "My Second Model 2.0"
        my_model_2.my_number = 95
        hour_2 = my_model_2.updated_at
        my_model_2.save()
        my_model_2_json_2 = my_model_2.to_dict()

        self.assertNotEqual(hour_1, hour_2)
        self.assertNotEqual(my_model_2_json, my_model_2_json_2)

    def test_base_model_2(self):
        """
        method 2 that tests BaseModel
        """
        dict_1 = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                  'created_at': '2017-09-28T21:03:54.052298',
                  '__class__': 'BaseModel',
                  'my_number': 89,
                  'updated_at': '2017-09-28T21:03:54.052302',
                  'name': 'My_First_Model'}

        my_model_3 = BaseModel(**dict_1)
        name = type(my_model_3).__name__
        format_date = '\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}'
        self.assertEqual(name, "BaseModel")
        self.assertEqual(len(my_model_3.id), 36)
        self.assertNotEqual(my_model_3.id, None)
        self.assertIsInstance(my_model_3.id, str)
        self.assertIsInstance(my_model_3.created_at, datetime)
        self.assertIsInstance(my_model_3.updated_at, datetime)
        self.assertRegex(str(my_model_3.created_at), format_date)
        self.assertRegex(str(my_model_3.updated_at), format_date)
        self.assertEqual(my_model_3.name, 'My_First_Model')
        self.assertEqual(my_model_3.my_number, 89)

    def test_base_model_3(self):
        """
        method 3 that tests BaseModel
        """
        basemodel_1 = BaseModel()
        basemodel_2 = BaseModel()
        self.assertNotEqual(basemodel_1.id, basemodel_2.id)

    def test_base_model_4(self):
        """
        method 4 that tests BaseModel
        """
        basemodel_3 = BaseModel()
        self.assertEqual(type(basemodel_3).__name__, "BaseModel")

    def test_base_model_5(self):
        """
        method 5 that tests BaseModel
        """
        basemodel_4 = BaseModel()
        formatD = '\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}'
        self.assertRegex(str(basemodel_4.created_at), formatD)
        self.assertRegex(str(basemodel_4.updated_at), formatD)

    def test_base_model_6(self):
        """
        method 6 that tests BaseModel
        """
        basemodel_5 = BaseModel()
        self.assertNotEqual(self.id, None)

    def test_base_model_7(self):
        """
        method 7 that tests BaseModel
        """
        basemodel_6 = BaseModel()
        self.assertEqual(len(basemodel_6.id), 36)

    def test_base_model_8(self):
        """
        method 8 that tests BaseModel
        """
        basemodel_7 = BaseModel()
        self.assertIsInstance(basemodel_7.id, str)
        self.assertIsInstance(basemodel_7.created_at, datetime)
        self.assertIsInstance(basemodel_7.updated_at, datetime)

    def test_base_model_9(self):
        """
        method 9 that tests BaseModel
        """
        bm_8 = BaseModel()
        dictionary = bm_8.__dict__
        format_representation = "[{}] ({}) {}".format(type(bm_8).__name__,
                                                      bm_8.id, dictionary)
        self.assertEqual(format_representation, str(bm_8))

    def test_base_model_10(self):
        """
        method 10 that tests BaseModel
        """
        basemodel_9 = BaseModel()
        basemodel_9.id = "2d09fbee-82be-4531-852f-2add6d6e4f23"
        result = "[BaseModel] (2d09fbee-82be-4531-852f-2add6d6e4f23)"
        self.assertTrue(result, basemodel_9.__str__)

    def test_base_model_11(self):
        """
        method 11 that tests BaseModel
        """
        basemodel_10 = BaseModel()
        basemodel_10.name = "paolo"
        basemodel_10.my_number = 89
        basemodel_10.save()
        self.assertEqual(basemodel_10.name, "paolo")
        self.assertEqual(basemodel_10.my_number, 89)

    def test_base_model_12(self):
        """
        method 12 that tests BaseModel
        """
        basemodel_10 = BaseModel()
        basemodel_10.name = "Fernando"
        basemodel_10.my_number = 20
        basemodel_10.save()
        basemodel_11 = BaseModel()
        basemodel_11.name = "Sanei"
        basemodel_11.my_number = 14
        basemodel_11.save()
        self.assertNotEqual(basemodel_10.created_at, basemodel_11.created_at)
        self.assertNotEqual(basemodel_10.updated_at, basemodel_11.updated_at)

    def test_base_model_13(self):
        """
        method 13 that tests BaseModel
        """
        basemodel_12 = BaseModel()
        dictionary_value = basemodel_12.to_dict()
        self.assertIn('__class__', dictionary_value)
        self.assertIn('created_at', dictionary_value)
        self.assertIn('updated_at', dictionary_value)
        self.assertIn('id', dictionary_value)

    def test_base_model_14(self):
        """
        method 14 that tests BaseModel
        """
        basemodel_14 = BaseModel()
        basemodel_14.name = "sanei"
        first = basemodel_14.my_number = 974133101
        first_date = basemodel_14.updated_at
        basemodel_14.save()
        second = basemodel_14.my_number = 943136201
        second_date = basemodel_14.updated_at
        basemodel_14.save()
        self.assertNotEqual(first, second)
        self.assertNotEqual(first_date, second_date)


if __name__ == "__main__":
    unittest.main()
