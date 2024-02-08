#!/usr/bin/python3
"""Unit tests for BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_init(self):
        """Test initialization of BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """Test __str__ method of BaseModel."""
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save(self):
        """Test save method of BaseModel."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method of BaseModel."""
        my_model = BaseModel()
        my_model.name = "TestModel"
        my_model.my_number = 42
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['name'], 'TestModel')
        self.assertEqual(my_model_dict['my_number'], 42)
        self.assertTrue('created_at' in my_model_dict)
        self.assertTrue('updated_at' in my_model_dict)


if __name__ == "__main__":
    unittest.main()
