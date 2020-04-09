import logging
from piteau import BaseClient


logging.basicConfig(level=logging.DEBUG)
client = BaseClient(server_host='localhost', server_port=1234)
client.run()
