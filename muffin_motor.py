""" Mongo DB support for Muffin Framework with Motor. """

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from muffin.plugins import BasePlugin

__version__ = "0.0.1"
__project__ = "muffin-motor"
__author__ = "Diego Garcia <drgarcia1986@gmail.com>"
__license__ = "MIT"


class Plugin(BasePlugin):

    """ Connect to Motor. """

    name = 'motor'
    defaults = {
        'host': '127.0.0.1',
        'port': 27017,
    }

    def __init__(self, *args, **kwargs):
        """ Initialize the plugin. """
        super().__init__(*args, **kwargs)
        self.conn = None

    def setup(self, app):
        """ Setup options. """
        super().setup(app)
        self.cfg.port = int(self.cfg.port)

    @asyncio.coroutine
    def start(self, app):
        """ Make a connection to mongo. """
        self.conn = yield from AsyncIOMotorClient(
            host=self.cfg.host,
            port=self.cfg.port,
            io_loop=app._loop
        ).open()
        self.conn = self.conn.client

        return self

    @asyncio.coroutine
    def finish(self, app):
        """ Close self connections. """
        yield from self.conn.disconnect()

    def __getattr__(self, name):
        """ Proxy attributes to self connection. """
        if not self.conn:
            raise AttributeError('Not connected')

        return getattr(self.conn, name)
