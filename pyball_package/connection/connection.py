import requests

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

        # Set all defaults if no parameters are provided
        if self.host_url is None:
            self.host_url = 'http://lookup-service-prod.mlb.com'

        if self.endpoint is None:
            self.endpoint = 'search_player_all'

        if self.request_path is None:
            self.request_path = f'/json/named.{self.endpoint}.bam'

    def make_request(self):
        # Build the full URL Path
        full_request_url = self.host_url + self.request_path

        # Make the request and set the data
        self.request_data = requests.get(full_request_url)
