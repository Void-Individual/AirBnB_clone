import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(email="example@example.com", password="password123",
                         first_name="John", last_name="Doe")

    def tearDown(self):
        del self.user

    def test_user_inherits_from_base_model(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_string_representation(self):
        expected_str = "[User] ({}) {}".format(
            self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_user_to_dict(self):
        user_dict = self.user.to_dict()

        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertEqual(user_dict['first_name'], self.user.first_name)
        self.assertEqual(user_dict['last_name'], self.user.last_name)

    def test_user_instance_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_user_id_generation(self):
        user1 = User()
        user2 = User()

        self.assertNotEqual(user1.id, user2.id)


if __name__ == '__main__':
    unittest.main()
