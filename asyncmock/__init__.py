from mock import *
from .__version__ import __version__

__all__ = (
    "Mock",
    "MagicMock",
    "patch",
    "sentinel",
    "DEFAULT",
    "ANY",
    "call",
    "create_autospec",
    "FILTER_DIR",
    "CallableMixin",
    "NonCallableMock",
    "NonCallableMagicMock",
    "mock_open",
    "PropertyMock",
    "seal",
)

version_info = tuple(int(p) for p in __version__.split("."))


class AsyncCallableMixin(CallableMixin):
    def __init__(_mock_self, not_async=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _mock_self.not_async = not_async

    def __call__(_mock_self, *args, **kwargs):
        # can't use self in-case a function / method we are mocking uses self
        # in the signature
        if _mock_self.not_async:
            _mock_self._mock_check_sig(*args, **kwargs)
            return _mock_self._mock_call(*args, **kwargs)

        else:

            async def wrapper():
                _mock_self._mock_check_sig(*args, **kwargs)
                return _mock_self._mock_call(*args, **kwargs)

            return wrapper()


class AsyncMock(AsyncCallableMixin, NonCallableMock):
    """
    Create a new `AsyncMock` object. `AsyncMock` several options that extends
    the behaviour of the basic `Mock` object:

    * `is_async`: This is a boolean flag used to indicate when the mock is
      called if it should return a `asyncio.Future` instance to make the mock
      awaitable. If this flag is not set the mock reverts to the default
      behaviour of a `Mock` instance.

    All other arguments are passed directly through to the underlying `Mock`
    object.

    """
