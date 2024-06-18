import unittest
from dataclasses import dataclass
from ..Model.user import User

class TestUser(unittest.TestCase):

    def test_valid_user_data(self):
        valid_data = {
            'username': 'Jacques Chirac',
            'email': 'president@elysee.com',
            'password': 'motdepasse75ù',  # Placeholder for hashed password
            'first_name': 'Jacques',
            'last_name': 'Chirac',
        }
        user = User(valid_data)
        self.assertEqual(user.username, 'johndoe')
        self.assertEqual(user.email, 'johndoe@example.com')
        # Assert other attributes as needed

    def test_invalid_username_type(self):
        invalid_data = {
            'username': 123,  # Not a string
            'email': 'jane@example.com',
            'password': 'secret',  # Placeholder
            'first_name': 'Jane',
            'last_name': 'Doe',
        }
        with self.assertRaises(ValueError) as cm:
            User(invalid_data)
        self.assertEqual(str(cm.exception), "Username must be a string. Received: <class 'int'>")

    def test_empty_username(self):
        invalid_data = {
            'username': '',
            'email': 'invalid@example.com',
            'password': 'weak_password',  # Placeholder
            'first_name': 'Invalid',
            'last_name': 'User',
        }
        with self.assertRaises(ValueError) as cm:
            User(invalid_data)
        self.assertEqual(str(cm.exception), "Username cannot be empty.")

# Run the tests
if __name__ == '__main__':
    unittest.main()
