import sys

from itertools import count, islice
from math import ceil


def main(argv):
    try:
        n = int(argv[0])

    except IndexError:
        print("Error: no argument given")
        sys.exit(1)

    except ValueError:
        print("Error: argument must be an integer")
        sys.exit(1)

    f = configurable({"fizz": 3, "buzz": 5, "jazz": 7})

    for _ in range(n):
        print(next(f))


def configurable(config):
    return (
        "".join(msg for msg,freq in config.items() if i%freq == 0) or i
        for i in count(1))


if __name__ == "__main__":
    main(sys.argv[1:])
