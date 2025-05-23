import unittest
from unittest.mock import MagicMock, patch
from app.database_manager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    @patch('app.database_manager.MongoClient')
    def setUp(self, mock_client):
        self.mock_client = mock_client.return_value
        self.mock_db = self.mock_client.__getitem__.return_value
        self.mock_users = self.mock_db.users

        self.db_manager = DatabaseManager()

    def test_add_user(self):
        self.db_manager.add_user("testuser", "testpass")
        self.mock_users.insert_one.assert_called_with({"login": "testuser", "password": "testpass"})

    def test_user_exists_true(self):
        self.mock_users.find_one.return_value = {"login": "testuser", "password": "testpass"}
        result = self.db_manager.user_exists("testuser", "testpass")
        self.assertTrue(result)

    def test_user_exists_false(self):
        self.mock_users.find_one.return_value = None
        result = self.db_manager.user_exists("testuser", "wrongpass")
        self.assertFalse(result)

    def test_close(self):
        self.db_manager.close()
        self.mock_client.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
