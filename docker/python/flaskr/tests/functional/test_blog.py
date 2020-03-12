import unittest
import flaskr

from flask import current_app
from flaskr.tables import database_schema
from flaskr.tables.database_engine import DatabaseEngine


class TestBlog(unittest.TestCase):
    """
    Functional Test
    """

    def setUp(self):
        """
        Initialize new test client.
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

    def log_in(self, username, password):
        """
        Check user logs into an application.
        """
        return self.client.post('/log-in', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def log_out(self):
        """
        Check user logs out from an application.
        """
        return self.client.get('/log-out', follow_redirects=True)

    def test_post(self):
        """
        Check the post addition.
        """
        self.log_in('admin', 'admin')
        response = self.client.post('/add', data=dict(
            title='Lorem Ipsum',
            text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vitae velit sit amet purus efficitur viverra id at quam. Nam vitae dictum erat.'
        ), follow_redirects=True)
        self.assertNotIn(b'Unbelievable. No posts here so far.', response.data)
        self.assertIn(b'Lorem Ipsum', response.data)
        self.assertIn(b'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', response.data)

if __name__ == '__main__':
    unittest.main()
