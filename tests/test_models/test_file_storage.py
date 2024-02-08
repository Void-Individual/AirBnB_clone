import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()
        self.storage = FileStorage()
        self.storage.new(self.base_model)
        self.storage.save()

    def tearDown(self):
        del self.base_model
        del self.storage

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIn("BaseModel." + self.base_model.id, all_objects)

    # Add other test methods here

if __name__ == '__main__':
    unittest.main()
