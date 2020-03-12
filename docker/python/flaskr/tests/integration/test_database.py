import unittest
import flaskr

from flask import current_app
from flaskr.tables import database_schema
from flaskr.tables.database_engine import DatabaseEngine


class TestDatabase(unittest.TestCase):
    """
    Integration Test
    """

    def setUp(self):
        """
        Initialize a new test client.
        """
        self.app = flaskr.app
        self.client = flaskr.app.test_client()

    def tearDown(self):
        """
        Finish the test client.
        """
        with self.app.app_context():
            db_session = DatabaseEngine(current_app).create_session()
            db_session.query(database_schema.Post).delete()
            db_session.commit()

    def test_empty_db(self):
        """
        Check the database is empty.
        """
        response = self.client.get('/')
        self.assertIn(b'Unbelievable. No posts here so far.', response.data)

if __name__ == '__main__':
    unittest.main()
