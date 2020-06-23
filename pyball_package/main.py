from . connection import Connection


class PyballAPI:

    connection = None

    def __init__(self, parameters=None):
        # Setup the new parameters if they exist
        if parameters is not None:
            # New connection parameters
            connection_params = {}

            # If an endpoint was provided
            if 'endpoint' in parameters:
                connection_params['endpoint'] = parameters['endpoint']

            # Make the connection with the new parameters
            self.connection = Connection(parameters=connection_params)
        else:
            # Make the connection with default parameters
            self.connection = Connection()


def get_default_api_parameters():
    return {
        'endpoint': 'search_player_all'
    }
