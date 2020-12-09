"""Partition Sequence

This is an attempt to answer the coding question from
[Mathologer's video](https://www.youtube.com/watch?v=iJ8pnCO0nTY&list=TLPQMTgxMDIwMjDEsLymLgUaXw&index=2)
on the sequence of numbers of unique partitions for consecutive integers.
"""


import sys
import functools
import operator as op

from itertools import chain, count, cycle, repeat, starmap


def main(argv):
    try:
        place = int(argv[0])

    except IndexError:
        print("Usage:\n\tpython partitions.py <nth>")
        sys.exit(1)

    gen = seq()
    for i in range(1, place+1):
        n = next(gen)

        print(n)


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


def offset_gen():
    diffs = chain.from_iterable(
        zip(arithmetic_seq(1, 1), arithmetic_seq(3, 2)))

    p = 0
    while True:
        yield (-1)**((p // 2) % 2)
        p += 1
        for i in range(next(diffs)-1):
            yield 0


def seq():
    wholes = count(0)
    evens = count(2, 2)
    zero_counts = chain.from_iterable(zip(wholes, evens))
    signs = cycle(((1,), (1,), (-1,), (-1,)))
    zero_groups = cycle, (repeat, zip(repeat(0), zero_counts))

    factors = chain.from_iterable(chain.from_iterable(zip(
        signs,
        zero_groups)))

    factor_mem = []
    mem = [1]

    for factor in factors:
        factor_mem.append(factor)

        mem.insert(0, sum(starmap(op.mul, zip(factor_mem, mem))))

        yield mem[0]


if __name__ == "__main__":
    main(sys.argv[1:])
