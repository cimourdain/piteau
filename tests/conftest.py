import asyncio

import pytest


def _call_coroutine(coroutine):
    return asyncio.get_event_loop().run_until_complete(coroutine)


@pytest.fixture()
def call_coroutine():
    return _call_coroutine
