import asyncio

import muffin
import pytest


@pytest.fixture(scope='session')
def app(loop):
    app = muffin.Application(
        'motor', loop=loop,

        PLUGINS=['muffin_motor']
    )

    return app


@pytest.mark.async
@asyncio.coroutine
def test_muffin_mongo(app):
    yield from app.ps.motor.test.insert({'test': 'foo'})
    doc = yield from app.ps.motor.test.find_one({'test': 'foo'})
    assert doc['test'] == 'foo'
