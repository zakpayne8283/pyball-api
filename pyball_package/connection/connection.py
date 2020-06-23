class Connection:

    host_url = None
    request_path = None
    request_data = None

    def __init__(self):
        # Sets up the connection w/ parameters

        self.host_url = 'http://lookup-service-prod.mlb.com'
        self.request_path = '/json/named.{endpoint}.bam'
        # TODO: determine parameters

    def make_request(self):
        pass
