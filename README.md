# DoubleStreamHandler

> A StreamHandler wrapper that outputs messages to different streams based on logLevel

[![See on PyPI](https://badgen.net/pypi/v/double-stream-handler)](https://pypi.org/project/double-stream-handler/)
[![Licenced under the BSD-3-Clause licence](https://badgen.net/pypi/license/double-stream-handler?label=licence)](LICENSE)
![for Python 3.6 and later](https://badgen.net/pypi/python/double-stream-handler)

Logging to the console is a nice feature to have, and Python's [`StreamHandler`](https://docs.python.org/3.9/library/logging.handlers.html#logging.StreamHandler) is of great help. However, it can only output to one stream at a time, and by default it's `stderr`.

This goes well with the default settings (`level=WARNING`), but it isn't good when you decide to output `INFO` messages as well.

This package prevents you from outputting non-error messages to `stderr` as well as from having to juggle with your output streams.

## Usage

```py
import logging
from double_stream_handler import DoubleStreamHandler

# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# create the handler
ch = DoubleStreamHandler()

# you can customize the logger by providing different streams and level, from which
# the stderr output will start
from io import StringIO
custom_out, custom_err = (StringIO(), StringIO())
ch = DoubleStreamHandler(err_level=25, streams=(custom_out, custom_err))

# set handler's level and add it to the logger
ch.setLevel(logging.INFO)
logger.addHandler(ch)

logger.debug("This is not printed")
logger.info("This is printed to stdout")
logger.error("This is printed to stderr")
```

## Install

**Requirements:** Python 3.6 or higher

This package is hosted on PyPI, so you can install it with your package manager of choice

```sh
# for Pip
pip install double-stream-handler
```

```sh
# for Pipenv
pipenv install double-stream-handler
```

```sh
# for Poetry
poetry add double-stream-handler
```

```sh
# for Poetry
conda install double-stream-handler
```

## Licence

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) © 2021, Nikita Karamov
