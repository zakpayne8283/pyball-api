from . connection import Connection


class PyballAPI:

    connection = None

    def __init__(self):
        self.connection = Connection()
        pass
