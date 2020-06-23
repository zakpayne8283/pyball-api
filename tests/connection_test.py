import unittest

from pyball_package.main import PyballAPI


class TestConnection(unittest.TestCase):

    def runTest(self):
        self.test_connection_is_not_none()

    def test_connection_is_not_none(self):
        # Create a new API instance
        api = PyballAPI()

        self.assertTrue(api.connection is not None)
