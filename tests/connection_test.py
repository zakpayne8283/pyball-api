import re
import unittest

from pyball_package.main import PyballAPI
from pyball_package.main import get_default_api_parameters


class TestConnection(unittest.TestCase):

    # Test if connection is not a null value
    def test_connection_is_not_none(self):
        # Create a new API instance
        api = PyballAPI()

        # Test Assert
        self.assertTrue(api.connection is not None)

    # Test if connection url is a valid URL
    def test_connection_url_is_valid(self):
        # Create a new API instance
        api = PyballAPI()

        # Create the valid regex
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        # Test Assert
        self.assertTrue(re.match(regex, api.connection.host_url) is not None)

    # Test if request data is received
    def test_connection_request_data_received(self):
        # Create a new API instance
        api = PyballAPI(parameters=get_default_api_parameters())

        # Test Assert
        self.assertTrue(api.connection.make_request() is not None)
