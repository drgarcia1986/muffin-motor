# Muffin-Motor

Muffin-Motor -- A simple [MOTOR](https://github.com/mongodb/motor) plugin for [muffin framework](https://github.com/klen/muffin).


## Requirements

- python >= 3.4
- muffin >= 0.1.6

## Installation

**Muffin-Motor** should be installed using pip:
```
pip install git+https://github.com/drgarcia1986/muffin-motor.git
```

## Usage

Add Muffin-Motor to muffin plugin list:

```python
import muffin


app = muffin.Application(
	'example',

	PLUGINS=(
		'muffin_motor',
	)
)
```

And use *motor* plugin:

```python
    @app.register('/example')
    class Example(muffin.Handler):

        @asyncio.coroutine
        def get(self, request):
            collection = app.ps.motor.test
            doc = yield from collection.find_one({'test': 'foo'})
            return doc

```
## Bug tracker

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/drgarcia1986/muffin-motor/issues

## Contributing

Development of Muffin-Motor happens at: https://github.com/drgarcia1986/muffin-motor


## Contributors
* Diego Garcia [github](https://github.com/drgarcia1986)
