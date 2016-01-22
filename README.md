# Muffin-Motor
[![Build Status](https://travis-ci.org/drgarcia1986/muffin-motor.svg)](https://travis-ci.org/drgarcia1986/muffin-motor)

Muffin-Motor -- A simple [MOTOR](https://github.com/mongodb/motor) plugin for [muffin framework](https://github.com/klen/muffin).


## Requirements

- python >= 3.4.1
- muffin >= 0.5.5
- motor >= 0.5

## Installation

**Muffin-Motor** should be installed using pip:
```
pip install muffin-motor
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
## Options
| | |
|------------|----------------|
| MOTOR_HOST | Host of mongodb server (`'127.0.0.1'`) |
| MOTOR_PORT | Port of mongodb server (`27017`) |
| MOTOR_MAX_POOL_SIZE | Max connection pool size (`1`) |
| MOTOR_DB | Database (`default`) |

## Bug tracker

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/drgarcia1986/muffin-motor/issues

## Contributing

Development of Muffin-Motor happens at: https://github.com/drgarcia1986/muffin-motor


## Contributors
* [Diego Garcia](https://github.com/drgarcia1986)
