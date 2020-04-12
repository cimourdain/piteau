import pytest

from piteau.base.client import BaseClient


class TestReceive:
    def test_on_new_message(self, call_coroutine):
        client = BaseClient()
        with pytest.raises(TypeError):
            call_coroutine(client.on_new_message('toto'))
