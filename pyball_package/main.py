from . connection import Connection


class PyballAPI:

    connection = None

    def __init__(self):
        self.connection = Connection()
        pass


def get_default_api_parameters():
    return {
        'endpoint': 'search_player_all'
    }
