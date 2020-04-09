import logging
from piteau import BaseServer


logging.basicConfig(level=logging.DEBUG)
server = BaseServer(host='localhost', port=1234)
server.run()
