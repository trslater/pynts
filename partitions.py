"""Partition Sequence

This is an attempt to answer the coding question from
[Mathologer's video](https://www.youtube.com/watch?v=iJ8pnCO0nTY&list=TLPQMTgxMDIwMjDEsLymLgUaXw&index=2)
on the sequence of numbers of unique partitions for consecutive integers.
"""


import sys
import itertools

from operator import add, sub


def main(argv):
    place = int(argv[0])

    gen = seq()
    for i in range(1, place+1):
        n = next(gen)

        print(i, n)


def seq():
    op_cycle = itertools.cycle((add, add, sub, sub))
    diff_cycle = itertools.cycle((1, 2))

    ops = [next(op_cycle), next(op_cycle), next(op_cycle)]
    diffs = [1, 3]
    offsets = [1, 2, 5]
    seq = [1, 1]

    while True:
        n = 0
        for op, offset in zip(ops, offsets):
            try:
                n = op(n, seq[-offset])

            except IndexError:
                pass

        seq.append(n)
        ops.append(next(op_cycle))
        diffs.append(diffs[-2] + next(diff_cycle))
        offsets.append(offsets[-1] + diffs[-1])

        yield seq[-3]


if __name__ == "__main__":
    main(sys.argv[1:])
