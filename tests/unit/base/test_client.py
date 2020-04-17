import asyncio

import pytest

from piteau.base.client import BaseClient


class TestInit:
    def test_base(self):
        client = BaseClient(server_host="test_host", server_port=1)
        assert client.server_host == "test_host"
        assert client.server_port == 1

    def test_defaults(self):
        client = BaseClient()
        assert client.server_host == "localhost"
        assert client.server_port == 1234

    def test_loop(self):
        client = BaseClient()
        assert isinstance(client.loop, asyncio.BaseEventLoop)

    def test_writer(self):
        client = BaseClient()
        assert client.writer is None

    def test_reader(self):
        client = BaseClient()
        assert client.reader is None


class TestStart:
    def test_base(self, mocker, async_f_mock, call_coroutine):
        open_connection_mock = mocker.patch(
            "asyncio.open_connection",
            new=async_f_mock(return_value=("test_reader", "test_writer")),
        )
        client = BaseClient(server_host="test_host", server_port=9876)
        call_coroutine(client.start())

        open_connection_mock.mock.assert_called_once_with(host="test_host", port=9876)

        assert client.reader == "test_reader"
        assert client.writer == "test_writer"


class TestOnNewMessage:
    def test_valid_message(self, mocker, call_coroutine):
        print_mock = mocker.patch("builtins.print")
        client = BaseClient()
        valid_message = {
            "from": "test_from",
            "message": "test_message",
        }
        call_coroutine(client.on_new_message(valid_message))
        print_mock.assert_called_once_with(f"<<< test_from > test_message")

    @pytest.mark.parametrize(
        ["invalid_message"],
        [
            pytest.param("test", id="str message"),
            pytest.param(None, id="None message"),
            pytest.param(34, id="Int message"),
        ],
    )
    def test_on_new_message_invalid_type(self, call_coroutine, invalid_message):
        client = BaseClient()
        with pytest.raises(TypeError):
            call_coroutine(client.on_new_message(invalid_message))

    @pytest.mark.parametrize(
        ["invalid_message"],
        [
            pytest.param({}, id="empty dict message"),
            pytest.param({"message": "test"}, id="missing from dict message"),
            pytest.param({"from": "test"}, id="missing message in dict"),
        ],
    )
    def test_on_new_message_invalid_content(self, call_coroutine, invalid_message):
        client = BaseClient()
        with pytest.raises(KeyError):
            call_coroutine(client.on_new_message(invalid_message))
