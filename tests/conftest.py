import asyncio
from unittest.mock import MagicMock

import pytest


def _call_coroutine(coroutine):
    return asyncio.get_event_loop().run_until_complete(coroutine)


@pytest.fixture()
def call_coroutine():
    return _call_coroutine


def async_func_mock(*args, **kwargs):
    m = MagicMock(*args, **kwargs)

    async def mock_coroutine(*args, **kwargs):
        return m(*args, **kwargs)

    mock_coroutine.mock = m
    return mock_coroutine


@pytest.fixture()
def async_f_mock():
    return async_func_mock
