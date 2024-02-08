#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


"""Unittest module for the BaseModel module"""

class TestBaseModel(unittest.TestCase):
    """Class to run different tests for the Basemodel
    """

    def test_BaseModelCreation(self):
        """Testing init of the basemodel class"""

        BM = BaseModel()
        self.assertIsInstance(BM.created_at, datetime)
        self.assertIsInstance(BM.updated_at, datetime)
        self.assertEqual(BM.created_at, BM.updated_at)
        self.assertIsInstance(BM.id, str)

    def test_save(self):
        """Method to test the base save method"""

        BM = BaseModel()
        BM.save()
        self.assertIsInstance(BM.updated_at, datetime)
        self.assertNotEqual(BM.created_at, BM.updated_at)

    def test_str_representation(self):
        """method to test the basemodel str method"""

        BM = BaseModel()
        expected = f"[BaseModel] ({BM.id}) {BM.__dict__}"
        self.assertEqual(str(BM), expected)

    def test_dict_representation(self):
        """Method to test the created dictionary"""

        BM = BaseModel()
        expected = {
            'id': BM.id,
            '__class__': 'BaseModel',
            'created_at': BM.created_at.isoformat(),
            'updated_at': BM.updated_at.isoformat()
        }
        self.assertEqual(BM.to_dict(), expected)
        self.assertNotIsInstance(BM.created_at, datetime)
        self.assertNotIsInstance(BM.updated_at, datetime)

    def test_basemodel_from_dict(self):
        """Method to test a fixed instance creation from a dict"""

        BM = BaseModel()
        BM.name = "My_first_model"
        BM.my_number = 89
        created_at_str = BM.created_at.isoformat()
        updated_at_str = BM.updated_at.isoformat()
        expected = {
            'id': BM.id,
            '__class__': 'BaseModel',
            'created_at': created_at_str,
            'updated_at': updated_at_str,
            'name': 'My_first_model',
            'my_number': 89
        }
        new = BM.to_dict()
        self.assertEqual(new, expected)
        self.assertIsInstance(BM, BaseModel)
        new_BM = BaseModel(**new)
        self.assertIsInstance(new_BM, BaseModel)
        self.assertIsInstance(new_BM.created_at, datetime)
        self.assertIsInstance(new_BM.updated_at, datetime)
        self.assertIsInstance(new_BM.id, str)


if __name__ == '__main__':
    unittest.main()
