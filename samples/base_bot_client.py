import logging
from datetime import datetime
from typing import Any, Dict

from piteau.base.client import BaseClient

logger = logging.getLogger(__name__)


class AskTimeBot(BaseClient):
    """
    Basic bot client that send a message with the current time
    when a client send a message stating with "/time"
    """

    async def on_new_message(self, data: Dict[str, Any]) -> None:
        if data["message"].startswith("/time"):
            self.send_message(f"{datetime.utcnow().isoformat()}")


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    bot = AskTimeBot(server_host="0.0.0.0", server_port=1234)
    bot.run()
