##########
Async Mock
##########

Extension to the mock framework to provide an awaitable Mock.

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
      :alt: Once you go Black...


Installation
============

Install using *pip*::

    pip install asyncmock


Usage
=====

Async Mock is designed as a drop in replacement for a `Mock` object eg::

    my_mock = AsyncMock()

    await my_mock("foo", bar=123)

    my_mock.assert_called_with("foo", bar=123)


This also works with nested methods::

    my_mock = AsyncMock()

    await my_mock.my_method("foo", bar=123)

    my_mock.my_method.assert_called_with("foo", bar=123)


Side effects, return values can also be awaited.

Including a non-awaitable item::

    my_mock = AsyncMock()

    my_mock.my_method.not_async = True
    my_mock.my_method("foo", bar=123)


This can also be provided as an init argument, the `not_async` argument is not
inherited by sub-mocks.


PyTest Example
==============

These examples use `pytest <https://docs.pytest.org/en/latest/>`_ along with the
`pytest-asyncio <https://github.com/pytest-dev/pytest-asyncio>`_ plugin.

Generating an exception::

    @pytest.mark.asyncio
    async def test_raise_exception():
        my_mock = AsyncMock(side_effect=KeyError)

        with pytest.raises(KeyError):
            await my_mock()

        my_mock.assert_called()
