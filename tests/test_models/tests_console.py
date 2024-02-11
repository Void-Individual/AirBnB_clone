import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.assertIsNotNone(storage.all().get("BaseModel." + obj_id))

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertIn(f"BaseModel.{obj_id}", f.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            self.assertNotIn(f"BaseModel.{obj_id}", storage.all())

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            self.assertIn("BaseModel", f.getvalue())

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"update BaseModel {obj_id} name 'test'")
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertIn("'name': 'test'", f.getvalue())

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("count BaseModel")
            self.assertIn("2", f.getvalue())


if __name__ == '__main__':
    unittest.main()
