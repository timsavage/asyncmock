import pytest

import asyncmock


@pytest.mark.asyncio
async def test_async():
    mock = asyncmock.AsyncMock()

    await mock("foo", 123, bar="eek")

    mock.assert_called_with("foo", 123, bar="eek")


@pytest.mark.asyncio
async def test_async__with_side_effect():
    mock = asyncmock.AsyncMock(side_effect=KeyError)

    with pytest.raises(KeyError):
        await mock("foo", 123, bar="eek")

    mock.assert_called_with("foo", 123, bar="eek")


@pytest.mark.asyncio
async def test_async__return_value():
    mock = asyncmock.AsyncMock(return_value="hi")

    actual = await mock("foo", 123, bar="eek")

    assert actual == "hi"
    mock.assert_called_with("foo", 123, bar="eek")


@pytest.mark.asyncio
async def test_async__nested_call():
    mock = asyncmock.AsyncMock()

    await mock.my_method("foo", 123, bar="eek")

    mock.my_method.assert_called_with("foo", 123, bar="eek")


@pytest.mark.asyncio
async def test_async_context_manager():
    mock = asyncmock.AsyncMock()

    async with mock as x:
        assert x is mock


def test_not_async():
    mock = asyncmock.AsyncMock(not_async=True)

    mock("foo", 123, bar="eek")

    mock.assert_called_with("foo", 123, bar="eek")


def test_not_async__nested_call():
    mock = asyncmock.AsyncMock()

    mock.my_method.not_async = True
    mock.my_method("foo", 123, bar="eek")

    mock.my_method.assert_called_with("foo", 123, bar="eek")
