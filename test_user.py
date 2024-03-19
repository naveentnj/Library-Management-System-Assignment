import unittest
from user import add_user, list_users, update_user, delete_user, search_users
from models import User
from storage import Storage

class MockStorage:
    """Mock storage class for testing purposes."""
    def __init__(self):
        self.users = []

    def load_users(self):
        """Mock load_users method."""
        return self.users

    def save_users(self, users):
        """Mock save_users method."""
        self.users = users

class TestUser(unittest.TestCase):
    def setUp(self):
        """Create a mock storage instance before each test."""
        self.storage = MockStorage()

    def test_add_user(self):
        """Test adding a new user."""
        add_user("Test User", 1, self.storage)
        self.assertEqual(len(self.storage.users), 1)
        self.assertEqual(self.storage.users[0].name, "Test User")

    def test_add_existing_user(self):
        """Test adding a user that already exists."""
        add_user("Test User", 1, self.storage)
        add_user("Test User", 1, self.storage)
        self.assertEqual(len(self.storage.users), 1)  
        
    def test_update_user(self):
        """Test updating a user's name."""
        add_user("Old Name", 1, self.storage)
        update_user(1, "New Name", self.storage)
        self.assertEqual(self.storage.users[0].name, "New Name")

    def test_delete_user(self):
        """Test deleting a user."""
        add_user("Test User", 1, self.storage)
        delete_user(1, self.storage)
        self.assertEqual(len(self.storage.users), 0)

    def test_search_users(self):
        """Test searching for users by name or ID."""
        add_user("Test User", 1, self.storage)
        self.assertIsNotNone(search_users("Test User", self.storage))
        self.assertIsNotNone(search_users("1", self.storage))

    def test_search_users_no_results(self):
        """Test searching for users that do not exist."""
        self.assertIsNone(search_users("Nonexistent User", self.storage))

if __name__ == '__main__':
    unittest.main()