import sys

from greet import hello

print(hello(sys.argv[1] if len(sys.argv) > 1 else "world"))
