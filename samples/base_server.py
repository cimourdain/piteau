import logging

from piteau import BaseServer


logging.basicConfig(level=logging.INFO)
server = BaseServer(host="0.0.0.0", port=1234)
server.run()
