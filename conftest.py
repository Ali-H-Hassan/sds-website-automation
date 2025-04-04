import asyncio
import pytest

@pytest.fixture(autouse=True)
def reset_event_loop():
    try:
        loop = asyncio.get_running_loop()
        if loop.is_running():
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
    except RuntimeError:
        pass

def pytest_configure(config):
    config.option.asyncio_mode = None
    try:
        config.pluginmanager.set_blocked("pytest-asyncio")
        config.pluginmanager.set_blocked("pytest-anyio")
    except Exception:
        pass