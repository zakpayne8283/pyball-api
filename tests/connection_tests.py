import unittest

from pyball_package.main import PyballAPI


class TestConnection(unittest.TestCase):

    def test_connection_is_not_none(self):
        # Create a new API instance
        api = PyballAPI()

        self.assertFalse(api.connection is not None)
