"""
This file contains the unit tests for the main application.
"""

import unittest

from app import app


class TestMain(unittest.TestCase):
    """
    This class contains the unit tests for the main application.
    """

    def test_hello(self):
        """
        This method tests the home page of the application.
        """
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Hello World!', response.data)

    def test_basic_logic(self):
        assert 2 == len('ad')


# if __name__ == '__main__':
#     unittest.main()
