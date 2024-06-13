import unittest
import sys
import os
from ..Persistence.repository import DataManager


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.data_manager = DataManager()

    def test_save(self):
        # Create a sample entity
        class User:
            def __init__(self, id, name):
                self.id = id
                self.name = name

        user1 = User(1, "Alice")

        self.data_manager.save(user1)

        self.assertEqual(self.data_manager._data["User"][1], user1)
