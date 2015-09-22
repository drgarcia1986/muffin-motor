import asyncio

import muffin
import pytest


@pytest.fixture(scope='session')
def app(loop):
    app = muffin.Application(
        'motor', loop=loop,

        PLUGINS=['muffin_motor'],
        MOTOR_MAX_POOL_SIZE=2
    )

    return app


@pytest.mark.async
@asyncio.coroutine
def test_muffin_mongo(app):
    yield from app.ps.motor.test.insert({'test': 'foo'})
    doc = yield from app.ps.motor.test.find_one({'test': 'foo'})
    assert doc['test'] == 'foo'
    yield from app.ps.motor.test.remove({})


@pytest.mark.async
@asyncio.coroutine
def test_pool(app):
    # Lazy connection
    yield from app.ps.motor.test.remove()
    pool = app.ps.motor.conn._get_primary_pool()
    assert pool.max_size == 2
