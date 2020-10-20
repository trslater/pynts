"""Partition Sequence

This is an attempt to answer the coding question from
[Mathologer's video](https://www.youtube.com/watch?v=iJ8pnCO0nTY&list=TLPQMTgxMDIwMjDEsLymLgUaXw&index=2)
on the sequence of numbers of unique partitions for consecutive integers.
"""


import sys
import itertools

from operator import add, sub


def main(argv):
    try:
        place = int(argv[0])

    except IndexError:
        print("Usage:\n\tpython partitions.py <nth>")
        sys.exit(1)

    gen = seq()
    for i in range(1, place+1):
        n = next(gen)

        print(i, n)


def arithmetic_seq(a_0, d):
    a_n = a_0
    while True:
        yield a_n
        a_n += d


def variable_arithmetic_seq(a_0, D):
    a_n = a_0
    while True:
        yield a_n
        a_n += next(D)


def seq():
    mem = [1]

    while True:
        ops = itertools.cycle((add, add, sub, sub))
        diffs = itertools.chain.from_iterable(
            zip(arithmetic_seq(1, 1), arithmetic_seq(3, 2)))
        offsets = variable_arithmetic_seq(1, diffs)

        yield mem[-1]

        n = 0
        try:
            for offset in offsets:
                n = next(ops)(n, mem[-offset])

        except IndexError as idx_err:
            pass

        mem.append(n)

    return mem


if __name__ == "__main__":
    main(sys.argv[1:])
