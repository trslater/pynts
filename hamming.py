"""Hamming code error finder
"""


import functools


def main():
    msg = 0b1001010010101111
    n = 16
    print(find_err(msg, n))


def find_err(msg, n):
    return functools.reduce(lambda a,b: a^b, (i for i in range(n) if 2**i & msg))


if __name__ == "__main__":
    main()
