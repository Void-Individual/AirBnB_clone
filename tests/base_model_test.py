#!/usr/bin/python3
import unittest
import datetime
import os
import sys
from models.base_model import BaseModel


"""Unittest module for the BaseModel module"""

# Add the parent directory of your project to the system path
project_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(project_dir)
sys.path.append(parent_dir)

class TestBaseModel(unittest.TestCase):
    """Class to run different tests for the Basemodel
    """

    def TestBaseModelCreation(self):
        """Init the basemodel class"""

        BM = BaseModel()
        self.assertEqual(BM.created_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
