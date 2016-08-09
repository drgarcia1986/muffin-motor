Muffin-Motor
############

.. _description:

Muffin-Motor -- A simple motor_ plugin for muffin_ framework.

.. _badges:

.. image:: http://img.shields.io/travis/drgarcia1986/muffin-motor.svg?style=flat-square
    :target: http://travis-ci.org/drgarcia1986/muffin-motor
    :alt: Build Status

.. _requirements:

Requirements
=============

- python >= 3.4.1
- muffin >= 0.5.5
- motor >= 0.5

.. _installation:

Installation
=============

**Muffin-Motor** should be installed using pip: ::

    pip install muffin-motor

.. _usage:

Usage
=====

Add *muffin-motor* to muffin plugin list:

.. code-block:: python

    import muffin


    app = muffin.Application(
        'example',

        PLUGINS=(
            'muffin_motor',
        )
    )

And use *motor* plugin:

.. code-block:: python

    @app.register('/example')
    class Example(muffin.Handler):

        @asyncio.coroutine
        def get(self, request):
            collection = app.ps.motor.test
            doc = yield from collection.find_one({'test': 'foo'})
            return doc

.. _options:

Options
-------

========================== ==============================================================
 *MOTOR_HOST*              Host of mongodb server (``127.0.0.1``)
 *MOTOR_PORT*              Port of mongodb server (``27017``)
 *MOTOR_MAX_POOL_SIZE*     Max connection pool size (``1``)
 *MOTOR_DB*                Database (``default``)
 *MOTOR_KWARGS*            Others args of client create(``{}``)
========================== ==============================================================

.. _bugtracker:

Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/drgarcia1986/muffin-motor/issues

.. _contributing:

Contributing
============

Development of Muffin-Motor happens at: https://github.com/drgarcia1986/muffin-motor


Contributors
=============

* drgarcia1986_ (Diego Garcia)

.. _license:

License
=======

Licensed under a `MIT license`_.

.. _links:


.. _muffin: https://github.com/klen/muffin
.. _motor: https://github.com/mongodb/motor
.. _drgarcia1986: https://github.com/drgarcia1986
.. _MIT license: http://opensource.org/licenses/MIT
