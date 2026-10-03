import argparse

from greet import hello


def main(argv=None) -> str:
    parser = argparse.ArgumentParser(prog="python3 -m greet")
    parser.add_argument("name", nargs="?", default="world")
    parser.add_argument("--shout", action="store_true", help="upper-case the greeting")
    args = parser.parse_args(argv)
    greeting = hello(args.name)
    return greeting.upper() if args.shout else greeting


if __name__ == "__main__":
    print(main())
