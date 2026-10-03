# greet

A tiny Python package that says hello.

## Usage

### As a library

```python
from greet import hello

hello("Ada")  # "Hello, Ada!"
```

`hello(name: str) -> str` returns the greeting `Hello, <name>!`.

### From the command line

```sh
$ python3 -m greet
Hello, world!

$ python3 -m greet Ada
Hello, Ada!

$ python3 -m greet Bob --shout
HELLO, BOB!
```

With no argument it greets `world`; otherwise it greets the first argument.
Pass `--shout` to upper-case the greeting.

## Tests

```sh
python3 -m unittest
```
