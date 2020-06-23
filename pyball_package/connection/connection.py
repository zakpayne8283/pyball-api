class Connection:

    host_url = None
    request_path = None
    request_data = None
    endpoint = None

    def __init__(self, parameters=None):
        # Sets up the connection w/ parameters
        if parameters is not None:

            # If a new endpoint was provided, set it. Else use default
            if 'endpoint' in parameters:
                # New endpoint
                self.endpoint = parameters['endpoint']
            else:
                # Default endpoint
                self.endpoint = 'search_player_all'
        else:
            # Set all defaults if no parameters are provided
            self.host_url = 'http://lookup-service-prod.mlb.com'
            self.request_path = '/json/named.{endpoint}.bam'
            self.endpoint = 'search_player_all'

    def make_request(self):
        pass
