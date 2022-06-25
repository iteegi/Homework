import pytest

from ..logger import Logger, StreamHandlerConfig


@pytest.fixture(scope="class",
                params=[StreamHandlerConfig,
                        NullHandlerConfig])
def logger_obj(request):
    yield Logger('test_name', request.param())
